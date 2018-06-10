// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueAuthenticate from 'vue-authenticate'

Vue.config.productionTip = false

Vue.use(VueMaterial)
Vue.use(VueAxios, axios)
Vue.use(VueAuthenticate, {
  baseUrl: 'https://6d2ca2a8.ngrok.io',
  providers: {
    facebook: {
      clientId: '177796502930980',
      redirectUri: 'https://81dff45d.ngrok.io/auth/callback',
      responseType: 'token',
      scope: ['user_likes', 'user_birthday', 'user_events']
    }
  }
})
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>'
})
