# Step 1: Run Solr Docker container
docker run -p 8983:8983 --name solr -v "$(pwd)":/data -d solr:9.3

# Step 2: Create Solr core
docker exec solr bin/solr create_core -c books_m3_keywords

# Step 3: Copy synonyms.txt to Solr container
# docker cp synonyms.txt solr:/var/solr/data/books_m3_keywords/conf/synonyms.txt

# Step 4: Update Solr schema
curl -X POST -H "Content-type:application/json" --data-binary "@schema_m3_keywords.json" http://localhost:8983/solr/books_m3_keywords/schema

# Step 5: Post data to Solr core
docker exec solr bin/post -c books_m3_keywords ../../data/books_data_reviews_sample_keywords.json
