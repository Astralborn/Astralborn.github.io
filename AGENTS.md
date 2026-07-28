# AGENTS.md

## Project Overview

Personal portfolio website for a Test Automation Engineer. Static site with a terminal/hacker-inspired UI, hosted on GitHub Pages at https://astralborn.github.io.

## Tech Stack

- **Frontend:** Vanilla HTML, CSS, JavaScript (no framework, no build step)
- **Testing:** Python 3.12, Pytest, Playwright (browser automation)
- **CI/CD:** GitHub Actions (uv for Python package management)
- **Hosting:** GitHub Pages

## Project Structure

```
├── index.html              # Single-page app entry point
├── 404.html                # Custom 404 page
├── pyproject.toml          # Project config, test deps, pytest settings
├── src/
│   ├── css/
│   │   ├── main.css        # Base styles, layout, responsive
│   │   ├── components.css  # Component-specific styles
│   │   └── animations.css  # Keyframe animations
│   ├── js/
│   │   └── main.js         # All client-side logic (no modules)
│   └── assets/             # Images, PDF, static files
├── tests/
│   ├── conftest.py         # Shared Pytest fixtures
│   ├── pages/              # Page Object Model classes
│   │   └── portfolio_page.py  # Top-level facade composing all sections
│   └── test_*.py           # Test files per section/feature
└── .github/workflows/
    ├── tests.yml           # Playwright test pipeline
    └── deploy.yml          # GitHub Pages deployment
```

## Conventions

### CSS
- Color palette: `#121212` (bg), `#00FF8C` (primary green), `#00D9FF` (accent blue), `#FF6B6B` (red accent)
- Font: `'Courier New', monospace` throughout
- BEM-like naming: `.block-element--modifier` (e.g. `.project-card--col`, `.skill-label--proficient`)
- Mobile breakpoint: `768px`

### JavaScript
- All logic in a single `DOMContentLoaded` listener
- IntersectionObserver for scroll-reveal animations and active nav highlighting
- No external JS dependencies

### Testing
- Page Object Model pattern — each section has its own page object in `tests/pages/`
- `PortfolioPage` is the top-level facade that composes all section objects
- Tests run against the live site by default; `portfolio_local` fixture runs against local `index.html`
- Run tests: `uv run pytest --browser chromium`
- Install deps: `uv sync --group test && uv run playwright install --with-deps chromium`

### CI/CD
- Use `uv` (via `astral-sh/setup-uv@v3`) for Python dependency management in GitHub Actions
- Tests run on push/PR to `main`/`master`
- Deployment uses `actions/deploy-pages@v4` (source must be set to "GitHub Actions" in repo settings)

## Key Design Decisions

- Zero frontend dependencies — no React, no bundler, no npm
- Terminal aesthetic applied consistently (dot headers, `$` prompts, blinking cursor)
- Accessibility: `.sr-only` hidden h1 for SEO, semantic sections, OpenGraph meta tags
- Font Awesome loaded from CDN (only for 2-3 icons)

## Running Locally

Open `index.html` directly in a browser — no server needed. For tests:

```bash
uv sync --group test
uv run playwright install --with-deps chromium
uv run pytest
```

