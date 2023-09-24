<template>
  <v-container style="max-width: 600px" class="pa-10">
    <v-card class="pa-9">
      <v-card-title class="justify-center" style="font-size: 1.5em">
        로그인
      </v-card-title>
      <v-text-field
        clearable
        label="ID"
        variant="outlined"
        v-model="this.id_input"
        prepend-inner-icon="mdi-account-outline"
        onchange="manage"
      ></v-text-field>
      <v-text-field
        clearable
        label="password"
        variant="outlined"
        v-model="this.ps_input"
        prepend-inner-icon="mdi-key"
        type="password"
      ></v-text-field>
      <button class="mb-5 button1" @click="submit">Log In</button>
      <button class="button">Sign In</button>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      id_input: "",
      ps_input: "",
    };
  },
  methods: {
    submit() {
      axios
        .post("http://127.0.0.1:5000/", {
          userID: this.id_input,
          password: this.ps_input,
        })
        .then(function (response) {
          console.log(response["data"]);
          if (response["data"]["status"] == "SUCCESS") {
            alert("Your membership registration has been successful.");
          } else if (response["data"]["status"] == "FAIL") {
            alert(this.id_input + ", this ID is already exists.");
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    manage() {
      this.id_input = this.id_input.trim();
    },
  },
};
</script>
<style>
.button {
  width: 445px;
  height: 45px;
  font-family: "Roboto", sans-serif;
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 2.5px;
  font-weight: 500;
  color: #000;
  background-color: #fff;
  border: none;
  border-radius: 45px;
  box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease 0s;
  cursor: pointer;
  outline: none;
}

.button:hover {
  background-color: #2ee59d;
  box-shadow: 0px 15px 20px rgba(46, 229, 157, 0.4);
  color: #fff;
  transform: translateY(-7px);
}

.button1 {
  width: 445px;
  height: 45px;
  font-family: "Roboto", sans-serif;
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 2.5px;
  font-weight: 500;
  color: #000;
  background-color: #fff;
  border: none;
  border-radius: 45px;
  box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease 0s;
  cursor: pointer;
  outline: none;
}

.button1:hover {
  background-color: #54c9de;
  box-shadow: 0px 15px 20px rgba(46, 229, 157, 0.4);
  color: #fff;
  transform: translateY(-7px);
}
</style>
