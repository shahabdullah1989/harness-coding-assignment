# ARG BASE_REGISTRY=repo.kenvue.com
ARG BASE_IMAGE=python
ARG BASE_TAG=3.11.3-slim-bullseye

# FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}
FROM ${BASE_IMAGE}:${BASE_TAG}

RUN set -ex \
    # Create a non-root user
    && addgroup --system --gid 1001 appgroup \
    && adduser --system --uid 1001 --gid 1001 --no-create-home appuser \
    # Upgrade the package index and install security upgrades
    && apt-get update \
    && apt-get upgrade -y \
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

ENV DEBUG=False
ENV PIP_DEFAULT_TIMEOUT=100
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_NO_CACHE_DIR=1

WORKDIR /app
COPY requirements.txt .
COPY --chown=appuser:appuser src ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
HEALTHCHECK --interval=10s --timeout=5s --start-period=10s --retries=3 CMD curl --fail --max-time 5 http://localhost:8000/api/health || exit 1

USER appuser
CMD ["python3", "server.py"]
