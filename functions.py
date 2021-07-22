from flask import Blueprint, jsonify
import pymongo

functions = Blueprint('functions', __name__)
client = pymongo.MongoClient(
    "mongodb+srv://Mezo:Almazni2013@tadawul-test.wkg8i.mongodb.net/Tadawul?retryWrites=true&w=majority")

# we need to match the Share Price, No. of shares & Paid Capital with its corresponding time period
# % items

# list of all important ratios:
#  https://cdn.wallstreetmojo.com/wp-content/uploads/2021/03/Ratio-Analysis-2.png
#


@functions.route("/functions/MarketCap", methods=["GET"])
def get_Market_Cap():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    price = float(res["PRICE"])
    shares = int(res["ISSUED SHARES"])

    response = {}
    response["MarketCap"] = (price * shares)
    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@functions.route("/functions/EPS", methods=["GET"])
def get_EPS():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    shares = int(res["ISSUED SHARES"])
    statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]

    response = []

    for statement in statement_of_income:
        year = statement.split('-')[0]
        current_response = {}
        net_income = float(
            statement_of_income[statement]["Net Income"])
        current_response["{}".format(year)] = net_income/shares
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@functions.route("/functions/Operating_EPS", methods=["GET"])
def get_Operating_EPS():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]
    shares = int(res["ISSUED SHARES"])

    response = []

    for statement in statement_of_income:
        year = statement.split('-')[0]
        current_response = {}
        total_income = float(
            statement_of_income[statement]["Total Income"])
        admin_marketing_expenses = float(
            statement_of_income[statement]["Admin and Marketing Expenses"])
        depreciation = float(
            statement_of_income[statement]["Depreciation"])
        current_response["{}".format(year)] = (
            total_income-admin_marketing_expenses-depreciation)/shares
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@functions.route("/functions/EBIT", methods=["GET"])
def get_EBIT():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]

    response = []

    for statement in statement_of_income:
        year = statement.split('-')[0]
        current_response = {}
        total_income = float(
            statement_of_income[statement]["Total Income"])
        admin_marketing_expenses = float(
            statement_of_income[statement]["Admin and Marketing Expenses"])
        depreciation = float(
            statement_of_income[statement]["Depreciation"])
        current_response["{}".format(
            year)] = total_income-admin_marketing_expenses-depreciation
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@functions.route("/functions/EBITDA", methods=["GET"])
def get_EBITDA():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]

    response = []

    for statement in statement_of_income:
        year = statement.split('-')[0]
        current_response = {}
        total_income = float(
            statement_of_income[statement]["Total Income"])
        admin_marketing_expenses = float(
            statement_of_income[statement]["Admin and Marketing Expenses"])
        current_response["{}".format(
            year)] = total_income-admin_marketing_expenses
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@functions.route("/functions/Non_Current_Assets", methods=["GET"])
def get_Non_Current_Assets():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    balance_sheet = res["BALANCE SHEET"]["ANNUALLY"]

    response = []

    for statement in balance_sheet:
        year = statement.split('-')[0]
        current_response = {}
        total_assets = float(
            balance_sheet[statement]["Total Assets"])
        current_assets = float(
            balance_sheet[statement]["Current Assets"])
        inventory = float(
            balance_sheet[statement]["Inventory"])
        current_response["{}".format(
            year)] = total_assets - current_assets - inventory
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@functions.route("/functions/Current_Assets", methods=["GET"])
def get_Current_Assets():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    balance_sheet = res["BALANCE SHEET"]["ANNUALLY"]

    response = []

    for statement in balance_sheet:
        year = statement.split('-')[0]
        current_response = {}
        current_assets = float(
            balance_sheet[statement]["Current Assets"])
        inventory = float(
            balance_sheet[statement]["Inventory"])
        current_response["{}".format(year)] = current_assets + inventory
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@functions.route("/functions/Total_Liabilities", methods=["GET"])
def get_Total_Liabilities():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    balance_sheet = res["BALANCE SHEET"]["ANNUALLY"]

    response = []

    for statement in balance_sheet:
        year = statement.split('-')[0]
        current_response = {}
        shareholders_equity = float(
            balance_sheet[statement]["Shareholders Equity"])
        total_liabilities_and_shareholder_equity = float(
            balance_sheet[statement]["Total Liabilities and Shareholder Equity"])
        current_response["{}".format(
            year)] = total_liabilities_and_shareholder_equity - shareholders_equity
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@functions.route("/functions/Cash_Change", methods=["GET"])
def get_Cash_Change():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    cash_flow = res["CASH FLOW"]["ANNUALLY"]

    response = []

    for statement in cash_flow:
        year = statement.split('-')[0]
        current_response = {}
        cash_at_end = float(
            cash_flow[statement]["Cash at End of Period"])
        cash_at_begining = float(
            cash_flow[statement]["Cash at Begining of Period"])
        current_response["{}".format(year)] = cash_at_end - cash_at_begining
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@functions.route("/functions/Book_Value", methods=["GET"])
def get_Book_Value():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    balance_sheet = res["BALANCE SHEET"]["ANNUALLY"]
    shares = int(res["ISSUED SHARES"])

    response = []

    for statement in balance_sheet:
        year = statement.split('-')[0]
        current_response = {}
        shareholders_equity = float(
            balance_sheet[statement]["Shareholders Equity"])
        current_response["{}".format(year)] = shareholders_equity/shares
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@functions.route("/functions/Dividends_Per_Share", methods=["GET"])
def get_Dividends_Per_Share():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    shares = int(res["ISSUED SHARES"])

    statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]

    response = []

    for statement in statement_of_income:
        year = statement.split('-')[0]
        current_response = {}
        cash_dividends = float(
            statement_of_income[statement]["Cash Dividends"])
        # cash_dividends value is not reported consistently (-/+)
        current_response["{}".format(year)] = abs(cash_dividends/shares)
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@functions.route("/functions/PE", methods=["GET"])
def get_PE():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    price = float(res["PRICE"])
    shares = int(res["ISSUED SHARES"])
    statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]

    response = []

    for statement in statement_of_income:
        year = statement.split('-')[0]
        current_response = {}
        net_income = float(
            statement_of_income[statement]["Net Income"])
        current_response["{}".format(year)] = price / \
            (net_income/shares)  # price/EPS
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@functions.route("/functions/Operating_Profit_Multiple", methods=["GET"])
def get_Operating_Profit_Multiple():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    price = float(res["PRICE"])
    shares = int(res["ISSUED SHARES"])
    statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]

    response = []

    for statement in statement_of_income:
        year = statement.split('-')[0]
        current_response = {}
        total_income = float(
            statement_of_income[statement]["Total Income"])
        admin_marketing_expenses = float(
            statement_of_income[statement]["Admin and Marketing Expenses"])
        depreciation = float(
            statement_of_income[statement]["Depreciation"])
        current_response["{}".format(year)] = price/(
            (total_income-admin_marketing_expenses-depreciation)/shares)  # price/Operating_EPS
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@functions.route("/functions/PB", methods=["GET"])
def get_PB():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    shares = int(res["ISSUED SHARES"])
    price = float(res["PRICE"])

    balance_sheet = res["BALANCE SHEET"]["ANNUALLY"]

    response = []

    for statement in balance_sheet:
        year = statement.split('-')[0]
        current_response = {}
        shareholders_equity = float(
            balance_sheet[statement]["Shareholders Equity"])
        current_response["{}".format(year)] = price / \
            (shareholders_equity/shares)
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@functions.route("/functions/PS", methods=["GET"])
def get_PS():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    shares = int(res["ISSUED SHARES"])
    price = float(res["PRICE"])

    statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]

    response = []

    for statement in statement_of_income:
        year = statement.split('-')[0]
        current_response = {}
        sales = float(
            statement_of_income[statement]["Sales"])
        current_response["{}".format(year)] = price/(sales/shares)
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@functions.route("/functions/Current_Ratio", methods=["GET"])
def get_Current_Ratio():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    balance_sheet = res["BALANCE SHEET"]["ANNUALLY"]

    response = []

    for statement in balance_sheet:
        year = statement.split('-')[0]
        current_response = {}
        current_assets = float(
            balance_sheet[statement]["Current Assets"])
        inventory = float(
            balance_sheet[statement]["Inventory"])
        current_liabilities = float(
            balance_sheet[statement]["Current Liabilities"])
        current_response["{}".format(year)] = (
            current_assets+inventory)/current_liabilities
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@functions.route("/functions/Dividend_Yield", methods=["GET"])
def get_Dividend_Yield():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    shares = int(res["ISSUED SHARES"])
    price = float(res["PRICE"])
    statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]

    response = []

    for statement in statement_of_income:
        year = statement.split('-')[0]
        current_response = {}
        cash_dividends = float(
            statement_of_income[statement]["Cash Dividends"])
        current_response["{}".format(year)] = abs(
            cash_dividends/shares)/price * 100  # abs
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@functions.route("/functions/Payout_Ratio", methods=["GET"])
def get_Payout_Ratio():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    shares = int(res["ISSUED SHARES"])
    statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]

    response = []

    for statement in statement_of_income:
        year = statement.split('-')[0]
        current_response = {}
        cash_dividends = float(
            statement_of_income[statement]["Cash Dividends"])
        net_income = float(
            statement_of_income[statement]["Net Income"])
        current_response["{}".format(year)] = abs(
            cash_dividends/shares) / (net_income/shares) * 100  # abs
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@functions.route("/functions/Operating_Profit_Margin", methods=["GET"])
def get_Operating_Profit_Margin():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]

    response = []

    for statement in statement_of_income:
        year = statement.split('-')[0]
        current_response = {}
        total_income = float(
            statement_of_income[statement]["Total Income"])
        admin_marketing_expenses = float(
            statement_of_income[statement]["Admin and Marketing Expenses"])
        depreciation = float(
            statement_of_income[statement]["Depreciation"])
        sales = float(
            statement_of_income[statement]["Sales"])
        current_response["{}".format(year)] = (
            total_income-admin_marketing_expenses-depreciation)/sales * 100  # %
        response.append(current_response)
        # AKA: EBIT margin , Return on Sales
    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@functions.route("/functions/Net_Margin", methods=["GET"])
