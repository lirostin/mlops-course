PYTHON_VERSION = 3.11

VENV = .venv

ACTIVATE_UNIX = . $(VENV)/bin/activate
ACTIVATE_WINDOWS = $(VENV)\Scripts\activate
ACTIVATE_MAC= . $(VENV)/bin/activate

LINUXMACOUSINSTALLUV:= curl -LsSf https://astral.sh/uv/install.sh | sh
WINDOWSINSTALLUV:= powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

.ONESHELL:

install_python310_macos:
	brew install python@$(PYTHON_VERSION)

delete_env:
	rm pyproject.toml
	rm -rf $(VENV)
	rm uv.lock
	rm .python-version

install_uv_mac_linux:
# 	pip install uv
	$(LINUXMACOUSINSTALLUV)
	uv --version

install_uv_windows:
	$(WINDOWS_INSTALL_UV)
	uv --version

init_uv:
	uv init --python $(PYTHON_VERSION)
	uv add pandas==2.3.3 scikit-learn==1.8.0 pydantic==2.12.5

init_dev:
	uv add --group dev pip-audit
	uv add --dev ruff
	uv pip install pre-commit
	uv add --dev mypy==1.19.1
	uv pip install pandas-stubs scikit-learn-stubs

init_full: init_uv init_dev

run_project:
	 uv run python predict.py

# Вносим изменения в версии файла pyproject.toml
update_uv:
	uv sync
	uv pip list
	uv lock

check_new_version_uv:
	uv pip list --outdated
	uv run pip-audit || true


lint:
	uv run ruff check *.py --fix --show-fixes
	uv run mypy *.py

activate_hooks:
	$(ACTIVATE_MAC); pre-commit install 

pre-commit:
	pre-commit clean
	pre-commit install --install-hooks
	pre-commit run --all-files