<script>
export default {
  name: "TextField",
  props: {
    modelValue: {
      type: String,
      default: "",
    },
    question: {
      type: Object,
      default: () => {
        return {
          order: 0,
          is_required: false,
          structure: {
            maxLength: null,
            minLength: null,
          },
        }
      },
      required: true,
    },
  },
  data() {
    return {
      value: this.$props.modelValue,
    }
  },
  computed: {
    isDone() {
      return (
          !this.$props.question.is_required
          || !!this.value
      )
    },
  },
}
</script>


<template>
  <textarea
      v-model="value"
      :name="'question_' + question.order"
      class="field"
  />
</template>


<style scoped lang="scss">
.field {
  width: 100%;
  min-height: 3rem;
  resize: vertical;
}
</style>
