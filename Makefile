.DEFAULT_GOAL := help

help: ## Shows this help text
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.PHONY: clean
clean: ## Cleans up virtual env
	rm -rf .cache .pytest_cache .mypy_cache coverage .coverage
	rm -rf venv
	rm -rf __pycache__

.PHONY: install
install: ## Creates venv and installs dependencies
	python -m venv venv
	venv/bin/pip install --upgrade --upgrade-strategy eager -r requirements.txt

reinstall: ## Cleans up virtual env then creates venv and installs dependencies
	make clean
	make install

shell: ## Starts interactive Flask Python console
	@ venv/bin/flask shell

serve: ## Runs local debug server
	@ venv/bin/flask --app manage.py --debug run --port=8008

test: ## Runs tests
	@ venv/bin/python -m pytest tests/
