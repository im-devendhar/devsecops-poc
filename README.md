# devsecops-poc

# DevSecOps POC – Advanced Pipeline

## Overview

This project demonstrates a complete DevSecOps pipeline with:

- SAST (CodeQL)
- SCA (Snyk)
- Secrets Scanning (GitLeaks)
- Container Scanning (Trivy)
- DAST (OWASP ZAP)
- IaC Security (Checkov)
- Deployment to AWS EC2
- CI/CD using GitHub Actions

---

## Architecture

GitHub → CI Pipeline → Security Scans → Docker Build → Image Scan → Deploy to AWS EC2 → DAST Scan

---

## Tools Used

| Category | Tool |
|----------|------|
| CI/CD | GitHub Actions |
| SAST | CodeQL |
| SCA | Snyk |
| Secrets | GitLeaks |
| Container Scan | Trivy |
| DAST | OWASP ZAP |
| IaC Scan | Checkov |
| Cloud | AWS EC2 |
| Container | Docker |

---

## Step 1: Add SCA (Snyk)

### Setup
- Create account in Snyk
- Add `SNYK_TOKEN` in GitHub Secrets

### Pipeline Step

```yaml
- name: Snyk Dependency Scan
  uses: snyk/actions/python@master
  env:
    SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
