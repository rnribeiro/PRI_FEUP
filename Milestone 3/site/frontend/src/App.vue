<template>
  <div>
    <!-- Header section -->
    <header class="header">
      <div class="logo">
        <img src="./assets/book.png" alt="Logo" class="logo-image" />
        <span class="logo-text">BOOKS</span>
      </div>
    </header>
    <HomePage/>
  </div>
</template>

<script>
import HomePage from './components/HomePage.vue'

export default {
  name: 'App',
  components: {
    HomePage
  },
}
</script>

<style>
/* General styles for the app */
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #50808E;
  margin-top: 60px; /* Keep space for the fixed header */
  padding-top: 30px; /* Alternatively, you can use padding-top */
}

/* Styles for the header */
.header {
  position: fixed; /* Fixed position */
  top: 0; /* Stick to the top */
  left: 0;
  right: 0;
  z-index: 1000; /* Set a higher z-index if needed */
  display: flex;
  align-items: center;
  background-color: #50808E;
  padding: 10px 20px;
  color: white;
}

/* Styles for the logo */
.logo {
  display: flex;
  align-items: center;
}

.logo-image {
  max-width: 80px; /* Set max width for the logo image */
  margin-right: 10px; /* Adjust spacing between image and text */
}

.logo-text {
  font-size: 24px;
  color:#DDD8C4
}
</style>

<!--
############COLORS################
Bone
#DDD8C4

Celadon
#A3C9A8

Cambridge Blue
#84B59F

Cambridge Blue
#69A297

Air Force Blue
#50808E
-->