def get_Net_Margin():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]

    response = []

    for statement in statement_of_income:
        year = statement.split('-')[0]
        current_response = {}
        net_income = float(
            statement_of_income[statement]["Net Income"])
        sales = float(
            statement_of_income[statement]["Sales"])
        current_response["{}".format(year)] = abs(net_income/sales) * 100  # %
        response.append(current_response)
        # AKA: net profit margin
    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@functions.route("/functions/Equity_to_Capital", methods=["GET"])
def get_Equity_to_Capital():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    capital = int(res["PAID CAPITAL (SAR)"])  # delete (SAR)?
    balance_sheet = res["BALANCE SHEET"]["ANNUALLY"]

    response = []

    for statement in balance_sheet:
        year = statement.split('-')[0]
        current_response = {}
        shareholders_equity = float(
            balance_sheet[statement]["Shareholders Equity"])
        # % # check the formula
        current_response["{}".format(year)] = shareholders_equity/capital * 100
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@functions.route("/functions/Debt_Ratio", methods=["GET"])
def get_Debt_Ratio():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    balance_sheet = res["BALANCE SHEET"]["ANNUALLY"]

    response = []

    for statement in balance_sheet:
        year = statement.split('-')[0]
        current_response = {}
        total_assets = float(
            balance_sheet[statement]["Total Assets"])
        shareholders_equity = float(
            balance_sheet[statement]["Shareholders Equity"])
        total_liabilities_and_shareholder_equity = float(
            balance_sheet[statement]["Total Liabilities and Shareholder Equity"])
        current_response["{}".format(year)] = (
            total_liabilities_and_shareholder_equity-shareholders_equity)/total_assets * 100  # %
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


