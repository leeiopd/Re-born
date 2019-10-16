<template>
  <v-toolbar-title id="app" style="height: 100vh">
    <v-toolbar-title>
      <v-toolbar style="background-color: #2196F3; height: 22vh;">
        <v-toolbar-title style="padding-top: 12vh;">
          <div style="display: inline;">
            <img
              class="animated tada slow infinite"
              style="height: 7vw; margin-left: 3vw;"
              src="./assets/reborn-logo.png"
            />
            <span style="color: white; font-size: 7vw; font-family: 'Oswald', sans-serif;">Re-born</span>
          </div>
          <div style="display: inline; margin-left: 13vw;">
            <img src="./assets/gps.png" style="height: 5vw;" />
            <span
              style="color: yellow; font-size: 3vw; margin-left: 2vw; font-family: 'Jua', sans-serif;"
            >대전시 유성구 덕명동 삼성화재연수원</span>
          </div>
        </v-toolbar-title>
      </v-toolbar>
    </v-toolbar-title>
    <div style="height: 68vh" fluid ma-0 pa-0 fill-height>
      <router-view style="height: 100%" />
    </div>
    <v-bottom-navigation v-model="bottomNav" dark horizontal style="height: 10vh">
      <!-- <div style="width: 100%; height: 100%;"> -->
      <v-btn
        v-for="item in items"
        :key="item.title"
        style="width: 100%"
        @click="actFunc(item.path)"
      >
        <span style="font-size: 2vw;">{{item.title}}</span>
        <v-icon>{{item.icon}}</v-icon>
      </v-btn>
      <!-- </div> -->
    </v-bottom-navigation>
  </v-toolbar-title>
</template>

<script>
import store from "./store";
import router from "./router";

export default {
  name: "App",
  store,
  router,
  components: {},
  data: () => ({
    items: [
      { title: "Home", icon: "home", path: "/" },
      { title: "지역 검색", icon: "fas fa-search", path: "/localSelect" },
      { title: "재활용 정보", icon: "info", path: "/moreInfo" }
    ]
  }),
  methods: {
    actFunc(path) {
      router.push(path);
    }
  }
};
</script>
