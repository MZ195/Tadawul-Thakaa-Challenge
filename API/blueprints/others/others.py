from flask import Blueprint, jsonify, request
import pymongo

others = Blueprint('others', __name__)
client = pymongo.MongoClient(
    "mongodb+srv://Mezo:Almazni2013@tadawul-test.wkg8i.mongodb.net/Tadawul?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")


@others.route("/others/MarketCap/", methods=["GET"])
def get_market_cap():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    price = float(res["PRICE"])
    shares = int(res["ISSUED_SHARES"])

    response = {}
    response["MarketCap"] = (price * shares)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/EPS/", methods=["GET"])
def get_EPS():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    shares = int(res["ISSUED_SHARES"])
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            net_income = float(
                statement_of_income[period][statement]["Net_Income"])
            current_response["{}".format(year)] = net_income/shares
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Operating_EPS/", methods=["GET"])
def get_Operating_EPS():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    statement_of_income = res["STATEMENT_OF_INCOME"]
    shares = int(res["ISSUED_SHARES"])

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            total_income = float(
                statement_of_income[period][statement]["Total_Income"])
            admin_marketing_expenses = float(
                statement_of_income[period][statement]["Admin_and_Marketing_Expenses"])
            depreciation = float(
                statement_of_income[period][statement]["Depreciation"])
            current_response["{}".format(year)] = (
                total_income-admin_marketing_expenses-depreciation)/shares
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/EBIT/", methods=["GET"])
def get_EBIT():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            total_income = float(
                statement_of_income[period][statement]["Total_Income"])
            admin_marketing_expenses = float(
                statement_of_income[period][statement]["Admin_and_Marketing_Expenses"])
            depreciation = float(
                statement_of_income[period][statement]["Depreciation"])
            current_response["{}".format(
                year)] = total_income-admin_marketing_expenses-depreciation
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/EBITDA/", methods=["GET"])
def get_EBITDA():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            total_income = float(
                statement_of_income[period][statement]["Total_Income"])
            admin_marketing_expenses = float(
                statement_of_income[period][statement]["Admin_and_Marketing_Expenses"])
            current_response["{}".format(
                year)] = total_income-admin_marketing_expenses
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Non_Current_Assets/", methods=["GET"])
def get_Non_Current_Assets():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}
            total_assets = float(
                balance_sheet[period][statement]["Total_Assets"])
            current_assets = float(
                balance_sheet[period][statement]["Current_Assets"])
            inventory = float(
                balance_sheet[period][statement]["Inventory"])
            current_response["{}".format(
                year)] = total_assets - current_assets - inventory
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Current_Assets/", methods=["GET"])
def get_Current_Assets():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}
            current_assets = float(
                balance_sheet[period][statement]["Current_Assets"])
            inventory = float(
                balance_sheet[period][statement]["Inventory"])
            current_response["{}".format(
                year)] = current_assets + inventory
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Total_Liabilities/", methods=["GET"])
def get_Total_Liabilities():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}
            shareholders_equity = float(
                balance_sheet[period][statement]["Shareholders_Equity"])
            total_liabilities_and_shareholder_equity = float(
                balance_sheet[period][statement]["Total_Liabilities_and_Shareholder_Equity"])
            current_response["{}".format(
                year)] = total_liabilities_and_shareholder_equity - shareholders_equity
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Cash_Change/", methods=["GET"])
def get_Cash_Change():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    cash_flow = res["CASH_FLOW"]

    response = {}

    for period in cash_flow:
        response['{}'.format(period)] = []
        for statement in cash_flow[period]:
            year = statement.split('-')[0]
            current_response = {}
            cash_at_end = float(
                cash_flow[period][statement]["Cash_at_End_of_Period"])
            cash_at_begining = float(
                cash_flow[period][statement]["Cash_at_Begining_of_Period"])
            current_response["{}".format(
                year)] = cash_at_end - cash_at_begining
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Book_Value/", methods=["GET"])
def get_Book_Value():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]
    shares = int(res["ISSUED_SHARES"])

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}
            shareholders_equity = float(
                balance_sheet[period][statement]["Shareholders_Equity"])
            current_response["{}".format(
                year)] = shareholders_equity/shares
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Dividends_Per_Share/", methods=["GET"])
def get_Dividends_Per_Share():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    statement_of_income = res["STATEMENT_OF_INCOME"]
    shares = int(res["ISSUED_SHARES"])

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            cash_dividends = float(
                statement_of_income[period][statement]["Cash_Dividends"])
            current_response["{}".format(
                year)] = abs(cash_dividends/shares)
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/PE/", methods=["GET"])
def get_PE():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    statement_of_income = res["STATEMENT_OF_INCOME"]
    shares = int(res["ISSUED_SHARES"])
    price = float(res["PRICE"])

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            net_income = float(
                statement_of_income[period][statement]["Net_Income"])
            current_response["{}".format(
                year)] = price / (net_income/shares)
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Operating_Profit_Multiple/", methods=["GET"])
def get_Operating_Profit_Multiple():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    statement_of_income = res["STATEMENT_OF_INCOME"]
    shares = int(res["ISSUED_SHARES"])
    price = float(res["PRICE"])

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            total_income = float(
                statement_of_income[period][statement]["Total_Income"])
            admin_marketing_expenses = float(
                statement_of_income[period][statement]["Admin_and_Marketing_Expenses"])
            depreciation = float(
                statement_of_income[period][statement]["Depreciation"])
            current_response["{}".format(
                year)] = price/(
                (total_income-admin_marketing_expenses-depreciation)/shares)
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/PB/", methods=["GET"])
def get_PB():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    shares = int(res["ISSUED_SHARES"])
    price = float(res["PRICE"])
    balance_sheet = res["BALANCE_SHEET"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}
            shareholders_equity = float(
                balance_sheet[period][statement]["Shareholders_Equity"])

            if shareholders_equity == 0 or shares == 0:
                current_response["{}".format(
                    year)] = 0
            else:
                current_response["{}".format(
                    year)] = price / (shareholders_equity/shares)
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/PS/", methods=["GET"])
def get_PS():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    shares = int(res["ISSUED_SHARES"])
    price = float(res["PRICE"])
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            sales = float(
                statement_of_income[period][statement]["Sales"])
            if sales == 0 or shares == 0:
                current_response["{}".format(
                    year)] = 0
            else:
                current_response["{}".format(
                    year)] = price / (sales/shares)
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Current_Ratio/", methods=["GET"])
def get_Current_Ratio():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}

            current_assets = float(
                balance_sheet[period][statement]["Current_Assets"])
            inventory = float(
                balance_sheet[period][statement]["Inventory"])
            current_liabilities = float(
                balance_sheet[period][statement]["Current_Liabilities"])

            current_response["{}".format(
                year)] = (
                current_assets+inventory)/current_liabilities
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Dividend_Yield/", methods=["GET"])
def get_Dividend_Yield():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    shares = int(res["ISSUED_SHARES"])
    price = float(res["PRICE"])
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}

            cash_dividends = float(
                statement_of_income[period][statement]["Cash_Dividends"])

            if shares == 0 or price == 0:
                current_response["{}".format(
                    year)] = 0
            else:
                current_response["{}".format(
                    year)] = abs(cash_dividends/shares)/price * 100
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Payout_Ratio/", methods=["GET"])
def get_Payout_Ratio():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    shares = int(res["ISSUED_SHARES"])
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}

            cash_dividends = float(
                statement_of_income[period][statement]["Cash_Dividends"])
            net_income = float(
                statement_of_income[period][statement]["Net_Income"])
            current_response["{}".format(
                year)] = abs(cash_dividends/shares) / (net_income/shares) * 100
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Operating_Profit_Margin/", methods=["GET"])
def get_Operating_Profit_Margin():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}

            total_income = float(
                statement_of_income[period][statement]["Total_Income"])
            admin_marketing_expenses = float(
                statement_of_income[period][statement]["Admin_and_Marketing_Expenses"])
            depreciation = float(
                statement_of_income[period][statement]["Depreciation"])
            sales = float(
                statement_of_income[period][statement]["Sales"])

            if sales == 0:
                current_response["{}".format(
                year)] = 0
            else:
                current_response["{}".format(
                    year)] = (
                    total_income-admin_marketing_expenses-depreciation)/sales * 100
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Net_Margin/", methods=["GET"])
def get_Net_Margin():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}

            net_income = float(
                statement_of_income[period][statement]["Net_Income"])
            sales = float(
                statement_of_income[period][statement]["Sales"])

            current_response["{}".format(
                year)] = abs(net_income/sales) * 100
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Equity_to_Capital/", methods=["GET"])
def get_Equity_to_Capital():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    capital = int(res["PAID_CAPITAL"])
    balance_sheet = res["BALANCE_SHEET"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}

            shareholders_equity = float(
                balance_sheet[period][statement]["Shareholders_Equity"])

            current_response["{}".format(
                year)] = shareholders_equity/capital * 100
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Debt_Ratio/", methods=["GET"])
def get_Debt_Ratio():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}

            total_assets = float(
                balance_sheet[period][statement]["Total_Assets"])
            shareholders_equity = float(
                balance_sheet[period][statement]["Shareholders_Equity"])
            total_liabilities_and_shareholder_equity = float(
                balance_sheet[period][statement]["Total_Liabilities_and_Shareholder_Equity"])

            current_response["{}".format(
                year)] = (
                total_liabilities_and_shareholder_equity-shareholders_equity)/total_assets * 100
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Debt_to_Equity/", methods=["GET"])
def get_Debt_to_Equity():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}

            shareholders_equity = float(
                balance_sheet[period][statement]["Shareholders_Equity"])
            total_liabilities_and_shareholder_equity = float(
                balance_sheet[period][statement]["Total_Liabilities_and_Shareholder_Equity"])

            if shareholders_equity == 0:
                current_response["{}".format(
                    year)] = 0
            else:
                current_response["{}".format(
                    year)] = (
                    total_liabilities_and_shareholder_equity-shareholders_equity)/shareholders_equity * 100
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Quick_Ratio/", methods=["GET"])
def get_Quick_Ratio():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]
    cash_flow = res["CASH_FLOW"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}

            # CASH_FLOW STATEMENT
            cash_at_end = float(
                cash_flow[period][statement]["Cash_at_End_of_Period"])
            accounts_receivable = float(
                cash_flow[period][statement]["Accounts_Receivable"])

            # BALANCE_SHEET
            current_liabilities = float(
                balance_sheet[period][statement]["Current_Liabilities"])

            current_response["{}".format(
                year)] = (
                cash_at_end + accounts_receivable)/current_liabilities
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Cash_Ratio/", methods=["GET"])
def get_Cash_Ratio():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]
    cash_flow = res["CASH_FLOW"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}

            # CASH_FLOW STATEMENT
            cash_at_end = float(
                cash_flow[period][statement]["Cash_at_End_of_Period"])

            # BALANCE_SHEET
            current_liabilities = float(
                balance_sheet[period][statement]["Current_Liabilities"])

            current_response["{}".format(
                year)] = cash_at_end/current_liabilities
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/ROA/", methods=["GET"])
def get_ROA():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}

            # STATEMENT_OF_INCOME
            net_income = float(
                statement_of_income[period][statement]["Net_Income"])

            # BALANCE_SHEET
            total_assets = float(
                balance_sheet[period][statement]["Total_Assets"])

            current_response["{}".format(
                year)] = net_income/total_assets * 100
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/ROTA/", methods=["GET"])
def get_ROTA():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}

            # STATEMENT_OF_INCOME
            total_income = float(
                statement_of_income[period][statement]["Total_Income"])
            admin_marketing_expenses = float(
                statement_of_income[period][statement]["Admin_and_Marketing_Expenses"])
            depreciation = float(
                statement_of_income[period][statement]["Depreciation"])

            # BALANCE_SHEET
            total_assets = float(
                balance_sheet[period][statement]["Total_Assets"])

            current_response["{}".format(
                year)] = (
                total_income-admin_marketing_expenses-depreciation)/total_assets * 100
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/ROE/", methods=["GET"])
def get_ROE():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}

            # STATEMENT_OF_INCOME
            net_income = float(
                statement_of_income[period][statement]["Net_Income"])

            # BALANCE_SHEET
            shareholders_equity = float(
                balance_sheet[period][statement]["Shareholders_Equity"])

            current_response["{}".format(
                year)] = net_income/shareholders_equity * 100
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Asset_Turnover_Ratio/", methods=["GET"])
def get_Asset_Turnover_Ratio():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}

            # STATEMENT_OF_INCOME
            sales = float(
                statement_of_income[period][statement]["Sales"])

            # BALANCE_SHEET
            total_assets = float(
                balance_sheet[period][statement]["Total_Assets"])

            current_response["{}".format(
                year)] = sales/total_assets
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Net_Fixed_Asset_Turnover_Ratio/", methods=["GET"])
def get_Net_Fixed_Asset_Turnover_Ratio():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}

            # STATEMENT_OF_INCOME
            sales = float(
                statement_of_income[period][statement]["Sales"])

            # BALANCE_SHEET
            fixed_assets = float(
                balance_sheet[period][statement]["Fixed_Assets"])

            current_response["{}".format(
                year)] = sales/fixed_assets
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Equity_Turnover_Ratio/", methods=["GET"])
def get_Equity_Turnover_Ratio():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}

            # STATEMENT_OF_INCOME
            sales = float(
                statement_of_income[period][statement]["Sales"])

            # BALANCE_SHEET
            shareholders_equity = float(
                balance_sheet[period][statement]["Shareholders_Equity"])

            current_response["{}".format(
                year)] = sales / shareholders_equity
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Receivables_Turnover_Ratio/", methods=["GET"])
def get_Receivables_Turnover_Ratio():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    cash_flow = res["CASH_FLOW"]
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}

            # STATEMENT_OF_INCOME
            sales = float(
                statement_of_income[period][statement]["Sales"])

            # CASH_FLOW
            accounts_receivable = float(
                cash_flow[period][statement]["Accounts_Receivable"])

            if accounts_receivable == 0:
                current_response["{}".format(
                    year)] = 0
            else:
                current_response["{}".format(
                    year)] = sales / accounts_receivable
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Payable_Turnover_Ratio/", methods=["GET"])
def get_Payable_Turnover_Ratio():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    cash_flow = res["CASH_FLOW"]
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}

            # STATEMENT_OF_INCOME
            sales_cost = float(
                statement_of_income[period][statement]["Sales_Cost"])

            # CASH_FLOW
            accounts_payable = float(
                cash_flow[period][statement]["Accounts_Payable"])

            if accounts_payable == 0:
                current_response["{}".format(
                    year)] = 0
            else:
                current_response["{}".format(
                    year)] = sales_cost/accounts_payable
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Inventory_Turnover_Ratio/", methods=["GET"])
def get_Inventory_Turnover_Ratio():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}

            # STATEMENT_OF_INCOME
            sales_cost = float(
                statement_of_income[period][statement]["Sales_Cost"])

            # BALANCE_SHEET
            inventory = float(
                balance_sheet[period][statement]["Inventory"])

            if inventory == 0:
                current_response["{}".format(
                    year)] = 0
            else:
                current_response["{}".format(
                    year)] = sales_cost/inventory
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Days_Inventory_Outstanding/", methods=["GET"])
def get_Days_Inventory_Outstanding():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            if statement_of_income[period][statement] == {}:
                break

            # STATEMENT_OF_INCOME
            sales_cost = float(
                statement_of_income[period][statement]["Sales_Cost"])

            # BALANCE_SHEET
            inventory = float(
                balance_sheet[period][statement]["Inventory"])

            if sales_cost == 0:
                current_response["{}".format(
                    year)] = 0
            else:
                current_response["{}".format(
                    year)] = abs(inventory/sales_cost * 365)
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Days_Sales_Outstanding/", methods=["GET"])
def get_Days_Sales_Outstanding():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    cash_flow = res["CASH_FLOW"]
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            if statement_of_income[period][statement] == {}:
                break

            # STATEMENT_OF_INCOME
            sales = float(
                statement_of_income[period][statement]["Sales"])

            # CASH_FLOW
            accounts_receivable = float(
                cash_flow[period][statement]["Accounts_Receivable"])

            current_response["{}".format(
                year)] = abs(accounts_receivable/sales * 365)
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@others.route("/others/Days_Payable_Outstanding/", methods=["GET"])
def get_Days_Payable_Outstanding():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    cash_flow = res["CASH_FLOW"]
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            if statement_of_income[period][statement] == {}:
                break

            # STATEMENT_OF_INCOME
            sales_cost = float(
                statement_of_income[period][statement]["Sales_Cost"])

            # CASH_FLOW
            accounts_payable = float(
                cash_flow[period][statement]["Accounts_Payable"])

            current_response["{}".format(
                year)] = abs(accounts_payable/sales_cost * 365)
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


