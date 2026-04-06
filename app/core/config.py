"""
Configuración central de la aplicación.

Objetivo:
- Tener en un único sitio la configuración importante del servicio.
- Evitar valores hardcodeados repartidos por muchos archivos.
- Facilitar que en el futuro podamos usar variables de entorno (.env)
  sin tener que rehacer la arquitectura.

Usamos pydantic-settings porque:
- permite definir configuración tipada,
- valida tipos,
- y es una forma limpia y moderna de gestionar settings.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Clase de configuración principal.

    Cada atributo aquí definido representa una configuración del sistema.

    En esta v0.1 dejamos solo lo básico:
    - nombre de la aplicación
    - versión
    - entorno actual

    Más adelante aquí añadiremos:
    - claves de Twilio
    - parámetros de base de datos
    - nivel de logs
    - otros valores de entorno
    """

    app_name: str = "Sapcas Call IA"
    app_version: str = "0.1.0"
    app_env: str = "local"


# Creamos una instancia única que importaremos desde otros módulos.
settings = Settings()