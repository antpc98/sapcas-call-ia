## README para el software

## app/

Es el paquete principal de Python.
Aquí vive el código del servicio.

## app/main.py

Es el punto de entrada de FastAPI.
Aquí se crea la aplicación y se conectan las rutas.

## app/api/routes/

Aquí van los endpoints HTTP.

Ejemplo:

health.py para saber si el servicio está vivo.
mañana twilio.py para recibir llamadas/eventos de Twilio.
app/core/

Aquí van cosas transversales del sistema:

configuración,
constantes,
logging,
utilidades globales.
app/schemas/

Aquí irán los modelos de entrada/salida con Pydantic.
Todavía no los necesitamos mucho, pero la carpeta debe existir.

## app/services/

Aquí irá la lógica de negocio real.
Todavía no la vamos a usar, pero queremos reservarle sitio desde ya.

## __init__.py

Sirve para que Python trate esas carpetas como paquetes importables.
No hace falta meter contenido; basta con que exista.