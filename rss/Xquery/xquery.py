import simplexquery as ohh
#query = "doc(\"books.xml\")/bookstore/book"
""" ["http://www.bbc.com/mundo/temas/economia/index.xml",
     "http://www.bbc.com/mundo/temas/cultura/index.xml",
     "http://feeds.bbci.co.uk/mundo/rss.xml",
     "http://www.huffingtonpost.es/news/es-economia/feed//",
     "http://www.huffingtonpost.es/news/tendencias/feed//",
     "http://www.huffingtonpost.es/feeds/verticals/spain/index.xml"]
"""
# query = "doc('books.xml')"
# query = "doc('http://www.bbc.com/mundo/temas/economia/index.xml')"
# query='for $prod in doc("catalog.xml")/catalog/product where $prod/@dept = "ACC" order by $prod/name return $prod/name'
query='for $prod in doc("catalog.xml")/catalog/product[@dept="ACC"] order by $prod/name return $prod/name'

x=ohh.execute_all(query)
#print(ohh.execute(query))
print([y.encode('utf-8') for y in x])

#doc=open("output.txt",'w')
#doc.write(x.encode('utf8'))
#doc.close()
#print(x)
#print(type(x))