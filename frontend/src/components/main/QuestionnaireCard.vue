<script>
export default {
  name: "QuestionnaireCard",
  props: {
    questionnaire: {
      type: Object,
      default: () => {
        return {
          token: "",
          title: "",
          description: "",
          isCompleted: false,
          questionCount: 0,
        }
      },
      required: true,
    },
  },
}
</script>


<template>
  <div class="card-block">
    <div class="card-title">
      <h3>{{ questionnaire.title }}</h3>
      <label v-if="questionnaire.isCompleted">Completed!</label>
      <a
          :href="'/form/' + questionnaire.token"
          class="button-view"
          :class="!questionnaire.isCompleted ? 'goto-form-button' : ''"
      >
        {{ questionnaire.isCompleted ? "View answers" : "Fill in" }}
      </a>
    </div>
    <p class="question-count-title">{{ questionnaire.questionCount }} questions</p>
    <p>{{ questionnaire.description }}</p>
  </div>
</template>


<style scoped lang="scss">
@import "public/styles";

.card-block {
  @extend .with-border;

  padding: 0.7rem 1rem 0.7rem 1rem;
  margin-bottom: 0.5rem;
}

.card-title {
  display: flex;

  h3 {
    margin: 0.4rem 0 0 0.6rem;
    font-size: 1.2rem;
  }
  label {
    color: $dark-blue;
    margin: 0.7rem 0 0 1rem;
    font-size: 0.7rem;
  }
  a {
    margin: 0 0 0.2rem auto;
    padding: 0.6rem 1.4rem 0.5rem 1.4rem;
    border-radius: 1.5rem;

    display: block;
    width: fit-content;
    height: fit-content;

    text-decoration: none;
    &.goto-form-button {
      text-decoration: underline;
    }
  }
}

.question-count-title {
  text-decoration: underline;
  margin: 0 0 0 0.2rem;
}
</style>
