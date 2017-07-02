<template>
  <div class="container">
    <match-loader v-if="loading" :match="match"></match-loader>
    <match-info v-else :info="info"></match-info>
  </div>
</template>

<script>

import MatchLoader from "@/components/MatchLoader";
import MatchInfo from "@/components/MatchInfo";

function getUrl(match) {
  return `?home=${match.home}&away=${match.away}`;
}

export default {
  name: 'match-info-container',
  props: ['match'],
  components: {
    MatchLoader,
    MatchInfo
  },
  data() {
    return {
      loading: true,
      url: getUrl(this.match),
      info: null
    };
  },
  mounted() {
    this.reload();
  },
  beforeUpdate() {
    const newUrl = getUrl(this.match);
    if (newUrl !== this.url) {
      this.url = newUrl;
      this.reload();
    }
  },
  methods: {
    reload() {
      this.loading = true;
      setTimeout(() => {
        this.info = {
          home: 0.6,
          draw: 0.1,
          away: 0.3
        };
        this.loading = false;
      }, 1500);
    }
  }
};
</script>

<style scoped>

</style>
