<script>
import Content from "@/components/Content.vue"

export default {
  name: "WithLoading",
  components: {
    Content,
  },
  props: {
    isLoading: {
      type: Boolean,
      default: true,
    },
    isError: {
      type: Boolean,
      default: false,
    },
    errorText: {
      type: String,
      default: "Not found",
    },
  }
}
</script>


<template>
  <Content v-if="isLoading">
    <p class="plain-text">Loading</p>
  </Content>

  <Content v-else-if="isError">
    <p class="plain-text">{{ errorText }}</p>
  </Content>

  <slot v-else></slot>
</template>


<style scoped lang="scss">
.plain-text {
}
</style>
