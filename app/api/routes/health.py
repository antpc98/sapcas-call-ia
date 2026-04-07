"""
Router de health check.

Este archivo define un endpoint simple para comprobar si la API está viva.

¿Por qué esto importa?
- Permite validar rápidamente que FastAPI arranca.
- Sirve como primer endpoint funcional del proyecto.
- Es útil para pruebas locales, Docker y despliegues futuros.
"""

from fastapi import APIRouter

# APIRouter permite agrupar endpoints relacionados.
router = APIRouter()


@router.get("/")
def health_check() -> dict:
    """
    Endpoint de comprobación del estado del servicio.

    Ruta final:
    GET /health

    Devuelve:
    - status: indica si el servicio responde
    - service: nombre lógico del servicio
    - version: versión actual de la aplicación
    """
    return {
        "status": "ok",
        "service": "sapcas-call-ia",
        "version": "0.1.0"
    }