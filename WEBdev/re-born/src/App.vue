<template>
  <v-toolbar-title id="app" style="height: 100vh">
    <v-toolbar-title>
      <v-toolbar style="background-color: #2196F3; height: 22vh;">
        <v-toolbar-title style="padding-top: 14vh;">
          <div style="display: inline;">
            <img
              class="animated tada slow infinite"
              style="height: 6rem; margin-left: 3vw;"
              src="./assets/reborn-logo.png"
            />
            <span style="color: white; font-size: 80px; font-family: 'Oswald', sans-serif;">Re-born</span>
          </div>
          <div style="display: inline; margin-left: 13rem;">
            <img src="./assets/gps.png" style="height: 4rem;" />
            <span
              style="color: yellow; font-size: 50px; margin-left: 2rem; font-family: 'Jua', sans-serif;"
            >대전시 유성구 덕명동 삼성화재연수원</span>
          </div>
        </v-toolbar-title>
      </v-toolbar>
    </v-toolbar-title>
    <div style="height: 68vh" fluid ma-0 pa-0 fill-height>
      <router-view style="height: 100%" />
    </div>
    <v-bottom-navigation :value="activeBtn" color="deep-purple accent-4" style="height: 10vh">
      <v-btn>
        <span>Recents</span>
        <v-icon>mdi-history</v-icon>
      </v-btn>

      <v-btn>
        <span>Favorites</span>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn>
        <span>Nearby</span>
        <v-icon>mdi-map-marker</v-icon>
      </v-btn>
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
    //
  })
};
</script>
