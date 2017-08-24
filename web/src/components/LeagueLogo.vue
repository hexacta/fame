<template>
  <img :src="leagueLogo" v-on:click="translate($event)" :alt="league.name" :title="league.name" />
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
  	translate(event) {
  		this.$emit('translate', event.target);
  	}
  }
};
</script>

<style scoped>
</style>
