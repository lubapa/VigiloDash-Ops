# common/sync_machines.py

from app.services.proxmox.vms import get_vms as get_proxmox_vms
from app.services.common.vm_metadata import load_vm_metadata as get_metadata
from app.services.common.vm_metadata import save_vm_metadata,set_vm_metadata

# from app.digitalocean import get_droplets as get_digitalocean_droplets
import json


def sync_all_machines():
    machines = []

    # Obtener VMs Proxmox
    proxmox_vms = get_proxmox_vms()
    machines.extend(proxmox_vms)

    # Obtener máquinas de oceano digital
    # do_droplets = get_digitalocean_droplets()
    # machines.extend(do_droplets)

    # Obtener data json
    existing_data = get_metadata()
    
    updated = False

    for vm in proxmox_vms:
        key = f"{vm['vmid']}"


        if key not in existing_data:
            existing_data[key] = {
                "provider": "proxmox",
                "name": vm['name'],
                "status": vm['status'],
                "client": None,
                "owner": None
            }
            updated = True
        if key in existing_data and (existing_data[key]["status"] != vm["status"] or existing_data[key]["name"] != vm["name"]):
            # Actualiza la data de una VM existente
             existing_data[key] = {
                "provider": "proxmox",
                "name": vm['name'],
                "status": vm['status'],
                "client": existing_data[key]["client"],
                "owner": existing_data[key]["owner"]
            }
             updated=True
            # set_vm_metadata(vm["vmid"],vm["name"],"proxmox",vm["status"],existing_data[key]["client"],existing_data[key]["owner"])

        # Añadir metadata a VM
        vm["provider"] = existing_data[key]["provider"]
        vm["client"] = existing_data[key]["client"]
        vm["owner"] = existing_data[key]["owner"]



    if updated:
        save_vm_metadata(existing_data)
    else: 
        print("No hay cambios en la metadata de las máquinas.")

    return proxmox_vms