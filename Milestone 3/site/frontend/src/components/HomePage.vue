<template>
  <div>
    <div class="search-container">
      <input v-model="query" class="search-input" placeholder="Enter your search query" />
      <button @click="search" class="search-button">Search</button>
    </div>

    <!-- Display search results or no results message -->
    <div v-if="searched" class="search-results">
      <h2 v-if="results.length > 0">Search Results</h2>
      <ul v-if="results.length > 0" class="book-list">
        <li v-for="result in results" :key="result.id">
          <div class="book-box">
            <h3 class="book-title">{{ result.book_title }}</h3>
            <p>Publisher: {{ result.publisher }}</p>
            <!-- Add other details you want to display -->
          </div>
        </li>
      </ul>
      <p v-else class="no-results"></p>
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
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  color: #333;
}

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
  border-radius: 25px;
  width: 300px;
}

.search-button {
  padding: 8px 16px;
  background-color: #50808E;
  color: white;
  border: none;
  border-radius: 25px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.search-button:hover {
  background-color: #50808E;
}

.search-results, .no-results {
  margin-top: 20px;
}

/* Styles for the grey box around the book title */
.book-box {
  background-color: #f2f2f2;
  padding: 10px;
  border-radius: 8px;
  margin-bottom: 10px;
}

.book-title {
  margin-bottom: 5px;
}

/* Define a grid layout for the book list */
.book-list {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* Three columns with equal width */
  gap: 20px; /* Spacing between items */
  padding: 0;
  margin: 0;
}

/* Remove list-style from each book item */
.book-item {
  list-style: none;
  padding: 0;
  margin: 0;
}
/* Remove default list-style */
.book-list {
  list-style: none;
  padding: 0;
  margin: 0;
}
</style>
