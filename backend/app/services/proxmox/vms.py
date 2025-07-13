from .client import get_proxmox_client

def get_vms(state_filter=None,template_filter=None):
    proxmox = get_proxmox_client()
    vms = []
    for node in proxmox.nodes.get():
        for vm in proxmox.nodes(node['node']).qemu.get():
            if state_filter and vm['status'] != state_filter:
                continue
            if template_filter is not None and bool(vm.get('template', 0)) != template_filter:
                continue
            vms.append({
                "vmid": vm['vmid'],
                "name": vm.get('name', 'unknown'),
                "status": vm['status'],
                "node": node['node'],
                "template": bool(vm.get('template', 0))
            })
    return vms