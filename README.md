# Robot Mesh VEX IQ Python B API Stubs

These API stubs work with Python 3.9 and later.

Modules not stubbed:
- `__bi` / `built_ins` (subset of Python's built-ins)
- `dict` (subset of Python's built-in `dict`; NOTE: NO `.items()`)
- `func` (not clear what it is for)
- `list` (subset of Python's built-in `list`)
- `margin` (not clear what it is for)
- `math` (subset of Python's built-in `math` module)
- `random` (subset of Python's built-in `random` module)
- `string` (subset of Python's built-in `string` module)
- `sys`: clash with Python's built-in `sys` module, with some extra funcs:
  - `run_in_thread`
  - `wait_for`
