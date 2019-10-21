<template>
  <v-container row>
    <v-flex class="kakaomap">
    <div id="map" style="width:100%;height:100%;"></div>
    
    </v-flex>
    <v-flex class="pick">
      <v-flex class="subpick1">
        <div id="location">현위치 : </div>
      </v-flex>
      <v-flex class="subpick2" wrap height=100%>
      <div>
        <v-btn id="btn1" @click="ab()" width="33%">서울</v-btn>
        <v-btn id="btn2" @click="aba()" width="33%">부산</v-btn>
        <v-btn id="btn3" width="33%">대구</v-btn><br>
        <v-btn id="btn4" @click="Yuseong" width="33%">인천</v-btn>
        <v-btn id="btn5" width="33%">광주</v-btn>
        <v-btn id="btn6" @click="Daejeon" width="33%">대전</v-btn><br>
        <v-btn id="btn7" width="33%">울산</v-btn>
        <v-btn id="btn8" width="33%">세종</v-btn>
        <v-btn id="btn9" width="33%">경기</v-btn><br>
        <v-btn id="btn10" width="33%">강원</v-btn>
        <v-btn id="btn11" @click="Deokmyeong" width="33%">충북</v-btn>
        <v-btn id="btn12" width="33%">충남</v-btn><br>
        <v-btn id="btn13" width="33%">전북</v-btn>
        <v-btn id="btn14" width="33%">전남</v-btn>
        <v-btn id="btn15" width="33%">경북</v-btn><br>
        <v-btn id="btn16" width="33%">경남</v-btn>
        <v-btn id="btn17" width="33%">제주</v-btn>
        <v-btn width="33%"></v-btn><br>
        <v-btn width="33%"></v-btn>
        <v-btn width="33%"></v-btn>
        <v-btn width="33%"></v-btn><br>
        <v-btn width="33%"></v-btn>
        <v-btn width="33%"></v-btn>
        <v-btn width="33%"></v-btn><br>
        <v-btn width="33%"></v-btn>
        <v-btn width="33%"></v-btn>
        <v-btn width="33%" @click="aa"></v-btn>
      </div>
<!-- 
      <div>
        <span @click="aa()">원상태로 </span><br>
        <span @click="ab()">연수원 </span>
        <span @click="aba()">한밭대 </span>
        <span @click="ac()">멀캠 </span><br>
        <span @click="ad()">섭지코지 </span> 
        <span @click="ae()">동백섬 </span> 
      </div> -->
    </v-flex>
      
    </v-flex>
  </v-container>

</template>

