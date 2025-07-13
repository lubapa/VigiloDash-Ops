from app.client_factory import get_client
from collections import defaultdict
from app.services.proxmox.vms import get_vms
# List existing backups of specific VM
def get_backups(node_name=None, vmid=None,proxmox=None):
    if proxmox is None:
        proxmox = get_client("proxmox")
    backups = []
    
    if node_name:
        nodes = [node_name]
    else:
        nodes = [node['node'] for node in proxmox.nodes.get()]
    for node in nodes:
        if vmid:
            backup_info = proxmox.nodes(node).qemu(vmid).backup.get()
            if backup_info:
                backups.append({
                    "node": node,
                    "vmid": vmid,
                    "backup_info": backup_info
                })
        else:
            for vm in vms:
                backup_info = proxmox.nodes(node).qemu(vm['vmid']).backup.get()
                if backup_info:
                    backups.append({
                        "node": node,
                        "vmid": vm['vmid'],
                        "backup_info": backup_info
                    })
    
    return backups
def get_not_backed_up_vms(proxmox=None):
    if proxmox is None:
        proxmox = get_client("proxmox")
    not_backed_up_vms = proxmox.cluster("backup-info").get("not-backed-up")

    return not_backed_up_vms
# Total size of disks that will be backed up grouped by the day of the week
def get_scheduled_backup_sizes(proxmox=None):
    if proxmox is None:
        proxmox = get_client("proxmox")
    schedules = proxmox.cluster.backup.get()
    daily_totals = defaultdict(int)

    for schedule in schedules:
        if not schedule.get("enabled"):
            continue
        
        day = schedule["schedule"].split()[0]  # ej: "sun"
        vmids = schedule["vmid"].split(",")

        for vmid in vmids:
            vmid = vmid.strip()
            disk_size_gb = get_vm_disk_size(proxmox, vmid)
            daily_totals[day] += disk_size_gb
    
    return daily_totals


def get_vm_disk_size(proxmox, vmid):
    for node in proxmox.nodes.get():
        node_name = node["node"]

        # Verificar si es QEMU
        try:
            config = proxmox.nodes(node_name).qemu(vmid).config.get()
            return sum_disk_sizes(config)
        except Exception:
            pass

        # Verificar si es LXC
        try:
            config = proxmox.nodes(node_name).lxc(vmid).config.get()
            return sum_disk_sizes(config)
        except Exception:
            continue

    return 0  # Si no se encuentra

def sum_disk_sizes(config):
    total_gb = 0
    for key, val in config.items():
        if key.startswith("virtio") or key.startswith("scsi") or key.startswith("ide") or key.startswith("sata") or key == "rootfs":
            if isinstance(val, str) and "size=" in val:
                size_str = val.split("size=")[-1]
                total_gb += parse_size_to_gib(size_str)
    return total_gb

def parse_size_to_gib(size_str):
    size_str = size_str.strip().upper()
    try:
        if size_str.endswith("G"):  # GiB
            return int(size_str[:-1])
        elif size_str.endswith("T"):  # TiB
            return int(size_str[:-1]) * 1024
        elif size_str.endswith("M"):  # MiB
            return int(size_str[:-1]) // 1024
        elif size_str.endswith("K"):  # KiB
            return int(size_str[:-1]) // (1024 * 1024)
        elif size_str.isdigit():  # bytes
            return int(size_str) // (1024 ** 3)
    except ValueError:
        return 0
    return 0

# Find VM or LXC with schedule backup in more than one schedule.
def get_vms_in_multiple_schedules(proxmox=None):
    if proxmox is None:
        proxmox = get_client("proxmox")

    schedules = proxmox.cluster.backup.get()

    # Mapea vmid -> lista de jobs donde aparece
    vmid_to_jobs = defaultdict(list)

    for job in schedules:
        job_id = job.get("id", "unknown-job")
        schedule = job.get("schedule", "")
        day_hour = schedule.strip()  # Ej: "sun 01:00"

        vmids = job.get("vmid", "")
        if not vmids:
            continue

        vmid_list = [v.strip() for v in vmids.split(",") if v.strip()]

        for vmid in vmid_list:
            vmid_to_jobs[vmid].append({
                "job_id": job_id,
                "schedule": day_hour
            })

    # Filtramos los VMIDs que están en más de un job
    duplicates = {
        vmid: jobs for vmid, jobs in vmid_to_jobs.items() if len(jobs) > 1
    }

    return {
        "duplicates": duplicates
    }
