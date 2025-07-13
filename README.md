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

