  GNU nano 7.2                                                                                         deploy.sh
\#!/bin/bash

# Update & install Docker
sudo apt update -y
sudo apt install -y docker.io git

# Start Docker and give permission
sudo systemctl start docker
sudo usermod -aG docker $USER

# Clone your GitHub repo
git clone https://github.com/SAMPREETHI26/TravelwebApp.git

# Build and run Docker container
cd TravelwebApp
docker build -t travelweb-app .
docker run -d -p 8080:8000 travelweb-app
#change the port if it is not available
