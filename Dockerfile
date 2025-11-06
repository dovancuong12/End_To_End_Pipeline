FROM python:3.13-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y gcc g++ python3-dev git curl && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get purge -y gcc g++ python3-dev && \
    apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

FROM python:3.13-slim
WORKDIR /app
COPY --from=builder /usr/local /usr/local
COPY . .
EXPOSE 8000
CMD ["python", "app.py"]
