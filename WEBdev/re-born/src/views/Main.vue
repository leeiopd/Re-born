<template>
  <v-row no-gutters style="height: 100%;">
    <v-col cols="6">
      <v-card class="pa-2" outlined tile style="height: 100%; text-align: center;">
        <Status></Status>
      </v-card>
    </v-col>
    <v-col cols="6" style="height: 100%;">
      <v-card class="pa-2" outlined tile style="height: 100%;">
        <Chart></Chart>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import Status from "../components/mainPage/Status.vue";
import Chart from "../components/mainPage/Chart.vue";
export default {
  components: {
    Status,
    Chart
  },
  created() {
    setInterval(() => {
      if (window.location.href == 'http://localhost:8081/') {
        location.reload()
      }
    }, 30000)
  }
};
</script>

<style>
</style>