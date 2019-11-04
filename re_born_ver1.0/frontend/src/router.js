import Vue from "vue";
import Router from "vue-router";
import firebase from "firebase";
import firebaseApp from "firebase/app";
import Sign from "./pages/sign/Sign.vue";
import Complaints from "./pages/complaints/Complaints.vue";
import Report from "./pages/complaints/Report.vue";
import Search from "./pages/complaints/components/Search.vue";
import mypage from "./pages/mypage/MyPage.vue";
import camera from "./pages/camera/main.vue";

import Menu from "./pages/menu/Menu.vue";
Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "Sign",
      component: Sign
    },
    {
      path: "/menu",
      name: "Menu",
      component: Menu
    },
    {
      path: "/complaints",
      name: "Complaints",
      component: Complaints
    },
    {
      path: "/report",
      name: "Report",
      component: Report
    },
    {
      path: "/mypage",
      name: "mypage",
      component: mypage
    },

    {
      path: "/camera",
      mane: "camera",
      component: camera
    }
  ]
});
