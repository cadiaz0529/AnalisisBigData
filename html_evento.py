from bs4 import BeautifulSoup
import requests
import re

facultades=['administracion', 'facartes', 'derecho', 'economia', 'ingenieria', 'medicina', 'egob', 'cider']

for facultad in facultades:
	url='https://'+facultad+".uniandes.edu.co"
	r=requests.get(url)
	soup=BeautifulSoup(r.content, "lxml")

	anclas=soup.body.find_all("a", href=re.compile('(evento|Evento)'))

	if len(anclas)==0:
		anclas=soup.body.find_all("a", href=re.compile('(events|news|noticia|Noticia|agenda|Agenda)'))

	for ancla in anclas:
		if ancla['href'].find("cat.listevents")!=-1 or ancla['href'].find("calendar")!=-1: 
			print(url+ancla['href'])
			break
		else:
			posibles=ancla.find_all(string=re.compile('(Eventos|eventos|Ver)'))
			if len(posibles)>0:
				print(url+ancla['href'])
				break


