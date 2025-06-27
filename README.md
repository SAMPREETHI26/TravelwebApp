# 🌊 TravelwebApp - Sails and More 

A simple Flask-based web application to book water adventure packages like kayaking, scuba diving, fishing, and more.  
Built with Docker, deployed on AWS EC2, and integrated with S3 using IAM Roles.

---

## ✨ Features

- User Registration & Login
- Book Adventure Packages with a Form
- View Bookings (User Dashboard)
- Admin Login & Booking Management
- Styled UI with background image
- Dockerized for easy deployment

---

## 🛠️ Tech Stack

- **Backend**: Flask, SQLAlchemy
- **Frontend**: HTML + Inline CSS
- **Database**: SQLite
- **Deployment**: Docker, AWS EC2
- **Storage**: AWS S3 (for future uploads)

---

## 🚀 Local Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/SAMPREETHI26/TravelwebApp.git
cd TravelwebApp
```

### 2. Build Docker Image

```bash
docker build -t travelweb-app .
```

### 3. Run Docker Container

```bash
docker run -d -p 8000:8000 travelweb-app
```

### 4. Open in Browser

Go to: [http://localhost:8000](http://localhost:8000)

---

## ☁️ Deploy to AWS EC2

### 1. Launch EC2 (Ubuntu 22.04+)

- Choose instance type (e.g., `t2.micro`)
- Add **port 8000** and **port 22 (SSH)** in Security Group
- Add IAM Role (with S3 Full Access)
- Create/download `.pem` key pair

### 2. SSH into EC2

```bash
ssh -i ~/.ssh/YourKey.pem ubuntu@<your-ec2-ip>
```

### 3. Install Docker

```bash
sudo apt update
sudo apt install -y docker.io
sudo usermod -aG docker $USER
exit
# Reconnect after exit
```

### 4. Copy Project to EC2

```bash
scp -i ~/.ssh/YourKey.pem -r /path/to/TravelwebApp ubuntu@<ec2-ip>:~/
```

### 5. Build and Run on EC2

```bash
cd TravelwebApp
docker build -t travelweb-app .
docker run -d -p 8000:8000 travelweb-app
```

Open `http://<EC2-Public-IP>:8000` in your browser 🎉

---

## 6.IAM + S3 Setup

- Create an IAM Role with `AmazonS3FullAccess`
- Attach it to your EC2 instance
- Use `awscli` from your Flask app to upload to S3

---

## 📁 Project Structure

```
TravelwebApp/
├── app.py
├── requirements.txt
├── Dockerfile
├── templates/
│   └── *.html (pages)
├── static/
│   └── background.jpg
├── database.db
└── README.md
```

---

## 🐳 Cloud-Init & Automation 

Add this to EC2 User Data (cloud-init):

```bash
#!/bin/bash
apt update -y
apt install docker.io -y
git clone https://github.com/SAMPREETHI26/TravelwebApp.git
cd TravelwebApp
docker build -t travelweb-app .
docker run -d -p 8000:8000 travelweb-app
```


## 🙋‍♀️ Maintainer

**Sampreethi Y**  
[GitHub](https://github.com/SAMPREETHI26)
