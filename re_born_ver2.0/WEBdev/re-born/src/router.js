import Vue from "vue";
import Router from "vue-router";
import Main from "./views/Main.vue";
import LocalSelect from "./views/LocalSelect.vue";
import Local from "./views/Local.vue";
import Info from "./views/Info.vue";
Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "main",
      component: Main
    },
    {
      path: "/localSelect",
      name: "localSelect",
      component: LocalSelect
    },
    {
      path: "/local",
      name: "local",
      component: Local
    },
    {
      path: "/info",
      name: "info",
      component: Info
    }
  ]
});
