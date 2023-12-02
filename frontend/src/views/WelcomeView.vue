<script>
export default {
  name: "WelcomeView",
}
</script>

<template>
  <div class="home-block">
    <div class="background-image">
      <img src="~@/assets/mainphoto.webp" alt="">
    </div>
    <div class="welcome-text">
      <h2>Welcome here!</h2>
      <p>
        This app is focused on questionnaires on all sorts of topics that you
        can fill out absolutely anonymously.
      </p>
      <a href="/login" class="letsgo-link">Login</a>
    </div>
</div>
</template>

<style scoped lang="scss">
@import "public/styles";

.home-block {
}

.background-image {
  overflow:hidden;
  position: fixed;
  z-index: -1;
  width: 100%;
  height: 100%;

  img {
    background-color: #3e241f;

    width: 100%;
    height: 100%;
    object-fit: cover;

    filter: blur(10px) brightness(0.4);
    transform: scale(1.05);
  }
}

.welcome-text {
  max-width: 70%;
  margin: auto;
  padding-top: 20vh;

  color: $white;
  text-align: center;
  font-size: 2rem;
}

.letsgo-link {
  color: $white;
  &:hover {
    color: $gray;
  }
}
</style>
