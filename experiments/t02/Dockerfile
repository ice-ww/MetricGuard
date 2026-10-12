FROM python:3.12.10-slim-bookworm@sha256:fd95fa221297a88e1cf49c55ec1828edd7c5a428187e67b5d1805692d11588db
RUN pip install --no-cache-dir duckdb==1.5.6 sqlglot==30.22.0
RUN printf 'T02_PUBLIC_CONTROL' > /canary.txt
WORKDIR /app
COPY worker.py policy.py limits.py ./
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
USER 65532:65532
ENTRYPOINT ["python", "-I", "/app/worker.py"]
