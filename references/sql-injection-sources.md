# SQL Injection Batch 01 — Research Sources and Provenance

This register identifies public references consulted when independently authoring the RedBase SQLi Batch 01 taxonomy, explanations, and test-record descriptions. RedBase records are not copied wholesale from these sources. The references support technical cross-checking; they do not imply endorsement or verification of each payload.

## Primary references

1. PortSwigger Web Security Academy, SQL injection cheat sheet: https://portswigger.net/web-security/sql-injection/cheat-sheet
   - DBMS syntax differences, comments, conditional errors, stacked queries, time delays, and out-of-band lookup concepts.
2. PortSwigger Web Security Academy, SQL injection: https://portswigger.net/web-security/sql-injection
   - Core SQLi classes and practical testing methodology.
3. OWASP Web Security Testing Guide, latest development guide: https://owasp.github.io/www-project-web-security-testing-guide/latest/
   - Structured web application testing methodology. The project identifies version 5.0 as in development; pin a version when citing a stable test case.
4. CWE-89, Improper Neutralization of Special Elements used in an SQL Command: https://cwe.mitre.org/data/definitions/89.html
   - Weakness definition and consequences.
5. PayloadsAllTheThings, SQL Injection: https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection
   - Community-maintained secondary reference. Consult its current license and per-file provenance before adapting or redistributing any material.

## DBMS-specific references

- Microsoft `xp_dirtree` documentation: https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/xp-dirtree-transact-sql
- Oracle `UTL_INADDR` documentation: https://docs.oracle.com/en/database/oracle/oracle-database/23/arpls/UTL_INADDR.html

## Provenance and licensing

- Technique articles are independently authored RedBase explanatory material and use `CC-BY-4.0` under the project's current policy.
- Payload records are marked `pending-policy-review`. Their syntax may be conventional or informed by public references; do not assign a final license until provenance and redistribution policy are reviewed.
- Every record remains `unverified`. Schema validation is not execution testing.
- Out-of-band examples use only tester-controlled DNS canaries and explicitly exclude query-result or secret exfiltration.

## Scope

This batch focuses on classic SQL injection in web application query contexts: error-based, UNION-based, boolean-blind, time-blind, stacked queries, second-order, and DNS-only out-of-band indicators. It intentionally excludes destructive statements, database file read/write, operating-system command execution, credential dumping, and data-exfiltration payloads.
