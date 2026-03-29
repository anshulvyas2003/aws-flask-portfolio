# AWS Flask Portfolio

A Python Flask web application deployed on AWS EC2 with Nginx reverse proxy.
Live at: http://65.2.49.110

## Tech Stack
- Python Flask
- AWS EC2 (Ubuntu 22.04)
- Nginx (Reverse Proxy)
- Elastic IP (Permanent IP)
- Linux CLI

## Project Structure
aws-flask-portfolio/
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── nginx.conf              # Nginx configuration
├── deployment-steps.md     # AWS deployment guide
└── screenshots/            # Project screenshots

## How I Deployed This

### 1. Launch EC2 Instance
- AMI: Ubuntu 22.04 LTS
- Instance type: t2.micro (Free tier)
- Region: ap-south-1 (Mumbai)

### 2. Connect via SSH
ssh -i "my-aws-key.pem" ubuntu@65.2.49.110

### 3. Install Dependencies
sudo apt update
sudo apt install python3-pip nginx -y
pip3 install flask

### 4. Run Flask App
python3 app.py

### 5. Configure Nginx
- Reverse proxy: port 80 → Flask port 5000
- App accessible at http://65.2.49.110

## Security
- SSH access on Port 22 (My IP only)
- HTTP access on Port 80 (Anywhere)
- Security Groups configured via AWS Console
- IAM best practices followed

## Screenshots
See screenshots/ folder for:
- EC2 Dashboard
- Security Groups
- Live Website
- Elastic IP

## Author
Anshul Vyas
- Email: vyasanshul318@gmail.com
- Location: Jodhpur, Rajasthan, India
- B.Tech CSE — JIET (2023-2027)

