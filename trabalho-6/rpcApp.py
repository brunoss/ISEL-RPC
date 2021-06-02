import sys
import os.path
from myENDPOINT_access import f_ENDPOINT_access
from SPARQLWrapper import SPARQLWrapper, XML, N3, TURTLE, RDF, JSON, JSONLD

def chooseElement(arr, prompt):
    print(prompt)
    i = 1
    for f in arr:
        print(str(i) + ". " + f)
        i += 1
    
    j = -1
    while j <= 0 or j > len(arr):
        j = int(input(prompt))
    return arr[j - 1]
    
if __name__ == "__main__":
    if not os.path.exists("query.txt"):
        print("please create query.txt with valid SPARQL Query")
        
    f = open("query.txt", "r")
    query = f.read()
    f.close()

    #print('default repository http://localhost:8280/rdf4j-server/repositories/repo-con')
    print('default repository http://dbtune.org/bbc/programmes/sparql/')
    repository = input('Introduza o url do repositório: ')
    if not repository:
        repository = "http://dbtune.org/bbc/programmes/sparql/"
    
    formats = [XML, N3, TURTLE, RDF, JSON, JSONLD]
    chosenFormat = chooseElement(formats, "Escolha o formato: ")
    
    responseFormat, resultSet = f_ENDPOINT_access( query, [chosenFormat], repository )

    f = open("out.txt", "w")
    f.write(str(resultSet))
    f.close()
    
    print(resultSet)