from flask import Flask, request, jsonify
import numpy as np
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

route = os.getcwd() + "\\user.csv"


@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        # get Request
        data = request.get_json()
        userID = data["userID"]
        password = data["password"]
        newItem = {"userID": userID, "password": password}
        
        # load csv
        df = pd.read_csv(route, encoding="cp949")
        
        if newItem["userID"] in df["userID"].values.tolist():
            return jsonify({"status": "FAIL"})
        
        
        newItem = pd.DataFrame([newItem])
        save = pd.concat([df, newItem])
        save.to_csv(route, index=False)
        
        return jsonify({"status": "SUCCESS"})
    else:
        gift = pd.read_csv(route,encoding="cp949")
        print(gift)
        return gift
if __name__ == "__main__":
    app.run()
