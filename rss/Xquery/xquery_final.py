# encoding: utf-8
# Codificación de archivo. Importante para que script de python reconozca los caracteres acentuados del código fuente
# sin que genere error de compilación. Se declara comentariado

# Importación de la librería python-simplexquery
import simplexquery as sxq

# Cambio de la codificación por defecto del sistema de ASCII a UTF-8. Soluciona errores para el manejo de conversión
# de caracteres en el encodingo
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

# TEST. Verificación de la codificación por defecto del sistema. Debe ser UTF-8
# print(sys.getdefaultencoding())

# Urls de feed/rss sugeridos por Vivian para análisis
""" ["http://www.bbc.com/mundo/temas/economia/index.xml",
     "http://www.bbc.com/mundo/temas/cultura/index.xml",
     "http://feeds.bbci.co.uk/mundo/rss.xml",
     "http://www.huffingtonpost.es/news/es-economia/feed//",
     "http://www.huffingtonpost.es/news/tendencias/feed//",
     "http://www.huffingtonpost.es/feeds/verticals/spain/index.xml"]
"""

# Código para guardar en archivo.xml la información de un feed. En este caso el primer feed
# Construcción de consulta xquery
# xquery = "doc('http://www.bbc.com/mundo/temas/economia/index.xml')"
# Ejecución de consulta xquery. Trae todos los resultados como una lista de cadenas de caracteres Unicode.
# Encoding por defecto de simplexquery
# x=sxq.execute_all(xquery)
# Abre archivo escribe el flujo de información devuelto por la consulta
# file = open("output1.xml",'w')
# file.write(x.encode('utf8'))
# file.close()

# Para pruebas están los siguientes archivos xml:
# bbc_cult.xml: Archivo XML Filtrado por Carlos
# books.xml, catalog.xml order.xml, prices.xml: Archivos XML Tutorial de python-simplexquery
# output.xml: Archivo XML obtenido de BBC
# output1.xml: Mismo archivo output.xml con el espacio de nombres xmlns="http://www.w3.org/2005/Atom" eliminado de la
# etiqueta feed pues entra en conflicto con simplexquery y no permite la devolución de información con execute_all

# Consulta para traer los títulos de noticias desde feed/rss. No trae información por la presencia del espacio de
# nombres xmlns="http://www.w3.org/2005/Atom" en la etiqueta feed
# Ciclo para traer elementos /feed/entry/title
# data retorna el contenido del elemento /feed/entry/title
# xquery='xquery version "1.0"; for $noticia in doc("http://www.bbc.com/mundo/temas/economia/index.xml")/feed/entry ' \
#       'return data($noticia/title)'
# Consulta alternativa para traer los títulos de noticias desde un archivo XML (output1.xml). Se define versión de xquery
###xquery='xquery version "1.0"; for $noticia in doc("output1.xml")/feed/entry return data($noticia/title)'
# Ejecución de consulta xquery.
###x=sxq.execute_all(xquery)
# TEST. Verificación que python entiende correctamente el uso de caracteres acentuados desde el código fuente.
# print([y.index('ó') for y in x])
# TEST. Verificación del tipo de dato devuelto en la consulta xquery
# print(type(x))
# print(x[0])
# Visualización de los contenidos de la lista de resultados devueltos por la consulta xquery
# Instrucción anterior que no interpretaba correctamente caracteres Unicode
# print([y.encode('utf-8') for y in x])
###for y in x : print(y)

# MUESTRA TODOS LOS TÍTULOS
xquery='xquery version "1.0"; for $noticia in doc("output1.xml")/feed/entry return data($noticia/title)'
x=sxq.execute_all(xquery)
print('BÚSQUEDA DE TODOS LOS TÍTULOS DE NOTICIAS\n')
for y in x : print(y)

print('\n\nBÚSQUEDA POR ELEMENTO Y CONTENIDO\n')
tipoBusqueda=raw_input('Ingrese el Tipo de búsqueda: [T]-Título [D]-Descripción [C]-Categorías:\n')
palabra=raw_input('Escriba palabra a buscar:\n')
if tipoBusqueda=='T':
	textoBusqueda='TITULO'
elif tipoBusqueda=='D':
	textoBusqueda='DESCRIPCIÓN'
elif tipoBusqueda=='C':
	textoBusqueda='CATEGORÍA'
print('\n\nBÚSQUEDA EN '+textoBusqueda+' DE LA PALABRA '+palabra.upper()+'\n')

if tipoBusqueda=='T':
	##xquery='xquery version "1.0"; for $noticia in doc("output1.xml")/feed/entry return data($noticia/title)'
    xquery='xquery version "1.0"; for $noticia in doc("output1.xml")/feed/entry return $noticia/title[contains(., "'+palabra+'")]/text()'
elif tipoBusqueda=='D':
	xquery='xquery version "1.0"; for $noticia in doc("output1.xml")/feed/entry where $noticia/summary[contains(., "'+palabra+'")] return  $noticia/title/text()'
elif tipoBusqueda=='C':
	xquery='xquery version "1.0"; for $noticia in doc("output1.xml")/feed/entry where $noticia/category[contains(@label, "'+palabra+'")] return $noticia/title/text()'
else:
    print('Tipo de búsqueda no existe')

x=sxq.execute_all(xquery)
for y in x : print(y)
