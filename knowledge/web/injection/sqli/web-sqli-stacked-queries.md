# Stacked-Query SQL Injection

## Overview

Stacked-query SQL injection occurs when an injection point permits a second SQL statement to execute after the original statement. Whether this is possible depends on DBMS syntax, driver configuration, and the application's query API.

## Technical explanation

A statement terminator is followed by another statement. Some drivers or APIs reject multiple statements in one call; others allow them. A harmless constant SELECT can be used as a controlled test marker where permitted.

## Detection

Use only a non-mutating statement in a controlled environment. Confirm the behavior through an expected, safe observable effect. Never use destructive DDL/DML, privilege changes, operating-system commands, or data extraction as a proof of concept.

## Contexts and variations

Multi-statement execution settings in database drivers, stored procedures, and query APIs. MySQL, PostgreSQL, and SQL Server support differs by interface and configuration; Oracle behavior is not equivalent to a generic semicolon-separated HTTP query.

## Related techniques

- `web-sqli-time-blind`
- `web-sqli-second-order`

## Defensive considerations

Use parameterized queries, disable multi-statement execution where unnecessary, restrict database privileges, and keep each application operation to a single intended statement.

## References

- PortSwigger SQL injection cheat sheet
- OWASP Web Security Testing Guide — Testing for SQL Injection
- CWE-89
