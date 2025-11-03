# Changelog

All notable changes to this project will be documented in this file.

The format roughly follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the
project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2024-06-12
### Added
- `pyproject.toml` packaging metadata with a `golfer-sim` console entry point for the curses dashboard.
- Explicit `__version__` export so clients and tests can detect the installed build.
- Changelog tracking published releases and major changes.

### Changed
- Expanded `.gitignore` to cover build artifacts generated during release packaging.
- Updated documentation to include installation and release guidance for the packaged build.

## [0.1.0] - 2024-05-15
### Added
- Initial playable M1 milestone including the weekly simulation engine, data-driven entities,
  persistence helpers, and the curses dashboard prototype.
