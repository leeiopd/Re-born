<template>
  <v-container>
    <h1>지역 선택</h1>
    <v-flex row wrap>
      <tiger class="tiger" />
      <pick class="pick" />
    </v-flex>
  </v-container>
</template>

<script>
import tiger from "../components/LocalSelect/tiger";
import pick from "../components/LocalSelect/pick";

export default {
  components: {
    tiger,
    pick
  },
};
</script>

<style>
.tiger {
  width: 57%;
  border: 3px ridge;
  height: 66vh;
  margin-left: 2%;
  margin-right: 1%;
}
.pick {
  width: 38%;
  border: 3px ridge;
  margin-left: 1%;
  margin-right: 1%;
}
</style>