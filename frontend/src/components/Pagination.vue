<script>
import utils from "@/utils"

export default {
  name: "Pagination",
  props: {
    lastPage: {
      type: Number,
      default: 1,
      required: true,
    },
    currentPage: {
      type: Number,
      default: 1,
    },
  },
  data() {
    return {
      utils: utils,
    }
  },
  computed: {
    prevPage() {
      return utils.max(this.$props.currentPage - 1, 1)
    },
    nextPage() {
      return utils.min(this.$props.currentPage + 1, this.$props.lastPage)
    },
    startInterval() {
      if (this.$props.lastPage <= 5) {
        // | 1 (2) 3 4 |
        return utils.arrayRange(1, this.$props.lastPage + 1)
      }
      if (this.$props.currentPage < 2) {
        // | (1) 2 ...
        return [1, 2]
      }
      if (this.$props.currentPage <= 5) {
        // | 1 2 (3) 4...
        return utils.arrayRange(1, this.$props.currentPage + 2)
      }

      // | 1 2 ...
      return [1, 2]
    },
    currentInterval() {
      if (this.$props.currentPage <= 5) {
        // | 1 2 (3) 4 ...
        return null
      }
      if (this.$props.currentPage >= (this.lastPage - 4)) {
        // ... 8 (9) 10 11 |
        return null
      }

      // ... 5 (6) 7 ...
      return utils.arrayRange(this.$props.currentPage - 1, this.$props.currentPage + 2)
    },
    endInterval() {
      if (this.$props.lastPage <= 5) {
        // | 1 (2) 3 4 |
        return null
      }
      if (this.$props.currentPage > (this.lastPage - 1)) {
        // ... 9 (10) |
        return utils.arrayRange(this.$props.lastPage - 1, this.$props.lastPage + 1)
      }
      if (this.$props.currentPage >= (this.lastPage - 4)) {
        // ... 8 (9) 10 |
        return utils.arrayRange(this.$props.currentPage - 1, this.$props.lastPage + 1)
      }

        // ... 8 9 10 |
        return utils.arrayRange(this.$props.lastPage - 1, this.$props.lastPage + 1)
    },
  },
}
</script>


<template>
  <div class="pagination-block">
    <a
        v-if="currentPage !== 1"
        :href="`/?page=${prevPage}`"
        class="prominent-el"
        title="prev"
    >
      &lt;
    </a>

    <a
        v-for="num in startInterval"
        :key="num"
        :href="`/?page=${num}`"
        :class="num === currentPage ? 'prominent-el disabled-el' : ''"
    >
      {{ num }}
    </a>

    <template v-if="currentInterval">
      <label>..</label>
      <a
          v-for="num in currentInterval"
          :key="num"
          :href="`/?page=${num}`"
          :class="num === currentPage ? 'prominent-el disabled-el' : ''"
      >
        {{ num }}
      </a>
    </template>

    <template v-if="endInterval">
      <label>..</label>
      <a
          v-for="num in endInterval"
          :key="num"
          :href="`/?page=${num}`"
          :class="num === currentPage ? 'prominent-el disabled-el' : ''"
      >
        {{ num }}
      </a>
    </template>

    <a
        v-if="currentPage !== lastPage"
        :href="`/?page=${nextPage}`"
        class="prominent-el"
        title="next"
    >
      &gt;
    </a>
  </div>
</template>


<style scoped lang="scss">
@import "public/styles";

.pagination-block {
  display: flex;
  text-align: center;

  label {
    font-size: 2rem;
    margin: auto 0.2rem 0 0.2rem;
  }
  a {
    text-decoration: none;
    color: $black;
    font-size: 1.2rem;

    min-width: 2rem;
    padding: 0.5rem 0.2rem 0.2rem 0.2rem;
    margin: 0 0.1rem 0 0.1rem;

    @extend .with-border;
    border-radius: 0.3rem;
  }

  .prominent-el {
    color: $white;
    background-color: $dark-blue;
  }
}
</style>
