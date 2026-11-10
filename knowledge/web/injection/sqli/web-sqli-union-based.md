# UNION-Based SQL Injection

## Overview

UNION-based SQL injection combines the result of an injected `SELECT` with the original query result. It is applicable only when the injection point is in a compatible query context and the number and types of selected columns can be made compatible.

## Technical explanation

A UNION operation generally requires each SELECT to return the same number of columns with compatible data types. Applications may render one or more resulting columns in the response. Database syntax and type coercion differ.

## Detection

Use harmless `NULL`-column probes in an authorized test environment to reason about column count, then use a non-sensitive canary marker to identify a reflected column. Do not use real account, credential, or customer data as a test marker.

## Contexts and variations

String and numeric contexts, reflected result pages, search endpoints, and report views. Some applications suppress query results or use query shapes that prevent UNION injection.

## Related techniques

- `web-sqli-error-based`
- `web-sqli-boolean-blind`

## Defensive considerations

Parameterize values, avoid constructing SQL fragments from user input, and use allowlists for dynamic column names and sort directions.

## References

- PortSwigger SQL injection cheat sheet
- OWASP Web Security Testing Guide — Testing for SQL Injection
- CWE-89
