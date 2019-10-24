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
        colors: ["#6BCFFA"],
        fill: {
          colors: ["#666AFF"]
        },
        plotOptions: {
          radialBar: {
            hollow: {
              size: "50%"
            }
          }
        },
        labels: ["PET"]
      }
    };
  },
  mounted() {
    this.checkPET();
  },
  methods: {
    checkPET: function() {
      const baseURL = "http://localhost:8080";
      const id = this.id;
      axios
        .get(`${baseURL}/api/place/${id}/`)
        .then(result => {
          const var1 = result.data.plastic;
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