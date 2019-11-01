module.exports = {
  transpileDependencies: ["vuetify"],
  devServer: {
    proxy: {
      baseURL: {
        target: "http://localhost:8080/"
      }
    }
  }
};
