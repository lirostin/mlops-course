VENV = .mlops-env
ACTIVATE_MAC:= . $(VENV)/bin/activate

install_python310_macos:
	brew install python@3.10

create_env_macos:
	python3.10 -m venv $(VENV)
	$(ACTIVATE_MAC) && \
	pip install --upgrade certifi && \
	pip install -r requirements.txt
