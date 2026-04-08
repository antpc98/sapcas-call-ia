"""
Router de simulación de entrada de llamada.

Objetivo:
- Simular cómo llegará en el futuro una entrada al sistema.
- Validar el flujo entre:
  - endpoint HTTP
  - schema de entrada
  - servicio de sesión
  - servicio de conversación

Importante:
- Este endpoint no representa Twilio todavía.
- Es una puerta de prueba para validar la arquitectura.

------------

Fase 2.

Router de simulación de entrada.

En esta versión:
- se detecta nombre del cliente
- se detecta objetivo de llamada
- se detecta cierre
- se exporta historial a txt al cerrar
"""

from fastapi import APIRouter

from app.schemas.call import TestCallInput, TestCallResponse
from app.services.conversation_service import conversation_service
from app.services.export_service import export_service
from app.services.session_service import session_service

router = APIRouter()


def log(call_id: str, message: str) -> None:
    """
    Logging simple por llamada.
    """
    print(f"[{call_id}] {message}")


@router.post("/", response_model=TestCallResponse)
def simulate_call_input(payload: TestCallInput) -> TestCallResponse:
    """
    Simula una interacción de llamada.

    Flujo:
    1. Recupera o crea sesión
    2. Guarda mensaje usuario
    3. Detecta nombre si no existe
    4. Detecta intención
    5. Guarda objetivo si aplica
    6. Si quiere cerrar:
       - responde
       - exporta historial
       - cierra sesión
    7. Si no:
       - genera respuesta normal
       - guarda historial
       - devuelve respuesta
    """
    call_id = payload.call_id

    log(call_id, "Incoming request")

    session = session_service.get_or_create_session(
        call_id=call_id,
        customer_id=payload.customer_id,
    )

    log(call_id, f"Session loaded: {session['session_id']}")

    session_service.increment_turn(call_id)
    log(call_id, f"Turn count: {session_service.get_turn_count(call_id)}")

    session_service.add_user_message(call_id, payload.user_text)
    log(call_id, f"User said: {payload.user_text}")

    extracted_name = None
    if session["caller_name"] is None:
        extracted_name = conversation_service.extract_caller_name(payload.user_text)
        if extracted_name:
            session_service.set_caller_name(call_id, extracted_name)
            session_service.set_conversation_state(call_id, "awaiting_goal")
            log(call_id, f"Caller name detected: {extracted_name}")

    # Refrescamos sesión
    session = session_service.get_or_create_session(call_id, payload.customer_id)

    detected_intent = conversation_service.detect_intent(payload.user_text, session)
    log(call_id, f"Intent detected: {detected_intent}")

    extracted_party_size = None

    if detected_intent in {"reservation", "business_hours", "support"}:
        session_service.set_call_goal(call_id, detected_intent)
        log(call_id, f"Call goal stored: {detected_intent}")

        if detected_intent == "reservation":
            session_service.set_conversation_state(call_id, "awaiting_party_size")
        else:
            session_service.set_conversation_state(call_id, "goal_identified")

    if detected_intent == "provide_party_size":
        extracted_party_size = conversation_service.extract_party_size(payload.user_text)
        if extracted_party_size is not None:
            session_service.set_party_size(call_id, extracted_party_size)
            session_service.set_conversation_state(call_id, "goal_completed")
            log(call_id, f"Party size detected: {extracted_party_size}")

    # Refrescamos sesión otra vez por si cambió algo
    session = session_service.get_or_create_session(call_id, payload.customer_id)

    assistant_message = conversation_service.build_response(
        detected_intent,
        session,
        extracted_name=extracted_name,
        extracted_party_size=extracted_party_size,
    )

    session_service.add_assistant_message(call_id, assistant_message)
    log(call_id, "Response generated")
    log(call_id, f"History length: {len(session_service.get_history(call_id))}")

    if detected_intent == "close_call":
        closed_session = session_service.close_session(call_id)

        if closed_session:
            export_path = export_service.export_session_to_txt(closed_session)
            log(call_id, f"Session exported to: {export_path}")
            log(call_id, "Session closed")

        return TestCallResponse(
            call_id=payload.call_id,
            session_id=session["session_id"],
            detected_intent=detected_intent,
            assistant_message=assistant_message,
            caller_name=session["caller_name"],
            call_goal=session["call_goal"],
            is_closed=True,
        )

    return TestCallResponse(
        call_id=payload.call_id,
        session_id=session["session_id"],
        detected_intent=detected_intent,
        assistant_message=assistant_message,
        caller_name=session["caller_name"],
        call_goal=session["call_goal"],
        is_closed=session["is_closed"],
    )