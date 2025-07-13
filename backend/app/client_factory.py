def get_client(provider: str = "proxmox"):
    if provider == "proxmox":
        from app.services.proxmox.client import get_proxmox_client
        return get_proxmox_client()
    elif provider == "digitalocean":
        raise NotImplementedError("Digital Ocean client not implemented yet.")
    elif provider == "huawei":
        raise NotImplementedError("Huawei client not implemented yet.")
    else:
        raise ValueError(f"Unknown Provider: {provider}")
