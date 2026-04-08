# Fase 2 - Session Manager básico + trazabilidad inicial

## Objetivo
Hacer que el sistema recuerde el estado básico de la conversación y deje trazabilidad mínima de lo que ocurre en cada interacción.

## Alcance
Esta fase añade:
- gestión básica de sesión en memoria
- turnos acumulados
- historial de mensajes
- logs simples por `call_id`
- mejora del flujo del endpoint `/test/input`

Esta fase no incluye:
- persistencia real en base de datos
- Twilio real
- STT / TTS / LLM reales
- despliegue con Docker

## Motivación
En Fase 1 el sistema ya podía recibir una entrada simulada y responder.  
El problema era que cada petición se trataba casi como aislada.

Con Fase 2 el sistema empieza a parecerse a un agente real:
- mantiene contexto básico
- conserva historial
- registra mejor lo que hace

## Flujo técnico
1. Entra petición `POST /test/input`
2. Se obtiene o crea una sesión
3. Se incrementa el número de turnos
4. Se añade el mensaje del usuario al historial
5. Se detecta la intención
6. Se genera respuesta
7. Se añade la respuesta del asistente al historial
8. Se registran logs básicos del proceso
9. Se devuelve respuesta JSON

## Archivos modificados
- `app/services/session_service.py`
- `app/services/conversation_service.py`
- `app/api/routes/test_input.py`

## Cambios funcionales
### Session Service (app/services/session_service.py)
- añade `history`
- añade métodos para guardar mensajes de usuario y asistente
- incrementa turnos por llamada

### Conversation Service (app/services/conversation_service.py)
- mantiene detección simple de intención
- acepta historial como parte del flujo

### Test Input Router (app/api/routes/test_input.py)
- crea o reutiliza sesión
- registra logs por `call_id`
- añade mensajes al historial
- devuelve respuesta coherente con el flujo actual

## Bitácora de fase
### Estado inicial
- backend FastAPI base funcionando
- endpoint `/health` funcional
- endpoint `/test/input` funcional en Fase 1
- sin memoria conversacional real

### Cambios realizados
- se amplía la estructura de sesión
- se añade historial de mensajes
- se añaden logs simples
- se mantiene compatibilidad con la simulación actual

### Riesgos conocidos
- la sesión vive en memoria, se pierde al reiniciar
- no hay persistencia real
- la lógica conversacional aún es simple
- el historial todavía no se usa de forma avanzada

## Ampliación de comportamiento
En esta revisión de la fase:
- se detecta nombre y apellidos del usuario
- se registra el objetivo principal de la llamada
- se detecta la intención de cierre de llamada
- al cerrar la llamada:
  - se exporta el historial a un archivo `.txt`
  - se elimina la sesión de memoria

## Nuevos archivos implicados
- `app/services/export_service.py`
