<template>
  <div>
    <div class="title">
      <h1>Football</h1>
      <h1>Association</h1>
      <h1>Match</h1>
      <h1>Estimator</h1>
    </div>
    <league-picker :leagues="leagues" v-on:pick="pick" class="picker"></league-picker>
  </div>
</template>

<script>
import LeaguePicker from '@/components/LeaguePicker';
import leagues from '@/data/leagues';
import Velocity from "velocity-animate";

function animateLeagueLogoPicked(leaguePicked) {
  const selectedLeagueImage = leaguePicked;
  const cloneImageForAnimation = leaguePicked.cloneNode(true);
  const body = document.querySelector('body');

  cloneImageForAnimation.style.top = `${leaguePicked.y}px`;
  cloneImageForAnimation.style.left = `${leaguePicked.x}px`;
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
  name: 'home',
  components: {
    LeaguePicker
  },
  data() {
    return {
      selectedLeague: null,
      cloneImageForAnimation: null,
      leagues
    };
  },
  methods: {
    pick(league, event) {
      this.selectedLeague = league;
      animateLeagueLogoPicked(event.target);

      this.$router.push({ name: 'League', params: { slug: league.slug } });
    }
  },
};
</script>

<style scoped>
.title {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.title>* {
  margin: 1px;
  width: 180px;
}

.picker {
  text-align: center;
}

</style>
