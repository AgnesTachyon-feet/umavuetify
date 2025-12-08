// vue router
import { createRouter, createWebHistory } from "vue-router";

import login from "../views/login/Login.vue";

const routes = [
  {
    path: "/",
    redireact: "/login",
    meta: { public: true},
  },
  {
    path: "/login",
    component: login,
    meta: { public: true }
  },
];

const router = createRouter({
  history: createWebHistory('/umavue/'),
  routes,
});

export default router;