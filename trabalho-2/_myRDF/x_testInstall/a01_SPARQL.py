# -*- coding: cp1252 -*-
# ===============================
# author: Paulo Trigo Silva (PTS)
# version: v08
# uses: rdflib-4.2.2
# not needed anymore: rdfextras-0.4.tar
# to: testar utilizacao do SPARQL
# comment: 6th Python3 version 
# ===============================

#_______________________________________________________________________________
# Considerar exemplo de apoio em:
# http://code.google.com/p/rdflib/source/browse/IntroSparql.wiki?repo=wiki&r=f01f522873a72af773ecb399b61364c0f68dd1c9
# (ja nao e necessario pois o SPARQL ja esta incluido (apos versao 4.1.1 do RDFLib)
  

#_______________________________________________________________________________
# Importar modulos
import rdflib
from rdflib import ConjunctiveGraph, Graph
from rdflib  import Namespace
import io
# from version 4.1.1 we do not need to set SPARQL as a plgin (it is already included)
#from rdflib import plugin



#_______________________________________________________________________________
# Registar o "plugin" com o SPARQL ja nao e necessario
#rdflib.plugin.register( 'sparql', rdflib.query.Processor, \
#                        'rdfextras.sparql.processor', 'Processor' )
#rdflib.plugin.register( 'sparql', rdflib.query.Result, \
#                        'rdfextras.sparql.query', 'SPARQLQueryResult' )



#_______________________________________________________________________________
# O "namespace" usado nestes exemplos
FBNAMESPACE = Namespace( "http://rdf.freebase.com/ns/" )
# como curiosidade ver a pagina: http://rdf.freebase.com/rdf/film


#_______________________________________________________________________________
# Exemplo1
g = ConjunctiveGraph()
g.parse( "moviedata-small.n3", format="n3" )

result = g.query(
    """
    SELECT ?film ?year
    WHERE { ?film fb:film.film.initial_release_date ?year. }""", \
    initNs={'fb':FBNAMESPACE})
for triple in result: print( triple )
print( "\n ok-1 \n" )


#_______________________________________________________________________________
# Exemplo2
gA = ConjunctiveGraph()
gA.parse( "moviedata-small.n3", format="n3" )
q1 = \
   """
   CONSTRUCT
   {
   ?who <http://employment.history/was_employed_in> ?year .
   ?who fb:type.object.name ?name .
   }
   WHERE
   {
   ?film fb:film.film.starring ?who .
   ?film fb:film.film.initial_release_date ?year .
   ?who fb:type.object.name ?name .
   FILTER( ?year > "2002" )
   }
   """

q1Result = gA.query(
    q1, \
    initNs={ 'fb':FBNAMESPACE } )

print( q1Result.serialize( format="n3" ) ) # format="xml"
print( "\n ok-2 \n" )


#_______________________________________________________________________________
# Exemplo3
gB = ConjunctiveGraph()
#gB = Graph()
q1Result = q1Result.serialize( format="n3" )
gB.parse( data=q1Result, format="n3" )

q2 = \
    """
    SELECT ?who ?name
    WHERE { ?who fb:type.object.name ?name. }
    """

q2Result = gB.query(
    q2, \
    initNs={ 'fb':FBNAMESPACE } )
for triple in q2Result: print( triple )
print( "\n ok-3 \n" )


#_______________________________________________________________________________
# Exemplo4
## Composicao de interrogacoes: q2 o q1
gC = ConjunctiveGraph()
#r = gC.parse( StringIO( g.query( q1, initNs={'fb':FBNAMESPACE} ).serialize( format="n3" ) ), format="n3" ). \
#        query( q2, initNs={ 'fb':FBNAMESPACE } )

r = gC.parse( data = g.query( q1, initNs={'fb':FBNAMESPACE} ).serialize( format="n3" ), \
              format="n3" ). \
              query( q2, initNs={ 'fb':FBNAMESPACE } )

for triple in r: print( triple )
print( "\n ok-4 \n" )


#_______________________________________________________________________________
# Exemplo5
# Diferenca de dois grafos
gB -= gA

for (s, p, o) in gB:
    s, p, o = str( s ), str( p ), str( o )
    print( ( s, p, o ) )

# resultado fomado como uma unica string
str_begin_triple = "( "
str_end_triple = " )"
list_graph = []
for triple in gB:
    str_triple = str_begin_triple
    for element in triple:
        if str_triple != str_begin_triple: str_triple += ", "
        str_triple += str( element )
    str_triple += str_end_triple
    list_graph.append( str_triple )
for i in list_graph: print( i )

print( "\n ok-5 \n" )

print( "\n\n< ok-1, ok-2, ok-3, ok-4, ok-5 >\n\n" )
#_______________________________________________________________________________
# FIM