# here we used 3 financial statements (check it with Mazen)
@others.route("/others/Operating_Cycle/", methods=["GET"])
def get_Operating_Cycle():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    cash_flow = res["CASH_FLOW"]
    statement_of_income = res["STATEMENT_OF_INCOME"]
    balance_sheet = res["BALANCE_SHEET"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            if statement_of_income[period][statement] == {}:
                break

            # STATEMENT_OF_INCOME
            sales = float(
                statement_of_income[period][statement]["Sales"])
            sales_cost = float(
                statement_of_income[period][statement]["Sales_Cost"])

            # BALANCE_SHEET
            inventory = float(
                balance_sheet[period][statement]["Inventory"])

            # CASH_FLOW
            accounts_receivable = float(
                cash_flow[period][statement]["Accounts_Receivable"])

            current_response["{}".format(
                year)] = abs(accounts_receivable/sales * 365) + abs(inventory/sales_cost * 365)
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


# here we used 3 financial statements (check it with Mazen)
@others.route("/others/Cash_Conversion_Cycle/", methods=["GET"])
def get_Cash_Conversion_Cycle():
    sector = request.args.get("sector")
    ticker = request.args.get("ticker")

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    cash_flow = res["CASH_FLOW"]
    statement_of_income = res["STATEMENT_OF_INCOME"]
    balance_sheet = res["BALANCE_SHEET"]
    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            if statement_of_income[period][statement] == {}:
                break

            # STATEMENT_OF_INCOME
            sales = float(
                statement_of_income[period][statement]["Sales"])
            sales_cost = float(
                statement_of_income[period][statement]["Sales_Cost"])

            # BALANCE_SHEET
            inventory = float(
                balance_sheet[period][statement]["Inventory"])

            # CASH_FLOW
            accounts_receivable = float(
                cash_flow[period][statement]["Accounts_Receivable"])
            accounts_payable = float(
                cash_flow[period][statement]["Accounts_Payable"])

            current_response["{}".format(
                year)] = (abs(accounts_receivable/sales * 365) + abs(inventory/sales_cost * 365)) - abs(accounts_payable/sales_cost * 365)
            response[period].append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


# comments  for later
# def comments():

    # Plowback ratio (retention)
    # retained earnings

    # Cash Dividend Payout Ratio = Cash_Dividends / (CASH_FLOW from Operations – Capital Expenditures – Preferred Dividend Paid)
    # Current Asset Turnover = (current_assets+inventory)/total_assets  #include inventory?  Avg values (beg+end)/2 ?
    # Total Asset Turnover = total_income/total_assets  #Avg values (beg+end)/2 ?

    # FCF + its reltated ratios
    # CFO
    # Working Capital

    # Bank-Related Ratios: (Page #6)
    # https://ecommons.luc.edu/cgi/viewcontent.cgi?article=1039&context=business_facpubs

    # file:///C:/Users/96656/Downloads/981-Article%20Text-529-0-10-19700101.pdf
    # The ratio of assets financed through borrowed capital
    # The financial dependency ratio
    # The financial leverage
    # The golden rule of the BALANCE_SHEET ratio
    # The working capital ratio
    # The permanent solvency ratio
    # The equity concentration ratio
