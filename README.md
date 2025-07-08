# Serverless Image Processing Application

![Architecture Diagram](architecture-diagram.png)

[![AWS Lambda](https://img.shields.io/badge/Built%20with-AWS%20Lambda-orange)](https://aws.amazon.com/lambda/)
[![Status: Completed](https://img.shields.io/badge/Status-Stable-brightgreen)]()

---

## Table of Contents

* [Solution Overview](#solution-overview)
* [Architecture Diagram](#architecture-diagram)
* [Features](#features)
* [AWS Services Used](#aws-services-used)
* [Repository Structure](#repository-structure)
* [How to Deploy](#how-to-deploy)
* [How to Test](#how-to-test)
* [Monitoring and Alerts](#monitoring-and-alerts)
* [License](#license)

---

## Solution Overview

This serverless solution processes user-uploaded images by resizing and watermarking them using AWS Lambda triggered by S3 events. Processed images are stored in a separate bucket for retrieval.

### Key Benefits:

* Event-driven and scalable
* No servers to manage
* Optimized for cost and reliability
* Infrastructure as Code using CloudFormation

---

## Architecture Diagram

![Default Architecture](architecture-diagram.png)

---

## Features

* Resize and watermark uploaded images
* Trigger AWS Lambda automatically on S3 upload
* Store results in a separate "processed" bucket
* Monitor Lambda errors via CloudWatch alarms

---

## AWS Services Used

* **Amazon S3** – Store uploads and processed images
* **AWS Lambda** – Process images using Pillow
* **Amazon SNS** – Receive alert notifications
* **Amazon CloudWatch** – Monitor and log errors
* **AWS IAM** – Secure Lambda function access
* **AWS CloudFormation** – Automate infrastructure

---

## Repository Structure

```plaintext
├── architecture-diagram.png      # AWS architecture
├── README.md                     # Documentation
├── deployment/                   # Infrastructure
│   └── template.yaml             # CloudFormation template
├── src/                          # Lambda function code
│   ├── handler.py                # Lambda handler
│   ├── utils.py                  # Image utilities
│   └── requirements.txt          # Dependencies
└── scripts/                      # Automation
    └── deploy.sh                 # Deployment script
```

---

## How to Deploy

### 1. Install Prerequisites

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
* `zip` utility (Linux/macOS/Windows Git Bash)

### 2. Deploy Using Script

```bash
chmod +x scripts/deploy.sh
./scripts/deploy.sh
```

### 3. Validate in AWS Console

* Go to CloudFormation → Stacks → `ImageProcStack`
* Confirm resources were created

---

## How to Test

### 1. Upload a Test Image

```bash
aws s3 cp test.jpg s3://<UploadsBucketName>/test.jpg
```

### 2. Check Processed Bucket

```bash
aws s3 ls s3://<ProcessedBucketName>/
```

### 3. Review Logs

* Go to AWS Console → Lambda → Monitor → View logs in CloudWatch

---

## Monitoring and Alerts

* Alarm triggers if Lambda errors > 0 in last 5 minutes
* SNS topic receives alerts (email subscription optional)

---


> Developed as part of the AWS Solutions Architect Associate Graduation Project by Ahmed Sameh Abo EL Ela. For support, contact [ahmeddssameh0@gmail.com](mailto:ahmeddssameh0@gmail.com).

---


