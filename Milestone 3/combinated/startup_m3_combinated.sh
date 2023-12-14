# Step 1: Run Solr Docker container
# docker run -p 8983:8983 --name solr -v "$(pwd)":/data -d solr:9.3

# Step 2: Create Solr core
docker exec solr bin/solr create_core -c books_m3_combinated

# Step 3: Copy synonyms.txt to Solr container
docker cp synonyms.txt solr:/var/solr/data/books_m3_combinated/conf/synonyms.txt

# Step 4: Update Solr schema

# Step 5: Post data to Solr core
docker exec solr bin/post -c books_m3_combinated ../../data/books_data_reviews.json
