// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import axios from 'axios'
import router from '@/router/index'
import store from '@/Vuex/index'
import $ from 'jquery'
import App from '@/App'
import Component from 'vue-class-component'
import VuePreview from 'vue-preview'
import echarts from 'echarts'


Vue.use(VuePreview);

// Register the router hooks with their names
Component.registerHooks([
  'beforeRouteEnter',
  'beforeRouteLeave',
  'beforeRouteUpdate' // for vue-router 2.2+
])
Vue.config.productionTip = false
Vue.prototype.$axios = axios
Vue.prototype.$echarts = echarts

var app = new Vue({
	el: "#app",
	router,
	store,
	components: { App },
	template: '<App/>'
})
