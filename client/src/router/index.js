import Vue from 'vue'
import Router from 'vue-router'
import Crosspost from '@/components/Crosspost'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Crosspost',
      component: Crosspost
    }
  ]
})
