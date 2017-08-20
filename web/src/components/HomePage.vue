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
      this.selectedLeagueImage = event.target;
      this.cloneImageForAnimation = event.target.cloneNode(true);
      this.cloneImageForAnimation.style.top = `${event.target.y}px`;
      this.cloneImageForAnimation.style.left = `${event.target.x}px`;
      this.cloneImageForAnimation.style.position = 'absolute';
      this.body = document.querySelector('body');
      this.selectedLeagueImage.style.visibility = 'hidden';
      this.body.appendChild(this.cloneImageForAnimation);
      
      this.$router.push({ name: 'League', params: { slug: league.slug } });

      Velocity.animate(
        this.cloneImageForAnimation, {
          transition: '0.85s ease-in-out;', 
          top: document.querySelector('main').offsetTop, 
          left: '50%', 
          marginLeft: `-${this.cloneImageForAnimation.width/2}px` 
        }
      ).then(() => {
        setTimeout(() => {
          this.body.removeChild(this.cloneImageForAnimation);
        },350);
      });
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
