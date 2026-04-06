"""
Punto de entrada principal de la aplicación FastAPI.

Responsabilidades de este archivo:
1. Crear la instancia principal de FastAPI.
2. Cargar la configuración básica de la app.
3. Registrar los routers (endpoints) disponibles.

Importante:
- Aquí NO debe ir lógica de negocio.
- Aquí NO debe ir lógica específica de Twilio.
- Aquí solo se "monta" la aplicación.
"""

from fastapi import FastAPI

# Importamos el router de health para registrarlo en la app
from app.api.routes.health import router as health_router

# Importamos la configuración central
from app.core.config import settings

# Creamos la aplicación principal usando configuración centralizada
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Base service for SAPCAS Call IA"
)

# Registramos el router de health.
# Esto hace que el endpoint final sea /health
app.include_router(health_router, prefix="/health", tags=["health"])