@functions.route("/functions/Debt_to_Equity", methods=["GET"])
def get_Debt_to_Equity():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    balance_sheet = res["BALANCE SHEET"]["ANNUALLY"]

    response = []

    for statement in balance_sheet:
        year = statement.split('-')[0]
        current_response = {}
        shareholders_equity = float(
            balance_sheet[statement]["Shareholders Equity"])
        total_liabilities_and_shareholder_equity = float(
            balance_sheet[statement]["Total Liabilities and Shareholder Equity"])
        current_response["{}".format(year)] = (
            total_liabilities_and_shareholder_equity-shareholders_equity)/shareholders_equity * 100  # %
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


# Doesn't work, need to use 2 different statements [Mazen]
@functions.route("/functions/َQuick_Ratio", methods=["GET"])
def get_Quick_Ratio():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    balance_sheet = res["BALANCE SHEET"]["ANNUALLY"]
    cash_flow = res["CASH FLOW"]["ANNUALLY"]

    # Quick Ratio = (Total current assets – Inventory(already not included in the total) – Prepaid Expenses) / Current Liabilities
    # Quick Ratio = (cash_at_end + accounts_receivable) / Current Liabilities

    response = []

    for statement in cash_flow, balance_sheet:  # wrong

        year = statement.split('-')[0]
        current_response = {}
        cash_at_end = float(
            cash_flow[statement]["Cash at End of Period"])
        accounts_receivable = float(
            cash_flow[statement]["Accounts Receivable"])
        current_liabilities = float(
            balance_sheet[statement]["Current Liabilities"])
        current_response["{}".format(year)] = (
            cash_at_end + accounts_receivable)/current_liabilities
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


