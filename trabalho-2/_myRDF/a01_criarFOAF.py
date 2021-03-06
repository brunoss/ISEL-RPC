# -*- coding: cp1252 -*-
# ===============================
# author: Paulo Trigo Silva (PTS)
# version: v12
# comment: 7th Python3 version 
# ===============================


#______________________________________________________________________________
# Importar modulos
from rdflib.graph import Graph
from rdflib import URIRef, Literal, BNode, Namespace, Variable
from rdflib import RDF


#______________________________________________________________________________
# O essencial para construir um grafo de FOAF
# FOAF significa: "Friend Of A Friend"
namespace_foaf = "http://xmlns.com/foaf/0.1/" #string com o "namespace"
qualificador_foaf = "foaf" #string com o qualificador a usar para o "namespace"
FOAF = Namespace( namespace_foaf ) #variavel com registo do "namespace" FOAF
# o meu "namespace"
namespace_mns = "http://meuMS/#"
MNS = Namespace( namespace_mns )

      
class GrafoFOAF:
   def __init__( self ):
      # criar um grafo vazio
      self.grafo = Graph()
      # ligar, no contexto do grafo, o "namespace" e o seu qualificador
      self.grafo.bind( qualificador_foaf, namespace_foaf)


   def adicionarPessoa( self, nomeDaPessoa, idPessoa ):
      """
      Adiciona dois triplos:
      <idPessoa, type, Person>, e
      <idPessoa, name, nomeDaPessoa>
      """
      #s = BNode( idPessoa ) #identificador para usar no "sujeito"
      s = MNS[idPessoa]
      p = RDF.type #predicado "rdf:type"
      o = FOAF[ "Person" ] #recurso "Person" definido em FOAF
      # adicionar tripo: <s, p, o>
      self.grafo.add( (s, p, o ) )

      p = FOAF[ "name" ] #recurso "name" definido em FOAF
      #o = Literal( nomeDaPessoa )
      o = MNS[nomeDaPessoa]
      # adicionar tripo: <s, p, o>
      self.grafo.add( (s, p, o ) )
      return (s, p, o )

   def s_knows_o( self, s, o ):
      """
      Adiciona um triplo:
      <s, knows, o>
      mantem o registo de 'quem cohece quem'
      """
      
      p = FOAF[ "knows" ]
      return self.grafo.add( (s, p, o ) )


#______________________________________________________________________________
# Iniciar uma instancia da especificacao FOAF
gf = GrafoFOAF()


#______________________________________________________________________________
# Criar uma pessoa: eu
(eu, _, _) = gf.adicionarPessoa( "o meu nome", "eu" )
# adicionar o meu cognome, ou alcunha ("nickname") e emdereco de email
gf.grafo.add( (eu, FOAF[ "nick" ], Literal( "o meu cognome" )) )
gf.grafo.add( (eu, FOAF[ "mbox" ], Literal( "meumail@" )) )

#______________________________________________________________________________
# Criar um amigo: amigoA
(amigoA, _, _) = gf.adicionarPessoa( "nome do amigo A", "amigoA" )
# adicionar o emdereco de email do amigo
gf.grafo.add( (amigoA, FOAF[ "mbox" ], Literal( "amigoA@" )) )


#______________________________________________________________________________
# Criar um amigo: amigoB
(amigoB, _, _) = gf.adicionarPessoa( "nome do amigo B", "amigoB" )

#______________________________________________________________________________
# Definir as relacoes "knows" entre os meus amigos
# "quem conhece quem"

# <eu, knows, amigoA>
# <amigoA, knows, eu>
# PTS: descomentar depois de implementar metodo: "s_knows_o"
gf.s_knows_o( eu, amigoA )
gf.s_knows_o( amigoA, eu )

# <eu, knows, amigoB>
# <amigoB, knows, eu>
gf.s_knows_o( eu, amigoB )
gf.s_knows_o( amigoB, eu )

# <amigoA, knows, amigoB>
gf.s_knows_o( amigoB, amigoA )


#______________________________________________________________________________
# Utilitario para apresentar cabecalho
def apresentarCabecalho( texto ):
   print
   print( len( texto )*"_" )
   print( texto )


#______________________________________________________________________________
# Iterar sobre os triplos no grafo
apresentarCabecalho( ".:: Apresentar os triplos: <s, p, o> ::." )
for s, p, o in gf.grafo:
    print( s, p, o )


#______________________________________________________________________________
# Para cada foaf:Person no grafo fazer:
# apresentar o nome da foaf:Person e o valor da sua propriedade "mbox"
apresentarCabecalho( ".:: Apresentar os enderecos de e-mail ::." )

for s in gf.grafo.subjects( RDF.type, FOAF[ "Person" ] ):
    for mbox in gf.grafo.objects( s, FOAF[ "mbox" ] ):
        print( "e-mail do \"%s\": \"%s\"" % (s, mbox) )

    for name in gf.grafo.objects( s, FOAF[ "name" ] ):
        print( "name do \"%s\": \"%s\"" % (s, name) )


#______________________________________________________________________________
# Apresentar os diferentes formatos para serializar o RDF
apresentarCabecalho( ".:: Serializar o RDF ::." )


#______________________________________________________________________________
# Serializar RDF com XML
apresentarCabecalho( ".:: Serializar RDF com XML ::." )
print( gf.grafo.serialize( format="xml" ) )


#______________________________________________________________________________
# Serializar RDF com XML e registar em ficheiro ("foaf.rdf")
file = open( "foaf.rdf", "wb" )
#gf.grafo.serialize( file, format="pretty-xml" )
#gf.grafo.serialize( file, format="xml" )
#gf.grafo.serialize( file, format="pretty-xml", max_depth=3 )
gf.grafo.serialize( file, format="pretty-xml", max_depth=1 )
file.close()


#______________________________________________________________________________
# Serializar RDF com N-Triples
apresentarCabecalho( ".:: Serializar RDF com N-Triples ::." )
file = open( "foaf.nt", "wb" )
gf.grafo.serialize( file, format="nt" ) 
file.close()


#______________________________________________________________________________
# Serializar RDF com N3
apresentarCabecalho( ".:: Serializar RDF com N3 ::." )
file = open( "foaf.n3", "wb" )
gf.grafo.serialize( file, format="n3" )
file.close()

