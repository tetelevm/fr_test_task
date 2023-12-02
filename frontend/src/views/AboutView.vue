<script>
import Content from "@/components/Content.vue";

export default {
  name: "AboutView",
  components: {Content},
  data() {
    return {
      isAnonymous: true,
    }
  },
}
</script>


<template>
  <Content>
    <div class="about">
      <h1>A little about the service</h1>
      <p>
        We are a service with questionnaires. Questionnaires here can be
        different on different topics, for example, about your preferences in
        clothes or eating habits.
      </p>
      <p>
        You can take any questionnaire if it's not closed or expired, and see
        your answers to previous questions.
      </p>
      <p>
        To do this, you need to
        <template v-if="isAnonymous"><a href="/login">log in</a> and </template>
        go to the main page.
      </p>
      <p>
        You can always see the questionnaires you have completed on your answers
        page, they are saved by the token you used to log in.
      </p>
    </div>
  </Content>
</template>


<style lang="scss">
.main-content {
  padding-top: 2rem;
}

.about {
  h1 {
    text-align: center;
    font-size: 2.3rem;
  }
  p {
    font-size: 1.4rem;
  }
}
</style>
