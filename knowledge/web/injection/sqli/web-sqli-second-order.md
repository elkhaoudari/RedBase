# Second-Order SQL Injection

## Overview

Second-order SQL injection occurs when input is stored or passed through one workflow and becomes dangerous only when a later operation uses it in dynamically constructed SQL.

## Technical explanation

The initial write path may use parameterized queries, giving the impression that the value is harmless. A later report, administrative action, search, export, or scheduled job may concatenate the stored value into a new SQL statement.

## Detection

In an authorized test system, use a unique inert marker and trace it through the write and subsequent read/use workflows. Review both the initial storage query and every later query that consumes the value. Do not use a payload that modifies or extracts real records.

## Contexts and variations

Profile fields, saved filters, report definitions, imported records, comments, product metadata, and administrative workflows that reuse stored values in SQL.

## Related techniques

- `web-sqli-error-based`
- `web-sqli-boolean-blind`
- `web-sqli-stacked-queries`

## Defensive considerations

Parameterize every query at the point of use. Treat stored data as untrusted, even if it was previously validated or inserted through a safe query.

## References

- PortSwigger SQL injection guidance
- OWASP Web Security Testing Guide — Testing for SQL Injection
- CWE-89
