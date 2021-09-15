
import os
import requests

    def baixar_fotos(url,endereco):
        dados = requests.get(url)
        if dados.status_code == requests.codes.OK:
            with open (endereco, 'wb') as nova_imagem:
                nova_imagem.write (dados.content)
        else:
            dados.raise_for_status()

    if _name_=="_main_":

        url_raiz = 'https://apod.nasa.gov/apod/ap{}.html'
        pasta = 'nasa'
        for i in range (210910,210916):
                nome_arq = os.path.join(pasta,'foto_nasa{}.img'.format(i) )
                baixar_foto(url_raiz.format(i),nome_arq)