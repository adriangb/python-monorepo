FROM python:3.10 as base

COPY pyproject.toml poetry.lock .
RUN pip install git+https://github.com/adriangb/poetry.git@skip-path-dep-install \
    && pip uninstall -y poetry-core \
    && pip install -U git+https://github.com/python-poetry/poetry-core.git@main \
    && poetry config virtualenvs.create false

FROM base as app
RUN poetry install --only app --no-path
COPY workspaces/ workspaces/
RUN poetry install --only app
CMD ["poetry", "run", "python", "workspaces/app/src/namespace/app/main.py"]

FROM base as cli
RUN poetry install --only cli --no-path
COPY workspaces/ workspaces/
RUN poetry install --only cli
CMD ["poetry", "run", "python", "workspaces/cli/src/namespace/cli/main.py"]