# Doesn't work, need to use 2 different statements [Mazen]
@functions.route("/functions/َCash_Ratio", methods=["GET"])
def get_Cash_Ratio():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    balance_sheet = res["BALANCE SHEET"]["ANNUALLY"]
    cash_flow = res["CASH FLOW"]["ANNUALLY"]

    response = []

    for statement in balance_sheet, cash_flow:  # wrong
        year = statement.split('-')[0]
        current_response = {}
        cash_at_end = float(
            cash_flow[statement]["Cash at End of Period"])
        current_liabilities = float(
            balance_sheet[statement]["Current Liabilities"])
        current_response["{}".format(year)] = cash_at_end/current_liabilities
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


# Doesn't work, need to use 2 different statements [Mazen]
@functions.route("/functions/ROA", methods=["GET"])
def get_ROA():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]
    balance_sheet = res["BALANCE SHEET"]["ANNUALLY"]

    response = []

    for statement in statement_of_income, balance_sheet:  # wrong
        year = statement.split('-')[0]
        current_response = {}
        total_assets = float(
            balance_sheet[statement]["Total Assets"])
        net_income = float(
            statement_of_income[statement]["Net Income"])
        current_response["{}".format(
            year)] = net_income/total_assets * 100  # %
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


# Doesn't work, need to use 2 different statements [Mazen]
@functions.route("/functions/ROTA", methods=["GET"])
def get_ROTA():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]
    balance_sheet = res["BALANCE SHEET"]["ANNUALLY"]

    response = []

    for statement in statement_of_income, balance_sheet:  # wrong
        year = statement.split('-')[0]
        current_response = {}
        total_assets = float(
            balance_sheet[statement]["Total Assets"])
        total_income = float(
            statement_of_income[statement]["Total Income"])
        admin_marketing_expenses = float(
            statement_of_income[statement]["Admin and Marketing Expenses"])
        depreciation = float(
            statement_of_income[statement]["Depreciation"])
        current_response["{}".format(year)] = (
            total_income-admin_marketing_expenses-depreciation)/total_assets * 100  # %
        response.append(current_response)
    # ROTA  vs. ROA >>(ROTA= EBIT/Total Assets : capital structure and different tax rates would not affect comparisons between different companies.)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


# Doesn't work, need to use 2 different statements [Mazen]
@functions.route("/functions/ROE", methods=["GET"])
def get_ROE():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]
    balance_sheet = res["BALANCE SHEET"]["ANNUALLY"]

    response = []

    for statement in statement_of_income, balance_sheet:  # wrong
        year = statement.split('-')[0]
        current_response = {}
        shareholders_equity = float(
            balance_sheet[statement]["Shareholders Equity"])
        net_income = float(
            statement_of_income[statement]["Net Income"])
        current_response["{}".format(
            year)] = net_income/shareholders_equity * 100  # %
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


# Doesn't work, need to use 2 different statements [Mazen]
@functions.route("/functions/Receivables_Turnover_Ratio", methods=["GET"])
def get_Receivables_Turnover_Ratio():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    cash_flow = res["CASH FLOW"]["ANNUALLY"]
    statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]

    response = []

    for statement in statement_of_income, cash_flow:  # wrong
        year = statement.split('-')[0]
        current_response = {}
        sales = float(
            statement_of_income[statement]["Sales"])
        accounts_receivable = float(
            cash_flow[statement]["Accounts Receivable"])  # Average Accounts Receivable?
        current_response["{}".format(year)] = sales / \
            accounts_receivable * 100  # %
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


