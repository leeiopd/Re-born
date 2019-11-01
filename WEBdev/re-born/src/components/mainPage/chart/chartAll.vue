<template>
  <div class="container" style="padding: 0;">
    <apexchart type="radialBar" :options="chartOptions" :series="series" style="padding-top: 15vh" />
  </div>
</template>

<script>
import VueApexCharts from "vue-apexcharts";
import axios from "axios";
export default {
  props: {
    stid: {
      type: Number,
      default: 1
    }
  },
  components: {
    apexchart: VueApexCharts
  },
  data() {
    return {
      id: this.stid,
      series: [0],
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
            },
            dataLabels: {
              name: {
                fontSize: '26px'
              },
              value: {
                fontSize: '24px'              }
            }
          }
        },
        labels: ["분리수거"]
      }
    };
  },
  mounted() {
    this.checkOther();
  },
  methods: {
    checkOther: function() {
      const baseURL = "http://localhost:8080";
      const id = this.id;
      axios
        .get(`${baseURL}/api/place/${id}/`)
        .then(result => {
          const var1 = result.data.mix;
          const var2 = result.data.trashCount;
          const a = var2 - var1;
          const b = Math.round((a / var2) * 100);
          this.series = [b];
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