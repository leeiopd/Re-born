<template>
  <div class="Complaints">
    <Search @emitParentString="updateParentString($event)"></Search>
    <v-layout mt-5 wrap style="justify-content:center;">
      <!-- v-bind="{ [xs${card.flex}]: true }" -->
      <v-flex v-for="com in company" :key="com.name" xs12 sm6 md4 lg3>
        <v-card>
          <v-img
            :src="com.companyImg"
            class="white--text"
            height="200px"
            gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
          >
            <v-card-text class="text-center" v-text="com.name"></v-card-text>
          </v-img>
          <v-card-actions style="justify-content:center;">
            <div class="flex-grow-1"></div>
            <router-link to="/report" style="text-decoration:none;">
              <v-btn icon @click="enterrepo(com)">
                <v-icon>mdi-bell-alert</v-icon>
              </v-btn>
            </router-link>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </div>
</template>
<script>
import Search from "./components/Search";
import FirebaseServices from "../../services/FirebaseServices";
import firebase from "firebase";
import { EventBus } from "../../utils/event-bus";

export default {
  components: {
    Search
  },
  data() {
    return {
      search_value: "",
      company: []
    };
  },

  methods: {
    updateParentString(val) {
      this.search_value = val;
    },
    async init() {
      const response = await FirebaseServices.getCompanyList();
      this.company = response;
      console.log(company);
    },
    enterrepo(com) {
      var companyname = com.name;
      EventBus.$emit("use-eventbus", companyname);
    }
  },
  
  mounted() {
    this.init();
  }
};
</script>
<style>
.flex {
  margin: 0px 0px 10px 0px;
}
</style>