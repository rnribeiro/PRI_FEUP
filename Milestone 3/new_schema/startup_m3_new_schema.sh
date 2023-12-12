# Step 1: Run Solr Docker container
docker run -p 8983:8983 --name solr -v "$(pwd)":/data -d solr:9.3

# Step 2: Create Solr core
docker exec solr bin/solr create_core -c books_m3_new_schema

# Step 4: Update Solr schema
curl -X POST -H "Content-type:application/json" --data-binary "@schema_m3_new_schema.json" http://localhost:8983/solr/books_m3_new_schema/schema

# Step 5: Post data to Solr core
docker exec solr bin/post -c books_m3_new_schema ../../data/books_data_reviews.json
