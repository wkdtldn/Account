from flask import Flask, request, jsonify
import numpy as np
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

route = os.getcwd() + "\\user.csv"



@app.route("/")
def main1():
    print("-----RESET-----")
    return "hello"


@app.route("/signin", methods=["POST", "GET"])
def main2():
    df = pd.read_csv(route, encoding="cp949")
    if request.method == "POST":
        # get Request
        data = request.get_json()
        userID = data["userID"]
        password = data["password"]
        newItem = {"userID": userID, "password": password}
        print(df["userID"])
        if newItem["userID"] in df["userID"].values.tolist():
            return jsonify({"status": "FAIL"})

        newItem = pd.DataFrame([newItem])
        save = pd.concat([df, newItem])
        save.to_csv(route, index=False)

        return jsonify({"status": "SUCCESS"})


@app.route("/login", methods=["POST", "GET"])
def main3():
    df = pd.read_csv(route, encoding="cp949")
    if request.method == "POST":
        data = request.get_json()
        userID = data["userID"]
        password = data["password"]
        newItem = {"userID": userID, "password": password}
        print(df["userID"])
        if newItem["userID"] in df["userID"].values.tolist():
            if newItem["password"] in df["password"].values.tolist():
                return jsonify({"status": "SUCCESS"})
        else:
            return jsonify({"status": "FAIL"})


if __name__ == "__main__":
    app.run()
