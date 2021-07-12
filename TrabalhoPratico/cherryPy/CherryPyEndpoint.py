import os.path
cherrypy_conf = 'cherrypy.conf'
import cherrypy
from queries import *
from x_util_JSONwithMD import getResultSet
from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF
from urllib.error import HTTPError

#______________________________________________________________________________
# Definir Global Variables
sparql_endpoint = "http://localhost:8280/rdf4j-server/"
repository_path = "repositories/"
repository = "tpratic"
FULL_SPARQL_ENDPOINT = sparql_endpoint + repository_path + repository

FORMAT="htlm"

def query_convert( connection ):
   result = None
   try: result = connection.query()
   except HTTPError: print( ">> HTTPError: SPARQL-endpoint unavailable! <<" )
   else: result = result.convert()
   return result

#______________________________________________________________________________
# Apresentacao do resultado da interrogacao
class Interrogacao():
   def __init__( self, url=None, sparql=None ):
      self.url = FULL_SPARQL_ENDPOINT
      self.query = sparql
      
   @cherrypy.expose
   def index( self ):
      lineBreak = "<BR>"
      usage = ""
      usage += "USAGE:" + lineBreak + lineBreak
      usage += "http://localhost:8580/interrogacao" + lineBreak
      usage += "or" + lineBreak
      usage += "http://localhost:8580/interrogacao"

      result = self.getResult( self.url )
      if FORMAT == "str": return str( result )
      
      result_html = ""
      separator = "&nbsp | &nbsp"
      for arr in result:
        result_html += "<div>"
        result_html += separator
        for elem in arr:
            result_html += str(elem) + separator
                
        result_html += "</div>"
      
      return result_html

   def getResult( self, url ):
      connection = SPARQLWrapper( FULL_SPARQL_ENDPOINT )
      print( "My endpoint: " + connection.endpoint )
      connection.setQuery( self.query )
      connection.setReturnFormat( JSON )
      result = connection.query()
      result = query_convert( connection )
      result = getResultSet( result )
      return result




#______________________________________________________________________________
# Main
class Main( object ):

   def __init__( self ):
      # Request handler objects can create their own nested request
      # handler objects. Simply create them inside their __init__ methods!
      self.formato = FORMAT
      self.subClassesQuery = Interrogacao( FULL_SPARQL_ENDPOINT, subClasses_query )
      self.instanciaQuery = Interrogacao( FULL_SPARQL_ENDPOINT, instancia_query )
      self.bookQuery = Interrogacao( FULL_SPARQL_ENDPOINT, book_query )
      self.journalQuery = Interrogacao( FULL_SPARQL_ENDPOINT, journal_query )
      self.proceedingsQuery = Interrogacao( FULL_SPARQL_ENDPOINT, proceedings_query )
      self.authoraffiliationpublicationQuery = Interrogacao( FULL_SPARQL_ENDPOINT, authoraffiliationpublication_query )
      

   @cherrypy.expose
   def index( self ):
      texto = "Lista de Queries Disponiveis"
      acessoURL = \
         """
         <ul>
            <li>
               <a href="./subClassesQuery?">
               %s
               </a>
            </li>
            <li>
               <a href="./instanciaQuery?">
               %s
               </a>
            </li>
            <li>
               <a href="./bookQuery?">
               %s
               </a>
            </li>
            <li>
               <a href="./journalQuery?">
               %s
               </a>
            </li>
            <li>
               <a href="./proceedingsQuery?">
               %s
               </a>
            </li>
            <li>
               <a href="./authoraffiliationpublicationQuery?">
               %s
               </a>
            </li>
         </ul>
         """ \
         % ( "Listagen de sub-classes", "Instancias de Article-Reference", "Listagem de Livros", "Listagem de Jornais", "Listagem de Procedimentos", "Algumas Relacoes" )
      texto += acessoURL
      return texto

if __name__ == '__main__':
   cherrypy.quickstart( Main(), config = cherrypy_conf )