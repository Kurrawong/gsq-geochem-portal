import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/profiles',
      name: 'profiles',
      component: () => import('../views/ProfilesView.vue')
    },
    {
      path: '/vocabs',
      name: 'vocabs',
      component: () => import('../views/VocabsView.vue')
    },
    {
      path: '/system',
      name: 'system',
      component: () => import('../views/SystemView.vue')
    }
  ]
})

export default router
