<template>
  <v-container>
    <div style="width: 80vw; height: 100%; text-align:center;">
      <h1>{{addressLevel1}} {{addressLevel2}} {{addressLevel3}} {{addressPlace}}</h1>
      <v-row>
        <v-col style="width: 20%;">
          <div>
            <v-btn
              v-on:click="level1ItemsPrev(level1ItemsStart)"
              style="font-size:2vw; width: 1vw; height: 2vw; "
            >
              <i class="fas fa-angle-double-up"></i>
            </v-btn>
            <v-list v-for="(item, i) in level1Items" :key="i" style="padding: 0;margin: 2vh;">
              <v-btn
                v-on:click="itemSelectLevel1(item.name, item.pk)"
                outlined
                color="indigo"
                style="width: 100%; font-size: 3vh"
              >{{item.name}}</v-btn>
            </v-list>
            <v-btn
              v-on:click="level1ItemsNext(level1ItemsStart)"
              style="font-size:2vw; width: 1vw; height: 2vw; "
            >
              <i class="fas fa-angle-double-down"></i>
            </v-btn>
          </div>
        </v-col>
        <v-col style="width: 20%;">
          <div>
            <v-btn
              v-on:click="level2ItemsPrev(level2ItemsStart)"
              style="font-size:2vw; width: 1vw; height: 2vw; "
            >
              <i class="fas fa-angle-double-up"></i>
            </v-btn>
            <v-list v-for="(item, i) in level2Items" :key="i" style="padding: 0;margin: 2vh;">
              <v-btn
                v-on:click="itemSelectLevel2(item.name, item.pk)"
                outlined
                color="indigo"
                style="width: 100%; font-size: 3vh;"
              >{{item.name}}</v-btn>
            </v-list>
            <v-btn
              v-on:click="level2ItemsNext(level2ItemsStart)"
              style="font-size:2vw; width: 1vw; height: 2vw; "
            >
              <i class="fas fa-angle-double-down"></i>
            </v-btn>
          </div>
        </v-col>
        <v-col style="width: 20%;">
          <div>
            <v-btn
              v-on:click="level3ItemsPrev(level3ItemsStart)"
              style="font-size:2vw; width: 1vw; height: 2vw; "
            >
              <i class="fas fa-angle-double-up"></i>
            </v-btn>
            <v-list v-for="(item, i) in level3Items" :key="i" style="padding: 0;margin: 2vh;">
              <v-btn
                v-on:click="itemSelectLevel3(item.name, item.pk)"
                outlined
                color="indigo"
                style="width: 100%; font-size: 3vh"
              >{{item.name}}</v-btn>
            </v-list>
            <v-btn
              v-on:click="level3ItemsNext(level3ItemsStart)"
              style="font-size:2vw; width: 1vw; height: 2vw; "
            >
              <i class="fas fa-angle-double-down"></i>
            </v-btn>
          </div>
        </v-col>
        <v-col style="width: 20%;">
          <div>
            <v-btn
              v-on:click="placeItemsPrev(placeItemsStart)"
              style="font-size:2vw; width: 1vw; height: 2vw; "
            >
              <i class="fas fa-angle-double-up"></i>
            </v-btn>
            <v-list v-for="(item, i) in placeItems" :key="i" style="padding: 0;margin: 2vh;">
              <v-btn
                v-on:click="itemSelectPalce(item.pk, item.name)"
                outlined
                color="indigo"
                style="width: 100%; font-size: 3vh"
              >{{item.name}}</v-btn>
            </v-list>
            <v-btn
              v-on:click="placeItemsNext(placeItemsStart)"
              style="font-size:2vw; width: 1vw; height: 2vw; "
            >
              <i class="fas fa-angle-double-down"></i>
            </v-btn>
          </div>
        </v-col>
      </v-row>
    </div>
    <v-dialog v-model="dialog" fullscreen hide-overlay transition="scale-transition" >
      <v-row no-gutters style="height: 100%;">
        <v-col cols="6">
          <v-card class="pa-2" outlined tile style="height: 100%; text-align: center;">
            <v-btn absolute @click="dialog=false">이것은 닫기버튼입니다 배치를 어떻게...</v-btn>
            <Status 
              :stid="this.stid"
              :placeName="this.stplaceName"
            />
          </v-card>
        </v-col>
        <v-col cols="6" style="height: 100%;">
          <v-card class="pa-2" outlined tile style="height: 100%;">
            <Chart 
              :stid="this.stid"
            />
          </v-card>
        </v-col>
      </v-row>
    </v-dialog>
  </v-container>
</template>

<script>
import axios from "axios";
import Status from "../mainPage/Status.vue";
import Chart from "../mainPage/Chart.vue";

