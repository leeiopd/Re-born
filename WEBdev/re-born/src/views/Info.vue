<template>
  <div style="width: 100%; height: 100%;">
    <div style="height: 20%; margin-bottom: 2vw">
      <h1 style="text-align: center; font-size: 4vw; ">
        <v-icon x-large style="font-size: 4vw;">info</v-icon>
        <span style="font-family: 'Oswald', sans-serif; font-size: 5vw; padding-right: 2vw;">Re-born</span>
        <span style="font-family: 'Jua', sans-serif;">가이드</span>
        <v-icon x-large style="font-size: 4vw;">info</v-icon>
      </h1>
    </div>
    <div style="height: 80%;">
      <div class="container" style="width: 100vw; height: 40%; text-align: center;">
        <info-paper style="margin-right: 5vw; margin-left: 5vw; display: inline-block;"></info-paper>
        <info-paper-pack style="margin-right: 5vw; margin-left: 5vw; display: inline-block;"></info-paper-pack>
        <infoCan style="margin-right: 5vw; margin-left: 5vw; display: inline-block;"></infoCan>
      </div>
      <div class="container" style="width: 100vw; height: 40%; text-align: center;">
        <info-glass style="margin-right: 5vw; margin-left: 5vw; display: inline-block;"></info-glass>
        <info-p-e-t style="margin-right: 5vw; margin-left: 5vw; display: inline-block;"></info-p-e-t>
      </div>
    </div>
  </div>
</template>

<script>
import infoCan from "../components/infoPage/infoCan.vue";
import infoGlass from "../components/infoPage/infoGlass.vue";
import infoPaper from "../components/infoPage/infoPaper.vue";
import infoPaperPack from "../components/infoPage/infoPaperPack.vue";
import infoPET from "../components/infoPage/infoPET.vue";

export default {
  components: {
    infoCan,
    infoGlass,
    infoPaperPack,
    infoPET,
    infoPaper
  }
};
</script>

<style>
</style>