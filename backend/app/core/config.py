from pydantic_settings import BaseSettings
from typing import Optional
from pydantic import model_validator, ValidationError

class Settings(BaseSettings):
    proxmox_host: str
    proxmox_user: Optional[str] = None
    proxmox_password: Optional[str] = None
    proxmox_token_name: Optional[str] = None
    proxmox_token_secret: Optional[str] = None
    proxmox_verify_ssl: bool = False
    proxmox_port: int = 8006  # Default Proxmox port

    class Config:
        env_file = ".env"

@model_validator(mode="after")
def check_auth(cls, values: "Settings") -> "Settings":
    user = values.proxmox_user
    password = values.proxmox_password
    token_name = values.proxmox_token_name
    token_secret = values.proxmox_token_secret

    token_provided = user and token_name and token_secret
    user_pass_provided = user and password

    if not (token_provided or user_pass_provided):
        raise ValueError(
            "Debe proveer proxmox_user, proxmox_token_name y proxmox_token_secret, "
            "o proxmox_user y proxmox_password para autenticación"
        )
    return values



settings = Settings()
