"""
Servicio de sesión para Fase 1.

Objetivo:
- Simular la creación o recuperación de una sesión de llamada.
- Mantener una estructura mínima de estado en memoria.

Importante:
- Esto NO es persistencia real.
- Esto NO sirve como solución final.
- Solo nos ayuda a validar arquitectura y flujo.
"""

from typing import Dict


class SessionService:
    """
    Servicio simple para gestionar sesiones simuladas.

    Usamos un diccionario en memoria:
    - clave: call_id
    - valor: datos básicos de la sesión

    Esto permite simular que una llamada tiene contexto asociado.
    """

    def __init__(self) -> None:
        self.sessions: Dict[str, dict] = {}

    def get_or_create_session(self, call_id: str, customer_id: str | None = None) -> dict:
        """
        Recupera una sesión existente o crea una nueva si no existe.

        Args:
            call_id: identificador de llamada
            customer_id: identificador opcional del cliente

        Returns:
            dict con datos básicos de sesión
        """
        if call_id not in self.sessions:
            self.sessions[call_id] = {
                "session_id": f"session-{call_id}",
                "call_id": call_id,
                "customer_id": customer_id,
                "turn_count": 0,
            }

        return self.sessions[call_id]

    def increment_turn(self, call_id: str) -> None:
        """
        Incrementa el contador de turnos de la sesión.

        Esto simula que la conversación va avanzando.
        """
        if call_id in self.sessions:
            self.sessions[call_id]["turn_count"] += 1


# Instancia única simple para reutilizar durante la ejecución local
session_service = SessionService()