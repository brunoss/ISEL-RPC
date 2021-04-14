# -*- coding: cp1252 -*-
# ===============================
# author: Paulo Trigo Silva (PTS)
# version: v12
# comment: 7th Python3 version 
# ===============================



#______________________________________________________________________________
# Importar modulos
from rdflib.graph import Graph
from rdflib import URIRef, Literal, BNode, Namespace
from rdflib import RDF
import os


#______________________________________________________________________________
# O essencial para construir um grafo de FOAF
# FOAF significa: "Friend Of A Friend"
namespace_foaf = "http://xmlns.com/foaf/0.1/" #string com o "namespace"
FOAF = Namespace( namespace_foaf ) #variavel com registo do "namespace" FOAF


#______________________________________________________________________________
# Construir grafo a partir de RDF (previamente) serializado em ficheiro

def construirGrafo( nomeDoFicheiro = "foaf.rdf", formato = "xml" ):
   """Le ficheiro e devolve um Grafo de objectos da 'rdflib'"""
   texto = ""
   grafo = None
   if os.path.isfile( nomeDoFicheiro ):
      grafo = Graph()
      grafo.parse( nomeDoFicheiro, format=formato )
      texto = "Leitura dos dados RDF em: \'.\\%s\'" % nomeDoFicheiro
   else:
      texto =  "Nao existe o ficheiro: \'.\\%s\'! " % nomeDoFicheiro
      texto += "(terminar exercicio com \'a01_criarFOAF.py\')" 
      
   apresentarCabecalho( texto )
   return grafo


#______________________________________________________________________________
# Obter lista de (sujeito, objecto) com relacao mutua de "knows"

def obterConhecidoMutuo( grafo ):
   if grafo == None: return
   """
   Obtem informacao de um grafo de objectos "rdflib"
   usando uma simples pesquisa no grafo
   e.g., lista = list( grafo.subject_objects( FOAF[ "knows" ] ) )
   """
   assert( isinstance( grafo, Graph ) )
   resultado = []
   lista_s_o = list( grafo.subject_objects( FOAF[ "knows" ] ) )
   for (s, o) in lista_s_o:
      #if >ALTERAR< #conhecido mutuo quando (o, s) pertence a lista_s_o
         resultado.append( (s, o) ) #(s, o) e (o, s) conhecem-se mutuamente
         # >ALTERAR< #remover (o, s) de lista_s_o pois nao precisa novo processamento
   return resultado


#______________________________________________________________________________
# Utilitario para apresentar cabecalho

def apresentarCabecalho( texto ):
   print()
   print( len( texto )*"_" )
   print( texto )


#______________________________________________________________________________
# Apresentar o valor da relacao "name" de pares (sujeito, objecto)

def apresentar_FOAFname( grafo, lista ):
   if grafo == None: return
   
   apresentarCabecalho( "Conhecidos mutuos: \'%d\'" % len( lista ) )
   for (s, o) in lista:
      [ s_nome ] = grafo.objects( s, FOAF[ "name" ] )
      [ o_nome ] = grafo.objects( o, FOAF[ "name" ] )
      print( "knows( \'%s\', \'%s\' )" % (s_nome, o_nome) )
      # PTS: descomentar proxima e comentar anterior quando tiver "conhecidos mutuos"
      #print( "knows( \'%s\', \'%s\' ) e \'vice-versa\'" % (s_nome, o_nome) )


#______________________________________________________________________________
# O "main" deste modulo (caso o modulo nao seja carregado de outro modulo) 

if __name__ == "__main__":
   from rdflib import __version__
   print( "\n%s RDFlib versao: \'%s\' %s" % (3*"*", __version__, 3*"*") )
   grafo = construirGrafo()
   lista = obterConhecidoMutuo( grafo )
   apresentar_FOAFname( grafo, lista )

