# SSRF via DNS Rebinding

## Summary

The hostname in the supplied URL resolves to an allowed address at validation
time and to a forbidden address at fetch time. The validator and the fetch
client each resolve the same name, and the two resolutions disagree because the
name's authoritative data has changed between them.

## Root cause

Time-of-check / time-of-use on hostname resolution. The validator resolves the
hostname once, approves the resolved address, and discards the result. The
fetch client then resolves the same hostname again. If the tester controls the
authoritative nameserver for that hostname and configures it to alternate
answers, the second resolution can return any address.

## How it works

1. The application validates the supplied URL. It resolves the hostname to an
   allowed address and approves the URL.
2. The application hands the URL to an HTTP client that resolves the same
   hostname independently.
3. The tester's authoritative nameserver has been configured with a low TTL
   and alternating answers: the first query returns an allowed address, the
   second (issued by the fetch client) returns a forbidden address.
4. The fetch client connects to the forbidden address and issues the request.
5. The application treats the request as if it targeted the allowed destination
   that was approved.

The mechanism is not a parser differential. The validator and the fetcher agree
on the URL's structure and disagree only on the address the hostname currently
maps to.

## How it fails

DNS rebinding is unreliable in practice. It is defeated by:

- **DNS pinning.** Many HTTP clients and operating systems pin the resolution
  for the duration of a request, or for longer, ignoring the TTL. A pinned
  client sees the first resolution.
- **Validation-time resolution reuse.** An application that resolves the
  hostname once, validates the resolved address, and then connects to that
  same address (rather than re-resolving) defeats the technique entirely.
- **Caching resolvers.** An intermediate resolver that honours a larger TTL
  than the tester configured returns a cached answer for the second query.
- **Short-lived fetch contexts.** A client that re-resolves but immediately
  connects within the caching window may never see the second answer.

A single failed test is inconclusive. Confirmation requires showing that the
client actually re-resolved within the TTL window and reached the second
address.

## Common contexts

Any application that fetches a user-supplied URL where validation includes a
DNS resolution and fetching performs a separate resolution. Less common than
parser confusion or redirect failure because the prerequisites — control of an
authoritative nameserver, short TTL, no client-side pinning — are demanding.

## Variants

- **Single-record rebinding** — one hostname with alternating `A` records.
- **Rebinding with CNAME indirection** — a stable CNAME pointing at a name
  whose authoritative data changes. Useful where the application's validator
  inspects the CNAME chain.
- **IPv4/IPv6 asymmetry** — alternating between an allowed `A` record and a
  forbidden `AAAA` record, or the reverse. Exploits clients that prefer one
  family over the other.

## Payload references

- `web-server-side-ssrf-dns-rebinding-hostname-placeholder-001`

The payload record for this technique is not a string that can be dropped into
an injection point. It is a documented shape: a hostname under tester control
whose authoritative data alternates. The record exists to describe the input
the application will see, not to be a copy-paste payload.

## Detection and testing considerations

Requires control of an authoritative nameserver. Set a low TTL (typically 0 or
a very small value) on the relevant records. Configure alternating answers.
Submit the hostname through the injection point and observe whether the second
resolution reaches the forbidden destination.

Because the technique depends on timing and caching, treat a single test as
inconclusive. Repeat with cache-busting (different subdomains per attempt),
different TTL values, and different client configurations to establish whether
the underlying mechanism — separate resolution between validation and fetch —
is present.

## Mitigations

- Resolve the hostname once, validate the resolved address, and connect to that
  address. Do not re-resolve.
- Where the client cannot be configured to connect to a validated address
  directly, pin the resolution for the duration of the fetch.
- Enforce the policy at the egress proxy rather than only in application code,
  so that a second resolution is still subject to the same allowlist.
- Treat a hostname whose authoritative data has a suspiciously low TTL with
  additional scrutiny, though this is a heuristic rather than a control.

## References

- [CWE-918: Server-Side Request Forgery (SSRF)](https://cwe.mitre.org/data/definitions/918.html)
- [RFC 1034 — Domain Names: Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034)
- [RFC 1035 — Domain Names: Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035)
- [PortSwigger Web Security Academy — SSRF](https://portswigger.net/web-security/ssrf)
