"""
Módulo de configuración central de la aplicación.

Objetivo:
- Centralizar la configuración básica del servicio.
- Evitar valores hardcodeados repartidos por distintos archivos.
- Preparar el proyecto para que, más adelante, pueda leer variables
  de entorno y configuración externa sin rehacer la arquitectura.

En esta Fase 0 solo definimos lo mínimo:
- nombre de la app
- versión
- entorno de ejecución
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Clase de configuración principal.

    Cada atributo representa una configuración del sistema.
    En el futuro aquí añadiremos:
    - configuración de base de datos
    - credenciales de Twilio
    - nivel de logs
    - flags de features

    De momento mantenemos la base simple para no complicar la Fase 0.
    """

    app_name: str = "Sapcas Call IA"
    app_version: str = "0.1.0"
    app_env: str = "local"


# Instancia única reutilizable en toda la aplicación.
settings = Settings()