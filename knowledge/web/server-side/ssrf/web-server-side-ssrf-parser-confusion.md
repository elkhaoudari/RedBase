# SSRF via URL Parser Confusion

## Summary

The component that validates a user-supplied URL and the component that fetches
it interpret the URL's authority component differently. A value that appears to
point at an allowed destination to the validator resolves to a different
destination when the fetch client connects.

This technique is limited to authority-component disagreement. Redirect-based
SSRF (policy applied to the first request only) and DNS rebinding (resolution
differs between validation and fetch) are separate mechanisms with separate
technique records.

## Root cause

Different URL parsers can interpret or normalize the same input differently.
This becomes an SSRF risk when the validator and the component performing
the network request disagree about the destination host.

Important cases include:

- **Userinfo:** In `scheme://user:pass@host/`, the host follows the
  `@` delimiter. Naive substring-based validation may mistake userinfo
  for the actual host.
- **Numeric host representations:** Some legacy or implementation-specific
  parsers accept decimal integer, octal or hexadecimal IPv4 representations.
  These are not universally supported alternative IPv4 literal formats
  defined by RFC 3986.
- **Short-form IPv4:** Some legacy parsers accept fewer than four dotted
  components. The interpretation of the final component is parser-dependent;
  omitted components are not necessarily padded with zero.
- **IPv4-mapped IPv6:** An IPv4 address can be represented in IPv6-mapped
  form. Address validation must account for the normalized address.
- **Backslashes:** URL implementations differ in their treatment of
  backslashes, particularly between browser-oriented and generic URI parsers.
- **Protocol-relative references:** A reference beginning with `//`
  inherits its scheme from a base URI. It is not necessarily a standalone
  absolute URL.
- **Trailing dots and case:** Hostname normalization can differ between
  validators, DNS resolution and fetch clients.

RFC 3986 defines URI syntax, but implementation-specific host parsing
behaviour must be tested against the actual components in use.

## How it works

1. The application validates the supplied URL with one parser and one policy.
2. The URL passes validation because the validator extracts an allowed host.
3. The URL is handed to a fetch client that interprets the authority
   differently.
4. The fetch client connects to a destination different from the one
   approved by the validator.

The practical consequence is that substring-based host allowlists and
inconsistent parsing between validation and fetching are not reliable
security controls.

DNS rebinding is a separate mechanism: in that case, the URL structure
remains the same but hostname resolution changes between validation and
connection.

## Common contexts

Any application that validates a user-supplied URL before fetching it,
especially where validation is implemented in application code and fetching is
delegated to a library or a proxy. Also relevant where a reverse proxy, WAF, or
CDN parses the URL separately from the origin application.

## Variants

Each variant represents a different URL or hostname parsing ambiguity:

- **Userinfo ambiguity** — `http://allowed.example@<ip>/`
- **Decimal integer** — a single 32-bit unsigned integer.
- **Octal dotted** — IPv4 octets represented in octal.
- **Hexadecimal dotted** — IPv4 octets represented in hexadecimal.
- **Short-form IPv4** — fewer than four dotted components.
- **IPv4-mapped IPv6** — an IPv4 address represented in IPv6-mapped form.
- **Backslash in authority** — implementation-specific parsing behaviour.
- **Protocol-relative reference** — `//<ip>/`, interpreted against a base URI.

Acceptance depends on the actual parser and client implementation.

## Payload references

- `web-server-side-ssrf-parser-userinfo-001`
- `web-server-side-ssrf-parser-ipv6-mapped-001`
- `web-server-side-ssrf-parser-decimal-001`
- `web-server-side-ssrf-parser-octal-001`
- `web-server-side-ssrf-parser-hex-001`
- `web-server-side-ssrf-parser-short-form-ipv4-001`
- `web-server-side-ssrf-parser-backslash-001`
- `web-server-side-ssrf-parser-protocol-relative-001`

## Detection and testing considerations

Test each representation form independently against the same injection point,
and record which forms the validator accepts and which the fetcher executes. A
form that the validator rejects tells you which parser is in use; a form the
validator accepts but the fetcher resolves elsewhere is the finding.

Use a canary host under tester control that logs the connection source and the
requested `Host` header, so you can distinguish "the validator saw host A" from
"the client connected to address B with `Host: A`". The two being different is
the confirmation.

The encoded-form payloads in this technique are templates: substitute the
address you are permitted to test, then compute the encoding. A decimal integer
form is the address as a single 32-bit unsigned integer in decimal. Octal and
hexadecimal dotted forms are each of the four octets expressed in the base,
joined by dots. The IPv6-mapped form is the IPv4 address in the low 32 bits of
an IPv6 address with the `::ffff:` prefix.

Whether a specific form is accepted depends on the client's host parser. No
statement in this document should be read as claiming universal acceptance or
universal rejection.

## Mitigations

- Parse the URL once, with one strict parser, and use the parsed components for
  both validation and connection.
- Reject non-canonical host forms: require the host to be a registered name or a
  canonical dotted-quad, and reject decimal, octal, hex, short-form, and
  IPv6-mapped forms.
- Reject URLs containing userinfo unless the feature explicitly requires it.
- Reject backslashes in the authority position.
- Require an explicit scheme; reject protocol-relative references.
- Enforce the same policy in the egress proxy as in the application, so a
  parser difference in application code is not the sole control.

## References

- [RFC 3986 — Uniform Resource Identifier (URI): Generic Syntax](https://www.rfc-editor.org/rfc/rfc3986)
- [CWE-918: Server-Side Request Forgery (SSRF)](https://cwe.mitre.org/data/definitions/918.html)
- [PortSwigger Web Security Academy — SSRF](https://portswigger.net/web-security/ssrf)
- [RFC 4291 — IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291)
- [RFC 6890 — Special-Purpose IP Address Registries](https://www.rfc-editor.org/rfc/rfc6890)
