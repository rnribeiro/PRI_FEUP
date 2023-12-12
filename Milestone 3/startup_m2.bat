REM Step 1: Run Solr Docker container
docker run -p 8983:8983 --name solr -v %cd%:/data -d solr:9.3

REM Step 2: Create Solr core
docker exec solr bin/solr create_core -c books_m2

REM Step 4: Update Solr schema
curl -X POST -H "Content-type:application/json" --data-binary "@schema_m2.json" http://localhost:8983/solr/books_m2/schema

REM Step 5: Post data to Solr core
docker exec solr bin/post -c books_m2 ../../data/books_data_reviews.json
