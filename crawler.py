from bs4 import BeautifulSoup
import requests
import re

def remove_duplicates(lista):
	return list(set(lista))

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

	def relative_link(self, link):
		if link.startswith("http"): return link
		else: return self.url+link

	def get_calendarios(self):
		ans=[]
		html=self.html_content(self.url)
		candidatos=html.find_all("a", href=re.compile('month.calendar'))
		for candidate in candidatos:
			if re.search("([E|e]vento?s?|agenda)", candidate['href']) is not None:
				ans.append(candidate['href'])
		ans=remove_duplicates(ans)
		print(ans)
		return ans


	def get_tablas(self):
		ans=[]
		html=self.html_content(self.url)
		candidatos=html.find_all("a", href=re.compile('(cat.listevents|icagenda)'))
		for candidate in candidatos:
			if re.search("([E|e]ventos?|agenda)", candidate['href']) is not None:
				ans.append(candidate['href'])
		ans=remove_duplicates(ans)
		print(ans)
		return ans

	def get_simples(self):
		ans=[]
		html=self.html_content(self.url)
		candidatos=html.find_all("a", href=re.compile('([E|e]vento|[E|e]vento)'))
		for candidate in candidatos:
			if candidate['href'].find(".uniandes.edu.co")==-1: continue
			ans.append(candidate['href'])
		ans=remove_duplicates(ans)
		print(ans)
		return ans

	def get_lista_eventos(self, page, tipo):
		html=self.html_content(self.relative_link(page))
		if tipo=='CALENDARIO':
			link_lista_anual=html.find("a", href=re.compile('year.listevents'))
			if link_lista_anual is not None:
				html_lista_anual=self.html_content(self.relative_link(link_lista_anual['href']))
				eventos=html_lista_anual.find_all("a", href=re.compile('icalrepeat'))
			else:
				eventos=html.find_all("a", href=re.compile('(evento.*?detalle|detalle.*?evento)'))

		elif tipo=='TABLE':
			eventos=html.find_all("a", href=re.compile('(icalrepeat|layout=.*?event)'))

		elif tipo=='SIMPLE':
			eventos=html.find_all("a", href=re.compile(page))

		eventos=remove_duplicates(eventos)
		return eventos

	def get_link_noticias(self):
		ans=[]
		html=self.html_content(self.url)
		candidatos=html.find_all("a", href=re.compile('([N|n]oticias|[N|n]ews)'))
		for candidate in candidatos:
			ans.append(candidate['href'])
		ans=remove_duplicates(ans)
		print(ans)

	def get_link_eventos(self):
		simples=self.get_simples()
		calendars=self.get_calendarios()
		tables=self.get_tablas()
		if len(calendars)>0:
			for link in calendars:
				eventos=self.get_lista_eventos(link, 'CALENDARIO')
				eventos=remove_duplicates(eventos)
				if len(eventos)>0:
					print(eventos)
					return eventos
		elif len(tables)>0:
			for link in tables:
				eventos=self.get_lista_eventos(link, 'TABLE')
				eventos=remove_duplicates(eventos)
				if len(eventos)>0:
					print(eventos)
					return eventos
		else:
			for link in simples:
				eventos=self.get_lista_eventos(link, 'SIMPLE')
				eventos=remove_duplicates(eventos)
				if len(eventos)>0:
					print(eventos)
					return eventos
		
		if len(simples)==0 and len(calendars)==0 and len(tables)==0:
			self.get_link_noticias()
			return []


	def lista_anual(self):
		return True

	def get_slides(self):
		ans=[]
		html=html_content(self.url)
		lista=html.ul(class_=re.compile('slide')).find_all("li")
		for slide in lista:
			ans.append(slide['href'])
		ans=remove_duplicates(ans)
		return ans

	def in_uniandes(self):
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

"""
for facultad in departamentos:
	print(facultad.upper()+"\n\n")
	try:
		crawlie.extraer_eventos(facultad)
		print("\n\n")
	except:
		print("No se pudo para: "+facultad)
		continue
"""
crawlie.extraer_eventos('matematicas')

"""
arquitectura
design
literatura --- manda a eventos
ingbiomedica --- sobre la página
industrial --- manda a eventos
sistemas --- manda a eventos
matematicas
musica
psicologia

"""

