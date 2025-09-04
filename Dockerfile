# Stage 1: Build stage
FROM python:3.12-slim as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Create and set working directory
WORKDIR /app

# Install build dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY pyproject.toml uv.lock ./
RUN python -m pip install --no-cache-dir uv \
    && uv venv /app/.venv \
    && . /app/.venv/bin/activate \
    && uv pip install --no-cache-dir .

# Copy source code
COPY src/ ./src/

# Stage 2: Runtime stage
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

# Create non-root user
RUN useradd -m -u 1000 appuser

# Create and set working directory
WORKDIR /app

# Copy virtual environment and source code from builder
COPY --from=builder --chown=appuser:appuser /app/.venv /app/.venv
COPY --from=builder --chown=appuser:appuser /app/src /app/src

# Switch to non-root user
USER appuser

# Set Python path
ENV PYTHONPATH=/app/src

# Command to run the application
CMD ["python", "-m", "trip_planning.main"]
