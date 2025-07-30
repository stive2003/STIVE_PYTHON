import tkinter as tk
#falta mejorar, algunas teclas hacen que salgan del programa
class PantallaCompleta(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configurar la ventana
        self.attributes('-fullscreen', True)  # Pantalla completa
        self.configure(background='black')   # Color de fondo negro

        # Bloquear la tecla Escape 
        self.bind('<Escape>', lambda event: "break")

        # Agregar contenido
        self.label = tk.Label(self, text="FUISTE HACKEADO", font=('Helvetica', 24), fg='white', bg='black')
        self.label.pack(padx=20, pady=20)

    def salir(self, event=None):
        # Método para salir de la aplicación
        self.destroy()

if __name__ == "__main__":
    app = PantallaCompleta()
    app.mainloop()
