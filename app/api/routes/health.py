"""
Router de health check.

Este archivo define endpoints muy simples cuyo objetivo es comprobar
que la API está levantada y respondiendo correctamente.

¿Por qué esto es importante?
- Porque permite validar rápido si la app vive.
- Porque ayuda a detectar si el problema es del servidor o de otra capa.
- Porque más adelante servirá para pruebas en Docker, despliegues y monitoring.
"""

from fastapi import APIRouter

# Creamos un router independiente.
# Un router agrupa endpoints relacionados por responsabilidad.
router = APIRouter()


@router.get("/")
def health_check() -> dict:
    """
    Endpoint de comprobación del estado de la API.

    Devuelve un diccionario simple para indicar:
    - que el servicio está vivo
    - el nombre del servicio
    - la versión actual

    Ruta final:
    GET /health
    """
    return {
        "status": "ok",
        "service": "sapcas-call-ia",
        "version": "0.1.0"
    }