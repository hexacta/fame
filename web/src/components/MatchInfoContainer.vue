<template>
  <div class="container">
    <match-loader v-if="loading" :match="match"></match-loader>
    <match-info v-else :info="info"></match-info>
  </div>
</template>

<script>

import MatchLoader from "@/components/MatchLoader";
import MatchInfo from "@/components/MatchInfo";

function getUrl(leagueId, match) {
  console.log(match);
  const homeQuery = match && match.home && `home=${match.home}`;
  const awayQuery = match && match.away && `away=${match.away}`;
  return `api/${leagueId}/match?${homeQuery}&${awayQuery}`;
}

export default {
  name: 'match-info-container',
  props: ['match', 'leagueId'],
  components: {
    MatchLoader,
    MatchInfo
  },
  data() {
    return {
      loading: true,
      url: getUrl(this.leagueId, this.match),
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
      fetch(this.url)
        .then(response => response.json())
        .then(json => {
          this.info = json;
          this.loading = false;
        });
    }
  }
};
</script>

<style scoped>

</style>
