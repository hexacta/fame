<template>
  <div>
    <img :src="leagueLogo" />
    <br />
    <match-form :league="league" :match="match" v-on:submit="loadMatch">
    </match-form>
    <match-info-container v-if="match" :match="match" :league-id="league.id"></match-info-container>
  </div>
</template>

<script>
import MatchForm from '@/components/MatchForm';
import MatchInfoContainer from '@/components/MatchInfoContainer';
import leagues from '@/data/leagues';

function getLogo(league) {
  return `/static/img/leaguesLogos/${league}.png`
}

export default {
  name: 'league-page',
  components: { MatchForm, MatchInfoContainer },
  props: ['slug', 'home', 'away'],
  data() {
    return {
      league: leagues.find(league => league.slug === this.slug),
      match: (this.home || this.away) ? { home: this.home, away: this.away } : null,
      leagueLogo: getLogo(this.slug)
    };
  },
  methods: {
    loadMatch(match) {
      this.$router.push({ name: 'League', params: { slug: this.slug }, query: match });
      this.match = match;
    },
  },
};
</script>

<style scoped>
div {
  display: flex;
  align-items: center;
  flex-direction: column;
}

</style>
