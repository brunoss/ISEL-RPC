book_query = \
"""
   PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
   PREFIX dblp:  <http://swat.cse.lehigh.edu/resources/onto/dblp.owl#>
   PREFIX owl:  <http://www.w3.org/2002/07/owl#>
  
   SELECT DISTINCT ?pub ?pub_title ?author ?author_full_name ?pub_date ?pub_volume ?pub_web_address ?same_as
   WHERE 
      {
      ?pub rdf:type dblp:Book-Reference .
      ?pub dblp:has-title ?pub_title .
      ?pub dblp:has-author ?author .
      ?author rdf:type dblp:Person .
      ?author dblp:full-name ?author_full_name .
      OPTIONAL { ?author dblp:has-affiliation ?author_affiliation . 
               ?author_affiliation dblp:has-pretty-name ?author_affiliation_name . } .
      ?pub dblp:has-date ?pub_date .
      ?pub dblp:has-volume ?pub_volume .
      ?pub dblp:has-web-address ?pub_web_address .
      OPTIONAL { ?pub owl:sameAs ?same_as } .
      }
   LIMIT 20
"""

subClasses_query= \
"""
   PREFIX dblp:  <http://swat.cse.lehigh.edu/resources/onto/dblp.owl#>
   SELECT DISTINCT ?sub_type ?o
   WHERE 
      { 
      ?sub_type rdfs:subClassOf ?o .
      }
   LIMIT 50
"""

instancia_query= \
"""
   PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
   PREFIX dblp:  <http://swat.cse.lehigh.edu/resources/onto/dblp.owl#>
   
   SELECT DISTINCT ?instance
   WHERE 
      { 
      ?instance rdf:type dblp:Article-Reference .
      }
   LIMIT 50
"""

journal_query= \
"""
   PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
   PREFIX dblp:  <http://swat.cse.lehigh.edu/resources/onto/dblp.owl#>
   
   SELECT DISTINCT ?pub ?pub_title ?author ?author_full_name ?author_affiliation_name ?pub_date ?pub_volume ?pub_web_address ?pub_type ?pub_type_title ?same_as
   WHERE 
      {
      ?pub rdf:type dblp:Article-Reference .
      ?pub dblp:article-of-journal ?pub_type .
      ?pub_type dblp:has-title ?pub_type_title .
      ?pub dblp:has-title ?pub_title .
      ?pub dblp:has-date ?pub_date .
      ?pub dblp:has-volume ?pub_volume .
      ?pub dblp:has-web-address ?pub_web_address .
      ?pub dblp:has-author ?author .
      ?author rdf:type dblp:Person .
      ?author dblp:full-name ?author_full_name .
      OPTIONAL { ?author dblp:has-affiliation ?author_affiliation . 
               ?author_affiliation dblp:has-pretty-name ?author_affiliation_name . } .
      }
   LIMIT 20
"""

proceedings_query= \
"""
   PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
   PREFIX owl:  <http://www.w3.org/2002/07/owl#>
   PREFIX dblp:  <http://swat.cse.lehigh.edu/resources/onto/dblp.owl#>
   
   SELECT DISTINCT ?pub ?pub_title ?author ?author_full_name ?pub_date ?pub_type ?pub_type_title ?pub_journal_type_title ?pub_journal_type ?pub_web_address ?same_as
   WHERE 
      {
      ?pub_type rdf:type dblp:Conference-Proceedings-Reference .
      ?pub_type dblp:has-title ?pub_type_title .
      ?pub dblp:cites-publication-reference ?pub_type .

      ?pub dblp:has-title ?pub_title .
      ?pub dblp:has-date ?pub_date .
      ?pub dblp:has-web-address ?pub_web_address .
      ?pub dblp:has-author ?author .
      ?author rdf:type dblp:Person .
      ?author dblp:full-name ?author_full_name .

      OPTIONAL { ?author dblp:has-affiliation ?author_affiliation . 
               ?author_affiliation dblp:has-pretty-name ?author_affiliation_name . } .

      OPTIONAL { ?pub dblp:article-of-journal ?pub_journal_type .
               ?pub_journal_type dblp:has-title ?pub_journal_type_title } .

      OPTIONAL { ?pub owl:sameAs ?same_as } .
      }
   LIMIT 20
"""

authoraffiliationpublication_query= \
"""
   PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
   PREFIX dblp:  <http://swat.cse.lehigh.edu/resources/onto/dblp.owl#>

   SELECT DISTINCT ?author ?author_name ?author_affiliation ?author_affiliation_name ?pub ?pub_title
   WHERE
      {
      ?author rdf:type dblp:Person .
      ?author dblp:full-name ?author_name .
      FILTER( regex( str( ?author_name ), "Dijkstra" ) )

      ?pub dblp:has-author ?author .
      ?pub dblp:has-title ?pub_title .

      OPTIONAL{ ?author dblp:has-affiliation ?author_affiliation .
               ?author_affiliation dblp:has-pretty-name ?author_affiliation_name } .
      }
   LIMIT 20
"""
