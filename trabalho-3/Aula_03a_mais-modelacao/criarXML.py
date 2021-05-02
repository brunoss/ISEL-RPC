# ______________________________________________________________________________
# Importar modulos
from rdflib.graph import Graph
from rdflib import URIRef, Literal, BNode, Namespace, Variable
from rdflib import RDF, RDFS

# ______________________________________________________________________________
# Namespaces
BNS = Namespace("http://book/#")


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
#def addTuple(nsSubject=None, Subject=None, nsPredicate=None, Predicate=None, nsObject=None, Object=None, Literal=False):



gf.addTuple(BNS, 'IEEE', RDF, 'type', BNS, 'Editora')
gf.addTuple(BNS, 'Springer', RDF, 'type', BNS, 'Editora')
gf.addTuple(BNS, '12345', RDF, 'type', BNS, 'ArtigoCientifico')
gf.addTuple(BNS, 'Pedro', RDF, 'type', BNS, 'Autor')
gf.addTuple(BNS, 'Maria', RDF, 'type', BNS, 'Autor')

gf.addTuple(None, '_pub1', RDF, 'type', BNS, 'Publicacao')
gf.addTuple(None, '_pub1', BNS, 'publicadoPor', BNS, 'Springer')
gf.addTuple(None, '_pub1', BNS, 'artigo', BNS, 'Publicacao')
gf.addTuple(None, '_pub1', BNS, 'autor', BNS, '_pub1a1')
gf.addTuple(None, '_pub1', BNS, 'autor', BNS, '_pub1a2')

gf.addStatement('_pub1a1', BNS, 'Maria', BNS, 'temOrdem', BNS, '1')
gf.addStatement('_pub1a2', BNS, 'Pedro', BNS, 'temOrdem', BNS, '2')

gf.addTuple(None, '_pub2', RDF, 'type', BNS, 'Publicacao')
gf.addTuple(None, '_pub2', BNS, 'publicadoPor', BNS, 'IEEE')
gf.addTuple(None, '_pub2', BNS, 'artigo', BNS, 'Publicacao')
gf.addTuple(None, '_pub2', BNS, 'autor', BNS, '_pub2a1')
gf.addTuple(None, '_pub2', BNS, 'autor', BNS, '_pub2a2')

gf.addStatement('_pub2a1', BNS, 'Pedro', BNS, 'temOrdem', BNS, '1')
gf.addStatement('_pub2a2', BNS, 'Maria', BNS, 'temOrdem', BNS, '2')

gf.addTuple(BNS, 'Pedro', BNS, 'dizer', BNS, '_stm')
gf.addStatement('_stm', BNS, 'Maria', BNS, 'gosta', BNS, 'IEEE')

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
