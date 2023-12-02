<template>
  <nav>
    <div class="row">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
}
</script>


<style scoped lang="scss">
@import "public/styles";

nav {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;

  background: $gray url("~@/assets/navbar-bg.png") 50% 100% repeat;

  border-bottom: 2px solid $dark-blue;
  font-size: 1.5rem;

  a {
    font-weight: bold;
    color: $black;

    &.router-link-exact-active {
      color: $dark-blue;
    }
  }
}
</style>
