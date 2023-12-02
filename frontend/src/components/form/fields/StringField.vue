<script>
export default {
  name: "StringField",
  props: {
    question: {
      type: Object,
      default: () => {
        return {
          order: 0,
          is_required: false,
          structure: {
            maxLength: null,
          },
        }
      },
      required: true,
    },
  },
  data() {
    return {
      value: "",
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
  <input
    type="text"
    :name="'question_' + question.order"
    class="field"
 />
</template>

<style scoped lang="scss">
.field {
  width: 100%;
  height: 1.5rem;
}
</style>
