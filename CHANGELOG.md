# Changelog

All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.3] - 2019-10-03

### Added

- Improved parsing sub-routine
- Improved project documentation
- New demonstration GIFs (Usage and Installation guide)
- New method for version detection via searching `__version__` file using AST (Abstract Syntax Trees). Works on Python > 3.4 as `importlib.util.find_spec` is not available in Python < 3.4
- `--verbose` flag for extended output

### Changed

- Moved `tests` to `testcases/`
- Updated `Rqmts.py` script
- Stdout process, fixed trailing newline via `.tell()` method and `os.linesep`

### Removed

- Old demos (Command-line & Interactive)