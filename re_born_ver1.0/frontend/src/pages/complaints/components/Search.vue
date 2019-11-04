<template>
  <div class="search">
    <v-text-field append-icon="search" v-model="search_value" @keyup="updateSearch"></v-text-field>
  </div>
</template>

<script>
import { functions } from "firebase";
export default {
  data: function() {
    return {
      search_value: ""
    };
  },
  methods: {
    updateSearch: function() {
      this.$emit("emitParentString", this.search_value);
    }
  }
};
</script>

<style>
.search {
  margin-left: 25px;
  width: 87%;
}
</style>