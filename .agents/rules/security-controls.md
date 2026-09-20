# Rule: Enterprise Security Controls (The 20-Point Checklist)

## Purpose
Enforces backend hardening, credential protection, and runtime security controls across all code generated in this repository.

## The 20 Mandatory Security Controls
1. **Row-Level Security (RLS)**: Enforce database tenant isolation at the engine level.
2. **Parameterized Queries**: Zero inline SQL string concatenation; use typed ORM or prepared statements.
3. **Password Hashing**: Argon2id or bcrypt (work factor $\ge 12$).
4. **Constant-Time Comparison**: Use `crypto.timingSafeEqual` for secret/hash comparisons.
5. **CORS Hardening**: Strict origin whitelisting; reject wildcard `*` with credentials.
6. **Rate Limiting**: Redis/token-bucket rate limiting on public and auth endpoints.
7. **CSRF Protection**: SameSite=Strict cookies and anti-CSRF token verification.
8. **Secure Headers**: Enforce Helmet (HSTS, CSP, X-Frame-Options: DENY).
9. **JWT Security**: Ephemeral access tokens (15m expiry) + rotating refresh tokens.
10. **Zero Secret Hardcoding**: All secrets read from environment variables; validated with Zod.
11. **Gitleaks Pre-Commit**: Pre-commit hook blocking AWS, Anthropic, or OpenAI API keys.
12. **Container Non-Root**: Docker containers must run as unprivileged `node` or `app` user.
13. **Dependency Auditing**: Automated `npm audit` / Trivy scanning for CVEs.
14. **Audit Logging**: Immutable logging for critical authorization and billing events.
15. **Input Sanitization**: Zod runtime schema validation on all inbound HTTP bodies.
16. **Output Escaping**: Automated XSS escaping for all HTML and template outputs.
17. **File Upload Isolation**: Store user uploads in private S3/GCS with signed download URLs.
18. **IDOR / BOLA Prevention**: Always verify user ownership of resource IDs before returning data.
19. **Secure Error Handling**: Never leak stack traces or database error messages in API responses.
20. **Dynamic AI Pen-Testing**: Mandatory Styx DAST scan before merging feature branches.
