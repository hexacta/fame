<template>
	<transition 
  	appear
  	v-on:appear="enter"
    v-bind:css="false"
  >
		<league-logo class="pointer" :league="league"></league-logo>
	</transition>
</template>

<script>
import Velocity from "velocity-animate"
import LeagueLogo from '@/components/LeagueLogo';

export default {
  name: 'league-item',
  props: ['league'],
  components: {
    LeagueLogo
  },

  methods: {
    enter(el) {
      Velocity(el, { opacity: [1,0] }, { duration: 300 })
    }
  }
};
</script>

<style scoped>

.pointer {
	cursor: pointer;
}

</style>
