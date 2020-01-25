
# coding: utf-8
from flask import Flask, render_template
from flask import request
import pandas as pd
import os
import sys


# setting
PATH_PLAYERLIST = 'templates/data/confirm/player_IdName_jp.csv'
PATH_GET_FOLDER = 'templates/data/get'

# read
app = Flask(__name__)
csv_pList = pd.read_csv(PATH_PLAYERLIST, delimiter=',', encoding="cp932")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login_manager", methods=["POST"])
def login_manager():
    # get player's ID
    pNo = request.form["user_No"]
    pNo_len = len(pNo)
    pGrop_dic = {1: {"Group": "1", "Pad": 2},
                 2: {"Group": "1", "Pad": 1},
                 3: {"Group": "2", "Pad": 0}, }
    group, pad = pGrop_dic[pNo_len].values()
    pNoID_str = group + "".join(["0" for _ in range(pad)]) + str(pNo)
    pNoID_int = int(pNoID_str)

    # read player's name from its ID
    pName_jp = csv_pList[csv_pList["NoID"] == pNoID_int]["Name_jp"].values[0]

    # save its data
    path_get = os.path.join(PATH_GET_FOLDER, pNoID_str + ".txt")
    print(path_get)
    with open(path_get, mode='w') as f:
        f.write("temp")

    return pName_jp


if __name__ == "__main__":
    app.run(debug=True)

