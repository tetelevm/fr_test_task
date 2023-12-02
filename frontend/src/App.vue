<script>
import { defineComponent } from "vue"
import Navbar from "@/components/Navbar.vue"

export default defineComponent({
  components: {
    Navbar,
  },
})

</script>

<template>
  <div class="navbar-div">
    <Navbar />
  </div>
  <div class="main-div">
    <router-view />
  </div>
</template>

<style lang="scss">
@import "public/styles";

body {
  margin: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: $black;
}

.navbar-div {
  height: 7vh;
}

.main-div {
  height: 93vh;
}
</style>
