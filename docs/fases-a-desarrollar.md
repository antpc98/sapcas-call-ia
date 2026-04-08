# Roadmap de Fases (Vertical Hostelería)

---

## 🟢 FASE 3 — Diseño e implementación del flujo de reserva

### 🎯 Objetivo
Cerrar un flujo de reserva realmente útil y natural.

### 🧩 Qué incluye
- nombre de la reserva  
- número de personas  
- fecha  
- hora  
- alergias o restricciones  
- niños o necesidad especial (carrito, etc.)  
- terraza o interior  
- teléfono de contacto *(para futuras confirmaciones reales)*  

### ❌ Qué no incluye aún
- disponibilidad real  
- integración con Twilio  
- base de datos real  
- audio real  

### 📦 Entregable
Flujo completo de reserva funcionando sobre `/test/input`.

---

## 🟡 FASE 3.5 — Generalización de subflujos de hostelería

### 🎯 Objetivo
Pasar de "reserva hardcodeada" a un **vertical de hostelería con múltiples subflujos reutilizables**.

---

### 🧠 Núcleo del flujo hostelería
- saludo  
- detección de intención  
- subflujo  
- confirmación  
- cierre  

---

### 🧩 Subflujos prioritarios
- reserva  
- horario  
- carta básica  
- pedido simple  
- cancelar / modificar reserva  
- consulta general / derivación  

---

### 🏗️ Qué implementar

Introducir una capa tipo:

```text
flow_service.py
```
Responsable de:

definir subflujos
definir campos requeridos
detectar siguiente campo pendiente
aplicar reglas de confirmación
### 📦 Entregable

Motor de subflujos reutilizable dentro del vertical hostelería.

## 🟠 FASE 4 — Persistencia + Docker
### 🎯 Objetivo

Hacer que el sistema tenga memoria real y un entorno reproducible.

### 🧩 Qué incluye
PostgreSQL
Docker Compose
modelos mínimos
guardar sesiones
guardar turnos
guardar eventos
guardar cierres / exportes
### 📦 Entregable

Sistema persistente y levantable de forma consistente.

## 🔵 FASE 5 — Logging serio
### 🎯 Objetivo

Tener control profesional del sistema.

### 🧩 Qué incluye
logging.py
formato estructurado
call_id en logs
eventos clave
trazabilidad clara
### 📊 Eventos recomendados
incoming_call_received
session_created
intent_detected
flow_selected
field_requested
field_collected
response_generated
call_closed
session_exported
### 📦 Entregable

Sistema observable y depurable sin sufrimiento.

## 🟣 FASE 6 — Integración real con Twilio
### 🎯 Objetivo

Conectar el primer canal real de llamadas.

### 🧩 Qué incluye
twilio.py
webhook
mapping de eventos de Twilio
.env
entrada real de llamada
### ⚠️ Condición previa

No entrar aquí sin:

flujo de hostelería claro
persistencia razonable
logs mínimos funcionales
### 📦 Entregable

Primera llamada real entrando al sistema.

## 🔴 FASE 7 — STT / LLM / TTS reales
### 🎯 Objetivo

Cambiar la simulación textual por voz real.

### 🧩 Qué incluye
stt_service.py
llm_service.py
tts_service.py
### ⚠️ Regla importante

El LLM NO controla el flujo.
El flujo lo controla el backend.

### 📦 Entregable

Agente de voz real funcionando con latencia razonable.

## ⚫ FASE 8 — Plataforma mínima / dashboard
### 🎯 Objetivo

Empezar la capa SaaS o capa interna de revisión.

### 🧩 Qué incluye
histórico de llamadas
estado de sesiones
visualización de logs
configuración básica por negocio
revisión de cierres y exportes
### 📦 Entregable

Primera versión operable del producto.