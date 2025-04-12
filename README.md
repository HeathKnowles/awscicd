Absolutely! Here's a **comprehensive test checklist** for **Tasks 1 to 4**, covering AWS services, automation, Lambda, and CI/CD. This ensures everything works end-to-end and validates your entire setup.

---

## ✅ **Final Test Plan – Tasks 1 to 4**

---

### ### 🔹**Task 1: AWS Basics**

#### ✅ 1.1: EC2 Instance Setup
- [ ] ✅ Launch Amazon Linux EC2 instance.
- [ ] ✅ SSH into the instance.
- [ ] ✅ Install Apache/Nginx.
- [ ] ✅ Host a basic HTML page.
- [ ] ✅ Confirm via browser: `http://<EC2_PUBLIC_IP>` shows the page.

#### ✅ 1.2: Security Group
- [ ] ✅ Allow HTTP (port 80) and SSH (port 22).
- [ ] ✅ Restrict access to **your public IP** for SSH.
- [ ] ✅ Confirm you **can SSH in** only from your IP.

#### ✅ 1.3: Lambda Function with S3
- [ ] ✅ Create an S3 bucket.
- [ ] ✅ Write Lambda function to log S3 upload events.
- [ ] ✅ Configure S3 trigger for **object creation**.
- [ ] ✅ Upload a test file to S3 → Check CloudWatch Logs for event logs.

#### ✅ 1.4: Python Script from EC2
- [ ] ✅ Python script using `boto3` from EC2:
  - Lists all S3 buckets.
  - Displays total objects in a specific bucket.

---

### ### 🔹**Task 2: Python & CSV Processing**
#### 2.1  text: boto3 sdk interaction
#### ✅ 2.2 [ ] text: CSV Analysis Script
- [ ] ✅ Create a CSV file with: `name`, `age`, `gpa`, etc.
- [ ] ✅ Python script (with **Polars or Pandas**) that:
  - Reads the file in chunks.
  - Converts **GPA to letter grades**.
  - Filters students above a user-provided GPA threshold.
  - Removes unwanted columns (`student ID`, `email`, `department`, etc.)

- [ ] ✅ Confirm correct output of qualifying students printed on screen.

---

### ### 🔹**Task 3: CI/CD Basics**

#### ✅ 3.1: GitHub Repository
- [ ] ✅ Create a GitHub repo.
- [ ] ✅ Push:
  - Web server script (Python/Bash).
  - Terraform files.

#### ✅ 3.2: GitHub Actions Workflow
- [ ] ✅ Create `.github/workflows/terraform.yml`.
- [ ] ✅ Add CI/CD steps:
  - Terraform init, fmt, plan, apply.
- [ ] ✅ Set required secrets: AWS credentials, region, key, bucket name.
- [ ] ✅ Push to main → Confirm CI/CD passes and deploys infra.

---

### ### 🔹**Task 4: Terraform Automation**

#### ✅ 4.1: Terraform Code
- [ ] ✅ Terraform file for:
  - EC2 instance with Apache/Nginx + user data.
  - S3 bucket.
  - Lambda function zip upload and trigger setup.
- [ ] ✅ Use `terraform.tfvars` or `variables.tf` to parameterize:
  - Region, key pair name, instance type, bucket name, etc.

#### ✅ 4.2: Deploy with Terraform
- [ ] ✅ Run `terraform init`, `plan`, and `apply`.
- [ ] ✅ Verify:
  - EC2 is launched and public IP is available.
  - S3 bucket is created.
  - Lambda is deployed and triggered on S3 uploads.



