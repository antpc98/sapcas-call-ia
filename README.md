# SAPCAS Call IA

Proyecto base para el desarrollo de un agente de IA orientado a gestión de llamadas de negocio.

## Objetivo
Construir una base técnica estable para:
- recepción de llamadas
- procesamiento de intención
- extracción de datos
- integración con lógica de negocio

## Ramas principales
- main: rama estable
- dev: rama de desarrollo principal

## Normas iniciales
- no subir secretos
- no trabajar directamente sobre main
- documentar cambios relevantes


## requirements.txt
```bash
fastapi: framework web
uvicorn[standard]: servidor ASGI para ejecutar FastAPI
pydantic: validación y modelos tipados
pydantic-settings: configuración centralizada y preparada para .env
```

## Fase 1
Se añade un flujo simulado de entrada de llamada mediante:

- `api/routes/test_input.py`
- `schemas/call.py`
- `services/session_service.py`
- `services/conversation_service.py`

Esto permite validar el primer flujo conversacional sin Twilio real.