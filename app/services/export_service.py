"""
Servicio de exportación de historial (FASE2).

Objetivo:
- Guardar el historial de una sesión cerrada en un archivo .txt
- Mantener trazabilidad simple fuera de memoria
"""

from datetime import datetime
from pathlib import Path


class ExportService:
    """
    Servicio para exportar sesiones cerradas a archivos de texto.
    """

    def __init__(self) -> None:
        self.output_dir = Path("exports")
        self.output_dir.mkdir(exist_ok=True)

    def export_session_to_txt(self, session: dict) -> str:
        """
        Exporta una sesión cerrada a un archivo .txt.

        Args:
            session: diccionario con los datos de la sesión

        Returns:
            Ruta del archivo generado en texto
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = self.output_dir / f"session-call-{timestamp}.txt"

        with open(file_path, "w", encoding="utf-8") as file:
            file.write("=== SESSION EXPORT ===\n")
            file.write(f"session_id: {session['session_id']}\n")
            file.write(f"call_id: {session['call_id']}\n")
            file.write(f"customer_id: {session['customer_id']}\n")
            file.write(f"turn_count: {session['turn_count']}\n")
            file.write(f"caller_name: {session['caller_name']}\n")
            file.write(f"call_goal: {session['call_goal']}\n")
            file.write(f"party_size: {session['party_size']}\n")
            file.write(f"conversation_state: {session['conversation_state']}\n")
            file.write(f"is_closed: {session['is_closed']}\n")
            file.write("\n=== HISTORY ===\n")

            for item in session["history"]:
                file.write(f"[{item['role']}] {item['message']}\n")

        return str(file_path)

export_service = ExportService()