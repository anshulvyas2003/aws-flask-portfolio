# AWS Deployment Steps

## 1. Launch EC2 Instance
- AMI: Ubuntu 22.04 LTS
- Instance type: t2.micro (Free tier)
- Region: ap-south-1 (Mumbai)
- Elastic IP: 65.2.49.110

## 2. Connect via SSH
ssh -i "my-aws-key.pem" ubuntu@65.2.49.110

## 3. Install Dependencies
sudo apt update
sudo apt install python3-pip nginx -y
pip3 install flask

## 4. Configure Nginx
- Reverse proxy: port 80 → Flask port 5000
- Config file: /etc/nginx/sites-available/default

## 5. Security Groups
- Port 22 (SSH) - My IP
- Port 80 (HTTP) - Anywhere
- Port 5000 (Flask) - Anywhere
