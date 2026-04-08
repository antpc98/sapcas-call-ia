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
"""

from fastapi import APIRouter

from app.schemas.call import TestCallInput, TestCallResponse
from app.services.session_service import session_service
from app.services.conversation_service import conversation_service

router = APIRouter()


@router.post("/", response_model=TestCallResponse)
def simulate_call_input(payload: TestCallInput) -> TestCallResponse:
    """
    Simula la entrada de una llamada.

    Flujo:
    1. Recibe el payload.
    2. Crea o recupera una sesión.
    3. Incrementa el contador de turnos.
    4. Detecta intención.
    5. Genera respuesta.
    6. Devuelve un JSON controlado.
    """
    session = session_service.get_or_create_session(
        call_id=payload.call_id,
        customer_id=payload.customer_id,
    )

    session_service.increment_turn(payload.call_id)

    detected_intent = conversation_service.detect_intent(payload.user_text)
    assistant_message = conversation_service.build_response(detected_intent)

    return TestCallResponse(
        call_id=payload.call_id,
        session_id=session["session_id"],
        detected_intent=detected_intent,
        assistant_message=assistant_message,
    )