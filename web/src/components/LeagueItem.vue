<template>
	<transition 
  	appear
  	v-on:appear="enter"
    v-bind:css="false"
  >
		<league-logo class="pointer" v-on:leagueSelected="animate" :league="league" ></league-logo>
	</transition>
</template>

<script>
import Velocity from "velocity-animate"
import LeagueLogo from '@/components/LeagueLogo';

/**
* In order to get always the correct position the league-logo component must always be the 
* first element in LeaguePage.vue to match the offsetTop of then 'main' element
**/

function calculateTop() {
  return document.querySelector('main').offsetTop;
}

function animateLeagueSelected(item) {
  const selectedLeagueImage = item;
  const cloneImageForAnimation = item.cloneNode(true);
  const body = document.querySelector('body');

  cloneImageForAnimation.style.top = `${item.y}px`;
  cloneImageForAnimation.style.left = `${item.x}px`;
  cloneImageForAnimation.style.position = 'absolute';
  selectedLeagueImage.style.visibility = 'hidden';
  body.appendChild(cloneImageForAnimation);
  
  Velocity.animate(
    cloneImageForAnimation, {
      transition: '0.85s ease-in-out;', 
      top: calculateTop(), 
      left: '50%', 
      marginLeft: `-${cloneImageForAnimation.width/2}px` 
    }
  ).then(() => {
    setTimeout(() => {
      body.removeChild(cloneImageForAnimation);
    },350);
  });
}

export default {
  name: 'league-item',
  props: ['league'],
  components: {
    LeagueLogo
  },

  methods: {
    enter(el) {
      Velocity(el, { opacity: [1,0] }, { duration: 300 })
    },
    animate(item) {
    	animateLeagueSelected(item);
    }
  },

};
</script>

<style scoped>

.pointer {
	cursor: pointer;
}

</style>
