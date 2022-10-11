FROM python:3.10 as base

COPY pyproject.toml poetry.lock .
COPY workspaces workspaces/

FROM base as app
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --only app
CMD ["poetry", "run", "python", "workspaces/cli/src/namespace/app/main.py"]

FROM base as cli
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --only cli
CMD ["poetry", "run", "python", "workspaces/cli/src/namespace/cli/main.py"]
