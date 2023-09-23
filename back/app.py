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
    # get Request
    data = request.get_json()

    userID = data["userID"]
    password = data["password"]
    newItem = {"userID": userID, "password": password}
    # load csv

    df = pd.read_csv(route, encoding="cp949")
    newItem = pd.DataFrame(newItem)
    save = df.append(newItem, ignore_index=True)
    save.to_csv(route, index=False)

    return jsonify({"status": "SUCCESS"})


if __name__ == "__main__":
    app.run()
