sync_uv_new_place:
# uv sync создаёт виртуальное окружение, устанавливает зависимости из pyproject.toml и обновляет uv.lock за один шаг
	uv sync

pip-audit:
	source .venv/bin/activate \
	uv pip install pip-audit \
	PIPAPI_PYTHON_LOCATION=.venv/bin/python pip-audit