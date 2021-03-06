import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

var routes = []

routes.push({
  path: `/`,
  name: 'App',
  component: () => import(`../App`),
  redirect: '/intermediate'
})

export default new Router({
  routes })
