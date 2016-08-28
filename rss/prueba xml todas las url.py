# Filtro a solicitud del usuario, consulta en el titulo, el contenido o resumen, y la categoria, devuelve el titulo 

from bs4 import BeautifulSoup
from xml.dom import minidom
import requests
import re

url = ["http://www.bbc.com/mundo/temas/economia/index.xml","http://www.bbc.com/mundo/temas/cultura/index.xml","http://feeds.bbci.co.uk/mundo/rss.xml","http://www.huffingtonpost.es/news/es-economia/feed//","http://www.huffingtonpost.es/news/tendencias/feed//","http://www.huffingtonpost.es/feeds/verticals/spain/index.xml"]

palabra = input("Que desea consultar?\n")

patronTitulo = '<title(.*'+palabra+'.*?)</title>'
#patronTitulo = '<title xml:lang="es">(.*'+palabra+'.*?)</title>|<title>(.*'+palabra+'.*?)</title>'
patronDescripcion = '<content xml:lang="es">(.*'+palabra+'.*?)</content>|<summary(.*'+palabra+'.*?)</summary>'
patronCategoria = '<category xml:lang="es"(.*'+palabra+'.*?)/>'

tmatch = []
tmatch1 = str('')

for data in url:
	r = requests.get(data)
	soup = BeautifulSoup(r.text, 'xml')
	#tmatch.append(re.findall(patronTitulo, str(soup), re.IGNORECASE))
	tmatch.append(re.findall(patronTitulo+'|'+patronDescripcion+'|'+patronCategoria, str(soup), re.IGNORECASE))
	tmatch1=tmatch1+'-'+str((re.findall(patronTitulo, str(soup), re.IGNORECASE)))
	

for dato in tmatch:
	if(len(dato)!=0):
			print(tmatch1)

#if tmatch1:
#		title = tmatch.group(0)
#		print ('Titulo de pagina ' + sys.argv[1] + ' es: ' + title)
	#print (tmatch)
	