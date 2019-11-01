<template>
  <div class="text-center">
    <v-dialog v-model="dialog" width="1200">
      <template v-slot:activator="{ on }">
        <v-btn
          color="#F2B705"
          dark
          v-on="on"
          @click="dialog = true"
          fab
          style="width: 11vw; height: 11vw; font-size: 3vw; font-family: 'Gamja Flower', cursive;"
        >종이팩</v-btn>
      </template>

      <v-card>
        <v-card-title class="display-1 grey lighten-2" primary-title>종이팩의 분리수거 방법</v-card-title>

        <v-card-text class="title font-weight-black">
          <br>- 내용물을 비운 뒤 물로 헹군 후 압착하여 배출<br>
          - 일반 종이류와 혼합되지 않게 구분
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="dialog = false">I accept</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
const app = document.createElement("div");
app.setAttribute("data-app", true);
document.body.append(app);

export default {
  data() {
    return {
      dialog: false
    };
  }
};
</script>