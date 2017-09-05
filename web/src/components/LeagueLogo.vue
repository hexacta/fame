<template>
  <img :src="leagueLogo" v-on:click="leagueSelected($event)" :alt="league.name" :title="league.name" />
</template>

<script>
function getLogo(league) {
	return `/static/img/leaguesLogos/${league}.png`
}

export default {
  name: 'league-logo',
  props: ['league'],

  data() {
  	return {
  		leagueLogo: getLogo(this.league.slug)
  	}
  },

  methods: {
  	leagueSelected(event) {
  		this.$emit('leagueSelected', event.target);
  	}
  }
};
</script>

<style scoped>
</style>
