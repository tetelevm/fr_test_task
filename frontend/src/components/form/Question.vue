<script>
import _ from "lodash"

import TextFiled from "./fields/TextField.vue"
import StringFiled from "./fields/StringField.vue"
import SingleFiled from "./fields/SingleField.vue"
import MultiFiled from "./fields/MultiField.vue"

export default {
  name: "Question",
  props: {
    modelValue: {
      type: Object,
      default: () => {
        return {
          questionNum: null,
          value: null,
          isDone: false,
        }
      },
      required: true,
    },
    question: {
      type: Object,
      default: () => {
        return {
          type: null,
          title: "",
          order: 0,
          description: "",
          is_required: false,
          structure: {},
        }
      },
      required: true,
    },
  },
  components: {
    TextFiled,
    StringFiled,
    SingleFiled,
    MultiFiled,
  },
  data() {
    return {
    }
  },
  computed: {
    type() {
      return this.$props.question.type
    },
  },
}
</script>

<template>
  <div class="question-block">

    <div class="title-block">
      <h4>{{ question.title }}</h4>
      <label v-if="question.is_required">required</label>
    </div>

    <p>{{ question.description }}</p>

    <div class="answer-block">
      <TextFiled v-if="type === `text`" :question="question" />
      <StringFiled v-else-if="type === `string`" :question="question" />
      <SingleFiled v-else-if="type === `single`" :question="question" />
      <MultiFiled v-else-if="type === `multi`" :question="question" />
    </div>
  </div>
</template>


<style scoped lang="scss">
@import "public/styles";

.question-block {
  @extend .with-border;

  padding: 0.7rem 1rem 0.7rem 1rem;
  margin-bottom: 0.5rem;

  p {
    margin: 0.3rem 0 0.3rem 0;
  }
}

.title-block {
  display: flex;

  h4 {
    margin: 0.3rem 0 0.3rem 0;
    font-size: 1.1rem;
  }
  label {
    color: $light-gray;
    font-size: 0.8rem;
    margin-left: 0.5rem;
  }
}

.answer-block {
  display: flex;
}
</style>
