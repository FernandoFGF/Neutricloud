class Evento:
    def __init__(self, title, description=None, hour=None):
        self.title = title
        self.description = description  # Descripción del evento (opcional)
        self.hour = hour  # Hora en formato "HH:MM" (opcional)

    def __str__(self):
        # Devuelve una representación legible del evento
        return f"{self.title} - Descripción: {self.description}, Hora: {self.hour}"

    def to_dict(self):
        """Convierte el evento en un diccionario serializable."""
        return {
            'title': self.title,
            'description': self.description,
            'hour': self.hour
        }

    @staticmethod
    def from_dict(data):
        """Crea un objeto Evento desde un diccionario."""
        return Evento(data['title'], data.get('description'), data.get('hour'))
