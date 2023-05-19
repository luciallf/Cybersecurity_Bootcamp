# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    spider.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lucilope <lucilope@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/24 17:34:43 by lucilope          #+#    #+#              #
#    Updated: 2023/05/02 14:17:59 by lucilope         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import argparse 
import requests 
import os 
from bs4 import BeautifulSoup as sopa 
from urllib.parse import urlparse, urljoin 

urls_webs = set()
urls_imag = set()


def extraer_url(sitioweb, niv):
    try:
        r = requests.get(sitioweb)   
    except:
        print("Se ha producido un error: no se puede abrir el URL", sitioweb)
    else:
        if r.status_code == 200:
            xml = sopa(r.content, "html.parser") 
            enlaces = [enlace.get("href") for enlace in xml.find_all("a") if enlace.has_attr("href") and (enlace["href"].startswith("http://") or enlace["href"].startswith("https://"))]
            urlparseada = urlparse(sitioweb)
            esquema = urlparseada.scheme
            dominio = urlparseada.netloc
            ruta = urlparseada.path 
            if int(niv) < 1:
                return
            else:
                for enlace in enlaces:
                    if enlace is not None and enlace.startswith(esquema + "://" + dominio):
                        urlparseada_enlace = urlparse(enlace)
                        dominio_enlace = urlparseada_enlace.netloc
                        if dominio_enlace == dominio:
                            if enlace not in urls_webs:
                                urls_webs.add(enlace)
                                print(" " * niv, enlace)
                                extraer_url(enlace, niv - 1)
                    else:
                        if enlace.startswith("/") and not enlace.startswith("//"):
                            enlace_completo = esquema + "://" + dominio + enlace
                            if enlace_completo not in urls_webs:
                                urls_webs.add(enlace_completo)
                                print(" " * niv, enlace_completo)
                                extraer_url(enlace_completo, niv - 1)
            return esquema, dominio, ruta



def descargar_imagen(contains):
    for elements in urls_webs:
        try:
            i = requests.get(elements)
            if i.status_code == 200:
                xmla = sopa(i.content, "html.parser")
                img_tags = xmla.find_all('img')
        except:
            continue
        else:
            urllink = [img['src'] for img in img_tags] 
            for url in urllink:
                if url in urls_imag:
                    continue
                else:
                    try:
                        url_imag= requests.get(url)
                    except:
                        continue   
                    else:
                        if not any(ext in url for ext in extensiones):
                            continue
                        else:
                            nombre = url.split("/")[-1] 
                            if not os.path.exists(folder):
                                os.makedirs(folder)
                            with open(folder + "/" + nombre, "wb") as archivo: 
                                archivo.write(url_imag.content)
                        urls_imag.add(url)

          

if __name__ == "__main__": 

    extensiones = ['.jpg', '.jpeg', '.png', '.gif', '.bmp'] 
    

    analizador = argparse.ArgumentParser(
    description = "Herramienta de scraping de imagenes en un sitio web"
    )
    analizador.add_argument("URL", help="URL del sitio web donde se quieren descargar las imagenes") 
    analizador.add_argument("-r", help= "descarga de forma recursiva de las imágenes en la URL recibida como parámetro ", action= 'store_true') 
    analizador.add_argument("-l", help="indica el nivel de prrofundidad maximo de la descarga recursiva", type= int, default= 5 ) 
    analizador.add_argument("-p", help= "indica la ruta donde se guardarán los archivos descargados.", type= str, default= "./data/") 
    analizador.add_argument("-o", help = "Muestra las URLS al terminar", action="store_true" )

    
    args = analizador.parse_args()

    global urls, folder, niv, recursiv, orden 
    
    
    urls = args.URL
    folder = args.p
    niv = int(args.l) 
    recursiv = args.r
    orden = args.o

    if str.startswith(folder, "http") or str.startswith(folder, "file://"):
        urls = folder 
        folder = "./data/"
    
    
    try: 
        print("Analizando las páginas..")
        if recursiv:
            extraer_url(urls, niv)
        else:
            urls_webs.add(urls)
        print(f'Descargando imágenes de {urls}...')
        
        descargar_imagen(urls_imag)
        
        for link in urls_webs.copy():
            filename = os.path.basename(link)
            file_path = os.path.join(folder, filename)
            extraer_url(link, niv)
    except:
        print("Error, no se puede leer la URL correctamente")   
        