<template>
  <v-btn @click="submit"> Button </v-btn>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    submit() {
      axios
        .post("http://127.0.0.1:5000/", { userID: "admin", password: "admin" })
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>