export default {
  components: {
    Status,
    Chart
  },
  data: () => ({
    addressLevel1: "서울특별시",
    level1Items: [],
    level1ItemSelect: "",
    level1ItemsStart: 0,
    level1ItemPk: 1,
    level1Last: 0,
    addressLevel2: "",
    level2Items: [],
    level2ItemSelect: "",
    level2ItemsStart: 0,
    level2ItemPk: 1,
    level2Last: 0,
    addressLevel3: "",
    level3Items: [],
    level3ItemSelect: "",
    level3ItemsStart: 0,
    level3ItemPk: 1,
    level3Last: 0,
    addressPlace: "",
    placeItems: [[], [], [], [], []],
    placeItemSelect: "",
    placeItemPk: 1,
    placeLast: 0,
    placeItemsStart: 0,
    dialog: false,
    stid: 1,
    stplaceName: '유성연수원점'
  }),
  created() {
    this.loadLevel1(this.level1ItemsStart);
    this.loadLevel2(this.level2ItemsStart, this.level1ItemPk);
    this.loadLevel3(this.level3ItemsStart, this.level2ItemPk);
    this.loadPlace(this.level2ItemPk);
  },
  methods: {
    loadLevel1(level1ItemsStart) {
      const baseURL = "http://localhost:8080";
      axios
        .get(`${baseURL}/api/lv1list/`)
        .then(result => {
          var len = result.data.length;
          this.level1Last = len - 5;
          const temp = [[], [], [], [], []];
          for (var i = level1ItemsStart; i < level1ItemsStart + 5; i++) {
            temp[i - level1ItemsStart] = result.data[i];
          }
          this.level1Items = temp;
        })
        .catch(error => {
          console.log(error);
        });
    },
    loadLevel2(level2ItemsStart, pk) {
      const baseURL = "http://localhost:8080";
      axios
        .get(`${baseURL}/api/lv2list/${pk}/`)
        .then(result => {
          var len = result.data.length;
          this.level2Last = len - 5;
          const temp = [[], [], [], [], []];
          for (var i = level2ItemsStart; i < level2ItemsStart + 5; i++) {
            temp[i - level2ItemsStart] = result.data[i];
          }
          this.level2Items = temp;
        })
        .catch(error => {
          console.log(error);
        });
    },
    loadLevel3(level3ItemsStart, pk) {
      const baseURL = "http://localhost:8080";
      axios
        .get(`${baseURL}/api/lv3list/${pk}/`)
        .then(result => {
          var len = result.data.length;
          if (len <= 5) {
            var temp = [];
            temp = result.data;
            this.level3Items = temp;
          } else {
            this.level3Last = len - 5;
            var temp = [[], [], [], [], []];
            for (var i = level3ItemsStart; i < level3ItemsStart + 5; i++) {
              temp[i - level3ItemsStart] = result.data[i];
            }

            this.level3Items = temp;
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    loadPlace(pk) {
      const baseURL = "http://localhost:8080";
      axios
        .get(`${baseURL}/api/placelist/${pk}/`)
        .then(result => {
          if (result.data.length === 0) {
            const temp = [[], [], [], [], []];
            temp[0] = { pk: 99999, name: "X" };
            temp[1] = { pk: 99999, name: "설치된 장소가" };
            temp[2] = { pk: 99999, name: "  없습니다.  " };
            temp[3] = { pk: 99999, name: "X" };
            temp[4] = { pk: 99999, name: "X" };
            this.placeItems = temp;
          } else {
            const temp = [[], [], [], [], []];
            const data = result.data[0];
            temp[0] = data;
            temp[1] = { pk: 99999, name: "X" };
            temp[2] = { pk: 99999, name: "X" };
            temp[3] = { pk: 99999, name: "X" };
            temp[4] = { pk: 99999, name: "X" };
            this.placeItems = temp;
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    itemSelectLevel1(city, pk) {
      this.level1ItemSelect = city;
      this.addressLevel1 = city;
      this.addressLevel2 = "";
      this.addressLevel3 = "";
      this.level2itemsStart = 0;
      this.level1ItemPk = pk;
      var start = this.level2ItemsStart;
      this.loadLevel2(start, pk);
    },
    itemSelectLevel2(city, pk) {
      this.level2ItemSelect = city;
      this.addressLevel2 = city;
      this.addressLevel3 = "";
      this.level3itemsStart = 0;
      this.level2ItemPk = pk;
      var start = this.level3ItemsStart;
      this.loadLevel3(start, pk);
    },
    itemSelectLevel3(city, pk) {
      this.level3ItemSelect = city;
      this.addressLevel3 = city;
      this.level3ItemPk = pk;
      this.loadPlace(pk);
    },
    itemSelectPalce(pk, city) {
      if (pk === 99999) {
        alert("아직 설치되지 않은 지역입니다.");
      }
      this.placesItemSelect = city;
      this.stid = pk;
      this.stplaceName = city;
      this.dialog = true;
    },
    level1ItemsNext(start) {
      if (start < this.level1Last) {
        this.level1ItemsStart = start + 1;
      }
      this.loadLevel1(this.level1ItemsStart);
    },
    level1ItemsPrev(start) {
      if (start > 0) {
        this.level1ItemsStart = start - 1;
      }
      this.loadLevel1(this.level1ItemsStart);
    },
    level2ItemsNext(start) {
      if (start < this.level2Last) {
        this.level2ItemsStart = start + 1;
      }
      this.loadLevel2(this.level2ItemsStart, this.level1ItemPk);
    },
    level2ItemsPrev(start) {
      if (start > 0) {
        this.level2ItemsStart = start - 1;
      }
      this.loadLevel2(this.level2ItemsStart, this.level1ItemPk);
    },
    level3ItemsNext(start) {
      if (start < this.level3Last) {
        this.level3ItemsStart = start + 1;
      }
      this.loadLevel3(this.level3ItemsStart, this.level2ItemPk);
    },
    level3ItemsPrev(start) {
      if (start > 0) {
        this.level3ItemsStart = start - 1;
      }
      this.loadLevel3(this.level3ItemsStart, this.level2ItemPk);
    },
    placeItemsNext(start) {},
    placeItemsPrev(start) {}
  }
};
</script>

<style>
.v-dialog--fullscreen {
  border-radius: 0;
  margin: 0;
  height: 68vh;
  position: fixed;
  overflow-y: auto;
  top: 22vh; 
  left: 0;
}
</style>