from bs4 import BeautifulSoup
import requests
import re

url='http://administracion.uniandes.edu.co'
link=''

try:
	r=requests.get(url)
except:
	print("No pudo abrir: "+facultad)
	
soup=BeautifulSoup(r.content, "lxml")

anclas=soup.body.find_all("a", href=re.compile('(evento|Evento)'))

if len(anclas)==0:
	anclas=soup.body.find_all("a", href=re.compile('(events|news|noticia|Noticia|agenda|Agenda)'))

for ancla in anclas:
	if ancla['href'].find("cat.listevents")!=-1 or ancla['href'].find("calendar")!=-1: 
		print(url+ancla['href'])
		link=ancla['href']
		break
	else:
		posibles=ancla.find_all(string=re.compile('(Eventos|eventos|Ver|ver|noticia|Noticia)'))
		if len(posibles)>0:
			print(url+ancla['href'])
			link=ancla['href']
			break

r=requests.get('https://administracion.uniandes.edu.co'+link)
soup=BeautifulSoup(r.content, "lxml")

m=re.search('(.*?)(evento|Evento)(.*?)/', link)
cuerpo=soup.body
if len(cuerpo.find_all("a", href=re.compile(m.group(0)+'.*?(icalrepeat|item.listevents|detalle|Detalle)')))>0:
	anclas=cuerpo.find_all("a", href=re.compile(m.group(0)+'.*?(icalrepeat|item.listevents|detalle|Detalle)'))
elif len(cuerpo.find_all("a", href=re.compile('(events|news|noticia|Noticia|agenda|Agenda).*?(icalrepeat|item.listevents|detalle|Detalle)')))>0:
	anclas=cuerpo.find_all("a", href=re.compile('(events|news|noticia|Noticia|agenda|Agenda).*?(icalrepeat|item.listevents|detalle|Detalle)'))
else:
	anclas=cuerpo.find_all("a", href=re.compile(m.group(1)+'.*?(evento|Evento)'))
	

ancla=anclas[0]
if ancla['href']!=link:
	print(ancla['href'])
	r=requests.get('https://administracion.uniandes.edu.co'+ancla['href'])
	soup=BeautifulSoup(r.content, "lxml")
	lista=soup.body.find_all(string=re.compile('La importancia de hacer networking'))
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

print(texto)
print('Terminó')