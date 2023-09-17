curl https://trade3space.sgp1.cdn.digitaloceanspaces.com/roop/models/cudnn-local-repo-ubuntu2204-8.9.3.28_1.0-1_amd64.deb --output cudnn-local-repo-ubuntu2204-8.9.3.28_1.0-1_amd64.deb
dpkg -i cudnn-local-repo-ubuntu2204-8.9.3.28_1.0-1_amd64.deb
cp /var/cudnn-local-repo-ubuntu2204-8.9.3.28/cudnn-local-7F7A158C-keyring.gpg /usr/share/keyrings/
apt update
apt-get install libcudnn8=8.9.3.28-1+cuda11.8
apt-get install libcudnn8-dev=8.9.3.28-1+cuda11.8
apt-get install libcudnn8-samples=8.9.3.28-1+cuda11.8
