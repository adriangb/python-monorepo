FROM python:3.10 as base

COPY pyproject.toml pdm.lock .
COPY workspaces workspaces/

FROM base as app
RUN pip install pdm && pdm install --no-editable --no-isolation -G app
CMD ["pdm", "run", "python", "workspaces/cli/src/namespace/app/main.py"]

FROM base as cli
RUN pip install pdm && pdm install --no-editable --no-isolation -G cli
CMD ["pdm", "run", "python", "workspaces/cli/src/namespace/cli/main.py"]
