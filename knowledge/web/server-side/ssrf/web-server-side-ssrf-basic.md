# Basic Server-Side Request Forgery

## Summary

The application fetches a user-controlled destination on the server side and
returns the response, or part of the response, to the requester. This is the
response-visible form of SSRF: the requester can read what the fetched
destination returned. Blind forms — where the request is made but the response
is not returned — are covered by `web-server-side-ssrf-blind`.

## Root cause

A trust-boundary error. The server treats a user-supplied destination as
trustworthy because the request originates from the server itself, and the
server is presumed to sit inside a trusted network segment. Validation, when
present, is typically applied to the string form of the URL rather than to the
resolved address.

## How it works

1. A feature accepts a URL as input: a webhook target, an image to fetch, a feed
   to import, a document to render.
2. The application passes that value to an HTTP client and issues the request
   from the server.
3. The client resolves the hostname, opens a connection, reads the response, and
   returns at least part of it to the requester.
4. If the resolved address is one the application should not reach — loopback, a
   private range, a link-local address, an internal administrative endpoint, a
   cloud instance metadata service — the response body reveals what the internal
   service returned.

## Common contexts

- Webhook configuration and "test webhook" features.
- URL import, link preview, and unfurl generation.
- PDF, screenshot, and headless-browser rendering of user-supplied URLs.
- Image fetch, resize, and avatar-from-URL features.
- RSS/Atom feed fetching and aggregation.
- OAuth/OIDC discovery and JWKS URL validation.
- SAML and SSO metadata URL import.
- File import by URL and document conversion services.
- Administrative "test connection" functions for integrations.
- Any proxy, redirect, or shortener feature that fetches a target server-side.

## Variants

Not applicable — this technique is the base response-visible case. Sibling
techniques cover the mechanisms that are commonly confused with it:

- `web-server-side-ssrf-blind` — no response returns to the requester.
- `web-server-side-ssrf-parser-confusion` — the validator and fetcher disagree
  on which URI component is the host.
- `web-server-side-ssrf-redirect-validation` — policy applied to the first
  request only; the redirect target is unvalidated.
- `web-server-side-ssrf-dns-rebinding` — resolution differs between validation
  and fetch.

## Payload references

- `web-server-side-ssrf-basic-loopback-http-001`
- `web-server-side-ssrf-basic-rfc1918-http-001`
- `web-server-side-ssrf-basic-file-scheme-001`
- `web-server-side-ssrf-basic-gopher-redis-001`
- `web-server-side-ssrf-basic-cloud-metadata-001`

## Detection and testing considerations

Because the response is returned, testing can inspect the body directly. Compare
responses across destinations that should behave differently: an open port
versus a closed port on the same host, a resolvable versus a non-resolvable
hostname, an allowed versus a disallowed scheme.

Where cloud metadata is the target, note that the response does not establish
that the service is present in general — only that the specific request was
answered. A token-required or header-required response indicates the service is
present but the request was insufficient; a connection refusal does not
establish that the service is absent.

## Mitigations

- Prefer an allowlist of permitted schemes and hosts over a denylist of blocked
  destinations. Denylists are defeated by encoding, redirects, and DNS.
- Resolve the hostname, validate every resulting IPv4 and IPv6 address
  against the permitted set, and connect to a validated address without
  performing an uncontrolled second resolution. Preserve the intended
  hostname for HTTP Host and TLS SNI handling. Account for proxies and
  redirects as well.
- Reject loopback, private, link-local and other prohibited special-purpose
  IPv4 and IPv6 destinations at the application layer. Enforce the same
  policy at the network layer with egress filtering.
- Disable unused URL schemes in the HTTP client.
- Route outbound fetches through a dedicated egress proxy that enforces the same
  policy, so that the policy is not solely dependent on application code.

## References

- [CWE-918: Server-Side Request Forgery (SSRF)](https://cwe.mitre.org/data/definitions/918.html)
- [OWASP Web Security Testing Guide — Testing for Server-Side Request Forgery](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/19-Testing_for_Server-Side_Request_Forgery)
- [PortSwigger Web Security Academy — Server-side request forgery](https://portswigger.net/web-security/ssrf)
- [RFC 6890 — Special-Purpose IP Address Registries](https://www.rfc-editor.org/rfc/rfc6890)
