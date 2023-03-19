PROJECTS := $(notdir $(wildcard workspaces/*))


.clean-venv:
	rm -rf .venv

.venv:
	pipx run poetry config virtualenvs.create true --local
	pipx run poetry install --sync

init: .clean-venv .venv

test-%: .venv
	pipx run poetry install --sync --with $*
	pipx run poetry run pytest workspaces/$*

tests: .venv $(addprefix test-, $(PROJECTS)) 

test-isolated-%: .venv
	pipx run poetry install --sync --only $*
	pipx run poetry run pytest workspaces/$*
