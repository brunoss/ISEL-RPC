# -*- coding: cp1252 -*-
# ===============================
# author: Paulo Trigo Silva (PTS)
# version: v07 | v03 corrigiu v02
# ===============================


#______________________________________________________________________________
# Exemplo de estrutura JSON
JSONvar = \
{ "head": { "link": [], "vars": ["x", "Concept"] }, \
  "results": { "distinct": False, "ordered": True, \
               "bindings": [ \
                  { "x": { "type": "uri", "value": "http://dbpedia.org/ontology/purpose" }, \
                    "Concept": { "type": "uri", "value": "http://www.w3.org/2002/07/owl#DatatypeProperty" }}, \
                  { "x": { "type": "uri", "value": "http://dbpedia.org/ontology/supplementalDraftRound" },
                    "Concept": { "type": "uri", "value": "http://www.w3.org/2002/07/owl#DatatypeProperty" }}, \
                  { "x": { "type": "uri", "value": "http://dbpedia.org/ontology/podiums" }, \
                    "Concept": { "type": "uri", "value": "http://www.w3.org/2002/07/owl#DatatypeProperty" }}, \
                  { "x": { "type": "uri", "value": "http://dbpedia.org/ontology/buildingStartDate" }, \
                    "Concept": { "type": "uri", "value": "http://www.w3.org/2002/07/owl#DatatypeProperty" }}, \
                  { "x": { "type": "uri", "value": "http://dbpedia.org/ontology/longtype" }, \
                    "Concept": { "type": "uri", "value": "http://www.w3.org/2002/07/owl#DatatypeProperty" }}, \
                  { "x": { "type": "uri", "value": "http://dbpedia.org/ontology/sessionNumber" }, \
                    "Concept": { "type": "uri", "value": "http://www.w3.org/2002/07/owl#DatatypeProperty" }}, \
                  { "x": { "type": "uri", "value": "http://dbpedia.org/ontology/orbitalPeriod" }, \
                    "Concept": { "type": "uri", "value": "http://www.w3.org/2002/07/owl#DatatypeProperty" }}, \
                  { "x": { "type": "uri", "value": "http://dbpedia.org/ontology/status" }, \
                    "Concept": { "type": "uri", "value": "http://www.w3.org/2002/07/owl#DatatypeProperty" }}, \
                  { "x": { "type": "uri", "value": "http://dbpedia.org/ontology/originalMaximumBoatBeam" }, \
                    "Concept": { "type": "uri", "value": "http://www.w3.org/2002/07/owl#DatatypeProperty" }}, \
                  { "x": { "type": "uri", "value": "http://dbpedia.org/ontology/nssdcId" }, \
                    "Concept": { "type": "uri", "value": "http://www.w3.org/2002/07/owl#DatatypeProperty" }} ] } } \


#JSONvar = \
#<COMPLETAR> alterando x e Concept para myX myY myZ


#______________________________________________________________________________
# Transforma estrutura JSON em lista de listas
# onde cada lista e' uma linha do resultado de uma interrogacao SPARQL
# JSON = JavaScript Object Notation; lightweight data-interchange format
# (easy for humans to read and write; easy for machines to parse and generate)
#______________________________________________________________________________
##def getResultSet( result ):
##   # descomentar para ver a estrutura JSON de "result"
##   # print result
##   if result == None: return None
##   resultSet = []
##   varSet = result[ 'head' ][ 'vars' ]
##   for dict_data in result[ 'results' ][ 'bindings' ]:
##      l_aux = []
##      for var in varSet:
##        l_aux += [ dict_data[ var ][ 'value' ] ]
##      resultSet += [ l_aux ]
##   return resultSet

# nova versao (v03): trata erro (da v02) acima comentada
# que ocorria ao usar um OPTIONAL que não devolva duplos
def getResultSet( result ):
   if result == None: return None
   resultSet = []
   varSet = result[ 'head' ][ 'vars' ]
   for dict_data in result[ 'results' ][ 'bindings' ]:
      l_aux = []
      for var in varSet:
         if var in dict_data.keys():
            l_aux += [ dict_data[ var ][ 'value' ] ]
         else: 
            l_aux += [None]
      resultSet += [ l_aux ]
   return resultSet



#______________________________________________________________________________
# Teste
if __name__ == '__main__':
   list_JSONvar = getResultSet( JSONvar )
   print()
   print( list_JSONvar )
   print()
   for [a, b] in list_JSONvar:
      print( "%s || %s" % (a, b) )
   print()
