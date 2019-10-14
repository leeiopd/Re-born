<template>
  <v-row no-gutters style="height: 100%;">
    <v-col cols="6">
      <v-card class="pa-2" outlined tile style="height: 100%;">
        <info></info>
      </v-card>
    </v-col>
    <v-col cols="6" style="height: 100%;">
      <v-card class="pa-2" outlined tile style="hegiht: 100%;">
        <Warning></Warning>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import Info from "../components/mainPage/Info.vue";
import Warning from "../components/mainPage/Warning.vue";
export default {
  components: {
    Info,
    Warning
  }
};
</script>

<style>
</style>