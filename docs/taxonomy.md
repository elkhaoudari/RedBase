# RedBase Taxonomy Master List

This is the initial taxonomy map for the Web + API phase. It is deliberately broad and can be extended through review. Categories are organizational homes; cross-cutting concepts should usually be represented as metadata tags and relationships rather than duplicated categories.

## Web security

### 1. Injection
- SQL injection
  - Error-based, union-based, boolean-based blind, time-based blind, stacked queries, second-order, out-of-band, stored procedure and DBMS-specific variants
  - DBMS dimensions: MySQL/MariaDB, PostgreSQL, Microsoft SQL Server, Oracle, SQLite, other supported engines
- NoSQL injection
  - Query/operator injection, aggregation pipeline injection, authentication logic flaws
- OS command injection
  - Direct, blind, time-based, out-of-band, argument injection
- Server-side template injection (SSTI)
  - Template-engine-specific families and sandbox boundary issues
- LDAP injection
- XPath/XQuery injection
- XML injection
- Expression Language / OGNL / SpEL injection
- CRLF and response-splitting injection
- HTTP header injection
- Second-order injection (cross-cutting classification; link from applicable injection families)

### 2. Client-side
- Cross-site scripting
  - Reflected, stored, DOM-based, mutation XSS, context-specific variants, polyglots
- HTML injection
- CSS injection
- DOM clobbering
- Client-side prototype pollution
- postMessage origin/trust flaws
- Cross-site request forgery (CSRF)
- Clickjacking / UI redressing
- Open redirect (client and server contexts)
- Client-side URL and navigation handling
- Web storage and client-side secrets exposure
- Client-side template injection

### 3. Server-side
- Server-side request forgery (SSRF)
  - URL parser discrepancies, protocol handling, redirect behavior, cloud metadata exposure, webhook-triggered SSRF
- Remote code execution (RCE) primitives
- Insecure deserialization
- HTTP request smuggling / desynchronization
- Host header attacks
- Web cache poisoning
- Web cache deception
- Cache-based side channels and timing discrepancies
- Server-side prototype pollution
- Server-side parameter pollution
- Path normalization and parser discrepancies
- WebSocket server-side security issues

### 4. File handling
- Path traversal
- Local file inclusion (LFI)
- Remote file inclusion (RFI)
- File upload validation and content-type discrepancies
- File overwrite and file read
- Archive extraction / Zip Slip
- Temporary file and race issues
- Unsafe file download and content disposition
- Image/document processing attack surface

### 5. Authentication and session management
- Authentication bypass
- Username/account enumeration
- Password reset and recovery flaws
- Password policy and credential handling weaknesses
- Multi-factor authentication weaknesses
- Session fixation
- Session hijacking and token handling
- Logout and session invalidation flaws
- Remember-me functionality
- CSRF (cross-reference to client-side taxonomy)
- SSO integration and identity-provider misconfiguration

### 6. Authorization and access control
- IDOR (use as alias where the underlying issue is object-level authorization)
- BOLA
- BFLA
- Function-level authorization failures
- Tenant isolation failures
- Horizontal and vertical privilege escalation
- Path-based and method-based access control bypass
- Mass assignment / property-level authorization (cross-reference API)
- Resource ownership and relationship authorization flaws

### 7. Business logic
- Race conditions and TOCTOU
- Workflow/state-machine bypass
- Payment and price manipulation
- Coupon, discount, and quota abuse
- Limit and threshold bypass
- Transaction and refund logic flaws
- Inventory and reservation logic flaws
- Business rule inconsistencies

### 8. Web cache and delivery infrastructure
- Cache poisoning
- Cache deception
- Cache key confusion
- CDN/origin behavior discrepancies
- Cache partitioning and unkeyed input issues
- Host and routing confusion

### 9. Browser and web platform security
- CORS misconfiguration
- Content Security Policy weaknesses
- Subresource Integrity issues
- Mixed content and transport assumptions
- WebSockets
- WebRTC and browser communication surfaces
- postMessage
- Service worker security
- Browser storage and origin boundaries

### 10. Misconfiguration and exposure
- Debug/development endpoints
- Directory listing and exposed files
- Backup/configuration file exposure
- Default credentials and unsafe defaults
- Subdomain takeover
- Exposed source maps and build artifacts
- Verbose errors and stack traces
- Security header misconfiguration
- Unintended methods and route exposure

### 11. Web protocol and parser behavior
- HTTP method handling discrepancies
- HTTP parameter pollution
- Request/response splitting
- HTTP/1.1 and HTTP/2 translation discrepancies
- URL parsing and normalization discrepancies
- Unicode normalization and best-fit mapping issues
- Content-type and multipart parsing discrepancies

## API security

### 1. REST and HTTP API
- Endpoint and version enumeration
- Authentication and token handling
- Object-level authorization (BOLA)
- Function-level authorization (BFLA)
- Property-level authorization / excessive data exposure
- Mass assignment
- Input validation and injection
- HTTP method manipulation
- Parameter pollution
- Pagination/filter/sort abuse
- Rate limiting and resource consumption
- Idempotency and replay handling
- API versioning and deprecated endpoint exposure
- Error handling and information disclosure
- Webhook security and SSRF
- CORS and cross-origin API exposure
- Content negotiation and serialization issues

### 2. GraphQL
- Introspection exposure and schema discovery
- Object and field authorization
- Resolver-level access control
- Query depth and complexity abuse
- Aliasing and batching abuse
- Excessive data exposure
- Mutation authorization
- ID-based object access
- Error and validation disclosure
- Federation and gateway trust boundaries
- Persisted query and caching issues

### 3. SOAP and XML APIs
- WSDL exposure and service discovery
- XML parser and XXE issues
- SOAP action and operation authorization
- XML signature and wrapping issues
- Serialization and schema validation discrepancies

### 4. API authentication and identity
- JWT validation and algorithm/configuration errors
- OAuth 2.0 flow and redirect URI weaknesses
- OpenID Connect validation issues
- API key leakage and lifecycle
- mTLS configuration and identity mapping
- SAML integration and assertion handling
- Token audience, issuer, scope and expiry validation

### 5. Real-time and event APIs
- WebSocket authentication and authorization
- Message-level authorization
- Origin validation
- Subscription/channel isolation
- Replay and sequence handling
- Webhook signature validation
- Event delivery and retry logic

### 6. API business logic and abuse
- Workflow bypass
- Race conditions
- Quota and rate-limit bypass
- Payment/transaction manipulation
- Resource exhaustion
- Batch operation abuse
- Idempotency flaws

## Cross-cutting metadata dimensions

These are not separate taxonomy roots by default:
- target technology, framework, database and version;
- injection point and input context;
- encoding and normalization;
- authentication requirement;
- interaction type (in-band, blind, out-of-band);
- platform and protocol;
- WAF/filter applicability;
- maturity and review status;
- CWE, OWASP and other classification references.

## Taxonomy governance

- Add a new category only when it represents a distinct vulnerability or useful organizational boundary.
- Use aliases for synonymous names (for example, IDOR and BOLA where appropriate).
- Prefer cross-references for overlapping concepts.
- Do not create a category solely for a framework; use target-technology metadata.
- Record the rationale for significant taxonomy changes in the pull request.
