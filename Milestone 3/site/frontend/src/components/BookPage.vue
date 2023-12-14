<template>
  <div class="modal" v-if="showModal">
    <div class="modal-content">
      <!-- Book details -->
      <h2>{{ selectedBook.book_title }}</h2>
      <p v-for="(author, index) in selectedBook.authors" :key="index"><b>Author:</b> {{ author }}</p>
      <p v-for="(category, index) in selectedBook.categories" :key="index"><b>Genre:</b> {{ category }}</p>
      <p><b>Description:</b> {{ selectedBook.description }}</p>
      <p><b>Publisher:</b> {{ selectedBook.publisher }}</p>
      <p><b>Published Year:</b> {{ selectedBook.publishedYear }}</p>
      <!-- Add other book details here -->
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
}

.close-icon {
  cursor: pointer; /* Set the cursor to pointer */
  color:#A3C9A8;
}
</style>
