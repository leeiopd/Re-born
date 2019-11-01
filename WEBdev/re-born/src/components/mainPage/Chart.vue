<template>
  <div class="container" style="padding-top: 5vh; height:100%">
    <v-row no-gutters style="height: 100%;">
      <span style="position: absolute; left:-6vw; top:-3vh; width:30vw; margin-left:0">
        <chartCan
          :stid="this.stid"
        />
        <chartPaper
          :stid="this.stid"
        />
      </span>
      <span style="position: absolute; right:50px; top:-5vh">
        <chartAll
          :stid="this.stid"
        />
      </span>
      <span style="position: absolute; right:-6vw; top:-3vh; width:30vw; margin-right:0">
        <chartPET
          :stid="this.stid"
        />
        <chartOther
          :stid="this.stid"
        />
      </span>
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