# Doesn't work, need to use 2 different statements [Mazen]
@functions.route("/functions/Payable_Turnover_Ratio", methods=["GET"])
def get_Payable_Turnover_Ratio():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    cash_flow = res["CASH FLOW"]["ANNUALLY"]
    statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]

    response = []

    for statement in statement_of_income, cash_flow:  # wrong
        year = statement.split('-')[0]
        current_response = {}
        sales_cost = float(
            statement_of_income[statement]["Sales Cost"])
        accounts_payable = float(
            cash_flow[statement]["Accounts Payable"])  # Average Accounts Payable?
        current_response["{}".format(
            year)] = sales_cost/accounts_payable * 100  # %
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


# Doesn't work, need to use 2 different statements [Mazen]
@functions.route("/functions/Inventory_Turnover_Ratio", methods=["GET"])
def get_Inventory_Turnover_Ratio():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]
    balance_sheet = res["BALANCE SHEET"]["ANNUALLY"]

    response = []

    for statement in statement_of_income, balance_sheet:  # wrong
        year = statement.split('-')[0]
        current_response = {}
        inventory = float(
            balance_sheet[statement]["Inventory"])  # average inventory?
        sales_cost = float(
            statement_of_income[statement]["Sales Cost"])

        current_response["{}".format(year)] = sales_cost/inventory * 100  # %
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


# Doesn't work, need to use 2 different statements [Mazen]
@functions.route("/functions/Asset_Turnover_Ratio", methods=["GET"])
def get_Asset_Turnover_Ratio():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    balance_sheet = res["BALANCE SHEET"]["ANNUALLY"]
    statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]

    response = []

    for statement in statement_of_income, balance_sheet:  # wrong
        year = statement.split('-')[0]
        current_response = {}
        sales = float(
            statement_of_income[statement]["Sales"])
        total_assets = float(
            balance_sheet[statement]["Total Assets"])  # average asset?
        current_response["{}".format(year)] = sales/total_assets * 100  # %
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


# Doesn't work, need to use 2 different statements [Mazen]
@functions.route("/functions/Net_Fixed_Asset_Turnover_Ratio", methods=["GET"])
def get_Net_Fixed_Asset_Turnover_Ratio():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    balance_sheet = res["BALANCE SHEET"]["ANNUALLY"]
    statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]

    response = []

    for statement in statement_of_income, balance_sheet:  # wrong
        year = statement.split('-')[0]
        current_response = {}
        sales = float(
            statement_of_income[statement]["Sales"])
        fixed_assets = float(
            balance_sheet[statement]["Fixed Assets"])  # net fixed assets, is it equal to fixed_assets?  use avrage value end-beg ?
        current_response["{}".format(year)] = sales/fixed_assets * 100  # %
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


# Doesn't work, need to use 2 different statements [Mazen]
@functions.route("/functions/Equity_Turnover_Ratio", methods=["GET"])
def get_Equity_Turnover_Ratio():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    balance_sheet = res["BALANCE SHEET"]["ANNUALLY"]
    statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]

    response = []

    for statement in statement_of_income, balance_sheet:  # wrong
        year = statement.split('-')[0]
        current_response = {}
        sales = float(
            statement_of_income[statement]["Sales"])
        shareholders_equity = float(
            balance_sheet[statement]["Shareholders Equity"])
        current_response["{}".format(year)] = sales / \
            shareholders_equity * 100  # %
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


# Doesn't work, need to use 2 different statements [Mazen]
@functions.route("/functions/Days_in_Inventory", methods=["GET"])
def get_Days_in_Inventory():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]
    balance_sheet = res["BALANCE SHEET"]["ANNUALLY"]

    response = []

    for statement in statement_of_income, balance_sheet:  # wrong
        year = statement.split('-')[0]
        current_response = {}
        inventory = float(
            balance_sheet[statement]["Inventory"])  # use average value?
        sales_cost = float(
            statement_of_income[statement]["Sales Cost"])

        # make it more robust 365 vs. 366 #leap_year?
        current_response["{}".format(year)] = inventory/sales_cost * 365
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


