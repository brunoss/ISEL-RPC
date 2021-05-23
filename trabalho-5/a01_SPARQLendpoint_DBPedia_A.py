#!/usr/bin/python
# -*- coding: utf-8 -*-

# ===============================
# author: Paulo Trigo Silva (PTS)
# version: v07
# ===============================
# - Adaptacao do exemplo fornecido no SPARQLWrapper
#   de modo a funcionar com Python3
# - Integracao do SPARQLWrapper com o RDFLib de modo a gerar
#   grafo com resposta a interrogacao em endpoint-SPARQL
# - Utilizacao do formato JSON-LD (JSON for Linked Data)



#______________________________________________________________________________
# Importar modulos
from rdflib.graph import Graph
from SPARQLWrapper import SPARQLWrapper, XML, N3, TURTLE, RDF, JSON
from SPARQLWrapper import JSONLD #e' preciso instalar suporte separadamente!
import warnings



#______________________________________________________________________________
# (codigo escrito de modo sequencial - para evidenciar o essencial)
UTF_8 = "utf-8"

querySELECT = \
"""
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?label
WHERE { 
<http://dbpedia.org/resource/Asturias> rdfs:label ?label 
FILTER (lang(?label) != "ja" && lang(?label) != "zh" && lang(?label) != "ru"  && lang(?label) != "ar" && lang(?label) != "ko")
}
"""

# construcao da estrutura de conexao ao "endpoint"
sparql = SPARQLWrapper( "http://dbpedia.org/sparql" )

# atribuicao da interrogacao a executar naquele "endpoint"
sparql.setQuery( querySELECT )



###______________________________________________________________________________
### utilizar o JSON
print( '\n\n*** Exemplo JSON' )
sparql.setReturnFormat( JSON )
resultSet = sparql.query()
assert JSON == resultSet.requestedFormat
resultSet = resultSet.convert()
print( resultSet )
for info in resultSet["results"]["bindings"]:
  print( info["label"]["value"] )



###______________________________________________________________________________
### utilizar o XML
print( '\n\n*** Exemplo XML' )
sparql.setReturnFormat( XML )
resultSet = sparql.query()
assert XML == resultSet.requestedFormat
resultSetXML = resultSet.convert().toxml()
print( resultSetXML )
##
### o "resultSet" tem um iterador para percorrer os seus elementos
### o iterarador "consome" os elementos pelo que no fim "resultSet" fica vazio
print('Decode')
for i in resultSet:
   print( i.decode(UTF_8) )
print( "NOTAR QUE O resultSet FICOU VAZIO:" )
try: resultSet = resultSet.convert()
except: print()
else: print( resultSet )
print( "=================================" )

###______________________________________________________________________________
### utilizar o N3
print( '\n\n*** Exemplo N3' )
sparql.setReturnFormat( N3 )
resultSet = sparql.query()
assert N3 == resultSet.requestedFormat
resultSet = resultSet.convert()
print( resultSet )
##
##
##
### Grafo RDF (com a estrutura da resposta 'a interrogacao)
print( '\n\n*** Grafo RFF (a partir da descricao N3)' )
g = Graph()
src = resultSet
g = g.parse( data=src, format="n3" )
for (s, p, o) in g:
  print( (str(s), str(p), str(o)) )



###______________________________________________________________________________
### utilizar o JSON-LD (JSON para a Linked Data)
print( '\n\n*** Exemplo JSON-LD' )
sparql.setReturnFormat( JSONLD )
resultSet = sparql.query()
assert JSONLD == resultSet.requestedFormat
##
##
print( "Fazer \"fallback\" de JSON-LD para XML dependendo do suporte do endpoint" )
# e' preciso filtrar este tipo de excepcao pois o SPARQLWrapper
# gera uma excepcao do tipo "Warning" quando nao consegue fazer a conversao
warnings.filterwarnings( "error" )

# controlar o "fallback" (de JSNON-LD para XML)
converted = True

resultSet.requestedFormat = JSONLD
if not converted:
  try: resultSet = resultSet.convert()
  except Warning: print( ">>> endpoint nao suporta JSONLD" )
  else: print( resultSet )

resultSet.requestedFormat = XML
if not converted:
  try: resultSet = resultSet.convert()
  except Warning: print( ">>> endpoint nao suporta XML" )
  else:
    resultSetXML = resultSet.toxml()
    print( resultSetXML )
