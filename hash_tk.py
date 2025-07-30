import tkinter as tk
import hashlib
#cifrar paralbras

def generar_hash(algoritmo):
    mensaje = entrada.get()
    hash_objeto = algoritmo()
    mensaje_hash = mensaje.encode("utf-8")
    hash_objeto.update(mensaje_hash)
    hash_resultado = hash_objeto.hexdigest()
    resultado.config(text="Texto = " + mensaje + "\nResultado del texto: " + hash_resultado)

ventana = tk.Tk()
ventana.title("Hash")

entrada = tk.Entry(ventana)
entrada.grid(row=0, column=0, padx=10)

boton256 = tk.Button(ventana, text="SHA-256", command=lambda: generar_hash(hashlib.sha256))
boton256.grid(row=0, column=1)

boton384 = tk.Button(ventana, text="SHA-384", command=lambda: generar_hash(hashlib.sha384))
boton384.grid(row=0, column=2)

boton512 = tk.Button(ventana, text="SHA-512", command=lambda: generar_hash(hashlib.sha512))
boton512.grid(row=0, column=3)

resultado = tk.Label(ventana, text="")
resultado.grid(row=1, column=0, columnspan=4, pady=10)

ventana.mainloop()
