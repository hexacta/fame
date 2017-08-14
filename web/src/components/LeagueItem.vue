<template>
  <div>
    <img :src="leagueLogo" />
    <br />
  	<span>{{league.name}}</span>
  </div>
  
</template>

<script>

function getLogo(league) {
	return `/static/img/leaguesLogos/${league}.png`
}

export default {
  name: 'league-item',
  props: ['league'],

  data() {
  	return {
  		leagueLogo: getLogo(this.league.slug)
  	}
  }
};
</script>

<style scoped>
</style>
