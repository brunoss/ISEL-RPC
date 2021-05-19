#!/usr/bin/python
# -*- coding: utf-8 -*-

# ===============================
# author: Paulo Trigo Silva (PTS)
# version: v07 (usa servidor RDF4J)
# v05 usava servidor Sesame
# ===============================
# Utilizacao do SPARQLWrapper
# - de modo a aceder ao RDF4J (repositorio local)


#______________________________________________________________________________
# Importar modulos
from SPARQLWrapper import SPARQLWrapper, XML, N3, TURTLE, RDF, JSON, JSONLD
from x_util_JSON import getResultSet


#______________________________________________________________________________
# Definir SPARQL-endpoint para o RDF4J (na maquina local)
#sparql_endpoint = "http://localhost:8280/openrdf-sesame/" #versao anterior
sparql_endpoint = "http://localhost:8280/rdf4j-server/"
repository_path = "repositories/"
repository = "repo-con"
FULL_SPARQL_ENDPOINT = sparql_endpoint + repository_path + repository
conn = SPARQLWrapper( FULL_SPARQL_ENDPOINT )

print( "My endpoint: " )
print( conn.endpoint )


#______________________________________________________________________________
# (codigo escrito de modo sequencial - para evidenciar o essencial)
q = \
"""
PREFIX foaf:  <http://xmlns.com/foaf/0.1/>
SELECT ?s ?o
WHERE { ?s foaf:name ?o . }
"""
conn.setQuery( q )

# Execucao do Pedido
conn.setReturnFormat( JSON )
result = conn.query()
print( '\n\n*** O pedido REST:' )
print( result.response.geturl() )

print( '\n\n*** Informacao sobre a conexao:' )
print( result.info() )
print()

# JSON
##print( '\n\n*** Exemplo JSON:' )
##result = conn.query().convert()
##for r in result["results"]["bindings"]:
##   print( r["s"]["value"] + " | " + r["o"]["value"] )
##print()
##
##
### JSON | iterar nos resultados usando getResultSet()
##result = conn.query().convert()
##print( "Uso de: getResultSet()" )
##for r in getResultSet( result ): print( r )
##
##
### XML
##print( '\n\n*** Exemplo JSON\XML:' )
##conn.setReturnFormat(XML)
##result = conn.query().convert()
##print( result.toxml() )


