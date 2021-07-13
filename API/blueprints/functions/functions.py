from flask import Blueprint, jsonify
import pymongo
from bson import ObjectId

functions = Blueprint('functions', __name__)
client = pymongo.MongoClient(
    "mongodb+srv://Mezo:Almazni2013@tadawul-test.wkg8i.mongodb.net/Tadawul?retryWrites=true&w=majority")


@functions.route("/functions/MarketCap", methods=["GET"])
def get_market_cap():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": ObjectId("60edbcdbd079723b37dd5bc9")})

    res["_id"] = 2222

    price = float(res['2222']["PRICE"])
    shares = int(res['2222']["ISSUED SHARES"])

    response = {}
    response["MarketCap"] = (price * shares)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@functions.route("/functions/EPS", methods=["GET"])
def get_EPS():
    # http://localhost:7979/functions/EPS
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": ObjectId("60edbcdbd079723b37dd5bc9")})

    res["_id"] = 2222

    shares = int(res['2222']["ISSUED SHARES"])
    statement_of_income = res['2222']["STATEMENT OF INCOME"]["ANNUALLY"]

    response = []

    for statement in statement_of_income:
        year = statement.split('-')[0]
        current_response = {}
        net_income = float(
            statement_of_income[statement][11]["Net Income"])*1000
        current_response["{}".format(year)] = net_income/shares
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result
