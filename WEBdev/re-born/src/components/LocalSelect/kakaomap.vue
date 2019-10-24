<template>
  <v-card class="mx-auto" max-width="300" tile>
    <v-list rounded>
      <v-subheader>Level1</v-subheader>
      <v-list-item-group v-model="item" color="primary">
        <v-list-item v-for="(item, i) in items" :key="i">
          <v-list-item-icon>
            <v-icon v-text="item.icon"></v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title v-text="item.text"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-card>
</template>

<script>
import axios from "axios";
export default {
  data: ()=>({
    level:[]
  })
  mounted() {
    this.aaa();
  },
  methods: {
    Daejeon() {
      document.getElementById("location").innerText = "현위치 : 대전시";
      document.getElementById("btn1").innerText = "동구";
      document.getElementById("btn2").innerText = "중구";
      document.getElementById("btn3").innerText = "서구";
      document.getElementById("btn4").innerText = "유성구";
      document.getElementById("btn5").innerText = "대덕구";
      document.getElementById("btn6").innerText = "";
      document.getElementById("btn7").innerText = "";
      document.getElementById("btn8").innerText = "";
      document.getElementById("btn9").innerText = "";
      document.getElementById("btn10").innerText = "";
      document.getElementById("btn11").innerText = "";
      document.getElementById("btn12").innerText = "";
      document.getElementById("btn13").innerText = "";
      document.getElementById("btn14").innerText = "";
      document.getElementById("btn15").innerText = "";
      document.getElementById("btn16").innerText = "";
      document.getElementById("btn17").innerText = "";
      this.map.setLevel(9);
      this.moveLatLon = new kakao.maps.LatLng(36.33333333, 127.4166667);
      this.map.panTo(this.moveLatLon);
    },
    Yuseong() {
      document.getElementById("location").innerText = "현위치 : 대전시 유성구";
      document.getElementById("btn1").innerText = "진잠동";
      document.getElementById("btn2").innerText = "온천1동";
      document.getElementById("btn3").innerText = "온천2동";
      document.getElementById("btn4").innerText = "노은1동";
      document.getElementById("btn5").innerText = "노은2동";
      document.getElementById("btn6").innerText = "신성동";
      document.getElementById("btn7").innerText = "전민동";
      document.getElementById("btn8").innerText = "구즉동";
      document.getElementById("btn9").innerText = "관평동";
      document.getElementById("btn10").innerText = "원신흥동";
      document.getElementById("btn11").innerText = "덕명동";
      this.map.setLevel(7);
      this.moveLatLon = new kakao.maps.LatLng(36.36694444, 127.3269444);
      this.map.panTo(this.moveLatLon);
    },
    Deokmyeong() {
      document.getElementById("location").innerText =
        "현위치 : 대전시 유성구 덕명동";
      document.getElementById("btn1").innerText = "연수원";
      document.getElementById("btn2").innerText = "한밭대";
      document.getElementById("btn3").innerText = "";
      document.getElementById("btn4").innerText = "";
      document.getElementById("btn5").innerText = "";
      document.getElementById("btn6").innerText = "";
      document.getElementById("btn7").innerText = "";
      document.getElementById("btn8").innerText = "";
      document.getElementById("btn9").innerText = "";
      document.getElementById("btn10").innerText = "";
      document.getElementById("btn11").innerText = "";
      this.map.setLevel(6);
      this.moveLatLon = new kakao.maps.LatLng(36.353302, 127.299758);
      this.map.panTo(this.moveLatLon);
    }
  }
};
</script>

<style>
</style>