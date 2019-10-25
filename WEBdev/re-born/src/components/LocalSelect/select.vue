<template>
  <div style="width: 80vw; height: 100%; text-align:center;">
    <h1 v-if="title === ''">지역을 선택해 주세요</h1>
    <h1 v-else>{{this.title}}</h1>
    <v-row>
      <v-col style="width: 20%;">
        <div>
          <v-btn
            v-on:click="level1ItemsPrev(level1ItemsStart)"
            style="font-size:2vw; width: 1vw; height: 2vw; "
          >
            <i class="fas fa-angle-double-up"></i>
          </v-btn>
          <v-list v-for="(item, i) in level1Items" :key="i">
            <v-btn
              v-on:click="itemSelectLevel1(item.name)"
              outlined
              color="indigo"
              style="width: 100%;"
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
            v-on:click="level1ItemsPrev(level1ItemsStart)"
            style="font-size:2vw; width: 1vw; height: 2vw; "
          >
            <i class="fas fa-angle-double-up"></i>
          </v-btn>
          <v-list v-for="(item, i) in level1Items" :key="i">
            <v-btn
              v-on:click="itemSelectLevel1(item.name)"
              outlined
              color="indigo"
              style="width: 100%;"
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
            v-on:click="level1ItemsPrev(level1ItemsStart)"
            style="font-size:2vw; width: 1vw; height: 2vw; "
          >
            <i class="fas fa-angle-double-up"></i>
          </v-btn>
          <v-list v-for="(item, i) in level1Items" :key="i">
            <v-btn
              v-on:click="itemSelectLevel1(item.name)"
              outlined
              color="indigo"
              style="width: 100%;"
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
            v-on:click="level1ItemsPrev(level1ItemsStart)"
            style="font-size:2vw; width: 1vw; height: 2vw; "
          >
            <i class="fas fa-angle-double-up"></i>
          </v-btn>
          <v-list v-for="(item, i) in level1Items" :key="i">
            <v-btn
              v-on:click="itemSelectLevel1(item.name)"
              outlined
              color="indigo"
              style="width: 100%;"
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
    </v-row>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data: () => ({
    title: "",
    level1Items: [],
    level1ItemSelect: "",
    level1ItemsStart: 0
  }),
  created() {
    this.loadLevel1(this.level1ItemsStart);
  },
  methods: {
    loadLevel1(level1ItemsStart) {
      const baseURL = "http://localhost:8080";
      axios
        .get(`${baseURL}/api/lv1list/`)
        .then(result => {
          const temp = [[], [], [], [], []];
          for (var i = level1ItemsStart; i < level1ItemsStart + 5; i++) {
            temp[i - level1ItemsStart] = result.data[i];
          }
          this.level1Items = temp;
          console.log(this.level1Items);
        })
        .catch(error => {
          console.log(error);
        });
    },
    itemSelectLevel1(city) {
      this.level1ItemSelect = city;
      this.title += city;
      console.log(this.level1ItemSelect);
    },
    level1ItemsNext(start) {
      if (start < 12) {
        this.level1ItemsStart = start + 1;
      }
      this.loadLevel1(this.level1ItemsStart);
    },
    level1ItemsPrev(start) {
      if (start > 0) {
        this.level1ItemsStart = start - 1;
      }
      this.loadLevel1(this.level1ItemsStart);
    }
  }
};
</script>
<style>
</style>