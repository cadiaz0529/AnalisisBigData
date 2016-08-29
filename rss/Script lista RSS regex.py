# script para listar los titulos de las fuentes
# se importan las librerias necesarias
import requests
import re

#fuentes
fuentes=["http://www.bbc.com/mundo/temas/economia/index.xml","http://www.bbc.com/mundo/temas/cultura/index.xml","http://feeds.bbci.co.uk/mundo/rss.xml","http://www.huffingtonpost.es/news/es-economia/feed//","http://www.huffingtonpost.es/news/tendencias/feed//","http://www.huffingtonpost.es/feeds/verticals/spain/index.xml"]


entradas = []
titulos = []
#para iterar sobre las fuentes
for fuente in fuentes:
	r=requests.get(fuente)
	#expresion regular que busca las entradas entry<> en cada fuente
	listaEntradas = re.findall(r'<entry>((.|\n)*?)</entry>', r.text)
	print("------------------")
	for entrada in listaEntradas:	
		# expresion regular que busca los titulos dentro de las entradas previamente filtradas
		titulo=re.findall(r'<title.*?>(.*?)</title>',str(entrada))
		for tit in titulo:
			print(tit)
#arreglo de titulos
			titulos.append(tit)
#print(titulos)

