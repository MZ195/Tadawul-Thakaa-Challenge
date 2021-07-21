from flask import Blueprint, jsonify, request
import pymongo

others = Blueprint('others', __name__)
client = pymongo.MongoClient(
    "mongodb+srv://Mezo:Almazni2013@tadawul-test.wkg8i.mongodb.net/Tadawul?retryWrites=true&w=majority")


@others.route("/others/MarketCap/", methods=["GET"])
def get_market_cap():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    price = float(res["PRICE"])
    shares = int(res["ISSUED SHARES"])

    response = {}
    response["MarketCap"] = (price * shares)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/EPS/", methods=["GET"])
def get_EPS():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    shares = int(res["ISSUED SHARES"])
    statement_of_income = res["STATEMENT OF INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            net_income = float(
                statement_of_income[period][statement]["Net Income"])
            current_response["{}".format(year)] = net_income/shares
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result
