from bs4 import BeautifulSoup
import requests
import re

"""
-Administración: /index.php/es/facultad/sobre-la-facultad/eventos/cat.listevents/2016/08/27/-
-Facartes: /index.php/eventos
-Ciencias: /eventos
-Derecho: /es/facultad/eventos
-Economía: /facultad/eventos-economia/cat.listevents/2016/08/27/-
-Ingeniería: /Paginas/Eventos.aspx
-Medicina: /index.php/es/facultad/eventos/month.calendar/2016/08/27/-
-Egob: /index.php/es/me-noticias-y-eventos/me-eventos/month_calendar/2016/08/-
-Cider: /Paginas/Eventos.aspx
"""

link='/es/facultad/eventos/'
r=requests.get('https://derecho.uniandes.edu.co'+link)
soup=BeautifulSoup(r.content, "lxml")

m=re.search('(.*?)(evento|Evento)(.*?)/', link)
cuerpo=soup.body
if len(cuerpo.find_all("a", href=re.compile(m.group(0)+'.*?(icalrepeat|item.listevents|detalle|Detalle)')))>0:
	anclas=cuerpo.find_all("a", href=re.compile(m.group(0)+'.*?(icalrepeat|item.listevents|detalle|Detalle)'))
elif len(cuerpo.find_all("a", href=re.compile('(events|news|noticia|Noticia|agenda|Agenda).*?(icalrepeat|item.listevents|detalle|Detalle)')))>0:
	anclas=cuerpo.find_all("a", href=re.compile('(events|news|noticia|Noticia|agenda|Agenda).*?(icalrepeat|item.listevents|detalle|Detalle)'))
else:
	anclas=cuerpo.find_all("a", href=re.compile(m.group(1)+'.*?(evento|Evento)'))
	

for ancla in anclas:
	if ancla['href']!=link:
		print(ancla['href'])
