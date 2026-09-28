FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:0.12.19 /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --locked --no-install-project

COPY . .

RUN uv sync --locked

CMD ["uv", "run", "python", "src/main.py"]