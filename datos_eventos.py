from bs4 import BeautifulSoup
import requests
import re

r=requests.get('http://ciencias.uniandes.edu.co/eventos/iii-jornadas-internacionales-de-autismo')
soup=BeautifulSoup(r.content, "lxml")
lista=soup.body.find_all(string=re.compile('III Jornadas Internacionales de Autismo'))
finish=False
for ev in lista:
	if finish: break
	success=False
	tag=ev
	i=0
	while not success:
		padre=tag.parent
		if len(padre.find_all(string=re.compile('(fecha|Fecha|agosto|Agosto)')))>0:
			success=True
			finish=True
			print(padre.text)
			break
		else:
			tag=padre
			print(i)
		i=i+1

print('Terminó')
