"""
Servicio de conversación para Fase 1.

Objetivo:
- Interpretar el texto de entrada de forma simple.
- Detectar intención básica.
- Generar una respuesta controlada.

Importante:
- En esta fase NO usamos LLM real.
- En esta fase NO usamos STT ni TTS.
- Esto es una simulación inicial del cerebro conversacional.
"""


class ConversationService:
    """
    Servicio simple para interpretar texto y devolver respuesta.
    """

    def detect_intent(self, user_text: str) -> str:
        """
        Detecta una intención básica a partir del texto del usuario.

        Reglas simples:
        - si contiene 'reserv' -> reservation
        - si contiene 'horario' o 'abierto' -> business_hours
        - si contiene 'ayuda' o 'soporte' -> support
        - en otro caso -> unknown
        """
        text = user_text.lower()

        if "reserv" in text:
            return "reservation"
        if "horario" in text or "abierto" in text:
            return "business_hours"
        if "ayuda" in text or "soporte" in text:
            return "support"

        return "unknown"

    def build_response(self, intent: str) -> str:
        """
        Devuelve una respuesta controlada según la intención detectada.
        """
        if intent == "reservation":
            return "Perfecto, puedo ayudarte con una reserva. ¿Para cuántas personas sería?"
        if intent == "business_hours":
            return "Puedo ayudarte con el horario. En una versión futura consultaré esa información automáticamente."
        if intent == "support":
            return "Entendido. He detectado una solicitud de soporte. Vamos a recoger más información."
        return "No he entendido bien la solicitud. ¿Podrías reformularla, por favor?"


# Instancia simple reutilizable
conversation_service = ConversationService()