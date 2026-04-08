"""
Schemas de la Fase 1.

Objetivo:
- Definir la forma esperada de los datos de entrada.
- Definir la estructura de salida del endpoint de prueba.
- Validar que el backend reciba información consistente.

En esta fase simulamos una llamada con texto directamente,
sin Twilio ni audio real.

----------

Schemas de la fase 2.

- seguimos recibiendo texto del usuario
- devolvemos más información del estado de la sesión
"""

from pydantic import BaseModel, Field


class TestCallInput(BaseModel):
    """
    Modelo de entrada para simular una llamada.
    """

    call_id: str = Field(..., description="Identificador único de la llamada simulada")
    user_text: str = Field(..., min_length=1, description="Texto que dice el usuario")
    customer_id: str | None = Field(default=None, description="Identificador opcional del cliente")


class TestCallResponse(BaseModel):
    """
    Modelo de respuesta del flujo simulado.

    Campos:
    - call_id: identificador de llamada
    - session_id: identificador de sesión
    - detected_intent: intención detectada
    - assistant_message: respuesta del asistente
    - caller_name: nombre detectado si existe
    - call_goal: objetivo de la llamada si existe
    - is_closed: indica si la sesión ha sido cerrada
    """

    call_id: str
    session_id: str
    detected_intent: str
    assistant_message: str
    caller_name: str | None = None
    call_goal: str | None = None
    is_closed: bool = False