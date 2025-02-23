# Poetry Plugin: Shell

[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)


Poetry plugin to define and execute shell scripts in pyproject.toml file like npm run.


## Installation

Install the `exec` plugin via the `poetry self add`:

```bash
poetry self add poetry-plugin-exec
```

## Usage

In the pyproject.toml file of your project, define the `[tool.poetry_plugin_exec.scripts]` section, adding your needed scripts:

```toml
[tool.poetry_plugin_exec.scripts]
check-format = "poetry run ruff check ."
```

Then, you can simply run the `poetry exec <script_name> command`:
```bash
poetry exec check-format
```



> [!NOTE]
> This plugin is based on examples from [the official Poetry repository](https://github.com/python-poetry).