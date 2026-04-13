#!/bin/bash

# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/debian
Suites: $(. /etc/os-release && echo "$VERSION_CODENAME")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update

#Downloading and installing docker
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

#configuring os for docker
sudo usermod -aG docker $USER
newgrp docker


#Setting up permissions
sudo chown -R 1000:1000 ./node-red-data
sudo chown -R 1883:1883 ./mosquitto
sudo chmod +x raspap-data/firewall-rules.sh

#building custom docker container for node red
if [[ "$(docker images -q custom-node-red 2> /dev/null)" == "" ]]; then
  echo "custom-node-red Docker Image not found, building now..."
  docker build -f dockerfiles/node-red/Dockerfile . -t custom-node-red
else
  echo "Image already exists, skipping build"
fi

#stop the networkmangaer from using the lan0 interface
if grep -qx "unmanaged-devices=interface-name:wlan0" /etc/NetworkManager/NetworkManager.conf; then
    echo "NetworkManager is already ignoring interface wlan0"
else
    sudo tee -a /etc/NetworkManager/NetworkManager.conf <<EOF

[keyfile]
unmanaged-devices=interface-name:wlan0
EOF
    sudo systemctl restart NetworkManager
	
fi
