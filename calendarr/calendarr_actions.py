from PySide6.QtWidgets import QMessageBox, QDialog, QInputDialog
from PySide6.QtCore import QTime
from calendarr.evento import Evento
from calendarr.event_ui import Ui_event  # Importar el diseño del formulario

def add_event(self):
    self.context_menu.close()
    """Añade un evento en la fecha seleccionada."""
    date = self.get_selected_date()

    # Crear una instancia del formulario
    dialog = QDialog(self)
    ui = Ui_event()  # Crea una instancia de la interfaz generada
    ui.setupUi(dialog)  # Configura el formulario en el diálogo

    # Función para cuando el botón "Confirmar" es presionado
    def on_confirm():
        event_title = ui.title.text()  # Obtener el texto del QLineEdit para el título
        event_description = ui.description.text()  # Obtener el texto del QLineEdit para la descripción
        event_hour = ui.time.time().toString("HH:mm")  # Obtener la hora del QTimeEdit

        if event_title and event_description and event_hour:
            # Crear el objeto Evento con los datos del formulario
            new_event = Evento(event_title, event_description, event_hour)

            # Si no existe una lista de eventos para esa fecha, la creamos
            if date not in self.config["events"]:
                self.config["events"][date] = []

            # Añadir el evento a la lista
            self.config["events"][date].append(new_event)
            self.config_manager.save_config(self.config)  # Usamos el save_config de ConfigManager

            QMessageBox.information(self, "Evento añadido", f"Evento '{event_title}' añadido en {date} a las {event_hour}.")
            # Resaltar los eventos en el calendario
            self.highlight_events()

            dialog.accept()  # Cerrar el diálogo después de confirmar

    # Conectar el botón "Confirmar"
    ui.confirm.clicked.connect(on_confirm)

    # Conectar el botón "Cancelar" para cerrar el diálogo sin hacer nada
    ui.cancel.clicked.connect(dialog.reject)

    # Mostrar el formulario y esperar la confirmación
    dialog.exec()

def edit_event(self):
    self.context_menu.close()
    """Modifica un evento existente."""
    date = self.get_selected_date()  # Obtener la fecha seleccionada
    if date in self.config["events"] and self.config["events"][date]:
        events = self.config["events"][date]  # Obtener los eventos para esa fecha

        # Generar la lista de eventos, convertidos a cadenas legibles
        event_list = [evento.title for evento in events]  # Solo los títulos de los eventos

        # Mostrar el cuadro de diálogo para seleccionar el evento a modificar
        event_name, ok = QInputDialog.getItem(self, "Modificar evento", 
                                              f"Selecciona un evento en {date}:",  # Título del cuadro de diálogo
                                              event_list,  # Lista de eventos para seleccionar
                                              0,  # Seleccionar el primer evento por defecto
                                              False)  # No editable

        if ok and event_name:
            # Buscar el evento seleccionado
            event_to_edit = next((evento for evento in events if evento.title == event_name), None)
            if event_to_edit:
                # Crear una instancia del formulario de edición
                dialog = QDialog(self)
                ui = Ui_event()  # Crear la instancia de la interfaz de evento
                ui.setupUi(dialog)  # Configurar el formulario en el diálogo

                # Rellenar los campos con los datos del evento actual
                ui.title.setText(event_to_edit.title)  # Rellenar el título
                ui.description.setText(event_to_edit.description)  # Rellenar la descripción
                ui.time.setTime(QTime.fromString(event_to_edit.hour, "HH:mm"))  # Rellenar la hora

                # Función para cuando el botón "Confirmar" es presionado
                def on_confirm():
                    # Tomar los nuevos valores del formulario
                    event_title = ui.title.text()
                    event_description = ui.description.text()
                    event_hour = ui.time.time().toString("HH:mm")

                    if event_title and event_description and event_hour:
                        # Actualizar el evento con los nuevos datos
                        event_to_edit.title = event_title
                        event_to_edit.description = event_description
                        event_to_edit.hour = event_hour

                        # Guardar los cambios
                        self.config_manager.save_config(self.config)
                        QMessageBox.information(self, "Evento modificado", f"Evento '{event_title}' modificado en {date}.")
                        self.highlight_events()  # Resaltar los eventos en el calendario

                        dialog.accept()  # Cerrar el diálogo después de confirmar

                # Conectar el botón "Confirmar" para guardar los cambios
                ui.confirm.clicked.connect(on_confirm)

                # Conectar el botón "Cancelar" para cerrar el diálogo sin hacer nada
                ui.cancel.clicked.connect(dialog.reject)

                # Mostrar el formulario de edición
                dialog.exec()

    else:
        QMessageBox.warning(self, "Modificar evento", "No hay eventos en esta fecha.")

def delete_event(self):
    self.context_menu.close()
    """Elimina un evento de la fecha seleccionada."""
    date = self.get_selected_date()  # Obtener la fecha seleccionada
    if date in self.config["events"] and self.config["events"][date]:
        events = self.config["events"][date]  # Obtener los eventos para esa fecha

        # Generar la lista de eventos, mostrando solo los títulos
        event_list = [evento.title for evento in events]  # Usamos solo los títulos de los eventos

        # Mostrar el cuadro de diálogo para seleccionar el evento a eliminar
        event_name, ok = QInputDialog.getItem(self, "Eliminar evento", 
                                              f"Selecciona un evento en {date}:",  # Título del cuadro de diálogo
                                              event_list,  # Lista de eventos para seleccionar
                                              0,  # Seleccionar el primer evento por defecto
                                              False)  # No editable

        if ok and event_name:
            # Buscar el evento seleccionado por su título
            event_to_delete = next((evento for evento in events if evento.title == event_name), None)
            if event_to_delete:
                events.remove(event_to_delete)  # Eliminar el evento de la lista

                # Si ya no hay eventos para esa fecha, eliminar la fecha del diccionario
                if not events:
                    del self.config["events"][date]

                # Guardar los cambios en el archivo de configuración
                self.config_manager.save_config(self.config)

                # Mostrar mensaje de confirmación
                QMessageBox.information(self, "Evento eliminado", f"Evento '{event_name}' eliminado de {date}")
                self.highlight_events()  # Resaltar los eventos en el calendario

    else:
        QMessageBox.warning(self, "Eliminar evento", "No hay eventos en esta fecha.")
