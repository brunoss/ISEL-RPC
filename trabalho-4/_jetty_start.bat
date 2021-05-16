#PTS


set jetty=".\..\jetty-distribution-9.4.8.v20171121"

cd %jetty%\

java -jar start.jar jetty.http.port=8280

#PTS
# depois de iniciar o Jetty (servidor http) pode testar o RDF4J (ex Sesame), para isso:
# 1) inicie o Browser
# 2) aponte o Browser para: http://localhost:8280/rdf4j-workbench