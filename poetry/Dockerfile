FROM python:3.10 as base

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && \
    poetry config virtualenvs.create false

FROM base as app
RUN poetry install --only app --no-directory
COPY workspaces/ workspaces/
RUN poetry install --only app
CMD ["poetry", "run", "python", "workspaces/app/src/namespace/app/main.py"]

FROM base as cli
RUN poetry install --only cli --no-directory
COPY workspaces/ workspaces/
RUN poetry install --only cli
CMD ["poetry", "run", "python", "workspaces/cli/src/namespace/cli/main.py"]
