<template>
  <div class="container" style="padding: 0;">
    <apexchart type="radialBar" :options="chartOptions" :series="series" />
  </div>
</template>

<script>
import VueApexCharts from "vue-apexcharts";
import axios from "axios";
export default {
  components: {
    apexchart: VueApexCharts
  },
  data() {
    return {
      id: 1,
      series: [0],
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
  },
  mounted() {
    this.checkPaper();
  },
  methods: {
    checkPaper: function() {
      const baseURL = "http://localhost:8080";
      const id = this.id;
      axios
        .get(`${baseURL}/api/place/${id}/`)
        .then(result => {
          const var1 = result.data.paper;
          const var2 = result.data.trashCount;
          const a = (var1 / var2) * 100;
          this.series = [a];
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style>
</style>