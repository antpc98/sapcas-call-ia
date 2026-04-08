"""
Servicio de sesión para Fase 1.

Objetivo:
- Simular la creación o recuperación de una sesión de llamada.
- Mantener una estructura mínima de estado en memoria.

Importante:
- Esto NO es persistencia real.
- Esto NO sirve como solución final.
- Solo nos ayuda a validar arquitectura y flujo.

--------------------------

Servicio de sesión para Fase 2 ampliada.

Objetivo:
- Mantener sesiones simuladas en memoria
- Guardar historial, turnos y estado conversacional
- Permitir cierre de sesión

Importante:
- Esto NO es persistencia real
- Si el servidor se reinicia, se pierde todo
"""

from typing import Any


class SessionService:
    """
    Servicio simple de sesiones en memoria.
    """

    def __init__(self) -> None:
        self.sessions: dict[str, dict[str, Any]] = {}

    def get_or_create_session(self, call_id: str, customer_id: str | None = None) -> dict[str, Any]:
        """
        Recupera una sesión existente o crea una nueva.
        """
        if call_id not in self.sessions:
            self.sessions[call_id] = {
                "session_id": f"session-{call_id}",
                "call_id": call_id,
                "customer_id": customer_id,
                "turn_count": 0,
                "history": [],
                "caller_name": None,
                "call_goal": None,
                "party_size": None,
                "conversation_state": "awaiting_name",
                "is_closed": False,
            }

        return self.sessions[call_id]

    def increment_turn(self, call_id: str) -> None:
        """
        Incrementa el contador de turnos de una sesión.
        """
        if call_id in self.sessions:
            self.sessions[call_id]["turn_count"] += 1

    def add_user_message(self, call_id: str, message: str) -> None:
        """
        Añade un mensaje del usuario al historial.
        """
        if call_id in self.sessions:
            self.sessions[call_id]["history"].append(
                {
                    "role": "user",
                    "message": message,
                }
            )

    def add_assistant_message(self, call_id: str, message: str) -> None:
        """
        Añade un mensaje del asistente al historial.
        """
        if call_id in self.sessions:
            self.sessions[call_id]["history"].append(
                {
                    "role": "assistant",
                    "message": message,
                }
            )

    def get_history(self, call_id: str) -> list[dict[str, Any]]:
        """
        Devuelve el historial de la sesión.
        """
        if call_id in self.sessions:
            return self.sessions[call_id]["history"]
        return []

    def get_turn_count(self, call_id: str) -> int:
        """
        Devuelve el número de turnos acumulados.
        """
        if call_id in self.sessions:
            return self.sessions[call_id]["turn_count"]
        return 0

    def set_caller_name(self, call_id: str, caller_name: str) -> None:
        """
        Guarda el nombre completo del usuario.
        """
        if call_id in self.sessions:
            self.sessions[call_id]["caller_name"] = caller_name

    def set_call_goal(self, call_id: str, call_goal: str) -> None:
        """
        Guarda el objetivo principal detectado de la llamada.
        """
        if call_id in self.sessions:
            self.sessions[call_id]["call_goal"] = call_goal

    def set_party_size(self, call_id: str, party_size: int) -> None:
        """
        Guarda el número de personas detectado para la reserva.
        """
        if call_id in self.sessions:
            self.sessions[call_id]["party_size"] = party_size

    def set_conversation_state(self, call_id: str, state: str) -> None:
        """
        Guarda el estado actual de la conversación.
        """
        if call_id in self.sessions:
            self.sessions[call_id]["conversation_state"] = state

    def close_session(self, call_id: str) -> dict[str, Any] | None:
        """
        Marca una sesión como cerrada y la elimina de memoria.

        Devuelve una copia de la sesión para poder exportarla antes
        de destruirla de la memoria del proceso.
        """
        if call_id in self.sessions:
            self.sessions[call_id]["is_closed"] = True
            session_data = self.sessions[call_id]
            del self.sessions[call_id]
            return session_data

        return None

# Instancia única simple para reutilizar durante la ejecución local
session_service = SessionService()