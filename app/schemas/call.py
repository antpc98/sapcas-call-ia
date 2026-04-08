"""
Schemas de la Fase 1.

Objetivo:
- Definir la forma esperada de los datos de entrada.
- Definir la estructura de salida del endpoint de prueba.
- Validar que el backend reciba información consistente.

En esta fase simulamos una llamada con texto directamente,
sin Twilio ni audio real.
"""

from pydantic import BaseModel, Field


class TestCallInput(BaseModel):
    """
    Modelo de entrada para simular una llamada.

    Campos:
    - call_id: identificador de la llamada simulada
    - user_text: texto que representaría lo que el usuario ha dicho
    - customer_id: identificador opcional del cliente/tenant
    """

    call_id: str = Field(..., description="Identificador único de la llamada simulada")
    user_text: str = Field(..., min_length=1, description="Texto que dice el usuario")
    customer_id: str | None = Field(default=None, description="Identificador del cliente")


class TestCallResponse(BaseModel):
    """
    Modelo de respuesta de la simulación.

    Campos:
    - call_id: identificador de la llamada
    - session_id: identificador de la sesión simulada
    - detected_intent: intención detectada por el sistema
    - assistant_message: respuesta del asistente
    """

    call_id: str
    session_id: str
    detected_intent: str
    assistant_message: str