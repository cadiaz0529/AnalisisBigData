from bs4 import BeautifulSoup
import requests
import re

class Evento(object):
	def __init__(self, url):
		self.nombre=""
		self.fecha=""
		self.hora=""
		self.lugar=""
		self.nom_contacto=""
		self.corr_contacto=""
		self.mas_info=""
		self.resumen=""
		self.keywords=""
		self.url=url

		def get_info(self):
			return True


class Unidad(object):
	def __init__(self, url, nombre):
		self.url=url
		self.nombre=nombre

	def html_content(self, link):
		r=requests.get(link)
		soup=BeautifulSoup(r.content, "lxml")
		return soup

	def get_calendarios(self):
		ans=[]
		html=self.html_content(self.url)
		candidatos=html.find_all("a", href=re.compile('month.calendar'))
		for candidate in candidatos:
			if re.search("([E|e]ventos?|agenda)", candidate['href']) is not None:
				ans.append(candidate['href'])
		return ans


	def get_tablas(self):
		ans=[]
		html=self.html_content(self.url)
		candidatos=html.find_all("a", href=re.compile('(cat.listevents|icagenda)'))
		for candidate in candidatos:
			if re.search("([E|e]ventos?|agenda)", candidate['href']) is not None:
				ans.append(candidate['href'])
		return ans

	def get_simples(self):
		ans=[]
		html=self.html_content(self.url)
		candidatos=html.find_all("a", href=re.compile('[E|e]ventos?'))
		for candidate in candidatos:
			ans.append(candidate['href'])
		return ans


	def get_link_noticias(self):
		ans=[]
		html=self.html_content(self.url)
		candidatos=html.find_all("a", href=re.compile('([N|n]oticias|[N|n]ews)'))
		for candidate in candidatos:
			ans.append(candidate['href'])
		print(ans)

	def get_link_eventos(self):
		simples=self.get_simples()
		calendars=self.get_calendarios()
		tables=self.get_tablas()
		print(simples)
		print(calendars)
		print(tables)
		if len(simples)==0 and len(calendars)==0 and len(tables)==0:
			self.get_link_noticias()


	def lista_anual(self):
		return True

	def get_slides(self):
		return True

	def get_lista_eventos(self):
		return True

	def in_uniandes(self):
		return True

	def relative_link(self):
		return True

	def pass_heuristics(self):
		return True


class Crawler(object):
	def __init__(self):
		self.name="Crawlie"

	def get_unidades(self):
		return True

	def extraer_eventos(self, name):
		url='http://'+name+'.uniandes.edu.co'
		unidad=Unidad(url, name)
		unidad.get_link_eventos()


crawlie=Crawler()
facultades=['administracion', 'arqdis', 'facartes', 'ciencias', 'derecho', 'economia', 'cife', 'ingenieria', 'medicina', 'egob', 'cider']
departamentos=['ceper', 'antropologia', 'arquitectura', 'arte', 'c-politica', 'cienciasbiologicas', 'design', 'filosofia', 'fisica', 'geociencias', 'historia', 'literatura', 'ingbiomedica', 'civil', 'electrica', 'industrial', 'mecanica', 'ingquimica', 'sistemas', 'lenguas', 'matematicas', 'musica', 'psicologia', 'quimicapr']

for facultad in facultades:
	print(facultad.upper()+"\n\n")
	try:
		crawlie.extraer_eventos(facultad)
		print("\n\n")
	except:
		print("No se pudo para: "+facultad)
		continue
