#!/usr/bin/python
# -*- coding: utf-8 -*-

# ===============================
# author: Paulo Trigo Silva (PTS)
# version: v07
# ===============================
# Adaptacao do exemplo fornecido no SPARQLWrapper
# de modo a funcionar com Python3


#______________________________________________________________________________
# Importar modulos
from SPARQLWrapper import SPARQLWrapper, XML, N3, TURTLE, RDF, JSON, JSONLD
from x_util_JSON import getResultSet


#______________________________________________________________________________
# (codigo escrito de modo sequencial - para evidenciar o essencial)
querySELECT = \
"""
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?person ?party ?name
WHERE
{
  ?person <http://dbpedia.org/ontology/birthPlace> <http://dbpedia.org/resource/Asturias> 
  OPTIONAL {
    ?person <http://dbpedia.org/property/party> ?party .
    ?person <http://dbpedia.org/property/name> ?name }
}
LIMIT 15
"""

#querySELECT = \
"""
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?person ?party ?name
WHERE
{
  ?person <http://dbpedia.org/ontology/birthPlace> <http://dbpedia.org/resource/Asturias> 
  OPTIONAL { ?person <http://dbpedia.org/property/party> ?party }
  OPTIONAL { ?person <http://dbpedia.org/property/name> ?name }
}
LIMIT 15
"""


sparql = SPARQLWrapper( "http://dbpedia.org/sparql" )
sparql.setQuery( querySELECT )



# JSON
print( '\n\n*** Exemplo JSON' )
sparql.setReturnFormat( JSON )
resultSet = sparql.query().convert()
for result in resultSet["results"]["bindings"]:
   if "party" in result:
      print( "* " + \
             result["person"]["value"] + " ** " + \
             result["party"]["value"] )
   else:
      print( result["person"]["value"] )


print( "\n\n" )
print( ">>> usar a funcao getResultSet implementada em x_util_JSON.py" )
for r in getResultSet( resultSet ): print( r )



