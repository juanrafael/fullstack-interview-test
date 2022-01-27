<template>
  <div id="app">
    <header class="border-bottom border-2">
      <div class="container">
        <h1 class="text-center py-3">MY GIT APPLICATION</h1>
      </div>
    </header>
    <main>
      <div class="container">
        <div id="menu" class="my-4">
          <ul class="nav nav-pills justify-content-center">
            <li class="nav-item">
              <a @click="changeView('Branch')" class="nav-link" :class="view=='Branch' ? 'active' : ''" href="#">Branches</a>
            </li>
            <li class="nav-item">
              <a @click="changeView('Commit')" class="nav-link" :class="view=='Commit' ? 'active' : ''" href="#">Commits</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" :class="view=='PullRequest' ? 'active' : ''" href="#">Link</a>
            </li>
          </ul>
        </div>
        <transition name="component-fade" mode="out-in">
          <component :is="view"></component>
        </transition>
      </div>
    </main>
  </div>
</template>

<script>
import Branch from './components/Branch.vue'
import Commit from './components/Commit.vue'

export default {
  name: 'App',
  components: {
    Branch,
    Commit,
  },
  data() {
    return {
      view: 'Branch',
    }
  },
  methods: {
    changeView(branch){
      this.view = branch
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.component-fade-enter-active, .component-fade-leave-active {
  transition: opacity .3s ease;
}
.component-fade-enter, .component-fade-leave-to
/* .component-fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
