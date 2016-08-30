# script para listar los titulos de las fuentes
# se importan las librerias necesarias
import requests
import re

#fuentes
fuentes=["http://www.bbc.com/mundo/temas/economia/index.xml","http://www.bbc.com/mundo/temas/cultura/index.xml","http://feeds.bbci.co.uk/mundo/rss.xml","http://www.huffingtonpost.es/news/es-economia/feed//","http://www.huffingtonpost.es/news/tendencias/feed//","http://www.huffingtonpost.es/feeds/verticals/spain/index.xml"]

palabra = input("Ingrese su consulta\n")
#tema = input("Ingrese su categoria\n")
tipoBusqueda=input("tipo de busqueda\n")
entradas = []
#titulos = []
#descripciones = []
#categorias = []

def busquedaTitulo(titulo, palabra): 
	if re.search(r"(.* " + palabra + " ).*\w+", titulo,re.IGNORECASE ) is not None:
		return True
	else:
		return False
		
def busquedaDescripcion(descripcion, palabra): 
	if re.search(r'(.* ' + palabra + ' ).*\w+', descripcion,re.IGNORECASE ) is not None:
		return True
	else:
		return False
		
def busquedaCategoria(categoria, palabra): 
	if re.search(r"(.* " + palabra + " ).*\w+", categoria,re.IGNORECASE ) is not None:
		return True
	else:
		return False
				
#para iterar sobre las fuentes
for fuente in fuentes:
	r=requests.get(fuente)
	#expresion regular que busca las entradas entry<> en cada fuente
	listaEntradas = re.findall(r'<entry>((.|\n)*?)</entry>|<item>((.|\n)*?)</item>', r.text)
	#print("------------------")
	#print(listaEntradas)

				
	def busqueda(palabra, tipoBusqueda):
		#print(len(listaEntradas[0]))
		for entrada in listaEntradas:
			if tipoBusqueda=="titulo":		
			# expresion regular que busca los titulos dentro de las entradas previamente filtradas		
				titulo=re.findall(r'<title.*?>(.*?)</title>|<title.<![CDATA*?>(.*?)]</title>',str(entrada))
				if busquedaTitulo(titulo[0], palabra):
					print(titulo)
				#else:
					#print("No encontrado")
					
			elif tipoBusqueda=="descripcion":
				print(type(entrada))
				descripcion=re.findall(r'(<description.*?>(.*?)</description>)|(<summary.*?>(.*?)</summary>)',str(entrada[0]))
				if busquedaDescripcion(descripcion[0], palabra):
					print(titulo)
				else:
					print("No encontrado")
			
			elif tipoBusqueda=="categoria":
				categoria=re.findall(r'<category.*?>(.*?)',str(entrada[0]))
				if busquedaCategoria(categoria[0], palabra):
					print(titulo)
				else:
					print("No encontrado")
			else:
				busqueda(palabra, tipoBusqueda)
		
	busqueda(palabra, tipoBusqueda)
	#print(titulo)
	
#	for tit in titulo:
#			print(tit)
#	for des in descripcion:
#			print(des)
#	for cat in categoria:
			#print(cat)

#arreglo de titulos
			#titulos.append(tit)
#print(titulos)



#patronTitulo = re.compile('<title(.*'+palabra+'.*?)</title>', re.IGNORECASE)
#patronDescripcion = re.compile('<description.*?>.*?)</description>|<summary.*?>(.*?)</summary>',  re.IGNORECASE)
#patronCategoria = re.compile('<category.*?>(.*'+palabra+'.*?)/>', re.IGNORECASE)

