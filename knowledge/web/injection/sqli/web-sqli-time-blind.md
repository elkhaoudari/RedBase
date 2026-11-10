# Time-Based Blind SQL Injection

## Overview

Time-based blind SQL injection uses a database-side delay as an observable side channel when query output and useful errors are unavailable.

## Technical explanation

A DBMS-specific delay expression is evaluated by the database. A measurable delay that correlates with a test condition can indicate that input influenced SQL execution. Delay functions, permissions, query cancellation, and driver timeouts vary by DBMS.

## Detection

Use short delays (for example, three seconds) only in an authorized test environment. Compare baseline and test requests repeatedly, keep concurrency low, and account for network jitter, application queues, retries, and rate limits. Stop if the test affects service stability.

## Contexts and variations

Blind filters, login flows, APIs, and asynchronous query-backed features. Conditional delays are more informative than unconditional delays but require a valid expression for the exact SQL context.

## Related techniques

- `web-sqli-boolean-blind`

## Defensive considerations

Use prepared statements, enforce query and request timeouts, monitor anomalous query latency, and avoid granting application database accounts unnecessary privileges.

## References

- PortSwigger SQL injection cheat sheet
- OWASP Web Security Testing Guide — Testing for SQL Injection
- CWE-89
