<template>
  <div>
    <div id="back"></div>
      <v-tabs vertical style="background-image:black">
        <v-tab style="margin-left:75px">내 정보 보기</v-tab>
        <v-tab style="margin-left:35px;">내 청원 내역</v-tab>
        <v-tab-item>
          <UserInfo />
          <UserExp />
        </v-tab-item>
        <v-tab-item>
          <UserInfo />
          <ComplaintList />
        </v-tab-item>
      </v-tabs>
  </div>
</template>

<script>
import UserInfo from "./components/UserInfo";
import UserExp from "./components/UserExp";
import ComplaintList from "./components/ComplaintList";
export default {
  name: "MyPage",
  components: {
    UserInfo,
    UserExp,
    ComplaintList
  }
};
</script>
<style scoped>
  body {font-family: 'Poiret One', cursive; }
</style>