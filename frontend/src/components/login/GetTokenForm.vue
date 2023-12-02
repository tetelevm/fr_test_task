<script>
export default {
  name: "GetTokenForm",
  data() {
    return {
      token: "",
      labelText: "",
    }
  },
  computed: {
    isShowToken() {
      return !!this.token
    },
  },
  methods: {
    getToken() {
      this.token = "1234qwer0p"
      this.labelText = "Click on the token to copy"
    },
    copyToken() {
      navigator.clipboard.writeText(this.token)
      this.labelText = "Copied!"
    },
    goBack() {
      this.$emit("input", this.token)
    }
  },
}
</script>


<template>
  <div class="gettoken-block">
      <p>
        Click the button and your token will be displayed below.
        <br />
        It is important to save it so that you can log in again later!
      </p>
      <button
          v-if="!isShowToken"
          class="button-view"
          @click="getToken"
      >
        Get token
      </button>
      <button
          v-else
          class="button-view"
          @click="goBack"
      >
        Back
      </button>
      <div v-if="isShowToken">
        <h3>Your token:</h3>
        <p>{{ labelText }}</p>
        <h4 @click="copyToken">{{ token }}</h4>
      </div>
    </div>
</template>


<style scoped lang="scss">
.gettoken-block {
  p {
    margin: 0 0 0.5rem 0;
    font-size: 1.3rem;
  }

  button {
    width: 15rem;
    height: 3rem;
    font-size: 1.5rem;
    border-radius: 1.5rem;
  }

  h3 {
    font-size: 2rem;
    margin-bottom: 0;
  }
  p {
    font-size: 1rem;
    margin-bottom: 1.5rem;
  }
  h4 {
    font-size: 1.5rem;
    margin: 0 0 0.5rem 0;
    text-decoration: underline;
  }
}
</style>
