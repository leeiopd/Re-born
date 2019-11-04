<template>
    <div>
        <center>
            <div id="gradient"></div>
            
            <img 
                :src="imgUrl"
                width="200"
                height="200"
                id="user_img"
            />
            <br>
            <div id="percent"></div>
            <a class="relative_position" style="font-size: 30px">{{user.displayName}}</a>
        </center>
    </div>
</template>

<script>
import FirebaseServices from "../../../services/FirebaseServices.js";
export default {
    name: 'MyPage',
    data () {
        return {
            user : {},
            imgUrl: ''
        }
    },
    mounted() {
        this.getUser()
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
    }
}
</script>
<style>
    #user_img {
        position: absolute;
        top: 150px;
        left: 100px;
        border-radius: 50%;
        float:center;
        z-index:10
    }
    .relative_position {
        position: relative;
        top: 100px;
    }
    #percent {
        height: 25px;
        background-color: black;
        z-index: 1000000;
        position: absolute;
        top: 300px;
    }
    #gradient {
        height: 300px;
        background-image: linear-gradient(to bottom right, #33cccc, #2196f3)
    }
</style>