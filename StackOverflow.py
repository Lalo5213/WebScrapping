#Importaciones
from  bs4 import BeautifulSoup
import requests

# Definimos la información de cabecera para enviar información falsa al servidor y evitar el posible baneo o bloqueo de requests.
encabezados={
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
}
#Definicion de la URL a extraer
url= "https://es.stackoverflow.com/questions"

# Inicio de peticion al servidor
respuesta = requests.get(url,headers=encabezados)

# la función .text especifica que lo que se va a almacenar en soup es la cadena html.
# El parámetro 'lxml' es para especificar el parser que se va a utilizar,(básicamente es # para quitar el WARNING que sale en la ejecución del programa)

soup=BeautifulSoup(respuesta.text,"html.parser")
#Nota:
# Se inicia el examen visual sobre la página. Buscando un patrón común para la obtención de la info.
# Todas la preguntas están dentro de un div principal con un id de nombre 'questions'.
# el método .find, devuelve UN SOLO ELEMENTO COINCIDENTE.

contenedor=soup.find(id="questions")
# Ahora ya tenemos el foco en el grupo que contiene los títulos de la preguntas y su detalle, por lo que procederemos a la extracción.
# Recordar que la ubicación de las cadenas a extraer se consigue acercando de las etiquetas padre a las etiquetas hijas más próximas al texto a extraer.
# Eso solo se consigue haciendo un chequeo visual de la página web a través de inspección de elementos.

lista_de_preguntas=contenedor.find_all("div", class_="s-post-summary")

for x in lista_de_preguntas:
    texto=x.find('h3').text
    descripcion=x.find('div',class_="s-post-summary--content-excerpt").text
   # Formateo de la salida
    descripcion=descripcion.replace("\n",' ').replace('\r',' ').strip()

    print('Titulo de pregunta', texto)
    print(f'Detalle pregunta: {descripcion}')
    print()