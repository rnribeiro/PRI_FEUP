<template>
  <div>
    <!-- Header section -->
    <header class="header">
      <div class="logo">
        <!-- Replace 'logo.png' with the path to your logo image -->
        <img src="assets/logo.png"/>
      </div>
      <div class="title">
        <!-- Add the name/title here -->
        <h1>BOOKS</h1>
      </div>
    </header>    
  </div>
  <HomePage msg="Books"/>
</template>


<script>
import HomePage from './components/HomePage.vue'

export default {
  name: 'App',
  components: {
    HomePage
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #50808E;
  margin-top: 60px;
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


<style scoped>
/* Styles for the header */
.header {
  position: fixed; /* Fixed position */
  top: 0; /* Stick to the top */
  left: 0;
  right: 0;
  z-index: 1000; /* Set a higher z-index if needed */
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #50808E;
  padding: 10px 20px;
  color: white;
}

.logo img {
  max-width: 100px; /* Set max width for the logo image */
}

.title h1 {
  margin: 0;
  font-size: 24px;
}

/* Adjust body margin to accommodate fixed header */
body {
  margin-top: 70px; /* Adjust this value based on your header's height */
}

</style>
