from fastapi import FastAPI
from app.routers import proxmox  # Proxmox Route
from app.routers import metadata  # Metadata Route



app = FastAPI(
    title="VigiloDash API",
    version="1.0.0",
    description="API para monitoreo de infraestructura Proxmox y otros proveedores"
)

@app.get("/")
def root():
    return {"message": "Bienvenido a VigiloDash API"}

# Incluir el router de Proxmox con prefijo /proxmox
app.include_router(proxmox.router, prefix="/proxmox", tags=["Proxmox"])
app.include_router(metadata.router)

