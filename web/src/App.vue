<template>
  
    <div id="app">
      <header>
        <router-link to="/"><span >FAME</span></router-link>
      </header>
      <main>
        <transition name="fade" mode="out-in">
          <router-view></router-view>
        </transition>
      </main>
    </div>
  
</template>

<script>
export default {
  name: 'app',
};
</script>

<style>
body {
  margin: 0;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

main {
  /*text-align: center;*/
  margin-top: 40px;
}

header {
  margin: 0;
  height: 56px;
  padding: 0 16px 0 24px;
  background-color: #4fc08d;
  color: #ffffff;
}

header a {
  text-decoration: none;
  color: inherit;
}

header span {
  display: block;
  position: relative;
  font-size: 20px;
  line-height: 1;
  letter-spacing: .02em;
  font-weight: 400;
  box-sizing: border-box;
  padding-top: 16px;
}

.fade-leave-active {
  transition: opacity 0.5s ease;
  opacity: 0;
}

.fade-enter-active {
  transition: opacity 0.25s ease;
}
</style>
