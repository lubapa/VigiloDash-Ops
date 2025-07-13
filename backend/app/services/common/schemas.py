from pydantic import BaseModel
from typing import Optional

class Machine(BaseModel):
    provider: str       # ej: "proxmox", "digitalocean"
    id: str             # vmid, droplet_id, etc.
    name: str
    type: Optional[str] # ej: "qemu", "lxc", "droplet"
    client: Optional[str] = ""  
    owner: Optional[str] = ""
