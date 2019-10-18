<template>
  <div class="text-center">
    <v-dialog v-model="dialog" width="1200">
      <template v-slot:activator="{ on }">
        <v-btn
          color="#7366F2"
          dark
          v-on="on"
          @click="dialog = true"
          fab
          style="width: 11vw; height: 11vw; font-size: 3vw; font-family: 'Gamja Flower', cursive;"
        >캔</v-btn>
      </template>

      <v-card>
        <v-card-title class="headline grey lighten-2" primary-title>캔의 분리수거 방법</v-card-title>

        <v-card-text>
          L철캔, 알루미늄캔 - 내용물을 비우고 가능한 압착
          - 겉 또는 속의 플라스틱 뚜겅 등 제거
          - 담배꽁초 등 이물질을 넣지 말 것
          기타 캔류 - 구멍을 뚫어 내용물을 비운 후 배출
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