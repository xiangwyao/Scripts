#!/bin/bash

# setup "strict" mode
set -euo pipefail
IFS=$'\n\t'

sudo rm /etc/ssh/sshd_config
sudo cp /vagrant/sshd_config /etc/ssh/sshd_config

# echo ">>> Installing critical software updates ..."
# sudo DEBIAN_FRONTEND=noninteractive apt-get -y upgrade

echo ">>> Restarting the VM to complete setup ... type \"vagrant ssh\" after ~5 mins to re-login"
sudo shutdown -r now
