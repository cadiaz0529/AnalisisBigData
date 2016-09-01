import subprocess

def buscarTitulos(palabra):
	query=open("query", 'w+')
	query.write('for $x in doc("bbc_econ.xml")/feed/entrada return $x/titulo[contains(., "'+palabra+'")]/text()')
	query.close()

def buscarDescripciones(palabra):
	query=open("query", 'w+')
	query.write('for $x in doc("bbc_econ.xml")/feed/entrada where $x/descripcion[contains(., "'+palabra+'")] return $x/titulo/text()')
	query.close()

def buscarCatergorias(palabra):
	query=open("query", 'w+')
	query.write('for $x in doc("bbc_econ.xml")/feed/entrada where $x/categoria[contains(@label, "'+palabra+'")] return $x/titulo/text()')
	query.close()

palabra=input('Escriba una palabra:\n')
tipoBusqueda=input('Tipo de búsqueda:\n')

if tipoBusqueda=='titulo':
	buscarTitulos(palabra)
elif tipoBusqueda=='descripcion':
	buscarDescripciones(palabra)
elif tipoBusqueda=='categoria':
	buscarCatergorias(palabra)

pipe = subprocess.Popen("xqilla query", shell=True, stdout=subprocess.PIPE).stdout
output = pipe.read().decode('utf-8')
titulos=output.split("\n")[:-1]
print(titulos)
