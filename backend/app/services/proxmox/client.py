from proxmoxer import ProxmoxAPI
from app.core.config import settings

def get_proxmox_client():
    if settings.proxmox_user and settings.proxmox_token_name and settings.proxmox_token_secret:
        return ProxmoxAPI(
            host=settings.proxmox_host,
            user=settings.proxmox_user,
            token_name=settings.proxmox_token_name,
            token_value=settings.proxmox_token_secret,
            verify_ssl=settings.proxmox_verify_ssl,
            port = settings.proxmox_port,
            timeout = 300
        )
    elif settings.proxmox_user and settings.proxmox_password and not settings.proxmox_token_name and not settings.proxmox_token_secret:
        return ProxmoxAPI(
            host=settings.proxmox_host,
            user=settings.proxmox_user,
            password=settings.proxmox_password,
            verify_ssl=settings.proxmox_verify_ssl,
            port = settings.proxmox_port,
            timeout = 300
        )
    else:
        raise ValueError("Credenciales de Proxmox no configuradas.")
