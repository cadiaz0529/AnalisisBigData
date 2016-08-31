

############################################################################

def extraer_info(self):
		r=requests.get(self.url)
		soup=BeautifulSoup(r.content, "lxml")
		self.nombre=soup.title.text
		"""
		if self.nombre.find("...")!=-1:
			name=re.search('(([0-90-9]:[0-90-9][a|p]m)?(.+?))\.\.\.', self.nombre).group(1)
			if re.search('([0-90-9]:[0-90-9][a|p]m)', name) is None:
				lista=soup.body.find_all(string=re.compile(name.strip()))
			else:
				lista=soup.body.find_all(string=re.compile(name[7:].strip()))
		else:
			lista=soup.body.find_all(string=re.compile(self.nombre))

		finish=False
		max_depth=0
		texto=""
		for ev in lista:
			tag=ev
			success=False
			i=0
			while not success:
				padre=tag.parent
				if len(padre.find_all(string=re.compile('(fecha|Fecha|agosto|Agosto)')))>0:
					success=True
					if len(ev.find_parents())>=max_depth:
						texto=padre.text
						max_depth=len(ev.find_parents())
					break
				else:
					tag=padre
				i=i+1
		"""
		return self.nombre

def link_eventos(self):
		try:
			r=requests.get(self.url)
		except:
			print("No pudo abrir: "+self.nombre)
			return ""

		soup=BeautifulSoup(r.content, "lxml")

		anclas=soup.body.find_all("a", href=re.compile('(evento|Evento)'))

		if len(anclas)==0:
			anclas=soup.body.find_all("a", href=re.compile('(events|news|noticia|Noticia|agenda|Agenda)'))

		for ancla in anclas:
			if ancla['href'].find("cat.listevents")!=-1 or ancla['href'].find("calendar")!=-1: 
				return ancla['href']
			else:
				posibles=ancla.find_all(string=re.compile('(Eventos|eventos|Ver|ver|noticia|Noticia)'))
				if len(posibles)>0 and not ancla['href'].startswith('http://'):
					return ancla['href']
		return ""

def lista_eventos(self, link):
		if link[-1]=="-": new_link=link[:-1]
		else: new_link=link+"/"

		eventos=list()

		r=requests.get(self.url+link)
		soup=BeautifulSoup(r.content, "lxml")
		cuerpo=soup.body

		m=re.search('(.*?)(evento|Evento)(.*?)/', new_link)
		
		if len(cuerpo.find_all("a", href=re.compile(m.group(0)+'.*?(icalrepeat|item.listevents|detalle|Detalle)')))>0:
			anclas=cuerpo.find_all("a", href=re.compile(m.group(0)+'.*?(icalrepeat|item.listevents|detalle|Detalle)'))
		elif len(cuerpo.find_all("a", href=re.compile('(events|news|noticia|Noticia|agenda|Agenda).*?(icalrepeat|item.listevents|detalle|Detalle)')))>0:
			anclas=cuerpo.find_all("a", href=re.compile('(events|news|noticia|Noticia|agenda|Agenda).*?(icalrepeat|item.listevents|detalle|Detalle)'))
		else:
			anclas=cuerpo.find_all("a", href=re.compile(m.group(1)+'.*?(evento|Evento)'))
			

		for ancla in anclas:
			if ancla['href']!=link and not ancla['href'].startswith('http://'):
				eventos.append(ancla)

		return eventos


def extraer_eventos(self, unidad):
		url='http://'+unidad+'.uniandes.edu.co'
		unit=Unidad(url, unidad)
		link=unit.link_eventos()
		eventos=unit.lista_eventos(link)
		evento=Evento(url+eventos[0]['href'])
		print(unidad.upper()+"\n\n"+evento.extraer_info()+"\n\n")
		print(link+"\n\n")

