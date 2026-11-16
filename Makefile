# The gate the committed hooks and CI run (VibeQM Level 2): the repository checks,
# then markdownlint. CI sets MDL to a pinned npx call.
MDL ?= markdownlint-cli2
.PHONY: check
check:
	python3 tools/check_repo.py
	$(MDL)
