#!/bin/bash

# Update system
sudo apt-get update
sudo apt-get upgrade -y

# Install required packages
sudo apt-get install -y \
    python3-pip \
    python3-venv \
    git \
    nginx \
    docker.io \
    docker-compose

# Setup Python virtual environment
python3 -m venv /opt/mcp/venv
source /opt/mcp/venv/bin/activate

# Install Python packages
pip install \
    flask \
    requests \
    google-api-python-client \
    google-auth \
    google-auth-httplib2

# Clone necessary repositories
git clone https://github.com/GoogleCloudPlatform/professional-services /opt/mcp/professional-services
git clone https://github.com/forseti-security/forseti-security /opt/mcp/forseti-security
git clone https://github.com/GoogleCloudPlatform/getting-started-python /opt/mcp/getting-started-python
git clone https://github.com/GoogleCloudPlatform/ml-on-gcp /opt/mcp/ml-on-gcp
git clone https://github.com/google/gcp_scanner /opt/mcp/gcp_scanner

# Setup service
sudo cp mcp.service /etc/systemd/system/
sudo systemctl enable mcp
sudo systemctl start mcp