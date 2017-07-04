<template>
  <div class="container">
    <div class="form">
      <label>
        <span>Home:</span>
        <select v-model="home">
          <option v-for="team in teams" :key="team">{{team}}</option>
        </select>
      </label>
      <label>
        <span>Away:</span>
        <select v-model="away">
          <option v-for="team in teams" :key="team">{{team}}</option>
        </select>
      </label>
      <button v-on:click="submit">Estimate</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'match-form',
  props: ['league', 'match'],
  data() {
    return {
      home: this.match && this.match.home,
      away: this.match && this.match.away,
      teams: this.league.teams.slice().sort(),
    };
  },
  methods: {
    submit() {
      const { home, away } = this;
      this.$emit('submit', { home, away });
    },
  },
};
</script>

<style scoped>
.form {
  display: flex;
  align-items: center;
  flex-direction: column;
}

.form>* {
  width: 200px;
  margin: 3px;
}

label {
  display: flex;
}

label span {
  text-align: right;
  width: 25%;
  padding-right: 2px;
}

label select {
  flex: 1;
  max-width: 75%;
}
</style>
