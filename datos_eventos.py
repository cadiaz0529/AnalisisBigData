from bs4 import BeautifulSoup
import requests
import re

"""
-Administración: https://administracion.uniandes.edu.co/index.php/es/facultad/sobre-la-facultad/eventos/icalrepeat.detail/2016/08/30/110/-/la-importancia-de-hacer-networking
-Facartes: https://facartes.uniandes.edu.co/index.php/eventos/icalrepeat.detail/2016/08/26/505/-/utopias-500-anos-del-libro-de-tomas-moro-iii-encuentro-de-estudios-interdisciplinarios-sobre-renacimiento-y-barroco
-Ciencias: http://ciencias.uniandes.edu.co/eventos/iii-workshop-on-adsorption-catalysis-and-porous-materials
-Derecho: https://derecho.uniandes.edu.co/es/facultad/eventos/icalrepeat.detail/2016/08/01/803/-/city-governance-in-an-age-of-diversity-university-of-chicago-press-2012
-Economía: https://economia.uniandes.edu.co/facultad/eventos-economia/?task=item.listevents&view=item&layout=detailevents&evento=450&5-Congreso-de-Econom%C3%ADa-Colombiana-
-Ingeniería: http://ingenieria.uniandes.edu.co/Paginas/DetalleEventos.aspx?eid=5
-Medicina: https://medicina.uniandes.edu.co/index.php/es/component/jevents/icalrepeat.detail/2016/08/16/95/-/ceremonia-de-batas-blancas
-Egob: https://egob.uniandes.edu.co/index.php/es/me-noticias-y-eventos/me-eventos/eventodetalle/148/-/inicio-de-clases
-Cider: http://cider.uniandes.edu.co/Paginas/DetalleEventos.aspx?eid=16
"""

r=requests.get('https://administracion.uniandes.edu.co/index.php/es/facultad/sobre-la-facultad/eventos/icalrepeat.detail/2016/08/30/110/-/la-importancia-de-hacer-networking')
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
