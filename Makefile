.DEFAULT_GOAL := help

help:
	@echo "Help menu:"
	@echo "- install      Install requirements"
	@echo "- lint         Lint using flake8"
	@echo "- black        Format using black"
	@echo "- clean        Delete cache and coverage files."
install:
	pip  install -r requirements.txt -r requirements-dev.txt

lint:
	flake8 --count --stat

black:
	black .

clean:
	rm -rf */__pycache__/
	rm -rf .pytest_cache
	rm -f .coverage