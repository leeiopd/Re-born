import Vue from "vue";
import Router from "vue-router";
import Main from "./views/Main.vue";
import LocalSelect from "./views/LocalSelect.vue";
import Local from "./views/Local.vue";
import MoreInfo from "./views/MoreInfo.vue";
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
      path: "/moreInfo",
      name: "moreInfo",
      component: MoreInfo
    }
  ]
});
