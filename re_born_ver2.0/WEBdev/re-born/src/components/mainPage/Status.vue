<template>
  <div style="height: 100%; background-color: #f0f0f0f0; padding-top:3vw;">
    <div class="container" style="margin-top: 5vh; width: 100%;">
      <img v-if="color=='green'" src="../../assets/light-green.png" style="width: 40vw" />
      <img v-else-if="color=='red'" src="../../assets/light-red.png" style="width: 40vw" />
      <img v-else-if="color=='yellow'" src="../../assets/light-yellow.png" style="width: 40vw" />
    </div>
    <div>
      <h1 style="font-size: 3vw; text-aling: center">{{this.placeName}}의 재활용 지수는</h1>
      <h1 style="font-size: 3vw; text-aling: center">
        <span v-if="color=='green'" style="color: limegreen; font-size: 5vw">{{this.state}} </span>
        <span v-else-if="color=='red'" style="color: red; font-size: 5vw">{{this.state}} </span>
        <span v-else-if="color=='yellow'" style="color: #ffd400; font-size: 5vw">{{this.state}} </span>입니다.</h1>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    id: {
      type: Number,
      default: 1
    },
    placeName: {
      type: String,
      default: '유성연수원점'
    }
  },
  data: function() {
    return {
      state: "나쁨",
      color: ""
    };
  },
  mounted() {
    this.checkState();
    setInterval(() => {
        this.checkState()
    }, 30000)
  },
  methods: {
    checkState: function() {
      const baseURL = "http://localhost:8080";
      const id = this.id;
      axios
        .get(`${baseURL}/api/place/${id}/`)
        .then(result => {
          const var1 = result.data.mix;
          const var2 = result.data.trashCount;
          const a = var2 - var1;
          const nowValue = (a / var2) * 100;
          axios
            .get(`${baseURL}/api/level1/6/`)
            .then(result => {
              const stateMix = result.data.trashMixed;
              const stateRecycled = result.data.trashRecycled;
              const stateAll = stateMix + stateRecycled;
              const stateDefault = (stateRecycled / stateAll) * 100;

              if (stateDefault + 10 < nowValue) {
                this.state = "좋음";
                this.color = 'green'
              } else if (stateDefault - 10 > nowValue) {
                this.state = "나쁨";
                this.color = 'red'
              } else {
                this.state = "보통";
                this.color = 'yellow'
              }
            })
            .catch(error => {
              console.log(error);
            });
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