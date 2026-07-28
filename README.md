<div align="center">

**Terminal-inspired portfolio.** Cyberpunk. Zero dependencies.

![HTML](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-FFD700?style=flat-square&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white)


<a href="https://astralborn.github.io">
  <img src="https://img.shields.io/badge/Live_Site-00FF8C?style=for-the-badge&logoColor=black" alt="Live site" />
</a>
</div>

---

## About

Personal portfolio site for a Test Automation Engineer — built with vanilla HTML, CSS, and JavaScript. No frameworks, no bundler, no npm. Terminal/hacker aesthetic throughout.

## Features

- 🖥️ Terminal-inspired UI with blinking cursor, `$` prompts, dot headers
- 📱 Fully responsive (mobile hamburger menu, grid reflow at 768px)
- ⚡ Zero frontend dependencies — instant load, no build step
- ♿ Accessible: semantic HTML, `.sr-only` h1, OpenGraph meta tags
- 🧪 Full Playwright test suite with Page Object Model

## Project Structure

```
├── index.html              # Single-page entry point
├── 404.html                # Custom 404 page
├── src/
│   ├── css/                # main.css, components.css, animations.css
│   ├── js/main.js          # All client-side logic
│   └── assets/             # Images, PDF, static files
├── tests/
│   ├── conftest.py         # Shared Pytest fixtures
│   ├── pages/              # Page Object Model classes
│   └── test_*.py           # Test files per section
└── .github/workflows/
    ├── tests.yml           # Playwright CI pipeline
    └── deploy.yml          # GitHub Pages deployment
```

## Running Locally

Open `index.html` directly in a browser — no server needed.

## Running Tests

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/):

```bash
uv venv
uv pip install -r requirements-test.txt
uv run playwright install --with-deps chromium
uv run pytest
```

## CI/CD

| Workflow | Trigger | Description |
|----------|---------|-------------|
| `tests.yml` | Push / PR to `main` | Runs Playwright tests with uv |
| `deploy.yml` | Push to `main` | Deploys to GitHub Pages |

> **Note:** In repo settings → Pages, set source to **"GitHub Actions"**.

## Deployment

Hosted on **GitHub Pages** via `actions/deploy-pages@v4`. The custom 404 page is picked up automatically.

---

*Built with vanilla JS and the audacity to not use React.*
