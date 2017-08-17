<template>
  	<transition 
	  	appear
	  	v-on:appear="enter"
	    v-bind:css="false"
    >
  		<img :src="leagueLogo" :alt="league.name" :title="league.name" />
  	</transition>
</template>

<script>
import Velocity from "velocity-animate"

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
  },

  methods: {
    enter(el) {
      Velocity(el, { opacity: [1,0] }, { duration: 300 })
    }
  }
};
</script>

<style scoped>
	img {
		cursor: pointer;
	}
</style>
