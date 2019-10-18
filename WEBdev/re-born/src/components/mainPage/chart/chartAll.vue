<template>
  <div class="container" style="padding: 0;">
    <apexchart type="radialBar" :options="chartOptions" :series="series" style="padding-top: 15vh" />
  </div>
</template>

<script>
import VueApexCharts from "vue-apexcharts";
export default {
  components: {
    apexchart: VueApexCharts
  },
  data() {
    return {
      series: [36],
      chartOptions: {
        toolbar: {
          show: true
        },
        colors: ["#F44336"],
        fill: {
          colors: ["#E91E63"]
        },
        plotOptions: {
          radialBar: {
            hollow: {
              size: "50%"
            }
          }
        },
        labels: ["분리수거"]
      }
    };
  }
};
</script>

<style>
</style>