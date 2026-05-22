#!/bin/bash


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

docker compose up -d
