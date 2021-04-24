# ______________________________________________________________________________
# Importar modulos
from rdflib.graph import Graph
from rdflib import URIRef, Literal, BNode, Namespace, Variable
from rdflib import RDF, RDFS

# ______________________________________________________________________________
# Namespaces
namespace_jogos = "http://tocha/#"
JNS = Namespace(namespace_jogos)
namespace_map = "http://map/#"
MNS = Namespace(namespace_map)
namespace_time = "http://time/#"
TNS = Namespace(namespace_time)
namespace_crit = "http://critica/#"
CNS = Namespace(namespace_crit)


class Grafo:
    def __init__(self):
      # criar um grafo vazio
      self.grafo = Graph()

    def adicionarType(self, namespace, nomeRecurso, rdfType):
      s = namespace[nomeRecurso]
      p = RDF.type
      o = namespace[rdfType]
      self.grafo.add((s, p, o))
      return (s, p, o)

    def adicionarTuplo_v1( self, namespaceSuj, nomeSuj , namespacePrd, nomePrd, namespaceObj, nomeObj ):
      s = namespaceSuj[nomeSuj]
      p = namespacePrd[nomePrd]
      o = namespaceObj[nomeObj]
      self.grafo.add( (s, p, o ) )
      return (s, p, o )

    def adicionarTuplo( self, namespace, nomeRecurso , predicado, objeto ):
      s = namespace[nomeRecurso]
      p = namespace[predicado]
      o = namespace[objeto]
      self.grafo.add( (s, p, o ) )
      return (s, p, o )

    def adicionarAnonimo( self, namespace, nomeRecurso , objeto ):
      s = BNode(nomeRecurso)
      p = RDF.type
      o = namespace[objeto]
      self.grafo.add((s, p, o))
      return (s, p, o)

    def adicionarTuploSujAnonimo( self, namespace, nomeRecurso , predicado, objeto ):
      s = BNode(nomeRecurso)
      p = namespace[predicado]
      o = namespace[objeto]
      self.grafo.add( (s, p, o ) )
      return (s, p, o )

    def adicionarTuploObjAnonimo( self, namespace, nomeRecurso , predicado, objeto ):
      s = namespace[nomeRecurso]
      p = namespace[predicado]
      o = BNode(objeto)
      self.grafo.add( (s, p, o ) )
      return (s, p, o )

    def adicionarStatementRef( self, namespace,nomeStatement ):
      s = BNode(nomeStatement)
      p = RDF.type
      o = RDF.Statement
      self.grafo.add( (s, p, o ) )
      return (s, p, o )

    def adicionarStatementSubject( self, namespace,nomeStatement,objecto ):
      s = BNode(nomeStatement)
      p = RDF.subject
      o = namespace[objecto]
      self.grafo.add( (s, p, o ) )
      return (s, p, o )

    def adicionarStatementPred( self, namespace,nomeStatement,objecto ):
      s = BNode(nomeStatement)
      p = RDF.predicate
      o = namespace[objecto]
      self.grafo.add( (s, p, o ) )
      return (s, p, o )

    def adicionarStatementobcj( self, namespace,nomeStatement,objecto ):
      s = BNode(nomeStatement)
      p = RDF.object
      o = namespace[objecto]
      self.grafo.add( (s, p, o ) )
      return (s, p, o )

    def adicionarStatementobcj_anon( self, nomeStatement,objecto ):
      s = BNode(nomeStatement)
      p = RDF.object
      o = BNode(objecto)
      self.grafo.add( (s, p, o ) )
      return (s, p, o )
    
    def adicionarStatementSuj_anon( self, nomeStatement,objecto ):
      s = BNode(nomeStatement)
      p = RDF.subject
      o = BNode(objecto)
      self.grafo.add( (s, p, o ) )
      return (s, p, o )

    def adicionarStatementobcj_literal( self, nomeStatement,objecto ):
      s = BNode(nomeStatement)
      p = RDF.object
      o = Literal(objecto)
      self.grafo.add( (s, p, o ) )
      return (s, p, o )

    def adicionarClassRef( self, namespace,nomeStatement ):
      s = namespace[nomeStatement]
      p = RDF.type
      o = RDFS.Class
      self.grafo.add( (s, p, o ) )
      return (s, p, o )

# ______________________________________________________________________________
# Iniciar uma instancia da especificacao FOAF
gf = Grafo()

gf.adicionarTuplo(JNS,'JogosOlimpicos','inventadoEm','Grecia')

gf.adicionarAnonimo(JNS,'_jogo1','JogosOlimpicos')
gf.adicionarTuploSujAnonimo(JNS,'_jogo1','noAno','1896')
gf.adicionarTuploSujAnonimo(JNS,'_jogo1','naCidade','Atenas')

gf.adicionarAnonimo(JNS,'_jogo2','JogosOlimpicos')
gf.adicionarTuploSujAnonimo(JNS,'_jogo2','noAno','2012')
gf.adicionarTuploSujAnonimo(JNS,'_jogo2','naCidade','Londres')

gf.adicionarTuplo(JNS,'Atenas','pertence','Grecia')
gf.adicionarTuplo(JNS,'Londres','pertence','Reino_Unido')

gf.adicionarType(JNS,'Atenas','Cidade')
gf.adicionarType(JNS,'Londres','Cidade')
gf.adicionarType(JNS,'Grecia','País')
gf.adicionarType(JNS,'Reino_Unido','País')
gf.adicionarType(JNS,'1896','Ano')
gf.adicionarType(JNS,'2012','Ano')

gf.adicionarTuploObjAnonimo(CNS,'Pedro','dizer','_opiniao1')
gf.adicionarStatementSubject(JNS,'_opiniao1','Londres')
gf.adicionarStatementPred(JNS,'_opiniao1','achar')
gf.adicionarStatementobcj_anon('_opiniao1','_opiniao2')

gf.adicionarStatementSuj_anon('_opiniao2','_jogo2')
gf.adicionarStatementPred(JNS,'_opiniao2','ser')
gf.adicionarStatementobcj_literal('_opiniao2','fabuloso')

gf.adicionarStatementRef(CNS,'_opiniao1')
gf.adicionarStatementRef(CNS,'_opiniao2')

gf.adicionarClassRef(JNS,'JogosOlimpicos')


def apresentarCabecalho( texto ):
   print
   print( len( texto )*"_" )
   print( texto )

apresentarCabecalho( ".:: Apresentar os triplos: <s, p, o> ::." )
for s, p, o in gf.grafo:
    print( s, p, o )

apresentarCabecalho( ".:: Serializar RDF com XML ::." )
print( gf.grafo.serialize( format="xml" ) )

# Serializar RDF com XML e registar em ficheiro ("foaf.rdf")
file = open( "grafo_auto.rdf", "wb" )
gf.grafo.serialize( file, format="pretty-xml", max_depth=1 )
file.close()

#______________________________________________________________________________
# Serializar RDF com N-Triples
apresentarCabecalho( ".:: Serializar RDF com N-Triples ::." )
file = open( "grafo_auto.nt", "wb" )
gf.grafo.serialize( file, format="nt" ) 
file.close()
