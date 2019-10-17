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
      series: [41],
      chartOptions: {
        colors: ["#92E352"],
        fill: {
          colors: ["#66FA67"]
        },
        plotOptions: {
          radialBar: {
            hollow: {
              size: "50%"
            }
          }
        },
        labels: ["Paper"]
      }
    };
  }
};
</script>

<style>
</style>