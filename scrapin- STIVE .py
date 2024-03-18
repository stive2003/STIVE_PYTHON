import requests
from bs4 import BeautifulSoup


url = input( "-> " )


responder = requests.get(url)


if responder.status_code == 200:
    soup = BeautifulSoup(responder.text, 'html.parser')
    enlace = soup.find_all('a')

    for link in enlace:
        print("- ",link.get('href'),"\n")
else:
    print('Error al cargar la página:', responder.status_code)
