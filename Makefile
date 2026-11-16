.PHONY: hooks help

help:
	@echo "make hooks   install the commit-msg hook (rules: .pi/ai-git-commit.json)"

hooks:
	@pre-commit install --hook-type commit-msg
