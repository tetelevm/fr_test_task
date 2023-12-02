<script>
export default {
  name: "Content",
}
</script>


<template>
  <div class="main-content-general">
    <div class="main-content">
      <slot></slot>
    </div>
  </div>
</template>


<style lang="scss">
.main-content-general {
  max-width: 50%;
  margin: 1rem auto 0 auto;
}

.main-content {
  // for overriding
}
</style>
