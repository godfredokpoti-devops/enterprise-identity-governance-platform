# Enterprise Identity Governance Platform

## Overview

The Enterprise Identity Governance Platform is a Python-based Identity and Access Management (IAM) solution designed to automate user lifecycle management, privileged access governance, compliance reporting, and access reviews.

The platform demonstrates enterprise IAM principles commonly used in Azure AD, AWS IAM Identity Center, Okta, SailPoint, CyberArk, and Microsoft Entra ID environments.

---

# Architecture

```
                        +-------------------------+
                        |      Web Dashboard      |
                        |       Flask UI          |
                        +-----------+-------------+
                                    |
                                    |
             +----------------------+----------------------+
             |                                             |
             |                                             |
     Identity Lifecycle                         Governance Portal
     Management Engine                          Compliance Engine
             |                                             |
             |                                             |
     User Provisioning                          Audit Reporting
     Deprovisioning                             Risk Analysis
     Access Reviews                             Compliance Reports
             |                                             |
             +----------------------+----------------------+
                                    |
                                    |
                           SQLite Database
                                    |
            +-----------------------+----------------------+
            |                       |                      |
      Audit Logs              User Records          Risk Events
```

---

# Components

## Identity Lifecycle Manager

Responsible for

- User onboarding
- User offboarding
- Department assignment
- Employee status tracking

---

## User Provisioning Engine

Automates

- AWS Console access
- Azure Portal access
- Kubernetes access
- Cloud IAM roles

---

## Privileged Session Manager

Tracks

- Active privileged sessions
- Session duration
- Session expiration
- Session approvals

---

## Compliance Dashboard

Provides

- Compliance Score
- Identity Risk Score
- Access Reviews
- Dormant Accounts
- Privileged Accounts
- MFA Coverage

---

## Governance Portal

Provides administrators with

- Audit Logs
- Risk Reports
- User Reviews
- Access Certifications

---

## Database Layer

Stores

- User records
- Audit logs
- Provisioning requests
- Compliance history

---

# Technologies

Python

Flask

SQLite

HTML

CSS

Git

GitHub

Terraform

Future AWS Deployment

---

# Security Controls

Least Privilege

Role Based Access Control (RBAC)

Segregation of Duties

Access Certification

Identity Lifecycle Management

Privileged Access Monitoring

Audit Logging

Continuous Compliance

---

# Future Enhancements

Deploy to AWS

Amazon RDS

AWS IAM Identity Center

AWS Lambda

Amazon CloudWatch

Terraform Infrastructure

Docker Containers

GitHub Actions CI/CD

Real-time Risk Analytics

Machine Learning Risk Detection

Open Policy Agent Integration

Microsoft Entra ID Integration

Okta Integration

SailPoint Integration

CyberArk Integration
