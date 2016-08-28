# Script para listar los titulos de las distintas URL usando libreria feedparser
import feedparser
import re
url_feed_lista = ["http://www.bbc.com/mundo/temas/economia/index.xml","http://www.bbc.com/mundo/temas/cultura/index.xml","http://www.huffingtonpost.es/news/es-economia/feed//","http://www.huffingtonpost.es/news/tendencias/feed//","http://www.huffingtonpost.es/feeds/verticals/spain/index.xml"]
#url_feed_lista = ["http://www.bbc.com/mundo/temas/economia/index.xml","http://www.bbc.com/mundo/temas/cultura/index.xml","http://feeds.bbci.co.uk/mundo/rss.xml","http://www.huffingtonpost.es/news/es-economia/feed//","http://www.huffingtonpost.es/news/tendencias/feed//","http://www.huffingtonpost.es/feeds/verticals/spain/index.xml"]

titulos = []
for data in url_feed_lista:
	feed = feedparser.parse(data)
	for post in feed.entries:
		titulos.append(post.title)

cadena = input("Que desea consultar?\n")
patron = "(" + cadena + (") \w+") 
print(patron)		
for f in titulos:		
	if (re.findall(patron,f)):
		print (titulos)
	

	
