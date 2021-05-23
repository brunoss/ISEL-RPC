import sys
from myENDPOINT_access import f_ENDPOINT_access
from SPARQLWrapper import SPARQLWrapper, XML, N3, TURTLE, RDF, JSON, JSONLD

if __name__ == "__main__":
    f = open("query.txt", "r")
    query = f.read()
    f.close()

    repository = sys.argv[1]
    list_FORMAT_fallback = [JSONLD, JSON, TURTLE, XML, N3, RDF]

    responseFormat, resultSet = f_ENDPOINT_access( query, list_FORMAT_fallback, repository )

    f = open("out.txt", "w")
    f.write(str(resultSet))
    f.close()
    
    print(resultSet)