#Librerias
import requests
from lxml import html

#Clave-Valor
encabezados={
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
}
#Definicion de la URL
url= "https://www.wikipedia.org/"
#Utilizamos get, pasando la URL y el headers
respuesta = requests.get(url,headers=encabezados)
#fromstring obtenemos el valor de la cadena
parser = html.fromstring(respuesta.text)
#Obtenemos una sola cadena de texto
ingles=parser.xpath("//*[ @id='js-link-box-en']/strong/text()")
print('El valor de la primera cadena es: ',ingles)
#Obtenemos todos los idiomas
idiomas = parser.xpath("//div[contains(@class, 'central-featured-lang')]//strong/text()")
i=0
for x in idiomas:
    i += 1
    print('El valor ',i, 'es el idioma: ', x)

i=0

#Obtenemos toda la clase
idiomas= parser.find_class('central-featured-lang')
#Iteramos la lista
for x in idiomas:
    i +=1
    print('El valor ', i, 'es el idioma: ', x.text_content())

# // Busqueda en cualquier parte del documento
# / Busqueda en el nivel de Raiz
# [] Predicados
# [@ id ="titulo" and, or @id="titulo"] Busqueda por atributos
#[@ id ="titulo" and, or @id="titulo"]//Busqueda en todos los hijos
