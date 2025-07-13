from fastapi import APIRouter, Query
from app.services.proxmox.schemas import VM
from enum import Enum
from typing import List
from app.services.proxmox import get_vms, get_lxcs, get_not_backed_up_vms, get_scheduled_backup_sizes,get_vms_in_multiple_schedules

router = APIRouter()

class VMState(str, Enum):
    running = "running"
    stopped = "stopped"

@router.get("/vms", response_model=List[VM])
def list_vms(state: VMState = Query(None), template: bool = None):
    return get_vms(state, template)

@router.get("/lxcs")
def list_lxcs(state: str = None, template: bool = None):
    return get_lxcs(state, template)

@router.get("/not-backed-up-vms")
def not_backed_up_vms():
    return get_not_backed_up_vms()

@router.get("/total-backedup-by-day")
def size_backedup_byday():
    return get_scheduled_backup_sizes()
@router.get("/vms/multiple-schedules")
def vms_in_multiple_schedules():
    return get_vms_in_multiple_schedules()


