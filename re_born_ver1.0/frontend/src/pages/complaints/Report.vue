<template>
  <div class="Report">
    <Search></Search>
    <v-layout wrap style="justify-content:center;">
      <v-flex xs12>
        <v-card>
          <div class="background">
            <h1>현재까지 청원 수</h1>
            <h2>{{count}}건</h2>
          </div>
          <div class="content">
            <h3>삼성</h3>
            <textarea id="txa" cols="30" rows="10">청원 내용을 입력해주세요.</textarea>
          </div>
          <v-card-actions>
            <v-btn outlined color="indigo" @click="show()">취소하기</v-btn>
            <v-btn outlined @click="repo()">청원하기</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import Search from "./components/Search";
import { EventBus } from "../../utils/event-bus";

import FirebaseServices from "../../services/FirebaseServices";
import firebase from "firebase";
import { ok } from "assert";

export default {
  components: {
    Search
  },
  data() {
    return {
      company_name: "",
      complaints_num: 0,
      count: 0,
      complaints: []
    };
  },
  methods: {
    async init() {
      const response = await FirebaseServices.getCompaintList();
      console.log(response);
      this.complaints = response;
    },
    repo() {
      swal("Good job!", "청원 성공", "success");
      this.count = this.count + 1;
    },
    show() {
      complaints.array.forEach(element => {
        console.log(element);
      });
    }
  },
  mounted() {
    EventBus.$once("use-eventbus", companyname => {
      this.company_name = companyname;
      this.init();
    });
  }
};
</script>

<style>
.v-card__actions {
  justify-content: flex-end;
}
.background {
  background: #87cefa;
}
.content {
  width: 85%;
  margin: 20px;
}
.v-btn {
  margin: 0px 15px;
}
.layout {
  margin: 20px;
}
textarea {
  width: 100%;
  padding: 5px;
}
h3 {
  margin: 5px;
}
h1 {
  text-align: center;
  color: white;
  height: 130px;
  line-height: 130px;
}
h2 {
  text-align: center;
  color: white;
  height: 50px;
  line-height: 25px;
}
</style>