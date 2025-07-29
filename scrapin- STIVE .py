import requests
from bs4 import BeautifulSoup
# busca todos los elementos de la etiqueta <A> de HTML #

url = input( "INGRESA LA URL ->  : " )


responder = requests.get(url)


if responder.status_code == 200:
    soup = BeautifulSoup(responder.text, 'html.parser')
    enlace = soup.find_all('a')

    for link in enlace:
        print("-> ",link.get('href'),"\n")
else:
    print('Error al cargar la página:', responder.status_code)
