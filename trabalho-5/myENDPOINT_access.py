#!/usr/bin/python
# -*- coding: utf-8 -*-

# ===============================
# author: RPC_??
# version: v04
# ===============================



#______________________________________________________________________________
# Importar modulos
from rdflib.graph import Graph
from SPARQLWrapper import SPARQLWrapper, XML, N3, TURTLE, RDF, JSON, JSONLD
from x_util_JSON import getResultSet
import warnings


#______________________________________________________________________________
# funcao para acesso e interrogacao a um SPARQL-endpoint

def f_ENDPOINT_access( SPARQL_statement, list_FORMAT_fallback, SPARQL_endpoint ):
    sparql = SPARQLWrapper( SPARQL_endpoint )
    
    for item in list_FORMAT_fallback:
        FORMAT_reply = item;
        sparql.setReturnFormat( FORMAT_reply )
        with warnings.catch_warnings(record = True) as w:
            warnings.filterwarnings( "always" )
            sparql.setQuery( SPARQL_statement )
            resultSet = sparql.query()
            resultSet = resultSet.convert()
            if(len(w) <= 1):
                break
    
    if resultSet == None:
        return None
    elif FORMAT_reply == XML:
        resultSet = resultSet.toxml()
    elif FORMAT_reply == JSON:
        resultSet = getResultSet(resultSet)
    
    return ( FORMAT_reply, resultSet )
                       



#______________________________________________________________________________
# utilizacao de "f_ENDPOINT_access"
querySELECT = \
"""
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?label
WHERE { 
<http://dbpedia.org/resource/Asturias> rdfs:label ?label 
FILTER (lang(?label) != "ja" && lang(?label) != "zh" && lang(?label) != "ru"  && lang(?label) != "ar" && lang(?label) != "ko")   
}
"""

def myMain():
   SPARQL_statement = querySELECT
   list_FORMAT_fallback = [JSONLD, JSONLD, JSON, TURTLE, XML, N3, RDF]
   SPARQL_endpoint = "http://dbpedia.org/sparql"

   responseFormat, resultSet = f_ENDPOINT_access( SPARQL_statement, list_FORMAT_fallback, SPARQL_endpoint )
   print(responseFormat)
   print( resultSet )


#______________________________________________________________________________
# O "main" deste modulo (caso o modulo nao seja carregado de outro modulo) 
if __name__ == "__main__":
   myMain()
