# -*- coding: cp1252 -*-
# ===============================
# author: Paulo Trigo Silva (PTS)
# version: v07
# ===============================


# Executar numa consola:
# python d01_cherryPy_olaMundo
#
# No Browser fazer:
# http://localhost:8580/
# (executa a funcao "index")
#
# http://localhost:8580/saudacao?nome=PT
# (executa a funcao saudacao e passa-lhe o parametro "nome"
#


#______________________________________________________________________________
# Importar modulos
import cherrypy


#______________________________________________________________________________
# Corpo principal

class Main( object ):

   @cherrypy.expose
   def index( self ):
      return "Ola Mundo"

   @cherrypy.expose
   def saudacao( self, nome ):
      return "Ola, %s" % nome


import os.path
#cherrypy_conf = os.path.join( os.path.dirname( __file__ ), 'e00_cherrypy.conf' )
cherrypy_conf = 'd00_cherrypy.conf'
if __name__ == '__main__':
   # iniciar o servico "cherryPy"
   cherrypy.quickstart( Main(), config = cherrypy_conf )


