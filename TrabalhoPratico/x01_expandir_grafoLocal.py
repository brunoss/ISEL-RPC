# -*- coding: cp1252 -*-
#______________________________________________________________________________
# author: Paulo Trigo Silva (PTS)
# version: v06
# adaptado de: "c01_combinar_local_e_global_rkbexplorer.py" (cf., aula pratica6)
# contem agora as classes:
# - Grafo
# - GrafoRemoto
# gera ficheiros:
# - z01_meu_grafo_INPUT.rdf,
#   um exemplo de grafo
# - z01_meu_grafo_OUTPUT.rdf,
#   grafo anterior estendido por execucao de varias interrogacoers remotas
#______________________________________________________________________________
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
# Global Variables
FOAF = Namespace( "http://xmlns.com/foaf/0.1/" )
qualificador_foaf="foaf"
DBLP = Namespace( "http://swat.cse.lehigh.edu/resources/onto/dblp.owl#" )
qualificador_dblp="dblp"
AKT = Namespace( "http://www.aktors.org/ontology/portal#" )
qualificador_akt="akt"
AKTS = Namespace( "http://www.aktors.org/ontology/support#" )
qualificador_akts="akts"

#______________________________________________________________________________
# A nocao de Grafo (i.e., estrutura RDF, RDFS, OWL)
# - pode ser lido de ficheiro local
# - pode ser escrito em ficheiro local
# - pode ser estendido por adicao de tripletos
# - pode ser interrogado via SPARQL
class Grafo:
   def __init__( self ):
      self.grafo = Graph()
      self.grafo.bind( qualificador_foaf, FOAF)
      self.grafo.bind( qualificador_dblp, DBLP )
      self.grafo.bind( qualificador_akt, AKT )
      self.grafo.bind( qualificador_akts , AKTS )

   def ler( self, nomeFicheiro, formato="xml" ):
      assert nomeFicheiro != "", "PTS | nomeFicheiro indefinido"
      grafo = Graph()
      try: grafo.parse( nomeFicheiro, format=formato )
      except: print( "\n >> ERRO: nao existe grafo em: %s <<\n" % nomeFicheiro )
      self.grafo = grafo
      return self

   def escrever( self, nomeFicheiro, formato="pretty-xml" ):
      assert nomeFicheiro != "" or self.grafo != None, "PTS | nomeFicheiro OU grafo INDEFINIDO"
      f = open( nomeFicheiro, "wb" )
      self.grafo.serialize( f, format=formato )

   def adicionarTripleto( self, sujeito, predicado, objecto ):
      assert self.grafo != None, "PTS | grafo INDEFINIDO"
      self.grafo.add( ( sujeito, predicado, objecto ) )

   def interrogar( self, interrogacao ):
      assert self.grafo != None, "PTS | grafo INDEFINIDO"
      return self.grafo.query( interrogacao )

#_______________________________________________________________________________
# Construir um grafo (exemplo)
# (numa versao posterior o grafo nao deve ficar aqui pre-definido)
# (i.e., o grafo que vier a construir nao deve ficar aqui "hard-coded")
def gerarTripletos( grafo, ns_FOAF ):
   s = BNode( "MISSBala" )
   
   p = rdflib.RDF.type
   o = ns_FOAF[ "Person" ]
   grafo.adicionarTripleto( s, p, o )
   
   p = DBLP [ "author" ]
   o = DBLP[ "doc01" ]
   grafo.adicionarTripleto( s, p, o )

   p = DBLP[ "full-name" ]
   o = Literal( "Edsger W. Dijkstra" )
   grafo.adicionarTripleto( s, p, o )

   s = BNode( "book_mi" )
   
   p = rdflib.RDF.type
   o = DBLP[ "Book" ]
   grafo.adicionarTripleto( s, p, o )

def gerarGrafoINPUT( nomeFicheiroGrafoINPUT, ns_FOAF ):
   g = Grafo()
   gerarTripletos( g, ns_FOAF )
   g.escrever( nomeFicheiroGrafoINPUT, formato="pretty-xml" )

#______________________________________________________________________________
# Utilitario: apresentar informacao
def apresentarCabecalho( texto ):
   print()
   print( len( texto )*"_" )
   print( texto )
  

#______________________________________________________________________________
def main():
   # nomes usados ao longo do programa
   nomeFicheiroGrafoINPUT = "./BaseData/inputGrafo.rdf"
   nomeFicheiroGrafoOUTPUT = "./BaseData/outputGrafo.rdf"

   # gerar e guardar um grafo (pode ser feito externamente a este programa)
   # (este grafo sera' posteriormente usado como INPUT para varias interrogacoes remotas)
   gerarGrafoINPUT( nomeFicheiroGrafoINPUT, FOAF )

   # interrogar um grafo local
   # (neste exemplo corresponde ao grafo acima gerado)
   grafoLocal = Grafo().ler( nomeFicheiroGrafoINPUT )
   interrogacaoLocal = \
     """
     PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
     PREFIX owl:  <http://www.w3.org/2002/07/owl#>
     PREFIX dblp: <http://swat.cse.lehigh.edu/resources/onto/dblp.owl#>
     SELECT DISTINCT ?author
     WHERE 
     {
     ?author rdf:type dblp:Person .
     }
     """
   resultadoInterrogacaoLocal = grafoLocal.interrogar( interrogacaoLocal )
   apresentarCabecalho( "Resultado da Interrogacao ao Grafo Local" )
   for linha in resultadoInterrogacaoLocal: print( linha )
   print()

#______________________________________________________________________________
# O "main" deste modulo (caso o modulo nao seja carregado de outro modulo)
if __name__ == "__main__":
   main()

