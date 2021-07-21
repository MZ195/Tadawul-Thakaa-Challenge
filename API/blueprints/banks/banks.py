from flask import Blueprint, jsonify
import pymongo

others = Blueprint('others', __name__)
client = pymongo.MongoClient(
    "mongodb+srv://Mezo:Almazni2013@tadawul-test.wkg8i.mongodb.net/Tadawul?retryWrites=true&w=majority")

@others.route("/banks/MarketCap", methods=["GET"])
def get_market_cap():
    tadawul_db = client["Tadawul_v2"]
    mycol = tadawul_db["Financials"]
    res = mycol.find_one({"_id": "1180"})

    price = float(res["PRICE"])
    shares = int(res["ISSUED SHARES"])

    response = {}
    response["MarketCap"] = (price * shares)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result