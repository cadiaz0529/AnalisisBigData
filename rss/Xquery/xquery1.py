# encoding: utf-8

import simplexquery as ohh

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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
# query='for $prod in doc("catalog.xml")/catalog/product[@dept="ACC"] order by $prod/name return $prod/name'
# query='for $prod in doc("output1.xml")/entry order by $prod/title return $prod/title'
# query='for $prod in doc("output1.xml")/entry order by $prod/title return data($prod/title)'
# query='xquery version "1.0"; for $prod in doc("output1.xml")/entry order by $prod/title return data($prod/title)'
query='xquery version "1.0"; for $prod in doc("output1.xml")/entry return data($prod/title)'

# query='xquery version "1.0"; for $prod in doc("bbc_cult.xml")/feed/entrada return data($prod/id)'
# query='xquery version "1.0"; for $prod in doc("bbc_cult.xml")/feed/entrada return data($prod/titulo)'

print(sys.getdefaultencoding())

x=ohh.execute_all(query)
#print(ohh.execute(query))
#print([y.encode('utf-8') for y in x])
#print([y.encode('iso-8859-1') for y in x])
#print([y.encode('utf-8') for y in x])
#print([y.index(u'ó') for y in x])
#print([y.index('ó') for y in x]) --Entiende UTF-8 OK

# print([y.encode('iso-8859-1') for y in x])
print([y.index('ó') for y in x])
print([y for y in x])

#doc=open("output.txt",'w')
#doc.write(x.encode('utf8'))
#doc.close()
#print(x)
#print(type(x))