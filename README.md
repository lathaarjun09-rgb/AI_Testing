# Playwright Python with AI

This project contains Playwright-based browser automation tests written in Python. It includes sample login, registration, employee, form, and table-related test cases for a practice website.

## Project Structure

- `testcases/` - Pytest test files
- `pages/` - Page Object Model classes
- `locators/` - Locator definitions
- `utils/` - Helper utilities and config files
- `data/` - Test data and sample JSON files
- `Pythoncode/` - Python learning examples and practice scripts

## Prerequisites

- Python 3.9+
- Git
- A browser supported by Playwright

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Install Playwright browsers:

```bash
python -m playwright install
```

## Run Tests

Run all tests:

```bash
pytest
```

Run a specific test file:

```bash
pytest testcases/test_table.py -q
```

Run a specific test case:

```bash
pytest testcases/test_login.py -q
```

## Example Target Website

The tests use:

- https://testautomationpractice.blogspot.com/

## Notes

This project is a learning and automation practice repository. It demonstrates:

- Playwright automation
- pytest test structure
- Page Object Model design
- Web table handling
- Form and registration automation
