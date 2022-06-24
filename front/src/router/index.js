import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
//import T from '../views/T.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  }
  // },{
  //   path: '/test',
  //   name:'test',
  //   component: T
  // }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
