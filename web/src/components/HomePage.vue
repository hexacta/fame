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

export default {
  name: 'home',
  components: {
    LeaguePicker
  },
  data() {
    return {
      selectedLeague: null,
      leagues
    };
  },
  methods: {
    pick(league, event) {
      this.selectedLeague = league;
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
