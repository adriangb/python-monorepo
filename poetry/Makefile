PROJECTS := $(notdir $(wildcard workspaces/*))


.clean-venv:
	rm -rf .venv

.venv:
	pipx run poetry config virtualenvs.create true --local
	pipx run poetry install --sync

init: .clean-venv .venv

test-%:
	pipx run poetry install --sync --with $*
	pipx run poetry run pytest workspaces/$*

tests: $(addprefix test-, $(PROJECTS)) 
