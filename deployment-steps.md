# Complete AWS Deployment Guide

## Project Overview
Python Flask portfolio app deployed on AWS EC2 with Nginx
as reverse proxy. Accessible at http://65.2.49.110

## AWS Services Used
- EC2 (t2.micro - Free tier) — Virtual server
- Elastic IP — Permanent public IP address
- Security Groups — Firewall rules
- IAM — Identity and access management

## Step 1 — Launch EC2 Instance
1. Login to AWS Console
2. Go to EC2 → Launch Instance
3. Select Ubuntu 22.04 LTS (Free tier)
4. Instance type: t2.micro
5. Create Key Pair (.pem file)
6. Configure Security Groups:
   - Port 22 (SSH) — My IP
   - Port 80 (HTTP) — Anywhere
   - Port 5000 (Flask) — Anywhere
7. Launch Instance

## Step 2 — Connect via SSH
cd /d/aws-keys
chmod 400 my-aws-key.pem
ssh -i "my-aws-key.pem" ubuntu@65.2.49.110

## Step 3 — Setup Server
sudo apt update
sudo apt upgrade -y
sudo apt install python3-pip nginx -y
pip3 install flask

## Step 4 — Deploy Flask App
nano app.py
python3 app.py

## Step 5 — Configure Nginx
sudo nano /etc/nginx/sites-available/default

Add inside location / block:
proxy_pass http://127.0.0.1:5000;
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;

sudo systemctl restart nginx

## Step 6 — Setup Elastic IP
1. EC2 → Elastic IPs → Allocate
2. Associate with my-first-server
3. Permanent IP: 65.2.49.110

## Result
Live website: http://65.2.49.110
Pages: Home, About, Projects, Skills, Contact
