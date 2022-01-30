<template>
  <div id="app">
    <header class="border-bottom border-2">
      <div class="container">
        <h1 class="fs-5 py-3 m-0">GIT APPLICATION</h1>
      </div>
    </header>
    <main class="mb-5">
      <div class="container">
        <div id="menu" class="border-bottom border-2 mb-3">
          <ul class="nav">
            <li class="nav-item">
              <a @click="changeView('Branch')" class="nav-link py-3" :class="view=='Branch' ? 'active' : ''" href="#">Branches</a>
            </li>
            <li class="nav-item">
              <a @click="changeView('Commit')" class="nav-link py-3" :class="view=='Commit' ? 'active' : ''" href="#">Commits</a>
            </li>
            <li class="nav-item">
              <a class="nav-link py-3" :class="view=='PullRequest' ? 'active' : ''" href="#">Pull request</a>
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
  color: #303030;
}

.nav .nav-link{
  color: #303030;
}

.nav .nav-link.active {
  box-shadow: inset 0 -2px 0 0 #6666c4;
  font-weight: 700;
}

.nav .nav-link:hover:not(.nav .nav-link.active) {
    box-shadow: inset 0 -2px 0 0 #bfbfbf;
}

.component-fade-enter-active, .component-fade-leave-active {
  transition: opacity .3s ease;
}
.component-fade-enter, .component-fade-leave-to
/* .component-fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
