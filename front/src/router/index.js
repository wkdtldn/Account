// Composables
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    component: () => import("@/layouts/default/Default.vue"),
    children: [
      {
        path: "/login",
        name: "Login",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
          import(/* webpackChunkName: "home" */ "@/views/Login.vue"),
      },
      {
        path: "/siginin",
        name: "Siginin",
        component: () =>
          import(/* webpackChunkName: "home" */ "@/views/Siginin.vue"),
      },
      {
        path: "/main",
        name: "Main",
        component: () =>
          import(/* webpackChunkName: "home" */ "@/views/Main.vue"),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
