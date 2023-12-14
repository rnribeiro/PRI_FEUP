<template>
  <div class="modal" v-if="showModal">
    <div class="modal-content">
      <!-- Book details -->
      <h2>{{ selectedBook.book_title }}</h2>
      <!-- Display Author(s) -->
      <p v-if="selectedBook.authors && selectedBook.authors.length > 0">
        <b>Author:</b>
        <span v-for="(author, index) in selectedBook.authors" :key="index">
          {{ author }}{{ index !== selectedBook.authors.length - 1 ? ', ' : '' }}
        </span>
      </p>
      <!-- Display Genre(s) -->
      <p v-if="selectedBook.categories && selectedBook.categories.length > 0">
        <b>Genre:</b>
        <span v-for="(category, index) in selectedBook.categories" :key="index">
          {{ category }}{{ index !== selectedBook.categories.length - 1 ? ', ' : '' }}
        </span>
      </p>
      <!-- Display Description -->
      <p v-if="selectedBook.description"><b>Description:</b> {{ selectedBook.description }}</p>
      <!-- Display Publisher -->
      <p v-if="selectedBook.publisher"><b>Publisher:</b> {{ selectedBook.publisher }}</p>
      <!-- Display Published Year -->
      <p v-if="selectedBook.publishedYear"><b>Published Year:</b> {{ selectedBook.publishedYear }}</p>
      <!-- Display reviews summaries -->
      <div v-if="selectedBook && selectedBook['reviews.summary']">
        <p><b>Opinions:</b> {{ formatSummary(selectedBook['reviews.summary']) }}</p>
      </div>
      <div v-if="selectedBook && selectedBook['reviews.text']">
        <p><b>Reviews:</b> {{ formatSummary(selectedBook['reviews.text']) }}</p>
      </div>
      <!-- Close icon in the top right corner -->
      <span class="close-icon" @click="closeModal">Close</span>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    selectedBook: {
      type: Object,
      default: () => ({})
    },
    showModal: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    closeModal() {
      this.$emit('close');
    },
    formatSummary(summaryArray) {
      return summaryArray.join(', ');
    },
    formatText(textArray) {
      return textArray.join(' ');
    }
  }
};
</script>

<style scoped>
/* Styles for the modal */
.modal {
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 25px;
  width: 70%; /* Set the desired width */
  height: 70%; /* Set the desired height */
  overflow: auto; /* Enable scrolling if content exceeds the set dimensions */
}

.close-icon {
  cursor: pointer; /* Set the cursor to pointer */
  color:#A3C9A8;
}
</style>
