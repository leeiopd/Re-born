<template>
  <div class="text-center">
    <v-dialog v-model="dialog" width="1200">
      <template v-slot:activator="{ on }">
        <v-btn
          color="#033E8C"
          dark
          v-on="on"
          @click="dialog = true"
          fab
          style="width: 11vw; height: 11vw; font-size: 3vw; font-family: 'Gamja Flower', cursive;"
        >페트병</v-btn>
      </template>

      <v-card>
        <v-card-title class="display-1 grey lighten-2" primary-title>페트병의 분리수거 방법</v-card-title>

        <v-card-text class="title font-weight-black">
          <br>- 뚜껑을 제거한 후, 내용물을 비우고 가능한 압착하여 배출<br>
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
export default {
  data() {
    return {
      dialog: false
    };
  }
};
</script>