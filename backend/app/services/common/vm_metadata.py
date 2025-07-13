import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent.parent / "data" / "vm_owners.json"

def load_vm_metadata():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_vm_metadata(data: dict):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def get_vm_metadata(provider: str, vmid: str):
    data = load_vm_metadata()
    return data.get(f"{provider}:{vmid}", {})

def set_vm_metadata(provider: str, vmid: str, cliente: str, owner: str):
    data = load_vm_metadata()
    data[f"{provider}:{vmid}"] = {"cliente": cliente, "owner": owner}
    save_vm_metadata(data)

def remove_vm_metadata(provider: str, vmid: str):
    data = load_vm_metadata()
    key = f"{provider}:{vmid}"
    if key in data:
        del data[key]
        save_vm_metadata(data)
