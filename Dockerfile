# Stage 1: Build stage
FROM python:3.12-slim-bookworm AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONPATH=/app/src \
    PATH="/app/.venv/bin:$PATH" \
    CREWAI_DISABLE_TELEMETRY=1 \
    CREWAI_DISABLE_TRACING=1

# Create and set working directory
WORKDIR /app

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    ca-certificates \
    openssl \
    curl \
    && update-ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/cache/apt/* \
    && python -m pip install --no-cache-dir uv \
    && python -m venv /app/.venv

# Copy only dependency files first
COPY pyproject.toml uv.lock ./

# Copy source code
COPY src/ ./src/

# Create venv and install dependencies
RUN python -m venv /app/.venv && \
    . /app/.venv/bin/activate && \
    uv pip install --no-cache-dir .

# Stage 2: Runtime stage
FROM python:3.12-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH" \
    PYTHONPATH=/app/src

# Install runtime dependencies and create user
RUN set -ex; \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    openssl \
    curl \
    && update-ca-certificates \
    && useradd -m -u 1000 appuser \
    && mkdir -p /app \
    && chown -R appuser:appuser /app \
    # Clean up
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/* /usr/share/man/*

# Set working directory
WORKDIR /app

# Copy only necessary files from builder
COPY --from=builder --chown=appuser:appuser /app/.venv /app/.venv
COPY --from=builder --chown=appuser:appuser /app/src /app/src
COPY --from=builder --chown=appuser:appuser /app/pyproject.toml /app/
COPY --chown=appuser:appuser gunicorn.conf.py /app/

# Switch to non-root user
USER appuser

# Expose port 8080
EXPOSE 8080

# Use gunicorn to run the application
CMD ["uv", "run", "trip_planning"]
