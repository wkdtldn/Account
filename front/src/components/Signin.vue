<template>
  <v-container style="max-width: 600px" class="pa-10">
    <v-card class="pa-14 me-16">
      <v-card-title class="justify-center" style="font-size: 1.2em">
        회원가입
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
      <button class="signin" @click="submit">Sign In</button>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "Signin",
  data() {
    return {
      id_input: "",
      ps_input: "",
    };
  },
  methods: {
    submit() {
      this.id_input = this.id_input.trim();
      this.ps_input = this.ps_input.trim();
      if (this.id_input == "") {
        alert("You must write your ID without 'Space'");
        this.id_input = "";
        this.ps_input = "";
      } else if (this.ps_input == "") {
        alert("You must write your Password without 'Space'");
        this.id_input = "";
        this.ps_input = "";
      } else if (this.id_input.includes(" ") == true) {
        alert("You must write your ID without 'Space'");
        this.id_input = "";
        this.ps_input = "";
      } else if (this.ps_input.includes(" ") == true) {
        alert("You must write your Password without 'Space'");
        this.id_input = "";
        this.ps_input = "";
      } else {
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
      }
    },
  },
};
</script>
<style>
.signin {
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

.signin:hover {
  background-color: #eee;
  color: black;
  transform: translateY(-1px);
}
</style>
