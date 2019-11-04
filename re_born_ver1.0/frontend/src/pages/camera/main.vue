<template>
  <div id="cam">
    <div style="width:100vw; height: 60vh">
      <video ref="video" id="video" autoplay></video>
      <canvas ref="canvas" id="canvas" width="640" height="480"></canvas>
    </div>
    <div style="height: 40vh">
      <img
        id="snap"
        src="../../assets/camera_button.png"
        v-on:click="capture()"
        style="width:20%; margin-top:25vh"
      />
    </div>
  </div>
</template>

<script>
import firebase from "firebase";
const axios = require("axios");
const Swal = require("sweetalert2");

export default {
  name: "cam",
  data() {
    return {
      video: {},
      canvas: {},
      captures: 0
    };
  },
  mounted() {
    this.video = this.$refs.video;
    console.log(this.video);
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices
        .getUserMedia({
          audio: false,
          video: {
            facingMode: "environment"
          }
        })
        .then(stream => {
          this.$refs.video.srcObject = stream;
          this.$refs.video.play();
        });
    }
  },
  methods: {
    capture() {
      this.canvas = this.$refs.canvas;
      var context = this.canvas
        .getContext("2d")
        .drawImage(this.video, 0, 0, 640, 480);
      this.captures = this.canvas.toDataURL("image/png");
      this.$refs.video.pause();

      var fileName =
        Math.random()
          .toString(36)
          .substring(2, 15) +
        Math.random()
          .toString(36)
          .substring(2, 15);
      let uploadTask = firebase
        .storage()
        .ref("/upload/")
        .child(fileName);
      fetch(this.captures)
        .then(res => res.blob())
        .then(blob =>
          uploadTask.put(blob).then(function(snapshot) {
            snapshot.ref.getDownloadURL().then(res => {
              console.log(res);
              // axios 요청\
              // axios
              //   .get("http://127.0.0.1:8000/api/get-result", {
              //     params: {
              //       src: res
              //     }
              //   })
              //   .then(function(response) {
              //     console.log(response);
              //   });

              axios
                .post("http://127.0.0.1:8000/api/get-result/", {
                  src: res
                })
                .then(response => {
                  console.log(response);
                });
            });
          })
        );
    }
  },
  watch: {
    captures: function(newCaptures) {
      if (newCaptures != 0) {
        Swal.fire("Good job!", "You clicked the button!", "success");
        this.captures = 0;
      } else {
        this.$refs.video.play();
      }
    }
  }
};
</script>

<style>
#cam {
  text-align: center;
  color: #2c3e50;
  height: 100%;
  width: 100%;
  background-color: #ddead3;
}
#video {
  background-color: #000000;
  width: 100%;
  height: 100%;
}
#canvas {
  display: none;
}
</style>