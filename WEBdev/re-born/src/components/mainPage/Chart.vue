<template>
  <div class="container" style="padding-top: 5vh">
    <v-row no-gutters style="height: 100%;">
      <v-col cols="4">
        <chartCan
          :stid="this.stid"
        />
        <chartPaper
          :stid="this.stid"
        />
      </v-col>
      <v-col cols="4">
        <chartAll
          :stid="this.stid"
        />
      </v-col>
      <v-col cols="4">
        <chartPET
          :stid="this.stid"
        />
        <chartOther
          :stid="this.stid"
        />
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
  props: {
    stid: {
      type: Number,
      default: 1
    },
    placeName: {
      type: String,
      default: '유성연수원점'
    }
  },
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