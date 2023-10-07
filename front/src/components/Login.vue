<template>
  <v-container style="max-width: 600px" class="pa-10">
    <v-card class="pa-14 me-16">
      <v-card-title class="justify-center" style="font-size: 1.2em">
        로그인
      </v-card-title>
      <v-text-field
        clearable
        label="ID"
        variant="outlined"
        v-model="this.id_input"
        prepend-inner-icon="mdi-account-outline"
      ></v-text-field>
      <v-text-field
        clearable
        label="password"
        variant="outlined"
        v-model="this.ps_input"
        prepend-inner-icon="mdi-key"
        type="password"
      ></v-text-field>
      <button class="mb-3 button" @click="login">Log In</button>
      <button class="button" @click="signin">Sign In</button>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "Login",
  data() {
    return {
      id_input: "",
      ps_input: "",
    };
  },
  methods: {
    signin() {
      this.$router.push("siginin");
    },
    login() {
      axios.defaults.headers.get["Content-Type"] = "application/json";
      axios
        .get("http://127.0.0.1:5000/")
        .then(function (response) {
          console.log(res.data);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>
<style>
.button {
  width: 100%;
  height: 45px;
  font-family: "Roboto", sans-serif;
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  font-weight: 500;
  color: #000;
  background-color: #fff;
  border: none;
  border-radius: 45px;
  box-shadow: 0px 3px 5px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease 0s;
  cursor: pointer;
  outline: none;
}

.button:hover {
  background-color: #eee;
  color: black;
  transform: translateY(-1px);
}
</style>
