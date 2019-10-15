<template>
    <v-container>
        <h2>여기에 지도를 그릴겁니다</h2>
        <h3>무서운 호랑이 지도로</h3>
        <!--MAP START-->
               <div id="k-map" class="row">
                   <div class="6u 12u$(small)">
                       <div id="main-map" class="map-container">
                           <div id="observe">
                               <div id="SelectArea" style="display: none;">지역</div>
                               <div id="SelectSigungu" style="display: none;">시군구</div>
                               <select id="latlon" style="display:none" >
                                   <option value='' selected>--좌표--</option>
                               </select>
                           </div>
                       </div>
                   </div>
                   <div class="6u$ 12u$(small)">
                       <div class="meta">
                           <div id="ctprvn-nm" class="display"></div>
                           <div id="sig-nm" class="display"></div>
                           <div id="emd-nm" class="display"></div>
                       </div>
                   </div>
               </div>
               <!--MAP END-->
    </v-container>
</template>

<script>
// import * as jQuery from 'http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'
// import * as d3 from '../../assets/js/d3.v5.min.js'
import * as kormapjs from '../../assets/js/kor-map.js'
// import * as skel from '../../assets/js/skel.min.js'
// import * as topojson from '../../assets/js/topojson.min.js'
import * as utiljs from '../../assets/js/util.js'

export default {
    
}
</script>

<style scoped>

</style>