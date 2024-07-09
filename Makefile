.PHONY: run install clean check runner
.DEFAULT_GOAL:=runner
SHELL := powershell.exe

run: install
	cd src; poetry run python runner.py

install: pyproject.toml
	poetry install

clean:
	Get-ChildItem -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force

check:
	poetry run flake8 src/

runner: check run clean