<template>
  <div>
    <div style="height: 100vh;">
      <v-layout style="background: none; margin-bottom: 1rem; margin-top: 0.7rem;">
        <img style="height: 3rem; margin-left: 25vw;" src="../../../public/reborn-logo.png" />

        <span
          id="reborn"
        >Re-born</span>
      </v-layout>
      <div >
        <img :src="user.photoURL" id="userImg" style="margin:30px 0 0 150px; border-radius: 50%" />
      </div>
      <v-divider />
      <div id="btnPosition">
        <v-btn
            v-for="item in items"
            :key="item.title"
            color="#DDEAD3"
            class="linkBtn"
            flat
            @click="actFunc(item.title, item.path)"
        >
            <v-icon left>{{item.icon}}</v-icon>
            <span style="font-family: 'Poiret One', cursive; font-size: 20px;">{{item.title}}</span>
        </v-btn>
      </div>
    </div>
  </div>
</template>

<script>
import FirebaseServices from "../../services/FirebaseServices.js";
import firebase from "firebase";
import router from "../../router";

export default {
  name: "Menu",
  data() {
    return {
      user: {
      },
      userId : '',
        items: [
            {title: 'my page', icon: 'dashboard', path: '/mypage'},
            {title: 'recycle', icon: 'eco', path: '/camera'},
            {title: 'connect', icon: 'question_answer', path: '/complaints'},
            {title: 'log out', icon: 'account_box', path: ''}
        ]
    }
  },
  mounted() {
    this.getUser();
    
  },
  methods: {
     getUser() {
      let _this = this;
      // this.user = firebase.auth().currentUser;
      firebase.auth().onAuthStateChanged(function(user){
        if (user) {
          _this.user = user;
          console.log(_this.user);
        }
      })
    },
    actFunc(title, path) {
      if (title == "log out") {
        let tmp = FirebaseServices.logoutUser();
        router.push("/");
      } else {
        router.push(path);
      }
    }
  }
};
</script>

<style>
html {
  background-color: #ddead3;
}
.button {
  text-decoration: none;
  color: rgba(255, 255, 255, 0.8);
  background: rgb(145, 92, 182);
  padding: 15px 40px;
  border-radius: 4px;
  font-weight: normal;
  text-transform: uppercase;
  transition: all 0.2s ease-in-out;
}

.glow-button:hover {
  color: rgba(255, 255, 255, 1);
  box-shadow: 0 5px 15px rgba(145, 92, 182, .4);
}
#reborn {
    color: #505050;
    font-family: 'Poiret One', cursive; 
    font-weight: bold; 
    font-size: 2rem; 
    padding-top: 0.5rem; 
    display: inline-block; 
    line-height: normal; 
    vertical-align: middle;
}
#userImg {
    width: 150px;
    height: 150px;
    margin-top : 20px;
    position : absolute;
    left: -20px;
}
#btnPosition {
  margin-top : 200px
}
.linkBtn {
  text-decoration: none;
  color: rgba(255, 255, 255, 0.8);
  background: rgb(145, 92, 182);
  padding: 15px 40px;
  border-radius: 4px;
  font-weight: normal;
  text-transform: uppercase;
  transition: all 0.2s ease-in-out;
  width: 80%;
  height: 50px;
  margin: 20px 0 0 35px;
}
.linkBtn {
  color: rgba(255, 255, 255, 1);
  box-shadow: 0 5px 15px rgba(145, 92, 182, .4);
}
</style>
