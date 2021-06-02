# -*- coding: cp1252 -*-
# ===============================
# author: Paulo Trigo Silva (PTS)
# version: v08
# ===============================
# Objectivo:
# construir uma interrogacao remota a partir de informacao local


#______________________________________________________________________________
# Importar modulos
import rdflib
from rdflib import ConjunctiveGraph, Graph
from rdflib  import Namespace
from rdflib import URIRef, Literal, BNode, Namespace, Variable
from rdflib import RDF

from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF
from x_util_JSONwithMD import getResultSet, getResultSet_withMetaData
from xml.dom import minidom




#______________________________________________________________________________
# Obter grafo a partir de RDF (previamente) serializado em ficheiro
def obter_Grafo( nomeFicheiro, formato ):
   apresentarCabecalho( "GRAFO: \'%s\'" % nomeFicheiro )
   grafo = Graph()
   try: grafo.parse( nomeFicheiro, format=formato )
   except: print( "\n >> ERRO: nao existe grafo em: %s <<\n" % nomeFicheiro )
   return grafo


#______________________________________________________________________________
# Registar, em ficheiro, o grafo
def registarEmFicheiro( grafo, nomeFicheiro, formato="nt" ):
   file = open( nomeFicheiro, "wb" )
   grafo.serialize( file, format=formato )

   
#______________________________________________________________________________
# Utilitarios: apresentar informacao
def apresentarCabecalho( texto ):
   print()
   print( len( texto )*"_" )
   print( texto )


#_______________________________________________________________________________
# Inicio do exemplo
FOAF = Namespace( "http://xmlns.com/foaf/0.1/" )
myNS = Namespace( "http://myNS/" )

graphFileName = "z01_meu_grafo.rdf"


# =====//=====
# Construir e guardar um grago local (g1)
g1 = Graph()
s = BNode( "x" )
p = rdflib.RDF.type
o = FOAF[ "Person" ]
g1.add( ( s, p, o ) )
p = FOAF[ "name" ]
o = Literal( "Edsger W. Dijkstra" )
g1.add( ( s, p, o ) )

s = BNode( "y" )
p = rdflib.RDF.type
o = FOAF[ "Person" ]
g1.add( ( s, p, o ) )
p = FOAF[ "name" ]
o = Literal( "Frederic Brenton Fitch" )
g1.add( ( s, p, o ) )
# guardar esta informacao num grafo local
# esta informacao servira' de "input" a uma interrogacao a um grafo remoto
apresentarCabecalho( "registar grafo local com informacao parcial" )
registarEmFicheiro( g1, graphFileName, formato="pretty-xml" )



### =====//=====
### Ler e interrogar um grafo anteriormente guardado
g2 = obter_Grafo( graphFileName, formato="xml" )

q = \
"""
PREFIX foaf: <""" + str( FOAF ) + """>
SELECT ?s ?name
WHERE
{
    ?s foaf:name ?name .
}
"""
print(str(FOAF))
print(q)   

for s, p, o in g2:
    print(s, p, o)
    
q_resultSet = g2.query( q )
#for result in q_resultSet: print( result )
##
##
##
### =====//=====
### Usar recursos de um grafo como constituintes
### de uma interrogacao a um "SPARQL endpoint" (usando o SPARQLWrapper)
### Notar que o SPARQLWrapper nao suporta passagem de parametros 'a interrogacao SPARQL
### (isso e' suportado pelo RDFLib que no entanto nao suporta acesso a "SPARQL endpoint")
##
###conn = SPARQLWrapper( "http://dbpedia.org/sparql" )
###conn = SPARQLWrapper( "http://citeseer.rkbexplorer.com/sparql" )
##conn = SPARQLWrapper( "http://dblp.rkbexplorer.com/sparql" )
##
### completar a interrogacao com a informacao guardada no grafo local
##for (nodeID, fullName) in q_resultSet:
##  q = \
##  """
##  PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
##  PREFIX akt: <http://www.aktors.org/ontology/portal#>
##  SELECT DISTINCT ?s ?pub ?title
##  WHERE
##  {
##  ?s rdf:type akt:Person .
##  ?s akt:full-name \"""" + str( fullName ) + """\" .
##  ?pub akt:has-author ?s .
##  ?pub akt:has-title ?title .
##  }
##  LIMIT 10
##  """
##  apresentarCabecalho( "Interrogacao (SPARQL):" )
##  print( q )
##  
##  conn.setQuery( q )
##  conn.setReturnFormat( JSON )
##  # ATENCAO: esta interrogacao e' remota pelo que o
##  # tempo de execucao depende da qualidade de servico oferecida
##  # (i.e., pode demorar um pouco a obter resposta)
##  result = conn.query().convert()
##
##  # obter dados e meta-dados
##  ( varSet, resultSet ) = getResultSet_withMetaData( result )
##  apresentarCabecalho( "Resultado (em JSON):" )
##  print( "metaDados = " % varSet )
##  for r in getResultSet( result ): print( r )
##
##  # estender um grafo com a nova informacao
##  apresentarCabecalho( "Estender grafo com a nova informação:" )
##  idxTitle = varSet.index( 'title' )
##  for row in resultSet:
##    title = row[ idxTitle ]
##    print( title )
##    s = nodeID
##    p = myNS[ "temPublicacaoComTitulo" ]
##    o = Literal( title )
##    g2.add( ( s, p, o ) )
##
### gravar o grafo estendido com a nova informacao  
##registarEmFicheiro( g2, graphFileName, formato="xml" )
##
