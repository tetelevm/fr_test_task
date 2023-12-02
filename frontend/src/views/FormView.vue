<script>
import utils from "@/utils"

import Content from "@/components/Content.vue"
import WithLoading from "@/components/WithLoading.vue"
import Question from "@/components/form/Question.vue"

export default {
  name: "FormView",
  components: {
    Question,
    WithLoading,
    Content,
  },
  props: {
    token: {
      type: String,
      default: null,
      required: true,
    },
    asAnswer: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      utils: utils,
      isLoading: true,
      isAdmin: true,
      isDone: false,

      questionnaire: {
        token: null,
        title: null,
        description: null,
        date_start: null,
        date_end: null,
        created_by: "",
        is_protected: true,
        questions: [],
      },

      answers: [],
    }
  },
  mounted() {
    this.load()
  },
  computed: {
    isSuccess() {
      return (
          !this.isLoading
          && (this.token || this.questionnaire.token)
          && this.questionnaire
          && this.questionnaire.questions.length > 0
      )
    },
    canChange() {
      return (
          !this.$props.asAnswer
          && this.isAdmin
          && this.isSuccess
          && this.questionnaire.date_start > new Date()
          && (!this.questionnaire.is_protected || (this.questionnaire.created_by === this.user.name))
      )
    },
    formattedDescription() {
      return this.questionnaire.description
          ? this.questionnaire.description.split("\n")
          : []
    },
    questions() {
      return this.questionnaire.questions.sort((a, b) => a.order - b.order)
    },
  },
  watch: {
    token(newVal) {
      if (newVal) {
        this.load()
      }
    },
  },
  methods: {
    load() {
      setTimeout(
          () => {
            this.questionnaire = this.loadForData()
            this.answers = this.questionnaire.questions.map((q) => {
              return {
                questionNum: q.order,
                value: null,
                isDone: !q.is_required,
              }
            })
            this.isDone = this.answers.every((a) => a.isDone)
            this.isLoading = false
          },
          1
      )
    },
    loadForData() {
      return {
        token: "12345678",
        title: "Questionnaire",
        description: (
            "Long description. Well, not too long, but still a description" +
            " that describes the questionnaire, how and why you should answer" +
            " and all that.\n" +
            " Although there may not be one, you should also take that into" +
            " consideration."
        ),
        date_start: new Date("2023-11-10 12:53:46"),
        date_end: new Date("2023-11-10 12:53:46"),
        is_hidden: false,
        created_by: "admin",
        is_protected: true,
        questions: [
          {
            type: "text",
            title: "Text question",
            order: 0,
            description: "This question is required and must be answered in text",
            is_required: true,
            structure: {maxLength: 256, minLength: 12},
          },
          {
            type: "string",
            title: "Second text question",
            order: 1,
            description: "This question is optional and can be answered with a short string",
            is_required: false,
            structure: {maxLength: 50},
          },
          {
            type: "single",
            title: "Choice question",
            order: 2,
            description: "This is a single-choice question and may not be answered.",
            is_required: false,
            structure: {
              variants: [
                {order: 0, text: "Yes"},
                {order: 1, text: "No"},
                {order: 2, text: "Bang! I'm Batman!"},
              ],
            },
          },
          {
            type: "multi",
            title: "Multichoice question",
            order: 3,
            description: "This is a multiple-choice question and must be answered (choose at least one choice).",
            is_required: true,
            structure: {
              variants: [
                {order: 0, text: "The first option"},
                {order: 1, text: "Second option"},
                {order: 2, text: "Third option"},
              ],
            },
          },
        ],
      }
    },
    done() {

    },
  },
}
</script>

<template>
  <WithLoading
      :isLoading="isLoading"
      :isError="!isSuccess"
      errorText="No such questionnaire was found"
  >
    <Content>
      <div class="form-title">
        <h2>{{ questionnaire.title }}</h2>
        <button v-if="canChange" class="button-view">Change</button>
      </div>

      <div v-if="asAnswer" class="date-block">
        <p>
          You completed this questionnaire ont the <b>123</b>
        </p>
      </div>
      <div v-else-if="isAdmin" class="date-block">
        <p>
          Start date <b>{{ utils.formatDate(questionnaire.date_start) }}</b>
        </p>
        <p v-if="questionnaire.date_end">
          End date <b>{{ utils.formatDate(questionnaire.date_end) }}</b>
        </p>
      </div>

      <div class="description-block">
        <p
            v-for="(paragraph, index) in formattedDescription"
            :key="index"
        >
          {{ paragraph }}
        </p>
      </div>

      <div class="form-content">
        <Question
            v-for="question in questions"
            :key="question.order"
            v-model="answers[question.order]"
            :question="question"
        />
      </div>

      <div v-if="!asAnswer" class="form-done">
        <button
            :disabled="!isDone"
            class="button-view"
            @click="done"
        >
          Done
        </button>
      </div>
    </Content>
  </WithLoading>
</template>

<style lang="scss">
@import "public/styles";

.main-content {
  padding-top: 1rem;
}

.form-title {
  display: flex;
  justify-content: space-between;
  margin-left: 0.5rem;

  h2 {
    font-size: 1.7rem;
    margin: 1rem 0 0.5rem 0;
  }
  button {
      width: 6rem;
      height: 2rem;
      margin: auto 0 auto 0;

      border-radius: 1rem;
  }
}

.date-block {
  color: $gray;
  font-size: 0.9rem;
  margin-left: 0.5rem;
  p {
    margin: 0.5rem 0 0 0;
  }
  b {
    color: $light-gray;
    margin-left: 1rem;
  }
}

.description-block {
  margin: 1rem 0.5rem 0.5rem  0.5rem;
}

.form-content {
}

.form-done {
  margin: 1rem 0 2rem 0;

  button {
    width: 8rem;
    height: 3rem;
    border-radius: 2rem;
    font-size: 1.5rem;
  }
}
</style>
