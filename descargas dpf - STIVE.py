import requests

def descargar_archivo(url, destino):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        with open(destino, 'wb') as archivo_pdf:
            archivo_pdf.write(response.content)

        print(f"Descarga exitosa. Archivo guardado en: {destino}")

    except requests.exceptions.RequestException as e:
        print(f"Error al descargar el archivo: {e}")

if __name__ == "__main__":
    
    url_archivo =input("=> ") 
    ruta_destino = "archivo.pdf"  

    descargar_archivo(url_archivo, ruta_destino)
