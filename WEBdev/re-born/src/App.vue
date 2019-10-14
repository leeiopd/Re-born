<template>
  <div id="app">
    <div>
      <v-toolbar style="background-color: #2196F3; height: 22vh;">
        <v-toolbar-title style="padding-top: 14vh;">
          <img
            class="animated tada slow infinite"
            style="height: 6rem; margin-left: 3vw;"
            src="./assets/reborn-logo.png"
          />
          <span style="color: white; font-size: 80px;">Re-Born</span>
        </v-toolbar-title>
      </v-toolbar>
    </div>
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
  </div>
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
