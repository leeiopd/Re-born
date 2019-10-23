<template>
  <div class="container" style="padding: 0;">
    <apexchart type="radialBar" :options="chartOptions" :series="series" />
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
      series: [14],
      chartOptions: {
        toolbar: {
          show: true
        },
        colors: ["#978BE8"],
        fill: {
          colors: ["#CA8BE8"]
        },
        plotOptions: {
          radialBar: {
            hollow: {
              size: "50%"
            }
          }
        },
        labels: ["CAN"]
      }
    };
  }
};
</script>

<style>
</style>