<template>
  <div>
    <div>
      <v-toolbar style="background-color: #2196F3; height: 10vh;">
        <v-toolbar-title>
          <img
            class="animated tada slow infinite"
            style="height: 8rem; margin-left: 5vw;"
            src="../assets/reborn-logo.png"
          />
          <span style="color: white; font-size: 60px;">Re-Born</span>
        </v-toolbar-title>
      </v-toolbar>
    </div>
    <div></div>
    <v-bottom-navigation :value="activeBtn" color="deep-purple accent-4">
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
export default {
  data() {
    return {
      activeBtn: 1
    };
  }
};
</script>