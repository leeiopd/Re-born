<template>
  <v-container>
    <h1>지역 선택</h1>
    <v-flex row wrap>
      <kakaomap />
    </v-flex>
  </v-container>
</template>

<script>
import kakaomap from "../components/LocalSelect/kakaomap";

export default {
  components: {
    kakaomap
  },
};
</script>

<style>
</style>