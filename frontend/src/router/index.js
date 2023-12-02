import { createRouter, createWebHistory } from "vue-router"
import MainView from "@/views/MainView.vue"


let parseNumber = (param) => Number.parseInt(param, 10) || undefined
let parseToken = (param) => param.match(/^[a-zA-Z\d]+$/)[0] || undefined


const routes = [
  {
    path: "/",
    name: "main",
    component: MainView,
    meta: { isAuth: true },
    props: (route) => {
      return { ...route.params, page: parseNumber(route.query.page) || 1}
    },
  },
  {
    path: "/welcome",
    component: () => import("../views/WelcomeView.vue"),
    meta: { isAuth: false },
  },
  {
    path: "/form/:token",
    name: "form",
    component: () => import("../views/FormView.vue"),
    meta: { isAuth: true },
    props: (route) => {
      return {
        ...route.params,
        token: parseToken(route.params.token),
      }
    },
  },
  {
    path: "/admin",
    name: "admin",
    component: () => import("../views/AdminView.vue"),
    meta: { isAdmin: true },
    children: [
      {
        path: "/results:token:page",
        name: "results",
        component: () => import("../views/ResultsView.vue"),
        props: (route) => {
          return {
            ...route.params,
            token: parseToken(route.params.token),
            page: parseNumber(route.params.page),
          }
        },
      },
      {
        path: "/statistic:token",
        name: "statistic",
        component: () => import("../views/StatisticView.vue"),
        props: (route) => {
          return {
            ...route.params,
            token: parseToken(route.params.token),
          }
        },
      },
      {
        path: "/form:token",
        name: "form_admin",
        component: () => import("../views/FormAdminView.vue"),
        props: (route) => {
          return {
            ...route.params,
            token: parseToken(route.params.token),
          }
        },
      },
    ],
  },
  {
    path: "/login",
    name: "login",
    component: () => import("../views/LoginView.vue"),
    meta: { isAuth: false },
  },
  {
    path: "/about",
    name: "about",
    component: () => import("../views/AboutView.vue"),
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
