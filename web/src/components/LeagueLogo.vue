<template>
  <img :src="leagueLogo" :alt="league.name" :title="league.name" />
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
};
</script>

<style scoped>
</style>
