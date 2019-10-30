<template>
  <div style="height: 100%; background-color: #f0f0f0f0; padding-top:3vw;">
    <div class="container" style="margin:auto; width: 100%;">
      <img src="../../assets/light-yellow.png" id="ppp" style="width: 40vw" />
    </div>
    <div>
      <h1 style="font-size: 3vw; text-aling: center">오늘의 재활용 지수는</h1>
      <h1 style="font-size: 3vw; text-aling: center">{{this.state}} 입니다.</h1>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: function() {
    return {
      state: "나쁨",
      id: 1,
      placeName: "",
      ImageSrc: ""
    };
  },
  mounted() {
    this.checkState();
  },
  methods: {
    checkState: function() {
      const baseURL = "http://localhost:8080";
      const id = this.id;
      axios
        .get(`${baseURL}/api/place/${id}/`)
        .then(result => {
          console.log(result);
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
              const stateDefualt = (stateRecycled / stateAll) * 100;

              if (stateDefualt + 10 < nowValue) {
                this.state = "좋음";
                var src = "../../assets/light-green.png";
                this.chanegImg(src);
                console.log(this.ImageSrc);
              } else if (stateDefualt - 10 > nowValue) {
                this.state = "나쁨";
                this.ImageSrc = "../../assets/light-red.png";
              } else {
                this.state = "보통";
                this.ImageSrc = "../../assets/light-yellow.png";
              }
            })
            .catch(error => {
              console.log(error);
            });
        })
        .catch(error => {
          console.log(error);
        });
    },
    changeImg: function() {
      const aaa = document.getElementById("ppp");
      aaa.src = "aaaaaaaaaaa";
    }
  }
};
</script>

<style>
</style>