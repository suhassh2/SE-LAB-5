# SE-LAB-5
Python static analysis using Pylint, Bandit, and Flake8
# Lab 5: Static Code Analysis

## Objective
Enhance Python code quality, security, and style by using **Pylint**, **Flake8**, and **Bandit** on the provided `inventory_system.py` program.  
This lab demonstrates how static analysis tools can detect and prevent logical, stylistic, and security-related issues in Python code.

---

## Known Issues and Fixes

| Issue Type | Tool | Line(s) | Description | Fix Approach |
|-------------|-------|----------|--------------|---------------|
| Mutable default argument | Pylint | 9 | `logs=[]` shared across calls | Changed default to `None` and initialized inside function |
| Broad exception | Bandit | 23 | Used `except:` which caught all exceptions | Replaced with specific `except KeyError` and `except Exception as e:` |
| Dangerous `eval()` usage | Bandit | 64 | Executed arbitrary code | Removed `eval()` entirely |
| Invalid input types | Pylint | 14 | Passing wrong types (`123`, `"ten"`) | Added input type validation and logging warning |
| File not closed properly | Pylint | 38, 43 | Used `open()` without context manager | Replaced with `with open(...) as f:` |
| Missing logging configuration | Pylint | 4 | No proper logging setup | Configured standard logging with timestamps |
| Non-PEP8 naming | Flake8 | Multiple | Functions used camelCase | Converted all function names to snake_case |
| Long lines and string formatting | Flake8 | Various | Lines longer than 79 chars | Used f-strings and proper line wrapping |

---

## Reflection

### 1. Which issues were the easiest to fix, and which were the hardest?
- **Easiest:** Flake8 formatting issues (line length, naming, spacing).  
- **Hardest:** Mutable default arguments and exception handling.  
  These required changing how functions worked internally to avoid shared state and silent errors.

### 2. Did the static analysis tools report any false positives?
- Bandit flagged a potential warning for file operations, even though they were safely handled using context managers.

### 3. How would you integrate static analysis tools into your workflow?
- Add **Pylint**, **Flake8**, and **Bandit** checks as part of a **GitHub Actions CI pipeline**.  
- Use **pre-commit hooks** locally so issues are caught before committing to the main branch.

### 4. What tangible improvements were observed after applying the fixes?
- Improved readability and maintainability.  
- Safer file handling and input validation.  
- Better error logging instead of silent failures.  
- The code now fully follows **PEP8**, runs without warnings, and passes all static analysis checks.

---

## How to Run the Tools

Run these commands in your Codespaces terminal:

```bash
pip install pylint flake8 bandit
pylint cleaned_inventory_system.py > pylint_report.txt
flake8 cleaned_inventory_system.py > flake8_report.txt
bandit -r cleaned_inventory_system.py > bandit_report.txt
