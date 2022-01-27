import Vue from 'vue';
import App from './App.vue';
import axios from './plugins/axios';

Vue.use(axios);
Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
  created() {
    console.log(this.$axios ? 'axios plugin works' : 'axios plugin does not work');
  }
}).$mount('#app')
