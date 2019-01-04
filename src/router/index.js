import Vue from 'vue'
import Router from 'vue-router'
import Signin from '@/components/Signin'
import Hello from '@/components/Hello'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Hello,
    },
    {
      path: '/signin',
      name: 'Signin',
      component: Signin,
    },
  ],
})
