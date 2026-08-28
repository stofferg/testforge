# TestForge

A small Python test automation project built with Playwright and pytest.

## Goals

- Learn modern UI test automation
- Practice pytest and Playwright
- Build toward a reusable test framework
- Add CI and reporting over time

## Current Features

- Playwright browser automation with Python
- pytest test runner and fixtures
- Playwright `expect()` assertions with automatic waiting
- Accessible locators such as `get_by_role()`
- Page Object Model structure for reusable UI behavior
- Page-to-page navigation using page objects
- Shared test setup in `conftest.py`
- Isolated tests that each start from a clean browser page
- Centralized project configuration with `pyproject.toml`
- Runtime base URL support via pytest's `--base-url` option
- Dependency tracking with `requirements.txt`
- Git/GitHub version control with small, incremental commits

## Project Structure

```text
testforge/
├── pages/              # Page objects and UI behavior
├── tests/              # Test cases and pytest fixtures
├── pyproject.toml      # pytest configuration
├── requirements.txt    # Python dependencies
└── README.md
```

## Running the Tests

Activate the virtual environment, then run:

```powershell
pytest
```

To run against a specific base URL:

```powershell
pytest --base-url https://example.com
```

To watch the browser while tests run:

```powershell
pytest --headed
```

## Concepts Practiced

The project is being built incrementally to practice framework design, maintainable selectors, reusable setup, test isolation, page objects, environment configuration, and reliable browser assertions.