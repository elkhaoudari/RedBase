# Out-of-Band SQL Injection

## Overview

Out-of-band SQL injection relies on a database-originated network interaction, such as a DNS lookup, as an observation channel when in-band output is unavailable.

## Technical explanation

Some DBMS features can cause name resolution or network access when invoked and when the database account, host policy, and network egress permit it. The mechanism is highly DBMS-, version-, privilege-, and platform-dependent.

## Detection

Only use a unique callback domain that you control, in an explicitly authorized environment. A DNS callback demonstrates name resolution, not necessarily a completed application-level request or data disclosure. Do not encode query results or secrets into callback hostnames.

## Contexts and variations

Database features that perform name resolution or external access. Availability often depends on elevated database privileges and outbound network configuration.

## Related techniques

- `web-sqli-boolean-blind`
- `web-sqli-time-blind`

## Defensive considerations

Apply least privilege, disable unnecessary external database features, restrict database-server egress, monitor DNS/network activity, and parameterize all application queries.

## References

- PortSwigger SQL injection cheat sheet — DNS lookup
- OWASP Web Security Testing Guide — Testing for SQL Injection
- CWE-89
