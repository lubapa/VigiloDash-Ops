from fastapi import FastAPI
from app.routers import proxmox  # Proxmox Route
from app.routers import metadata  # Metadata Route
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(
    title="VigiloDash API",
    version="1.0.0",
    description="API para monitoreo de infraestructura Proxmox y otros proveedores"
)

app.add_middleware(
    CORSMiddleware,
    # allow_origins=["http://localhost:8080"],  # o ["*"] para desarrollo
    allow_origins=["*"],  # o ["*"] para desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Bienvenido a VigiloDash API"}

# Incluir el router de Proxmox con prefijo /proxmox
app.include_router(proxmox.router, prefix="/proxmox", tags=["Proxmox"])
app.include_router(metadata.router)