# Doesn't work, need to use 2 different statements [Mazen]
@functions.route("/functions/Days_Payable_Outstanding", methods=["GET"])
def get_Days_Payable_Outstanding():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    cash_flow = res["CASH FLOW"]["ANNUALLY"]
    statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]

    response = []

    for statement in statement_of_income, cash_flow:  # wrong
        year = statement.split('-')[0]
        current_response = {}
        sales_cost = float(
            statement_of_income[statement]["Sales Cost"])
        accounts_payable = float(
            cash_flow[statement]["Accounts Payable"])  # Average Accounts Payable?
        # make it more robust 365 vs. 366 #leap_year?
        current_response["{}".format(year)] = accounts_payable/sales_cost * 365
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


# Doesn't work, need to use 2 different statements [Mazen]
@functions.route("/functions/Days_Sales_Outstanding", methods=["GET"])
def get_Days_Sales_Outstanding():
    tadawul_db = client["Tadawul"]
    mycol = tadawul_db["Energy"]
    res = mycol.find_one({"_id": 4200})

    cash_flow = res["CASH FLOW"]["ANNUALLY"]
    statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]

    response = []

    for statement in statement_of_income, cash_flow:  # wrong
        year = statement.split('-')[0]
        current_response = {}
        sales = float(
            statement_of_income[statement]["Sales"])
        accounts_receivable = float(
            cash_flow[statement]["Accounts Receivable"])  # Average Accounts Receivable?
        # make it more robust 365 vs. 366 #leap_year ?
        current_response["{}".format(year)] = accounts_receivable/sales * 365
        response.append(current_response)

    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result


# comments  for later
# def comments():

    # FCF + its reltated ratios
    # CFO
    # Working Capital

    # Plowback ratio (retention)
    # retained earnings
    # Cash Conversion Cycle

    # Bank-Related Ratios: (Page #6)
    # https://ecommons.luc.edu/cgi/viewcontent.cgi?article=1039&context=business_facpubs

    # file:///C:/Users/96656/Downloads/981-Article%20Text-529-0-10-19700101.pdf
    # The ratio of assets financed through borrowed capital
    # The financial dependency ratio
    # The financial leverage
    # The golden rule of the balance sheet ratio
    # The working capital ratio
    # The permanent solvency ratio
    # The equity concentration ratio

    # Cash Dividend Payout Ratio = Cash Dividends / (Cash Flow from Operations – Capital Expenditures – Preferred Dividend Paid)
    # Interest Coverage Ratio = EBITDA / Interest Expense
    # @functions.route("/functions/Current_Asset_Turnover", methods=["GET"])
    # def get_Current_Asset_Turnover():
    #     tadawul_db = client["Tadawul_v2"]
    #     mycol = tadawul_db["Industrials"]
    #     res = mycol.find_one({"_id": "4031"})

    #     balance_sheet = res["BALANCE SHEET"]["ANNUALLY"]
    #     statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]
    #     response = []

    #     for statement in balance_sheet,statement_of_income: ########
    #         year = statement.split('-')[0]
    #         current_response = {}
    #         current_assets = float(
    #             balance_sheet[statement]["Current Assets"])
    #         inventory = float(
    #             balance_sheet[statement]["Inventory"])
    #         total_assets = float(
    #             balance_sheet[statement]["Total Assets"])
    #         current_response["{}".format(year)] = (current_assets+inventory)/total_assets  #include inventory?  Avg values (beg+end)/2 ?
    #         response.append(current_response)

    #     result = jsonify(response)
    #     result.headers.add('Access-Control-Allow-Origin', '*')

    #     return result

    # @functions.route("/functions/Total_Asset_Turnover", methods=["GET"])
    # def get_Total_Asset_Turnover():
    #     tadawul_db = client["Tadawul_v2"]
    #     mycol = tadawul_db["Industrials"]
    #     res = mycol.find_one({"_id": "4031"})

    #     balance_sheet = res["BALANCE SHEET"]["ANNUALLY"]
    #     statement_of_income = res["STATEMENT OF INCOME"]["ANNUALLY"]

    #     response = []

    #     for statement in balance_sheet,statement_of_income: ########
    #         year = statement.split('-')[0]
    #         current_response = {}
    #         total_income = float(
    #             statement_of_income[statement]["Total Income"])
    #         total_assets = float(
    #             balance_sheet[statement]["Total Assets"])
    #         current_response["{}".format(year)] = total_income/total_assets  #Avg values (beg+end)/2 ?
    #         response.append(current_response)

    #     result = jsonify(response)
    #     result.headers.add('Access-Control-Allow-Origin', '*')

    #     return result
