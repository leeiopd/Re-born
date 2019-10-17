<template>
  <v-row no-gutters style="height: 100%;">
    <v-col cols="6">
      <v-card class="pa-2" outlined tile style="height: 100%; text-align: center;">
        <Status></Status>
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
import Status from "../components/mainPage/Status.vue";
import Warning from "../components/mainPage/Warning.vue";
export default {
  components: {
    Status,
    Warning
  }
};
</script>

<style>
</style>