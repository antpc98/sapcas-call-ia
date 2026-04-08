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

---------------------

Servicio de conversación para Fase 2.

Objetivo:
- Detectar una intención básica a partir del texto del usuario.
- Detectar nombre del usuario
- Detectar si quiere cerrar llamada
- Generar respuesta según el estado de la sesión

"""


import re


class ConversationService:
    """
    Servicio conversacional simple.
    """

    def extract_caller_name(self, user_text: str) -> str | None:
        """
        Intenta extraer nombre y apellidos usando patrones simples.

        Ejemplos válidos:
        - me llamo Antonio Prieto Crespo
        - soy Antonio Prieto Crespo
        - mi nombre es Antonio Prieto Crespo
        """
        text = user_text.strip()

        patterns = [
            r"me llamo\s+([A-Za-zÁÉÍÓÚáéíóúÑñ]+\s+[A-Za-zÁÉÍÓÚáéíóúÑñ]+(?:\s+[A-Za-zÁÉÍÓÚáéíóúÑñ]+)?)",
            r"soy\s+([A-Za-zÁÉÍÓÚáéíóúÑñ]+\s+[A-Za-zÁÉÍÓÚáéíóúÑñ]+(?:\s+[A-Za-zÁÉÍÓÚáéíóúÑñ]+)?)",
            r"mi nombre es\s+([A-Za-zÁÉÍÓÚáéíóúÑñ]+\s+[A-Za-zÁÉÍÓÚáéíóúÑñ]+(?:\s+[A-Za-zÁÉÍÓÚáéíóúÑñ]+)?)",
        ]

        for pattern in patterns:
            match = re.search(pattern, text, flags=re.IGNORECASE)
            if match:
                return match.group(1).strip()

        return None

    def detect_intent(self, user_text: str, session: dict) -> str:
        """
        Detecta intención simple.
        """
        text = user_text.lower()

        if self.detect_close_call(user_text):
            return "close_call"

        # Si estamos esperando número de personas, intentamos capturarlo
        if session["conversation_state"] == "awaiting_party_size":
            if self.extract_party_size(user_text) is not None:
                return "provide_party_size"

        if "reserv" in text:
            return "reservation"

        if "horario" in text or "abierto" in text:
            return "business_hours"

        if "ayuda" in text or "soporte" in text or "pedido" in text:
            return "support"

        return "unknown"

    def detect_close_call(self, user_text: str) -> bool:
        """
        Detecta si el usuario quiere cerrar la llamada.
        """
        text = user_text.lower()

        close_keywords = [
            "adiós",
            "adios",
            "hasta luego",
            "gracias eso es todo",
            "eso es todo",
            "ya está",
            "ya esta",
            "puedes colgar",
            "terminar llamada",
            "cerrar llamada",
            "nada más",
            "nada mas",
        ]

        return any(keyword in text for keyword in close_keywords)

    def build_response(self, intent: str, session: dict, extracted_name: str | None = None, extracted_party_size: int | None = None) -> str:
        """
        Construye una respuesta usando el estado actual de la sesión.
        """
        if intent == "close_call":
            return "Perfecto, cierro la llamada. Gracias por contactar con nosotros."

        if extracted_name and session["caller_name"] is None:
            return f"Encantado, {extracted_name}. ¿En qué puedo ayudarte hoy?"

        if session["caller_name"] is None:
            return "Hola, antes de continuar, ¿podrías indicarme tu nombre y apellidos?"

        if intent == "reservation":
            return f"Perfecto, {session['caller_name']}. Entiendo que quieres hacer una reserva. ¿Para cuántas personas sería?"

        if intent == "provide_party_size" and extracted_party_size is not None:
            return f"Perfecto, {session['caller_name']}. Queda anotado: reserva para {extracted_party_size} personas. De momento damos por recogida la solicitud."

        if intent == "business_hours":
            return f"Perfecto, {session['caller_name']}. Entiendo que quieres consultar el horario. En una versión futura lo consultaré automáticamente."

        if intent == "support":
            return f"Entendido, {session['caller_name']}. Veo que necesitas ayuda o soporte. Vamos a recoger más información."

        if session["caller_name"] and session["call_goal"] is None:
            return f"Entendido, {session['caller_name']}. ¿Qué necesitas exactamente con esta llamada?"

        return f"No he entendido bien la solicitud, {session['caller_name']}. ¿Podrías reformularla, por favor?"

    def extract_party_size(self, user_text: str) -> int | None:
        """
        Intenta extraer el número de personas.

        Casos válidos:
        - para 4 personas
        - somos 4
        - 4 personas
        - para cuatro personas
        """
        text = user_text.lower()

        word_to_number = {
            "una": 1,
            "uno": 1,
            "dos": 2,
            "tres": 3,
            "cuatro": 4,
            "cinco": 5,
            "seis": 6,
            "siete": 7,
            "ocho": 8,
            "nueve": 9,
            "diez": 10,
        }

        digit_match = re.search(r"\b(\d+)\b", text)
        if digit_match:
            return int(digit_match.group(1))

        for word, value in word_to_number.items():
            if re.search(rf"\b{word}\b", text):
                return value

        return None

# Instancia simple reutilizable
conversation_service = ConversationService()