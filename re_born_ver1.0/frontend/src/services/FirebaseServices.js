import firebase from "firebase/app";
import "firebase/database";
import "firebase/auth";
import "firebase/firestore";
import "firebase/storage";

import router from "../router";
import store from "../store";

const firebaseConfig = {
  apiKey: "AIzaSyB7BDC4zo1QEInT-LhEZgaNt9pbXhDeN3g",
  authDomain: "reborn-4c850.firebaseapp.com",
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

var db = firebase.firestore();
const storage = firebase.storage();

export default {
  // login with google
  loginUserWithGoogle() {
    var provider = new firebase.auth.GoogleAuthProvider();
    firebase
      .auth()
      .signInWithPopup(provider)
      .then(function(result) {
        // This gives you a Google Access Token. You can use it to access the Google API.
        var token = result.credential.accessToken;
        // The signed-in user info.
        var user = result.user;
        // ...
      });
  },
  // // user db update
  createdForNewUser(userID, name) {
    db.collection("users")
      .doc(userID)
      .set({
        created_at: firebase.firestore.FieldValue.serverTimestamp(),
        displayName: name,
        level: "0",
        photoURL: "http://dy.gnch.or.kr/img/no-image.jpg",
        points: 0
      })
      .then(function(docRef) {
        console.log("Document written with ID: ", docRef.id);
      })
      .catch(function(error) {
        console.error("Error adding document: ", error);
      });
  },
  // logout
  logoutUser() {
    firebase
      .auth()
      .signOut()
      .then(function() {})
      .then(sessionStorage.clear())
      .then(router.push("/"))
      .catch(function(error) {
        /* eslint-disable no-console */
        console.log(error);
      });
  },

  async getFirebaseUser(uid) {
    await db
      .collection("users")
      .doc("" + uid)
      .get()
      .then(doc => {
        var data = doc.data();
        console.log("data", data);
        return data;
      })
      .catch(err => {
        console.log(err);
      });
  },
  async getCompanyList() {
    const DBCOMPANY = await db.collection("company");
    return DBCOMPANY.orderBy("name")
      .get()
      .then(docSnapshots => {
        return docSnapshots.docs.map(doc => {
          let data = doc.data();
          return data;
        });
      }) /* eslint-disable no-console */
      .catch(error => console.log(error));
  },

  async getCompaintList() {
    const DBCOMPLAINTS = await db.collection("complaints");
    return DBCOMPLAINTS.get()
      .then(docSnapshots => {
        return docSnapshots.docs.map(doc => {
          let data = doc.data();
          return data;
        });
      }) /* eslint-disable no-console */
      .catch(error => console.log(error));
  }
  // add complaint db
  // async addRepo(complaint) {
  //   await db.collection("complaints").set({});
  // }
};
