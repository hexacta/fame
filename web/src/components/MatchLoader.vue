<template>
  <div>
    Calculating {{match.home}} vs {{match.away}}...
  </div>
</template>

<script>
export default {
  name: 'match-loader',
  props: ['match'],
};
</script>

<style scoped>

</style>
