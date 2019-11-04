import firebase from "firebase/app";
import "firebase/database";
import "firebase/auth";
import "firebase/firestore";
import "firebase/storage";

import router from "../router";
import store from "../store";

const firebaseConfig = {
  apiKey: "AIzaSyB7BDC4zo1QEInT-LhEZgaNt9pbXhDeN3g",
  authDomain: "localhost:8080",
  databaseURL: "https://reborn-4c850.firebaseio.com",
  projectId: "reborn-4c850",
  storageBucket: "reborn-4c850.appspot.com",
  messagingSenderId: "362958430568",
  appId: "1:362958430568:web:b50613f82bc57ede"
};

firebase.initializeApp(firebaseConfig);

// firebase 인승상태 지속성
// login 시 페이지 로드가 한번 일어남으로 NONE으로 설정하면 인증이 해제됨

firebase.auth().setPersistence(firebase.auth.Auth.Persistence.SESSION);

const db = firebase.firestore();
const storage = firebase.storage();

export default {
    // login with google
    async loginUserWithGoogle() {
        let _this = this;
        var provider = new firebase.auth.GoogleAuthProvider();
        firebase.auth().signInWithRedirect(provider);
        await firebase.auth().getRedirectResult()
            .then(function(result) {
                if (result.additionalUserInfo.isNewUser) {
                    _this.createdForNewUser(result.user.uid, result.user.displayName)
                }
        })
        .catch(function(error) {
            alert(error.code, error.message)
        })
    },
    // user db update
    async createdForNewUser(userID, name) {
        await db.collection('users').doc(userID).set({
            points: 0,
            level: '0',
            displayName: name,
            created_at: firebase.firestore.FieldValue.serverTimestamp(),
            photoURL: 'http://dy.gnch.or.kr/img/no-image.jpg',
        })
    },
    // logout
    logoutUser() {
        firebase.auth().signOut().then(function() {})
        .then(sessionStorage.clear())
        .then(router.push('/sign'))
        .catch(function(error) {
            console.log(error)
        })
    }
}
