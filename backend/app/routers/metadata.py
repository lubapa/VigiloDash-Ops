from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from app.services.common import (
    get_vm_metadata,
    set_vm_metadata,
    load_vm_metadata,
    remove_vm_metadata,
    sync_all_machines
)

router = APIRouter(prefix="/metadata", tags=["VM Metadata"])

class VMMetaInput(BaseModel):
    provider: str
    vmid: str
    cliente: str
    owner: str

@router.get("/", summary="Obtener toda la metadata")
def list_all_metadata():
    return load_vm_metadata()

@router.get("/sync_all", summary="Update Metadata para todos los providers")
def sync_all_data():
    return sync_all_machines()

@router.get("/{provider}/{vmid}", summary="Obtener metadata para una VM")
def get_metadata(provider: str, vmid: str):
    return get_vm_metadata(provider, vmid)

@router.post("/", summary="Asignar cliente/owner a una VM")
def assign_metadata(meta: VMMetaInput):
    set_vm_metadata(meta.provider, meta.vmid, meta.cliente, meta.owner)
    return {"message": "Metadata guardada correctamente"}

@router.delete("/{provider}/{vmid}", summary="Eliminar metadata de una VM")
def delete_metadata(provider: str, vmid: str):
    remove_vm_metadata(provider, vmid)
    return {"message": "Metadata eliminada"}
