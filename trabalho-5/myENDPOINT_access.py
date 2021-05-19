#!/usr/bin/python
# -*- coding: utf-8 -*-

# ===============================
# author: RPC_??
# version: v04
# ===============================



#______________________________________________________________________________
# Importar modulos
from rdflib.graph import Graph
from SPARQLWrapper import SPARQLWrapper, XML, N3, TURTLE, RDF, JSON
import warnings



#______________________________________________________________________________
# funcao para acesso e interrogacao a um SPARQL-endpoint

def f_ENDPOINT_access( SPARQL_statement, list_FORMAT_fallback, SPARQL_endpoint ):
   FORMAT_reply, resultSet = None, None
   return ( FORMAT_reply, resultSet )
                       



#______________________________________________________________________________
# utilizacao de "f_ENDPOINT_access"
querySELECT = \
"""
SELECT ...      
"""

def myMain():
   SPARQL_statement = querySELECT
   list_FORMAT_fallback = []
   SPARQL_endpoint = "http://..."

   resultSet = f_ENDPOINT_access( SPARQL_statement, list_FORMAT_fallback, SPARQL_endpoint )
   print( resultSet )


#______________________________________________________________________________
# O "main" deste modulo (caso o modulo nao seja carregado de outro modulo) 
if __name__ == "__main__":
   myMain()
