<template>
  <div class="container" style="padding-top: 5vh">
    <v-row no-gutters style="height: 100%;">
      <v-col cols="4">
        <chartCan></chartCan>
        <chartPaper></chartPaper>
      </v-col>
      <v-col cols="4">
        <chartAll></chartAll>
      </v-col>
      <v-col cols="4">
        <chartPET></chartPET>
        <chartOther></chartOther>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import chartCan from "./chart/chartCan.vue";
import chartPET from "./chart/chartPET.vue";
import chartPaper from "./chart/chartPaper.vue";
import chartOther from "./chart/chartOther.vue";
import chartAll from "./chart/chartAll.vue";

export default {
  components: {
    chartCan,
    chartPET,
    chartPaper,
    chartOther,
    chartAll
  }
};
</script>

<style>
</style>