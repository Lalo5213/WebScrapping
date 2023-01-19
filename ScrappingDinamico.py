"""
OBJETIVO:
    - Extraer el precio, titulo y descripcion de productos en Mercado Libre.
    - Aprender a realizar extracciones verticales y horizontales con Selenium.
    - Demostrar que Selenium no es optimo para realizar extracciones que requieren traversar mucho a traves de varias pagina de una web
    - Aprender a manejar el "retroceso" del navegador
    - Aprender a definir user_agents en Selenium
CREADO POR: Castillo Garcia Eduardo

"""

from time import sleep
from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

# Definimos el User Agent en Selenium utilizando la clase Options
opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
driver = webdriver.Chrome('./chromedriver', chrome_options=opts)

#URL SEMILLA
driver.get('https://listado.mercadolibre.com.mx/bujias')
# LOGICA DE MAXIMA PAGINACION CON LAZO WHILE
# VECES VOY A PAGINAR HASTA UN MAXIMO DE 10
PAGINACION_MAX = 10
PAGINACION_ACTUAL = 1
sleep(3) # Esperar a que todo cargue correctamente
# Debemos darle click al boton de disclaimer para que no interrumpa nuestras acciones
try: # Encerramos todo en un try catch para que si no aparece el discilamer, no se caiga el codigo
  disclaimer = driver.find_element(By.XPATH, '//button[@data-testid="action:understood-button"]')
  disclaimer.click() # lo obtenemos y le damos click
except Exception as e:
  print (e)
  None

# Mientras la pagina en la que me encuentre, sea menor que la maxima pagina que voy a sacar... sigo ejecutando...
while  PAGINACION_MAX >= PAGINACION_ACTUAL:

    link_producto=driver.find_elements(By.XPATH, '//a[@class="ui-search-item__group__element shops__items-group-details ui-search-link"]')
    links_de_la_pagina  = []
    # la mejor estrategia es obtener todos los links como cadenas de texto y luego iterarlos.
    for a_link in link_producto:
        links_de_la_pagina.append(a_link.get_attribute("href"))
    for link in links_de_la_pagina:
        sleep(2)  # Prevenir baneos de IP
        try:
            # Voy a cada uno de los links de los detalles de los productos
            driver.get(link)

            titulo=driver.find_element(By.XPATH,'//h1').text
            precio= driver.find_element(By.XPATH,'//span[contains(@class,"ui-pdp-price")]').text
            print(precio)
            print(titulo)

            # Aplasto el boton de retroceso
            driver.back()
        except Exception as e:
            print(e)
            # Si sucede algun error dentro del detalle, no me complico. Regreso a la lista y sigo con otro producto.
            driver.back()
    try:
        # Intento obtener el boton de SIGUIENTE y le intento dar click
        puedo_seguir_horizontal = driver.find_element(By.XPATH, '//span[text()="Siguiente"]')
        puedo_seguir_horizontal.click()
    except:
        # Si obtengo un error al intentar darle click al boton, quiere decir que no existe
        # Lo cual me indica que ya no puedo seguir paginando, por ende rompo el While
        break

    PAGINACION_ACTUAL += 1

