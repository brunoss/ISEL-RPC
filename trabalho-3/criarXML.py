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


class graph:
  def __init__(self):
    self.graph = Graph()

  def addTuple(self, nsSubject=None, Subject=None, nsPredicate=None, Predicate=None, nsObject=None, Object=None, Literal=False):
    if nsSubject:
      s = nsSubject[Subject]
    else:
      s = BNode(Subject)
    p = nsPredicate[Predicate]
    if nsObject:
      o = nsObject[Object]
    elif Literal:
      o = Literal(Object)
    else:
      o = BNode(Object)
    self.graph.add((s, p, o))
    return (s, p, o)

  def addStatement(self, StatementNode, nsSubject=None, Subject=None, nsPredicate=None, Predicate=None, nsObject=None, Object=None, isLiteral=False):
    s = BNode(StatementNode)
    # Adding Statement Subject
    p = RDF.subject
    if nsSubject:
      o = nsSubject[Subject]
    else:
      o = BNode(Subject)
    self.graph.add((s, p, o))
    # Adding Statement Predicate
    p = RDF.predicate
    o = nsPredicate[Predicate]
    self.graph.add((s, p, o))
    # Adding Statement Object
    p = RDF.object
    if nsObject:
      o = nsObject[Object]
    elif isLiteral:
      o = Literal(Object)
    else:
      o = BNode(Object)
      
    self.addTuple(None, StatementNode, RDF, 'type', RDF, 'Statement')  
    self.graph.add((s, p, o))

# ______________________________________________________________________________
# Iniciar uma instancia da especificacao FOAF
gf = graph()
#def addTuple(self, nsSubject=None, Subject=None, nsPredicate=None, Predicate=None, nsObject=None, Object=None, Literal=False):
gf.addTuple(JNS, 'JogosOlimpicos',JNS, 'inventadoEm',MNS, 'Grecia')

gf.addTuple(None, '_jogo1', RDF, 'type', JNS, 'JogosOlimpicos')
gf.addTuple('','_jogo1',JNS,'noAno',TNS, '1896')
gf.addTuple('','_jogo1',JNS,'naCidade',MNS,'Atenas')

gf.addTuple(None, '_jogo2', RDF, 'type', JNS, 'JogosOlimpicos')
gf.addTuple('','_jogo2',JNS,'noAno',TNS, '2012')
gf.addTuple('','_jogo2',JNS,'naCidade',MNS,'Londres')

gf.addTuple(MNS,'Atenas',MNS,'pertence',MNS, 'Grecia')
gf.addTuple(MNS,'Londres',MNS,'pertence',MNS,'Reino_Unido')

gf.addTuple(MNS, 'Atenas', RDF, 'type', JNS, 'Cidade')
gf.addTuple(MNS, 'Londres', RDF, 'type', JNS, 'Cidade')
gf.addTuple(MNS, 'Grecia', RDF, 'type', JNS, 'País')
gf.addTuple(MNS, 'Reino_Unido', RDF, 'type', JNS, 'País')
gf.addTuple(TNS, '1896', RDF, 'type', TNS, 'Ano')
gf.addTuple(TNS, '2012', RDF, 'type', TNS, 'Ano')

gf.addTuple(CNS,'Pedro',CNS,'dizer','','_opiniao1')
gf.addStatement('_opiniao1',MNS,'Londres',CNS,'achar','','_opiniao2')
gf.addStatement('_opiniao2','','_jogo2',CNS,'ser','',"Fabuloso", True)

gf.addTuple(JNS, 'JogosOlimpicos', RDF, 'type', RDFS, 'Class')


def apresentarCabecalho(texto):
    print
    print(len(texto)*"_")
    print(texto)


apresentarCabecalho(".:: Apresentar os triplos: <s, p, o> ::.")
for s, p, o in gf.graph:
    print(s, p, o)

apresentarCabecalho(".:: Serializar RDF com XML ::.")
print(gf.graph.serialize(format="xml"))

# Serializar RDF com XML e registar em ficheiro ("foaf.rdf")
file = open("graph_auto.rdf", "wb")
gf.graph.serialize(file, format="pretty-xml", max_depth=1)
file.close()

# ______________________________________________________________________________
# Serializar RDF com N-Triples
apresentarCabecalho(".:: Serializar RDF com N-Triples ::.")
file = open("graph_auto.nt", "wb")
gf.graph.serialize(file, format="nt")
file.close()
