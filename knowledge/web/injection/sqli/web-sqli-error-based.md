# Error-Based SQL Injection

## Overview

Error-based SQL injection occurs when attacker-controlled input changes SQL syntax or evaluation and database errors become observable through the application. Errors can disclose that input reached a query, identify a DBMS family, or expose query details. An error alone is an indicator, not proof of exploitable data access.

## Technical explanation

The application builds or executes a query using untrusted input. A malformed quote, delimiter, conversion, or expression can cause the database to raise an error. The application may return the database message directly, wrap it in an application error, or suppress it.

## Detection

In an authorized test environment, compare a normal value with minimally disruptive syntax probes. Look for consistent database-specific error changes and confirm with a second independent indicator. Avoid relying on a generic HTTP 500 response.

## Contexts and variations

Common contexts include quoted string values, numeric expressions, search filters, sort expressions, and JSON fields that are later incorporated into SQL. Error wording and trigger syntax vary by DBMS and version.

## Related techniques

- `web-sqli-union-based`
- `web-sqli-boolean-blind`
- `web-sqli-time-blind`

## Defensive considerations

Use parameterized queries for values, allowlist dynamic identifiers, avoid exposing database errors to clients, and log detailed errors server-side with correlation IDs.

## References

- PortSwigger SQL injection cheat sheet
- OWASP Web Security Testing Guide — Testing for SQL Injection
- CWE-89