<script>
import axios from 'axios';
export default {
  prop() {
    moveLatLon = ''
    map = ''
    option = ''
    market = ''
  },
  mounted() {
    this.aaa()
  },
  methods: {
    aaa() {
      var container = document.getElementById('map'); //지도를 담을 영역의 DOM 레퍼런스
    
      this.options = { //지도를 생성할 때 필요한 기본 옵션
        center: new kakao.maps.LatLng(35.523599, 127.756119), //지도의 중심좌표.
        level: 15 //지도의 레벨(확대, 축소 정도)
      };
      this.map = new kakao.maps.Map(container, this.options); //지도 생성 및 객체 리턴

      var positions = [
        {
            title: '삼성화재 유성연수원', 
            latlng: new kakao.maps.LatLng(36.355099, 127.298362)
        },
        {
            title: '멀티캠퍼스', 
            latlng: new kakao.maps.LatLng(37.503939, 127.042801)
        },
        {
            title: '섭지코지', 
            latlng: new kakao.maps.LatLng(33.424317, 126.931122)
        },
        {
            title: '동백섬',
            latlng: new kakao.maps.LatLng(35.155223, 129.152037)
        },
        {
            title: '한밭대학교',
            latlng: new kakao.maps.LatLng(36.350832, 127.301166)
        }
    ];

    // 마커 이미지의 이미지 주소입니다
    var imageSrc = "http://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png"; 
        
    for (var i = 0; i < positions.length; i ++) {
        
        // 마커 이미지의 이미지 크기 입니다
        var imageSize = new kakao.maps.Size(24, 35); 
        
        // 마커 이미지를 생성합니다    
        var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize); 
        
        // 마커를 생성합니다
        var marker = new kakao.maps.Marker({
            map: this.map, // 마커를 표시할 지도
            position: positions[i].latlng, // 마커를 표시할 위치
            title : positions[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
            image : markerImage // 마커 이미지 
        });
      }
    },
    aa() {
      document.getElementById('location').innerText = '현위치 : 대전시 유성구 덕명동 삼성화재연수원'
      
      // 이동할 위도 경도 위치를 생성합니다 
      this.moveLatLon = new kakao.maps.LatLng(35.523599, 127.756119);
      this.map.setLevel(15)
      // 지도 중심을 부드럽게 이동시킵니다
      // 만약 이동할 거리가 지도 화면보다 크면 부드러운 효과 없이 이동합니다
      this.map.panTo(this.moveLatLon);            
    },
    ab() { //삼성화재 유성연수원
      document.getElementById('location').innerText = '현위치 : 대전시 유성구 덕명동 삼성화재연수원'
      this.map.setLevel(4)
      this.moveLatLon = new kakao.maps.LatLng(36.355099, 127.298362);
      
      this.map.panTo(this.moveLatLon); 
    },
    aba() { //한밭대학교
      document.getElementById('location').innerText = '현위치 : 대전시 유성구 덕명동 한밭대학교'
      this.map.setLevel(4)
      this.moveLatLon = new kakao.maps.LatLng(36.350832, 127.301166);
      
      this.map.panTo(this.moveLatLon); 
    },
    ac() { //멀티캠퍼스
      document.getElementById('location').innerText = '현위치 : 서울시 어딘가 역삼동 멀티캠퍼스'
      this.map.setLevel(5)
      this.moveLatLon = new kakao.maps.LatLng(37.503939, 127.042801);
      
      this.map.panTo(this.moveLatLon); 
    },
    ad() { //섭지코지
      document.getElementById('location').innerText = '현위치 : 제주시 섭지코지'
      this.map.setLevel(5)
      this.moveLatLon = new kakao.maps.LatLng(33.424317, 126.931122);
      
      this.map.panTo(this.moveLatLon); 
    },
    ae() { //동백섬
      document.getElementById('location').innerText = '현위치 : 부산시 동백섬'
      this.map.setLevel(5)
      this.moveLatLon = new kakao.maps.LatLng(35.155223, 129.152037);
      
      this.map.panTo(this.moveLatLon); 
    },
    Daejeon() {
      document.getElementById('location').innerText = '현위치 : 대전시'
      document.getElementById('btn1').innerText = '동구'
      document.getElementById('btn2').innerText = '중구'
      document.getElementById('btn3').innerText = '서구'
      document.getElementById('btn4').innerText = '유성구'
      document.getElementById('btn5').innerText = '대덕구'
      document.getElementById('btn6').innerText = ''
      document.getElementById('btn7').innerText = ''
      document.getElementById('btn8').innerText = ''
      document.getElementById('btn9').innerText = ''
      document.getElementById('btn10').innerText = ''
      document.getElementById('btn11').innerText = ''
      document.getElementById('btn12').innerText = ''
      document.getElementById('btn13').innerText = ''
      document.getElementById('btn14').innerText = ''
      document.getElementById('btn15').innerText = ''
      document.getElementById('btn16').innerText = ''
      document.getElementById('btn17').innerText = ''
      this.map.setLevel(9)
      this.moveLatLon = new kakao.maps.LatLng(36.33333333, 127.4166667);
      this.map.panTo(this.moveLatLon); 
    },
    Yuseong() {
      document.getElementById('location').innerText = '현위치 : 대전시 유성구'
      document.getElementById('btn1').innerText = '진잠동'
      document.getElementById('btn2').innerText = '온천1동'
      document.getElementById('btn3').innerText = '온천2동'
      document.getElementById('btn4').innerText = '노은1동'
      document.getElementById('btn5').innerText = '노은2동'
      document.getElementById('btn6').innerText = '신성동'
      document.getElementById('btn7').innerText = '전민동'
      document.getElementById('btn8').innerText = '구즉동'
      document.getElementById('btn9').innerText = '관평동'
      document.getElementById('btn10').innerText = '원신흥동'
      document.getElementById('btn11').innerText = '덕명동'
      this.map.setLevel(7)
      this.moveLatLon = new kakao.maps.LatLng(36.36694444, 127.3269444);
      this.map.panTo(this.moveLatLon); 
    },
    Deokmyeong() {
      document.getElementById('location').innerText = '현위치 : 대전시 유성구 덕명동'
      document.getElementById('btn1').innerText = '연수원'
      document.getElementById('btn2').innerText = '한밭대'
      document.getElementById('btn3').innerText = ''
      document.getElementById('btn4').innerText = ''
      document.getElementById('btn5').innerText = ''
      document.getElementById('btn6').innerText = ''
      document.getElementById('btn7').innerText = ''
      document.getElementById('btn8').innerText = ''
      document.getElementById('btn9').innerText = ''
      document.getElementById('btn10').innerText = ''
      document.getElementById('btn11').innerText = ''
      this.map.setLevel(6)
      this.moveLatLon = new kakao.maps.LatLng(36.353302, 127.299758);
      this.map.panTo(this.moveLatLon); 
    }
  }
}
</script>

<style scoped>
  .kakaomap {
    width: 57%;
    border: 3px ridge;
    height: 56vh;
    margin-left: 2%;
    margin-right: 1%;
  }
  .pick {
    width: 38%;
    border: 3px ridge;
    height: 56vh;
    margin-left: 1%;
    margin-right: 1%;
  }
  .subpick1 {
    border: 3px ridge;
    height: 15%;
  }
  .subpick2 {
      border: 3px ridge;
      height: 85%;
  }
</style>