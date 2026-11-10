# Boolean-Based Blind SQL Injection

## Overview

Boolean-based blind SQL injection is present when a Boolean condition in an injected SQL expression causes a repeatable difference in the application's observable response, while the query result itself is not directly returned.

## Technical explanation

A true and false predicate is introduced into a query context. The application may return different content, row counts, status codes, or stable response characteristics depending on the predicate result.

## Detection

Compare paired true/false probes under the same conditions. Repeat tests and control for caching, personalization, asynchronous processing, and ordinary response variability. A single difference is insufficient evidence.

## Contexts and variations

Quoted string values, numeric filters, search terms, and API parameters that influence SQL predicates. The exact quote and comment syntax depends on the surrounding query and DBMS.

## Related techniques

- `web-sqli-time-blind`
- `web-sqli-error-based`
- `web-sqli-second-order`

## Defensive considerations

Use parameterized queries and avoid string concatenation. Normalize response behavior where appropriate, but do not treat response masking as a substitute for fixing unsafe query construction.

## References

- PortSwigger SQL injection cheat sheet
- OWASP Web Security Testing Guide — Testing for SQL Injection
- CWE-89
