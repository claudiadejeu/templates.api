# templates.api

## Description

Template for python API development using FastAPI.

## Setup
To set up this project locally, follow these steps:

### 1. Install Poetry using pipx
Poetry is a dependency manager for Python. For installation methods, refer to the [official Poetry documentation](https://python-poetry.org/docs/#installing-with-pipx).

```cmd
pip install pipx
pipx install poetry
```

### 2. Install Pyenv
Pyenv is a python version manager, it can be installed [here](https://github.com/pyenv/pyenv).
Note that, when on Windows, Pyenv-win will be the target.

### 3. Create a virtual environment
Run the following commands, in order to create a virtual environment and use it on your project.

```cmd
pyenv install 3.11.9
pyenv local 3.11.9
```

### 4. Install the Project dependencies
Once Poetry is installed, navigate to the project directory and install the dependencies listed in the `pyproject.toml` file using Poetry.

```cmd
poetry env use 3.11
poetry install
```

This will create a virtual environment and install all the dependencies specified in `pyproject.toml`.

### 5. Install pre-commit
Install pre-commit from its [official installation page](https://pre-commit.com/#install).

```cmd
pre-commit install
```

## Run the app

### Locally
To run the application locally run the following command:

```cmd
uvicorn app.main:app --reload
```

Then open your browser and go to `http://127.0.0.1:8000` or `http://localhost:8000` to see the app running.

## Styling

Please ensure you adhere to [PEP8 Style Guide](https://peps.python.org/pep-0008/). The following packages should help with this, if you haven't come across them before. These are installed automatically using poetry.

We also use a multitude of linters and formatters:

- [mypy](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html) → Strong typing hints
- [ruff](https://docs.astral.sh/ruff/) → Linter (checks against pep8 style), sorts imports, and formats text

Please use the settings from `.vscode/settings.json` if using VSCode and only `settings.local.json` to overwrite these. If using another editor, please transfer these settings across.

Ensure you run the formatter before committing.

```shell
poetry run format
```

### Pre-commit

Pre-commit hooks are a set of tests that run locally before a commit. These are executed using [pre-commit hooks](https://pre-commit.com/) package.

If your commit does not meet these requirements, then it will fail. You will have to rectify the errors and then commit again.

All pre-commit tests can be found in `.pre-commit-config.yaml`

Run `pre-commit autoupdate` to update the pre-commit hook repositories.

## Testing
We use the pytest framework. Run the tests using:

```cmd
poetry run pytest
```
