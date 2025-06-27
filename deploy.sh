#!/bin/bash
# Install Docker if not already installed
if ! command -v docker &> /dev/null
then
    echo "Docker not found. Installing Docker..."
    sudo apt update
    sudo apt install -y docker.io
    sudo systemctl start docker
    sudo systemctl enable docker
    sudo usermod -aG docker $USER
    newgrp docker
fi

# Navigate to app directory and build image
cd ~/DevOpsAssignment
docker build -t travelweb-app .

# Run container
docker run -d -p 8000:8000 travelweb-app
