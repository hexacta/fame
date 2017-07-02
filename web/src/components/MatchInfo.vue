<template>
  <div>
    <p>Home: {{info.home}}</p>
    <p>Draw: {{info.draw}}</p>
    <p>Away: {{info.away}}</p>
  </div>
</template>

<script>

export default {
  name: 'match-info',
  props: ['info']
};
</script>

<style scoped>

</style>
