<template>
  <div>
    <div class="search-container">
      <input v-model="query" class="search-input" placeholder="Enter your search query" />
      <button @click="search" class="search-button">Search</button>
    </div>

    <!-- Display search results or no results message -->
    <div v-if="searched">
      <div v-if="results.length > 0" class="search-results">
        <h2>Search Results</h2>
        <ul>
          <li v-for="result in results" :key="result.id">
            {{ result.title }}
          </li>
        </ul>
      </div>
      <div v-else class="no-results">
        <p>No results found.</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      query: '',
      results: [],
      searched: false,
    };
  },
  methods: {
    search() {
      this.searched = true;
      axios.post('http://localhost:8000/solr/request', {
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Content-Type': 'application/json',
        },
        data: JSON.stringify({
          params: {
            q: this.query
          }
        })
      })
      .then(response => {
        this.results = response.data.response.docs;
      })
      .catch(error => {
        console.error('Error searching:', error);
      });
    },
  },
};
</script>

<style scoped>
/* Styles for search box */
.search-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}

.search-input {
  padding: 8px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 300px;
}

.search-button {
  padding: 8px 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.search-button:hover {
  background-color: #0056b3;
}

.search-results, .no-results {
  margin-top: 20px;
}
</style>
