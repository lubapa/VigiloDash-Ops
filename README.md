# VigiloDash-Ops
VigiloDash is a modular dashboard for monitoring and analyzing virtual infrastructures like Proxmox, GCP, or DigitalOcean. It uses plugins to extract data on backups, unprotected VMs, IPs, and metadata. Built with Python, Docker, and GitHub Actions.


# Quick execution for backend
- Build
``` bash
docker build -t vigilodash-backend:latest . 
```
- Run

``` bash
docker run --env-file .env -p 8000:8000 -v .\data\:/app/app/data/ vigilodash-backend
```
This first deploy requires to attach the data folder to the docker in order to edit the vm_owners.json file.

Note: The .env has to be in the same folder level as the Dockerfile but is not mandatory.

Visit for API docs

> http://localhost:8000/docs

Docker-compose added, fast deploy with .env file in the same level.
```
PROXMOX_HOST=<proxmox_host>
PROXMOX_TOKEN_NAME=<token_name>
PROXMOX_TOKEN_SECRET=<secret_token>
PROXMOX_PORT=<proxmox_port>
PROXMOX_USER=<user@realm>
# PROXMOX_PASSWORD=<password> # optional if token(recommended) is not used 
PROXMOX_VERIFY_SSL=false # or true 
VITE_API_URL="<URL for API backend>"
```

Quick Changelog:
> Simple dashboard with simple button functionality, the button can update json file for the proxmox provider to update and sync all the VMs, their status, and metadata.
> The button will update the vm_owners.json file, which is used to map VM IDs to their owners and metadata. This is essential for tracking VM ownership and ensuring proper management of virtual machines.
> Tested with Proxmox in local enviroment through Cloudflare Tunnels to Proxmox Home Lab.