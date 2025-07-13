from pydantic import BaseModel

class VM(BaseModel):
    vmid: int
    name: str
    status: str
    node: str
    template: bool
