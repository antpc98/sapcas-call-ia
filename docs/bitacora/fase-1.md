# Fase 1 - Simulación de entrada de llamada

## Objetivo
Simular la futura entrada de Twilio sin consumir dinero todavía.

## Alcance
Incluye:
- endpoint POST /test/input
- schema básico de entrada y salida
- servicio simple de sesión
- servicio simple de conversación
- respuesta controlada

No incluye:
- Twilio real
- STT
- TTS
- LLM real
- persistencia en base de datos

## Flujo
1. Cliente simulado envía texto
2. El endpoint recibe el JSON
3. Se crea o recupera una sesión
4. Se detecta una intención básica
5. Se genera una respuesta controlada

## Objetivo técnico
Validar la arquitectura:
- routes
- schemas
- services
- flujo conversacional básico
