<template>
  <div>
    <match-form :league="league" :match="match" v-on:submit="loadMatch">
    </match-form>
    <match-info-container v-if="match" :match="match"></match-info-container>
  </div>
</template>

<script>
import MatchForm from '@/components/MatchForm';
import MatchInfoContainer from '@/components/MatchInfoContainer';
import leagues from '@/data/leagues';

export default {
  name: 'league-page',
  components: { MatchForm, MatchInfoContainer },
  props: ['name', 'home', 'away'],
  data() {
    return {
      league: leagues.find(league => league.name === this.name),
      match: (this.home || this.away) ? { home: this.home, away: this.away } : null,
    };
  },
  methods: {
    loadMatch(match) {
      this.$router.push({ name: 'League', params: { name: this.name }, query: match });
      this.match = match;
    },
  },
};
</script>

<style scoped>

</style>
