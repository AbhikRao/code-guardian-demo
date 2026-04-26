# Code Guardian — Demo Repository

**Version-locked at v1.0.0** — 12 intentional bugs across two files.
This is the canonical target for Code Guardian demo runs.

## Bug Inventory

### app.py — 7 bugs
| # | Type | Severity |
|---|------|---------|
| 1 | SQL injection — INSERT query | CRITICAL |
| 2 | SQL injection — SELECT query | CRITICAL |
| 3 | MD5 password hashing (use hashlib.pbkdf2_hmac) | HIGH |
| 4 | Path traversal — no filename sanitisation | HIGH |
| 5 | Division by zero — no guard when b=0 | MEDIUM |
| 6 | Connection leak — conn.close() never called | MEDIUM |
| 7 | Bare except — swallows all errors silently | MEDIUM |

### utils.py — 5 bugs
| # | Type | Severity |
|---|------|---------|
| 1 | No JSON error handling — unhandled JSONDecodeError | MEDIUM |
| 2 | Hardcoded secret fallback ("supersecret123hardcoded") | CRITICAL |
| 3 | List mutated during iteration — elements skipped | MEDIUM |
| 4 | File handle never closed — resource leak | MEDIUM |
| 5 | ZeroDivisionError on empty list | LOW |

**Total: 12 bugs — 2 CRITICAL, 2 HIGH, 7 MEDIUM, 1 LOW**

## Usage

Paste this URL into [code-guardian.streamlit.app](https://code-guardian.streamlit.app):

```
https://github.com/AbhikRao/code-guardian-demo
```

Or click **Load demo** — the URL is pre-filled automatically.

## Version Lock Note

Do not modify `app.py` or `utils.py`. The metrics in the project report
(12 bugs found, 18/19 tests passed, PR opened) are derived from this exact state.
