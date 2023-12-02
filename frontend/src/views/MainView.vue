<script>
import utils from "@/utils"

import Content from "@/components/Content.vue"
import Pagination from "@/components/Pagination.vue"
import WithLoading from "@/components/WithLoading.vue"
import QuestionnaireCard from "@/components/main/QuestionnaireCard.vue"

export default {
  name: "MainView",
  components: {
    Content,
    Pagination,
    WithLoading,
    QuestionnaireCard,
  },
  props: {
    page: {
      type: Number,
      default: 1,
      required: true,
    },
  },
  data() {
    return {
      utils: utils,
      isLoading: true,

      isOnlyBlank: false,
      questionnaires: [],
    }
  },
  mounted() {
    this.load()
  },
  computed: {
    isSuccess() {
      return (
          !this.isLoading
          && this.questionnaires.length > 0
      )
    },
  },
  watch: {
    isOnlyBlank(newVal, oldVal) {
      if (newVal === oldVal) {
        return
      }
      this.load()
    },
  },
  methods: {
    load() {
      this.isLoading = true
      setTimeout(
          () => {
            this.questionnaires = this.loadQuestionnaires().map((q) => {
              return {
                token: q.token,
                title: q.title,
                description: utils.crop(q.description, 250, "..."),
                isCompleted: q.isCompleted || false,
                questionCount: q.questionCount || 0,
              }
            })
            this.isLoading = false
          },
          1
      )
    },
    loadQuestionnaires() {
      const allQuestionnaires = [
        {
          token: "01234567",
          title: "First questionnaire",
          description: (
              "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do" +
              " eiusmod tempor incididunt ut labore et dolore magna aliqua."
          ),
          isCompleted: false,
          questionCount: 10,
        },
        {
          token: "12345678",
          title: "Second questionnaire",
          description: (
              "Sed ut perspiciatis unde omnis iste natus error sit voluptatem" +
              " accusantium doloremque laudantium, totam rem aperiam, eaque" +
              " ipsa quae ab illo inventore veritatis et quasi architecto" +
              " beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem" +
              " quia voluptas sit aspernatur aut odit aut fugit, sed quia" +
              " consequuntur magni dolores eos qui ratione voluptatem sequi" +
              " nesciunt."
          ),
          isCompleted: true,
          questionCount: 5,
        },
        {
          token: "23456789",
          title: "Third questionnaire",
          description: (
              "Vivamus risus lorem, feugiat vitae erat vitae, vehicula" +
              " convallis nulla. Praesent iaculis ultricies mauris vel auctor."
          ),
          isCompleted: false,
          questionCount: 7,
        },
        {
          token: "3456789a",
          title: "Fourth questionnaire",
          description: (
              "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
          ),
          isCompleted: false,
          questionCount: 3,
        },
        {
          token: "456789ab",
          title: "Fifth questionnaire",
          description: (
              "At vero eos et accusamus et iusto odio dignissimos ducimus" +
              " qui blanditiis praesentium voluptatum deleniti atque corrupti" +
              " quos dolores et quas molestias excepturi sint occaecati" +
              " cupiditate non provident, similique sunt in culpa qui officia" +
              " deserunt mollitia animi, id est laborum et dolorum fuga."
          ),
          isCompleted: true,
          questionCount: 15,
        },
        {
          token: "56789abc",
          title: "Sixth questionnaire",
          description: (
              "Aenean euismod luctus tellus, eget interdum mauris tempus" +
              " egestas. Donec fermentum, tellus et feugiat mollis, mi magna" +
              " lacinia ipsum, ac euismod justo sem sit amet risus."
          ),
          isCompleted: true,
          questionCount: 10,
        },
        {
          token: "6789abcd",
          title: "Seventh questionnaire",
          description: (
              "Donec hendrerit velit id magna blandit, at vulputate massa" +
              " sagittis. Donec metus libero, finibus et porta id, vulputate" +
              " a felis. Praesent nec semper erat."
          ),
          isCompleted: false,
          questionCount: 5,
        },
      ]
      return this.isOnlyBlank
          ? allQuestionnaires.filter((q) => !q.isCompleted)
          : allQuestionnaires
    },
  },
}
</script>

<template>
  <Content>
    <div class="main-head">
      <div class="main-pagination">
        <Pagination :lastPage="20" :currentPage="page" />
      </div>
      <div class="only-blank-check">
        <input
            v-model="isOnlyBlank"
            type="checkbox"
        >
        <label>Only blank</label>
      </div>
    </div>
    <WithLoading
      :isLoading="isLoading"
      :isError="!isSuccess"
      errorText="Failed to download the questionnaires"
    >
      <div class="cards-block">
        <QuestionnaireCard
            v-for="questionnaire in questionnaires"
            :key="questionnaire.token"
            :questionnaire="questionnaire"
        />
      </div>
    </WithLoading>
  </Content>
</template>


<style lang="scss">
.main-head {
  display: flex;
}
.main-pagination {
  margin: 0 auto 1.5rem 0;
  width: fit-content;
}
.only-blank-check {
  padding: 0.6rem 0 0 0;

  input {
    width: 1.5rem;
    height: 1.5rem;
  }
  label {
    margin: 0 0.7rem 0 0.3rem;
    font-size: 1.1rem;
  }
}

.cards-block {
}
</style>
