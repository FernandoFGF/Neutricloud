def handle_home_click(self, event):
        # Cierra la ventana actual y abre el menú
        from menu import MenuWindow  # Importación diferida
        self.close()  # Cierra la ventana actual
        self.menu_window = MenuWindow(self.user, self.password)  # Crea el menú con el usuario
        self.menu_window.show()  # Muestra el menú

def update_label_data(self, message):
        """
        Actualiza el texto de label_data con el mensaje proporcionado.
        """
        self.ui.label_data.setText(message)  # Muestra el mensaje en la etiqueta
        self.ui.label_data.setToolTip(message)  # Añade un tooltip por si el texto es largo