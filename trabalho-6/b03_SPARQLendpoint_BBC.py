#!/usr/bin/python
# -*- coding: utf-8 -*-

# ===============================
# author: Paulo Trigo Silva (PTS)
# version: v08
# v03: inclui "query_convert()"
# v08: inclui tratamento "fino" de excepcoes
# ===============================
# Utilizacao do SPARQLWrapper
# - de modo a aceder 'a BBC


#_______________________________________________________________________________
# Ler:
# - http://blog.dbtune.org/post/2010/01/13/Live-SPARQL-end-point-for-BBC-Programmes
#
# Analisar a "Programmes Ontology" em:
# - http://www.bbc.co.uk/ontologies/programmes/2009-09-07.shtml
#
# Aceder ao site (abaixo) para confirmar o resultado das interrogacoes:
# - http://dbtune.org/bbc/programmes/test/
# notar que este site está "unavailable"
#_______________________________________________________________________________



#______________________________________________________________________________
# Importar modulos
from SPARQLWrapper import SPARQLWrapper, XML, N3, TURTLE, RDF, JSON
from x_util_JSONwithMD import getResultSet
from urllib.error import HTTPError, URLError
from SPARQLWrapper.SPARQLExceptions import EndPointNotFound, QueryBadFormed, EndPointInternalError


#______________________________________________________________________________
# Utility functions
def query_convert( connection ):
   result = None
   try: result = connection.query()
   except HTTPError: print( ">> HTTPError: http protocol error! <<" )
   except URLError: print( ">> URLError: url bad formed! <<" )
   except EndPointNotFound: print( ">> EndPointNotFound: SPARQL-endpoint unavailable! <<" )
   except QueryBadFormed: print( ">> QueryBadFormed: SPARQL-query problem! <<" )
   except EndPointInternalError: print( ">> EndPointInternalError: SPARQL-endpoint error! <<" )
   except Exception as e:
      print( ">> Exception: fallback! <<" )
      print( e )
   else: result = result.convert()
   return result


#______________________________________________________________________________
# Definir SPARQL-endpoint
sparql_endpoint = "http://dbtune.org/bbc/programmes/sparql/"
repository_path = ""
repository = ""
FULL_SPARQL_ENDPOINT = sparql_endpoint + repository_path + repository
conn = SPARQLWrapper( FULL_SPARQL_ENDPOINT )

        
#______________________________________________________________________________
# (codigo escrito de modo sequencial - para evidenciar o essencial)
# q = "All programmes related to James Bond"
# (cf., http://blog.dbtune.org/post/2010/01/13/Live-SPARQL-end-point-for-BBC-Programmes)
# e ver o link> http://dbtune.org/bbc/programmes/sparql/
q = \
   """
   PREFIX po: <http://purl.org/ontology/po/>
   PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
   SELECT ?uri ?label
   WHERE
   {
   ?uri po:category <http://www.bbc.co.uk/programmes/people/bmFtZS9ib25kLCBqYW1lcyAobm8gcXVhbGlmaWVyKQ#person> .
   ?uri rdfs:label ?label .
   }
   """


# set the connection
conn.setQuery( q )

# JSON example
print( '\n\n*** JSON Example' )
conn.setReturnFormat( JSON )
result = query_convert( conn )
if result:
   for r in result["results"]["bindings"]:
      print( r["uri"]["value"] + ", " + r["label"]["value"] )

   # JSON example | iterar nos resultados usando getResultSet()
   print()
   print( "Usando getResultSet()" )
   for r in getResultSet( result ): print( r )


# XML example
print( '\n\n*** XML Example' )
conn.setReturnFormat(XML)
result = query_convert( conn )
if result: print( result.toxml() )

