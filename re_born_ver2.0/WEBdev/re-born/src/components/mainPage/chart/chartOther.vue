<template>
  <div class="container" style="padding: 0;">
    <apexchart type="radialBar" :options="chartOptions" :series="series" />
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
        colors: ["#E3B64B"],
        fill: {
          colors: ["#CBE35B"]
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
                fontSize: '22px'              }
            }
          }
        },
        labels: ["Mix"]
      }
    };
  },
  mounted() {
    this.checkOther();
    setInterval(() => {
        this.checkOther()
    }, 30000)
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
          const a = Math.round((var1 / var2) * 100);
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