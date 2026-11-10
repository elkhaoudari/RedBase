# Blind Server-Side Request Forgery

## Summary

The server issues a request to a user-controlled destination, but no part of the
response reaches the requester. The vulnerability is real and the request is
made, but confirmation requires observing the request from outside the
application, or detecting a side effect of the request.

## Root cause

The same trust-boundary error as basic SSRF: the server fetches a destination it
should not. The distinguishing property is what the requester can observe.

## How it works

1. A feature accepts a URL and issues a request to it.
2. The application discards the response body and returns a generic
   success or failure. It may still expose limited information through
   errors, status differences or response timing, which is commonly
   described as semi-blind SSRF.
3. The request still arrives at the destination. If the destination is a host
   the tester controls, the arrival is observable from outside the application.
4. If the destination is internal, the request may still trigger a side effect
   even though nothing is returned to the tester.

Three observation channels are available without a response body:

- **Out-of-band confirmation.** The target resolves or connects to a hostname
  the tester controls, proving the request was issued from the server. An
  observed HTTP request to the listener confirms a completed HTTP exchange; an
  observed DNS resolution alone confirms only that name resolution occurred, and
  does not by itself prove a connection was established or a request was sent.
- **Timing.** A destination that accepts a connection and then hangs produces a
  measurably different response time than a destination that refuses
  immediately. Repeated measurements across destinations are required.
- **Side effects on internal services.** Some internal services act on a single
  request regardless of what the caller sees: cache and key-value stores,
  search clusters, internal administrative endpoints that accept `GET`.

## Common contexts

Same surface as basic SSRF. Blind behaviour is especially common where the
fetch is asynchronous and its result is written to a queue, a background job, or
a log rather than returned to the caller.

## Variants

- **Semi-blind** — error text, status codes, or response timing differ between
  destinations, allowing enumeration without a response body. This is a variant
  of blind, not a separate technique: the response is not returned to the
  requester, but the application leaks information about the destination through
  a channel other than the destination's body.
- **DNS-only out-of-band** — a resolution is observed at an authoritative
  nameserver the tester controls. Confirms name resolution, not a completed
  HTTP request.
- **HTTP out-of-band** — a full HTTP request is observed at a listener the
  tester controls. Confirms the client executed the fetch.
- **Side-effect-only** — no observable callback, but a state change on the
  destination (cache write, log entry, resource allocation, job enqueue)
  provides evidence the request landed.

## Payload references

- `web-server-side-ssrf-blind-http-callback-001`
- `web-server-side-ssrf-blind-dns-callback-001`
- `web-server-side-ssrf-blind-internal-port-probe-001`

- `web-server-side-ssrf-blind-webhook-callback-001`

## Detection and testing considerations

Use a distinct, unique identifier per injection point and per test. If the same
identifier is reused across parameters, a callback cannot be attributed to a
specific input, and the result is ambiguous.

Distinguish DNS-only confirmation from full HTTP confirmation. A DNS query proves
the target's resolver was asked to resolve a tester-controlled name. It does not
prove the HTTP client connected, sent a request, or accepted a response. Where
both are available, prefer an HTTP listener and log the request method, path,
and headers.

For timing-based enumeration, take repeated measurements per destination.
Network noise produces false positives from single samples.

Absence of a callback does not disprove the vulnerability. Egress filtering, DNS
pinning, or a client that does not resolve external names will suppress the
observation while leaving the underlying fetch intact.

## Mitigations

All mitigations for basic SSRF apply. Blind SSRF additionally argues for:

- Egress DNS logging and alerting on resolution of names outside an expected
  set, so that a successful blind request is visible even when the application
  discards the response.
- Restricting outbound connections to an explicit set of destinations rather
  than blocking a set of forbidden ones.
- Not performing server-side fetches from the same network position as
  privileged internal services.

## References

- [CWE-918: Server-Side Request Forgery (SSRF)](https://cwe.mitre.org/data/definitions/918.html)
- [PortSwigger Web Security Academy — Blind SSRF](https://portswigger.net/web-security/ssrf/blind)
- [OWASP Web Security Testing Guide — Testing for Server-Side Request Forgery](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/19-Testing_for_Server-Side_Request_Forgery)
