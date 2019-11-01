<template>
  <div class="text-center">
    <v-dialog v-model="dialog" width="1200">
      <template v-slot:activator="{ on }">
        <v-btn
          color="#D9043D"
          dark
          v-on="on"
          @click="dialog = true"
          fab
          style="width: 15vw; height: 15vw; font-size: 5vw; font-family: 'Gamja Flower', cursive;"
        >종이</v-btn>
      </template>
      <v-card>
        <v-card-title class="display-1 grey lighten-2" primary-title>종이의 분리수거 방법</v-card-title>
        <v-card-text class="title font-weight-black">
          <br>- 테이프나 철판을 제거<br>
          - 코팅된 표지, 스프링은 제거<br>
          - 물기에 젖지 않은 상태로 배출
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="dialog = false">닫기</v-btn>
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