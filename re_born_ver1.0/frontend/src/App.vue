<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
import store from "./store";
import router from "./router";

export default {
  name: "App",
  store,
  router,
  components: {},
  data: () => ({
    //
  })
};
</script>
