<template>
	<transition 
  	appear
  	v-on:appear="enter"
    v-bind:css="false"
  >
		<league-logo class="pointer" v-on:translate="translate" :league="league" ></league-logo>
	</transition>
</template>

<script>
import Velocity from "velocity-animate"
import LeagueLogo from '@/components/LeagueLogo';

function animateItemPicked(item) {
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
      top: document.querySelector('main').offsetTop, 
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
    translate(item) {
    	animateItemPicked(item);
    }
  },

};
</script>

<style scoped>

.pointer {
	cursor: pointer;
}

</style>
