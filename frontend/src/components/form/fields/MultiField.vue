<script>
export default {
  name: "MultiField",
  props: {
    question: {
      type: Object,
      default: () => {
        return {
          order: 0,
          is_required: false,
          structure: {
            variants: [],
          },
        }
      },
      required: true,
    },
  },
  data() {
    return {
      value: [],
    }
  },
  computed: {
    variants() {
      const variants = this.$props.question.structure.variants || []
      return variants.sort((a, b) => a.order - b.order)
    },
    isDone() {
      return (
          !this.$props.question.is_required
          || !!this.value.length
      )
    },
  },
}
</script>


<template>
  <div>
    <div
        v-for="variant in variants"
        :key="variant.order"
        class="field"
    >
      <input
          type="checkbox"
          :name="'question_' + question.order"
          :value="variant.order"
      >
      <label :for="variant.order">{{ variant.text }}</label>
    </div>
  </div>
</template>


<style scoped lang="scss">
.field {
  margin-top: 0.3rem;
  display: flex;

  input {
    margin-left: 0.3rem;
    width: 1.3rem;
    height: 1.3rem;
    cursor: pointer;
  }
  label {
    margin: auto 0 auto 0.5rem;
  }
}
</style>
