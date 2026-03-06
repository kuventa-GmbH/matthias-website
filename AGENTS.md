# Repository Guidelines

## Project Structure & Module Organization
This repository is a Jekyll-based website.
- Root pages: `index.md`, `about.md`, `blog.md`, `contact.md`, legal pages (`impressum.md`, `datenschutzerklarung.md`).
- Layouts: `_layouts/` (`default.html`, `page.html`, `post.html`) define page shells.
- Reusable partials: `_includes/` (home and about section fragments, navbar, footer).
- Content data: `_data/*.yml` for structured page content.
- Blog posts: `_posts/` using `YYYY-MM-DD-title.markdown` naming.
- Assets: `assets/css/`, `assets/img/`, `assets/fonts/`, `assets/files/`.
- Generated output: `_site/` (build artifact; do not edit manually).

## Build, Test, and Development Commands
Use Ruby/Bundler for all site tasks:
- `bundle install` installs Ruby dependencies from `Gemfile`.
- `bundle exec jekyll serve` starts local dev server at `http://127.0.0.1:4000`.
- `bundle exec jekyll build` generates static output into `_site/`.
- `bundle exec jekyll doctor` checks configuration and common issues.

Note: `npm test` currently exists only as a placeholder and always fails.

## Coding Style & Naming Conventions
- Use 2-space indentation in HTML, Markdown front matter, and YAML data files.
- Keep Markdown filenames lowercase with hyphens (for posts: `YYYY-MM-DD-title.markdown`).
- Prefer descriptive include names grouped by section (for example `_includes/home-sections/hero.html`).
- Keep CSS changes in `assets/css/site.scss` and avoid editing generated maps unless required.

## Testing Guidelines
There is no automated test suite yet. Validate changes by:
- Running `bundle exec jekyll build` with zero errors.
- Manually checking key routes (`/`, `/about/`, `/blog/`, `/contact/`) in local serve mode.
- Verifying responsive behavior and image/font loading after asset updates.

## Commit & Pull Request Guidelines
No commit history is available yet on `main`, so follow this baseline:
- Commit messages: imperative, concise subject (for example `Add about hero section copy`).
- Keep commits focused to one logical change.
- PRs should include: purpose summary, changed paths, local verification steps, and screenshots for UI/content updates.
- Link related issues/tasks when applicable.

## Configuration & Content Tips
- Site-wide settings live in `_config.yml` (`url`, `baseurl`, metadata).
- Restart `jekyll serve` after changing `_config.yml`.
- Prefer `_data/*.yml` for frequently updated structured content over hardcoding in layouts.
