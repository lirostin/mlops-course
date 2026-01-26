PYTHON_VERSION = 3.10

VENV = .mlops-env

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
	rm -rf .venv/
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
	uv init --python 3.10
	uv add "numpy==1.25.2" "pandas==2.0.3" "scikit-learn==1.3.2"

init_dev:
	uv add --group dev pip-audit

init_full: init_uv init_dev

run_project:
	 uv run python predict.py

# Вносим изменения в версии файла pyproject.toml
update_uv:
#	Обновляем зависимости
	uv sync
#	Проверьте все установленные пакеты
	uv pip list
	uv lock

check_new_version_uv:
	uv pip list --outdated
	uv run pip-audit || true