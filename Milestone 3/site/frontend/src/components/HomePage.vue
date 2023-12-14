<template>
  <div>
    <div class="search-container">
      <input v-model="query" id="searchInput" name="searchQuery" class="search-input" placeholder="Enter your search query" />
      <button @click="search" class="search-button">Search</button>
    </div>

    <!-- Display search results or no results message -->
    <div v-if="searched" class="search-results">
      <h2 v-if="results.length > 0">Search Results</h2>
      <ul v-if="results.length > 0" class="book-list">
        <div v-for="result in results" :key="result.book_id" class="book-item" @click="showBookDetails(result)">
          <div class="book-box">
            <h3 class="book-title">{{ result.book_title }}</h3>
            <!-- Add other book details -->
          </div>
        </div>
      </ul>
      <p v-else class="no-results"></p>
    </div>
  </div>
  <!-- Include the modal component -->
  <Modal :selectedBook="selectedBook" :showModal="isModalVisible" @close="closeModal" />
</template>

<script>
import axios from 'axios';
import Modal from './BookPage.vue';

export default {
  components: {
    Modal
  },
  data() {
      return {
        query: '',
        results: [],
        searched: false,
        isModalVisible: false,
        selectedBook: {}
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
                    q: this.query,
                    qf: "book_title^2 reviews.text^2 reviews.summary description categories",
                    rows: 40,
                    defType:"edismax",
                    "q.op":"OR"
                }
            })
        })
            .then(response => {
            this.results = response.data.response.docs;
            //console.log(this.results[0]["reviews.summary"]);
        })
            .catch(error => {
            console.error('Error searching:', error);
        });
    },
    showBookDetails(book) {
      this.selectedBook = book;
      this.isModalVisible = true;
    },
    closeModal() {
      this.isModalVisible = false;
    }
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
  background-color: #DDD8C4;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 20px;
  width: 200px; /* Set a fixed width */
  height: 200px; /* Set a fixed height */
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.book-title {
  margin-bottom: 5px;
}

/* Define a grid layout for the book list */
.book-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); /* Three columns with equal width */
  gap: 20px; /* Spacing between items */
  padding: 0;
  margin: 0;
  list-style: none;
  list-style: none;
  padding: 0;
  margin: 0;
}

/* Remove list-style from each book item */
.book-item {
  list-style: none;
  padding: 0;
  margin: 0;
  cursor: pointer; /* Set the cursor to pointer */
  text-decoration: none; /* Remove underline */
  color: inherit; /* Use parent's color */
}
/* Remove underlines specifically from h3 elements inside .book-box */
.book-box h3 {
  text-decoration: none;
}
</style>
