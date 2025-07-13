from app.client_factory import get_client

def get_lxcs(state_filter=None,template_filter=None,proxmox=None):
    if proxmox is None:
        proxmox = get_client("proxmox")
    vms = []
    for node in proxmox.nodes.get():
        for lxc in proxmox.nodes(node['node']).lxc.get():
            if state_filter and lxc['status'] != state_filter:
                continue
            if template_filter is not None and bool(lxc.get('template', 0)) != template_filter:
                continue
            vms.append({
                "vmid": lxc['vmid'],
                "name": lxc.get('name', 'unknown'),
                "status": lxc['status'],
                "node": node['node'],
                "template": bool(lxc.get('template', 0))
            })
    return vms