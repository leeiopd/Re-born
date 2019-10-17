import Vue from "vue";
import Vuex from "vuex";
import Vuetify from "vuetify/lib";
import "material-design-icons-iconfont/dist/material-design-icons.css"; // Ensure you are using css-loader
import "@fortawesome/fontawesome-free/css/all.css"; // Ensure you are using css-loader

Vue.use(Vuetify);

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  icons: {
    iconfont: "md",
    iconfont: "fa"
  }
});
