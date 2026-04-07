"""
Punto de entrada principal de la aplicación FastAPI.

Responsabilidades de este archivo:
- Crear la instancia principal de FastAPI.
- Cargar configuración básica.
- Registrar routers disponibles.

Importante:
- Aquí no debe ir lógica de negocio.
- Aquí no debe ir lógica específica de Twilio.
- Aquí solo montamos la aplicación.
"""

from fastapi import FastAPI

# Importamos el router del health check
from app.api.routes.health import router as health_router

# Importamos configuración centralizada
from app.core.config import settings

# Creamos la aplicación principal.
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Base backend service for SAPCAS Call IA"
)

# Registramos el router de health bajo el prefijo /health
app.include_router(health_router, prefix="/health", tags=["health"])