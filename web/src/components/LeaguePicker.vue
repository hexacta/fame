<template>
  <div>
    <ul>
      <li v-for="league in leagues" :key="league.name">
        <a v-on:click="pick(league, $event)">
          <league-item :league="league"></league-item>  
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
import LeagueItem from './LeagueItem';

export default {
  name: 'league-picker',
  components: {
    LeagueItem,
  },
  props: ['leagues'],
  data() {
    return {
      league: null,
    };
  },
  methods: {
    pick(league, event) {
      this.league = league;
      this.$emit('pick', league, event);
    },
  },
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
