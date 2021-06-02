# -*- coding: cp1252 -*-
# ===============================
# author: Paulo Trigo Silva (PTS)
# version: v07
# v03 tem acesso DBPedia
# v03 contem varias melhorias
# v04 mudou de nome:
# - d02_cherryPy_DBPedia.py (nome anterior)
# - d02_cherryPy_navegadorSPARQLendpoint.py (nome atual)
# v04 acesso a YAGO esta' indisponivel, pelo que:
# - interrogacao sobre rkbexplorer foi adicionada
# v04 generalizado acesso a diferentes SPARQLendpoint com interrogacao especifica
# ===============================


# Executar numa consola:
# python d02_cherryPy_DBPedia
#
# No Browser fazer:
# http://localhost:8580/
# (excuta a funcao "index")
#


#______________________________________________________________________________
# Importar modulos
import cherrypy
from x_util_JSONwithMD import getResultSet
from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF
from urllib.error import HTTPError



#______________________________________________________________________________
# Utility functions
def getConnection( url ):
   repository_path = ""
   repository = ""
   FULL_SPARQL_ENDPOINT = url + repository_path + repository
   connection = SPARQLWrapper( FULL_SPARQL_ENDPOINT )
   return connection


def query_convert( connection ):
   result = None
   try: result = connection.query()
   except HTTPError: print( ">> HTTPError: SPARQL-endpoint unavailable! <<" )
   else: result = result.convert()
   return result



#______________________________________________________________________________
# Corpo principal
class Main( object ):
   def __init__( self, url, sparql, info, formato="str" ):
      # Request handler objects can create their own nested request
      # handler objects. Simply create them inside their __init__ methods!
      self.info = info
      self.formato = formato
      self.interrogacao = Interrogacao( url, sparql )


   @cherrypy.expose
   def index( self ):
      texto = \
         """
         <form action="saudacao" method="GET">
           Nome? <input type="text" name="nome" />
           <input type="submit" value=">>>" />
         </form>
         """
      return texto


   @cherrypy.expose
   def saudacao( self, nome=None ):
      # CherryPy passes all GET and POST variables as method parameters.
      # It doesn't make a difference where the variables come from, how
      # large their contents are, and so on.
      #
      # You can define default parameter values as usual. In this
      # example, the "name" parameter defaults to None so we can check
      # if a name was actually specified.
      texto = 'Favor editar nome <a href="./">aqui</a>.'
      if nome:
         texto = "Ola, %s" % nome
         acessoURL = \
            """
            <ul>
               <li>
                  <a href="./interrogacao?formato=%s">
                  %s
                  </a>
               </li>
            </ul>
            """ \
            % ( self.formato, self.info )
         
         texto += acessoURL
      return texto



#______________________________________________________________________________
# Apresentacao do resultado da interrogacao
class Interrogacao( object ):
   def __init__( self, url=None, sparql=None ):
      if( not url ): self.url = "http://dblp.rkbexplorer.com/sparql/"
      if( not sparql ): self.sparql = sparql_rkbexplorer
      self.url = url
      self.sparql = sparql

      
   @cherrypy.expose
   def index( self, formato=None ):
      lineBreak = "<BR>"
      usage = ""
      usage += "USAGE:" + lineBreak + lineBreak
      usage += "http://localhost:8580/interrogacao?formato=str" + lineBreak
      usage += "or" + lineBreak
      usage += "http://localhost:8580/interrogacao?formato=html"
      # tambem poderia ser RDF e assim contribuir para a "linked Data"
      if formato != "html" and formato != "str": return usage

      result = self.getResult( self.sparql, self.url )
      if formato == "str": return str( result )
      
      result_html = ""
      separator = "&nbsp | &nbsp"
      for [x] in result:
         result_html += separator
         result_html += "<a href=" + str( x ) + ">" + str( x ) + "</a>" + separator
         result_html += lineBreak
      
      return result_html


   def getResult( self, query, url ):
      connection = getConnection( url )
      connection.setQuery( query )
      connection.setReturnFormat( JSON )
      result = query_convert( connection )
      result = getResultSet( result )
      return result



#______________________________________________________________________________
# The SPARQL Query Set
# sparql = "Quais as publicações do tipo "Book-Reference" posteriores a 2013?"
# (cf., http://dblp.rkbexplorer.com/sparql/)
sparql_rkbexplorer = \
  """
  PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
  PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
  PREFIX akt:  <http://www.aktors.org/ontology/portal#>
  PREFIX akt_supp: <http://www.aktors.org/ontology/support#>
  PREFIX akts_date: <http://www.aktors.org/ontology/date#>

  SELECT ?pub
  WHERE {
   ?sub_type rdfs:subClassOf akt:Publication-Reference .
   FILTER( ?sub_type = akt:Book-Reference ) .
   ?pub rdf:type ?sub_type .
   ?pub akt:has-title ?pub_title .
   ?pub akt:has-author ?author .
   ?pub akt:has-date ?pub_date .
   FILTER( ?pub_date >= akts_date:2013 )
   }
  LIMIT 50
  """



#______________________________________________________________________________
# The SPARQL Query Set
# sparql = "Quais as bandas de Jazz e respetivos membros (apenas de "England")?"
# (cf., http://dbpedia.org/sparql)
sparql_dbpedia = \
  """
  PREFIX dbo: <http://dbpedia.org/ontology/>
  PREFIX dbr: <http://dbpedia.org/resource/>
  PREFIX dbp: <http://dbpedia.org/property/>
  PREFIX foaf: <http://xmlns.com/foaf/0.1/>
  PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

  SELECT STR(?bandName) ?personName 
  WHERE {
    ?band dbo:genre dbr:Jazz .
    ?band foaf:name ?bandName .
    FILTER( lang(?bandName) = "en" )

    ?band dbo:bandMember ?person .
    ?person foaf:name ?personName .
    FILTER( lang(?personName) = "en" )
  }
  ORDER BY DESC( ?band )
  """



#______________________________________________________________________________
import os.path
#cherrypy_conf = os.path.join( os.path.dirname( __file__ ), 'd00_cherrypy.conf' )
cherrypy_conf = 'd00_cherrypy.conf'
if __name__ == '__main__':
   url = "http://dblp.rkbexplorer.com/sparql/"
   sparql = sparql_rkbexplorer
   info = "dblp.rkbexplorer: Quais as publicações do tipo 'Book-Reference' posteriores a 2013?"
   #atencao: o seguimento de alguns links pode demorar um pouco!

   # o SPARQLendpoint da DBPedia esteve algum tempo sem responder (MAI.2017 \ PTS)
   #url = "http://dbpedia.org/sparql"
   #sparql = sparql_dbpedia
   #info = "Quais as bandas de Jazz e respetivos membros (apenas de \"England\")?"

   #formato = "str"
   formato = "html"
   # iniciar o servico "cherryPy"
   cherrypy.quickstart( Main( url=url, sparql=sparql, info=info, formato=formato ), \
                        config = cherrypy_conf )




