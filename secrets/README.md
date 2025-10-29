# Secrets Management

## ⚠️ SECURITY WARNING
**NEVER commit files containing secrets to Git!**

## Directory Structure

```
secrets/
├── .env                    # Actual environment file (gitignored)
├── certificates/           # SSL/TLS certificates
│   ├── kafka/
│   ├── postgres/
│   └── minio/
└── vault/                  # Vault configuration (if used)
```
### 1. Setup Certificates
- Generate SSL certificates for Kafka, PostgreSQL, MinIO
- Store in the certificates/ directory
- Update paths in .env

### 2. Vault Integration (Optional)
- Configure Vault server
- Setup policies for each service
- Implement secret rotation

### 3. Best Practices
- Use environment variables
- Rotate secrets periodically
- Audit access logs
- Encrypt secrets at rest
