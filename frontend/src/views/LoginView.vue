<script>
import Content from "@/components/Content.vue"
import GetTokenForm from "@/components/login/GetTokenForm.vue"

export default {
  name: "LoginView",
  components: {
    Content,
    GetTokenForm,
  },
  data() {
    return {
      token: "",
      isNewUser: true,
    }
  },
  methods: {
    setToken(newVal) {
      this.token = newVal
      this.isNewUser = false
    },
    resetToken() {
      this.token = ""
      this.isNewUser = true
    },
    checkToken() {
    },
  },
}
</script>


<template>
  <Content>
    <div class="token-form">
      <div v-if="isNewUser">
        <GetTokenForm @input="setToken"/>
      </div>
      <div v-else>
        <div class="entry-block">
          <h4>Enter your token:</h4>
          <div class="token-input">
            <input
                id="userToken"
                name="userToken"
                :value="token"
                type="text"
                required
                autofocus
            />
            <button @click="checkToken" class="button-view">Ok</button>
          </div>
        </div>
        <p
            class="gettoken-text"
            @click="resetToken"
        >
          I don't have a token
        </p>
      </div>
    </div>
  </Content>
</template>


<style lang="scss">
@import "public/styles";

.main-content {
  padding-top: 4rem;
}

.token-form {
  @extend .with-border;
  padding: 1.5rem 2rem 1rem 2rem;
  margin-top: 4rem;
}

.entry-block {
  h4 {
    font-size: 1.5rem;
    margin: 0 0 0.5rem 0.5rem;
  }
}

.token-input {
  @extend .with-border;
  border-radius: 1.5rem;
  width: fit-content;

  input {
    height: 2rem;
    width: 15rem;
    border: 0;
    padding: 0 1rem 0 1rem;
    border-radius: 1rem 0 0 1rem;
    font-size: 1.5rem;
    &:focus {
      outline: none;
    }
  }
  button {
    height: 2.5rem;
    width: 6rem;
    font-size: 1.3rem;
    border-radius: 0 1rem 1rem 0;
  }

}

.gettoken-text {
  margin: 1rem 0 0 0.5rem;

  text-decoration: underline;
  font-weight: bold;
  color: $light-blue;
  cursor: pointer;
}
</style>
