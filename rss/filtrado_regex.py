# script para listar los titulos de las fuentes
# se importan las librerias necesarias
import requests
import re

#fuentes
#fuentes=["http://www.bbc.com/mundo/temas/economia/index.xml","http://www.bbc.com/mundo/temas/cultura/index.xml","http://feeds.bbci.co.uk/mundo/rss.xml","http://www.huffingtonpost.es/news/es-economia/feed//","http://www.huffingtonpost.es/news/tendencias/feed//","http://www.huffingtonpost.es/feeds/verticals/spain/index.xml"]
fuentes=["bbc_cult.xml", "bbc_mun.xml", "bbc_econ.xml", "huff_tend.xml", "huff_econ.xml", "huff_vert.xml"]
#palabra = input("Ingrese su consulta:\n")
#tema = input("Ingrese su categoria\n")
#tipoBusqueda=input("Tipo de búsqueda:\n")
#entradas = []
#titulos = []
#descripciones = []
#categorias = []

def extraer_id(content):
		return int(re.search('<id>(.+?)</id>', content).group(1))

def extraer_titulo(content):
	try:
		title = re.search('<titulo>(.+?)</titulo>', content).group(1)
		title= title.replace("\\", "\n")
		return title
	except:
		return ""

def extraer_descripcion(content):
	try:
		description = re.search('<descripcion>(.+?)</descripcion>', content).group(1)
		description = description.replace("\\", "\n")
		return description
	except:
		return ""

def extraer_categoria(content):
	try:
		category = re.search('<categoria label=(.+?)/>', content).group(1)
		category = category.replace("\\", "\n")
		return category
	except: 
		return ""

def extraer_url(content):
	try:
		url = re.search('<url>(.+?)</url>', content).group(1)
		return url
	except:
		return ""

def extraer_pubdate(content):
	try:
		pubdate = re.search('<publicado>(.+?)</publicado>', content).group(1)
		return pubdate
	except:
		return ""

class Entrada(object):
	def __init__(self, content):
		self.content=content
		self.identifier=extraer_id(content)
		self.titulo=extraer_titulo(content)
		self.descripcion=extraer_descripcion(content)
		self.categoria=extraer_categoria(content)
		self.url=extraer_url(content)
		self.pubdate=extraer_pubdate(content)

	def busquedaTitulo(self, palabra): 
		if re.search('([^>]'+palabra+'[^<])', self.titulo, re.IGNORECASE ) is not None:
			return True
		else:
			return False
			
	def busquedaDescripcion(self, palabra): 
		if re.search('([^>]'+palabra+'[^<])', self.descripcion, re.IGNORECASE ) is not None:
			return True
		else:
			return False
			
	def busquedaCategoria(self, palabra): 
		if re.search('([^>]'+palabra+'[^<])', self.categoria, re.IGNORECASE ) is not None:
			return True
		else:
			return False
				

def extraer_noticias(xml):
		noticias=[]
		texto=open(xml).read()
		entradas=re.findall('<entrada>(.+?)</entrada>', texto.replace("\n", "\\").replace("\t", " "))
		for contenido in entradas:
			noticias.append(Entrada(contenido))
		return noticias

class Feed(object):
	def __init__(self, xml):
		self.xml=xml
		self.noticias=extraer_noticias(xml)

	def busqueda(self, palabra, tipoBusqueda):
		titulos=[]
		#print(len(listaEntradas[0]))
		
		if tipoBusqueda=="titulo":
			for entrada in self.noticias:		
		# expresion regular que busca los titulos dentro de las entradas previamente filtradas		
				if entrada.busquedaTitulo(palabra):
					titulos.append(entrada.titulo)
				else:
					continue
		elif tipoBusqueda=="descripcion":
			for entrada in self.noticias:		
		# expresion regular que busca los titulos dentro de las entradas previamente filtradas		
				if entrada.busquedaDescripcion(palabra):
					titulos.append(entrada.titulo)
				else:
					continue

		elif tipoBusqueda=="categoria":
			for entrada in self.noticias:		
		# expresion regular que busca los titulos dentro de las entradas previamente filtradas		
				if entrada.busquedaCategoria(palabra):
					titulos.append(entrada.titulo)
				else:
					continue

		return titulos			

			
#para iterar sobre las fuentes

def main(palabra, tipoBusqueda):
	titulos=[]
	for fuente in fuentes:
		feed=Feed(fuente)
		titulos+=feed.busqueda(palabra, tipoBusqueda)
	return titulos



