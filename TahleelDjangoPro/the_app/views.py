from django.shortcuts import render
from django.http import JsonResponse,request
from .models import client


# Create your views here.

def get_market_cap(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    price = float(res["PRICE"])
    shares = int(res["ISSUED SHARES"])

    response = {}
    response["MarketCap"] = (price * shares)

    result = JsonResponse(response)

    return result

def get_EPS(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

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

    result = JsonResponse(response)
    # # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Operating_EPS(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    statement_of_income = res["STATEMENT OF INCOME"]
    shares = int(res["ISSUED SHARES"])

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            total_income = float(
                statement_of_income[period][statement]["Total Income"])
            admin_marketing_expenses = float(
                statement_of_income[period][statement]["Admin and Marketing Expenses"])
            depreciation = float(
                statement_of_income[period][statement]["Depreciation"])
            current_response["{}".format(year)] = (
                total_income-admin_marketing_expenses-depreciation)/shares
            response[period].append(current_response)

    result = JsonResponse(response)
    # # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_EBIT(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    statement_of_income = res["STATEMENT OF INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            total_income = float(
                statement_of_income[period][statement]["Total Income"])
            admin_marketing_expenses = float(
                statement_of_income[period][statement]["Admin and Marketing Expenses"])
            depreciation = float(
                statement_of_income[period][statement]["Depreciation"])
            current_response["{}".format(
                year)] = total_income-admin_marketing_expenses-depreciation
            response[period].append(current_response)

    result = JsonResponse(response)
    # # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_EBITDA(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    statement_of_income = res["STATEMENT OF INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            total_income = float(
                statement_of_income[period][statement]["Total Income"])
            admin_marketing_expenses = float(
                statement_of_income[period][statement]["Admin and Marketing Expenses"])
            current_response["{}".format(
                year)] = total_income-admin_marketing_expenses
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Non_Current_Assets(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    balance_sheet = res["BALANCE SHEET"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}
            total_assets = float(
                balance_sheet[period][statement]["Total Assets"])
            current_assets = float(
                balance_sheet[period][statement]["Current Assets"])
            inventory = float(
                balance_sheet[period][statement]["Inventory"])
            current_response["{}".format(
                year)] = total_assets - current_assets - inventory
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Current_Assets(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    balance_sheet = res["BALANCE SHEET"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}
            current_assets = float(
                balance_sheet[period][statement]["Current Assets"])
            inventory = float(
                balance_sheet[period][statement]["Inventory"])
            current_response["{}".format(
                year)] = current_assets + inventory
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Total_Liabilities(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    balance_sheet = res["BALANCE SHEET"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}
            shareholders_equity = float(
                balance_sheet[period][statement]["Shareholders Equity"])
            total_liabilities_and_shareholder_equity = float(
                balance_sheet[period][statement]["Total Liabilities and Shareholder Equity"])
            current_response["{}".format(
                year)] = total_liabilities_and_shareholder_equity - shareholders_equity
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Cash_Change(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    cash_flow = res["CASH FLOW"]

    response = {}

    for period in cash_flow:
        response['{}'.format(period)] = []
        for statement in cash_flow[period]:
            year = statement.split('-')[0]
            current_response = {}
            cash_at_end = float(
                cash_flow[period][statement]["Cash at End of Period"])
            cash_at_begining = float(
                cash_flow[period][statement]["Cash at Begining of Period"])
            current_response["{}".format(
                year)] = cash_at_end - cash_at_begining
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Book_Value(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    balance_sheet = res["BALANCE SHEET"]
    shares = int(res["ISSUED SHARES"])

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}
            shareholders_equity = float(
                balance_sheet[period][statement]["Shareholders Equity"])
            current_response["{}".format(
                year)] = shareholders_equity/shares
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Dividends_Per_Share(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    statement_of_income = res["STATEMENT OF INCOME"]
    shares = int(res["ISSUED SHARES"])

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            cash_dividends = float(
                statement_of_income[period][statement]["Cash Dividends"])
            current_response["{}".format(
                year)] = abs(cash_dividends/shares)
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_PE(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    statement_of_income = res["STATEMENT OF INCOME"]
    shares = int(res["ISSUED SHARES"])
    price = float(res["PRICE"])

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            net_income = float(
                statement_of_income[period][statement]["Net Income"])
            current_response["{}".format(
                year)] = price / (net_income/shares)
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Operating_Profit_Multiple(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    statement_of_income = res["STATEMENT OF INCOME"]
    shares = int(res["ISSUED SHARES"])
    price = float(res["PRICE"])

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            total_income = float(
                statement_of_income[period][statement]["Total Income"])
            admin_marketing_expenses = float(
                statement_of_income[period][statement]["Admin and Marketing Expenses"])
            depreciation = float(
                statement_of_income[period][statement]["Depreciation"])
            current_response["{}".format(
                year)] = price/(
                (total_income-admin_marketing_expenses-depreciation)/shares)
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_PB(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    shares = int(res["ISSUED SHARES"])
    price = float(res["PRICE"])
    balance_sheet = res["BALANCE SHEET"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}
            shareholders_equity = float(
                balance_sheet[period][statement]["Shareholders Equity"])
            current_response["{}".format(
                year)] = price / (shareholders_equity/shares)
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_PS(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    shares = int(res["ISSUED SHARES"])
    price = float(res["PRICE"])
    statement_of_income = res["STATEMENT OF INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            sales = float(
                statement_of_income[period][statement]["Sales"])
            current_response["{}".format(
                year)] = price / (sales/shares)
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Current_Ratio(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    balance_sheet = res["BALANCE SHEET"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}

            current_assets = float(
                balance_sheet[period][statement]["Current Assets"])
            inventory = float(
                balance_sheet[period][statement]["Inventory"])
            current_liabilities = float(
                balance_sheet[period][statement]["Current Liabilities"])

            current_response["{}".format(
                year)] = (
                current_assets+inventory)/current_liabilities
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Dividend_Yield(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    shares = int(res["ISSUED SHARES"])
    price = float(res["PRICE"])
    statement_of_income = res["STATEMENT OF INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}

            cash_dividends = float(
                statement_of_income[period][statement]["Cash Dividends"])

            current_response["{}".format(
                year)] = abs(cash_dividends/shares)/price * 100
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Payout_Ratio(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

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

            cash_dividends = float(
                statement_of_income[period][statement]["Cash Dividends"])
            net_income = float(
                statement_of_income[period][statement]["Net Income"])
            current_response["{}".format(
                year)] = abs(cash_dividends/shares) / (net_income/shares) * 100
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Operating_Profit_Margin(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    statement_of_income = res["STATEMENT OF INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}

            total_income = float(
                statement_of_income[period][statement]["Total Income"])
            admin_marketing_expenses = float(
                statement_of_income[period][statement]["Admin and Marketing Expenses"])
            depreciation = float(
                statement_of_income[period][statement]["Depreciation"])
            sales = float(
                statement_of_income[period][statement]["Sales"])

            current_response["{}".format(
                year)] = (
                total_income-admin_marketing_expenses-depreciation)/sales * 100
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Net_Margin(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    statement_of_income = res["STATEMENT OF INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}

            net_income = float(
                statement_of_income[period][statement]["Net Income"])
            sales = float(
                statement_of_income[period][statement]["Sales"])

            current_response["{}".format(
                year)] = abs(net_income/sales) * 100
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Equity_to_Capital(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    capital = int(res["PAID CAPITAL (SAR)"])
    balance_sheet = res["BALANCE SHEET"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}

            shareholders_equity = float(
                balance_sheet[period][statement]["Shareholders Equity"])

            current_response["{}".format(
                year)] = shareholders_equity/capital * 100
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Debt_Ratio(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    balance_sheet = res["BALANCE SHEET"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}

            total_assets = float(
                balance_sheet[period][statement]["Total Assets"])
            shareholders_equity = float(
                balance_sheet[period][statement]["Shareholders Equity"])
            total_liabilities_and_shareholder_equity = float(
                balance_sheet[period][statement]["Total Liabilities and Shareholder Equity"])

            current_response["{}".format(
                year)] = (
                total_liabilities_and_shareholder_equity-shareholders_equity)/total_assets * 100
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Debt_to_Equity(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    balance_sheet = res["BALANCE SHEET"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}

            shareholders_equity = float(
                balance_sheet[period][statement]["Shareholders Equity"])
            total_liabilities_and_shareholder_equity = float(
                balance_sheet[period][statement]["Total Liabilities and Shareholder Equity"])

            current_response["{}".format(
                year)] = (
                total_liabilities_and_shareholder_equity-shareholders_equity)/shareholders_equity * 100
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Quick_Ratio(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    balance_sheet = res["BALANCE SHEET"]
    cash_flow = res["CASH FLOW"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}

            # CASH FLOW STATEMENT
            cash_at_end = float(
                cash_flow[period][statement]["Cash at End of Period"])
            accounts_receivable = float(
                cash_flow[period][statement]["Accounts Receivable"])

            # BALANCE SHEET
            current_liabilities = float(
                balance_sheet[period][statement]["Current Liabilities"])

            current_response["{}".format(
                year)] = (
                cash_at_end + accounts_receivable)/current_liabilities
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Cash_Ratio(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    balance_sheet = res["BALANCE SHEET"]
    cash_flow = res["CASH FLOW"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}

            # CASH FLOW STATEMENT
            cash_at_end = float(
                cash_flow[period][statement]["Cash at End of Period"])

            # BALANCE SHEET
            current_liabilities = float(
                balance_sheet[period][statement]["Current Liabilities"])

            current_response["{}".format(
                year)] = cash_at_end/current_liabilities
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_ROA(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    balance_sheet = res["BALANCE SHEET"]
    statement_of_income = res["STATEMENT OF INCOME"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}

            # STATEMENT OF INCOME
            net_income = float(
                statement_of_income[period][statement]["Net Income"])

            # BALANCE SHEET
            total_assets = float(
                balance_sheet[period][statement]["Total Assets"])

            current_response["{}".format(
                year)] = net_income/total_assets * 100
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_ROTA(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    balance_sheet = res["BALANCE SHEET"]
    statement_of_income = res["STATEMENT OF INCOME"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}

            # STATEMENT OF INCOME
            total_income = float(
                statement_of_income[period][statement]["Total Income"])
            admin_marketing_expenses = float(
                statement_of_income[period][statement]["Admin and Marketing Expenses"])
            depreciation = float(
                statement_of_income[period][statement]["Depreciation"])

            # BALANCE SHEET
            total_assets = float(
                balance_sheet[period][statement]["Total Assets"])

            current_response["{}".format(
                year)] = (
                total_income-admin_marketing_expenses-depreciation)/total_assets * 100
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_ROE(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    balance_sheet = res["BALANCE SHEET"]
    statement_of_income = res["STATEMENT OF INCOME"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('-')[0]
            current_response = {}

            # STATEMENT OF INCOME
            net_income = float(
                statement_of_income[period][statement]["Net Income"])

            # BALANCE SHEET
            shareholders_equity = float(
                balance_sheet[period][statement]["Shareholders Equity"])

            current_response["{}".format(
                year)] = net_income/shareholders_equity * 100
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result





def get_Asset_Turnover_Ratio(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    balance_sheet = res["BALANCE SHEET"]
    statement_of_income = res["STATEMENT OF INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}

            # STATEMENT OF INCOME
            sales = float(
                statement_of_income[period][statement]["Sales"])

            # BALANCE SHEET
            total_assets = float(
                balance_sheet[period][statement]["Total Assets"])

            current_response["{}".format(
                year)] = sales/total_assets
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Net_Fixed_Asset_Turnover_Ratio(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    balance_sheet = res["BALANCE SHEET"]
    statement_of_income = res["STATEMENT OF INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}

            # STATEMENT OF INCOME
            sales = float(
                statement_of_income[period][statement]["Sales"])

            # BALANCE SHEET
            fixed_assets = float(
                balance_sheet[period][statement]["Fixed Assets"])

            current_response["{}".format(
                year)] = sales/fixed_assets
            response[period].append(current_response)

    result = JsonResponse(response)
    # # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Equity_Turnover_Ratio(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    balance_sheet = res["BALANCE SHEET"]
    statement_of_income = res["STATEMENT OF INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}

            # STATEMENT OF INCOME
            sales = float(
                statement_of_income[period][statement]["Sales"])

            # BALANCE SHEET
            shareholders_equity = float(
                balance_sheet[period][statement]["Shareholders Equity"])

            current_response["{}".format(
                year)] = sales / shareholders_equity
            response[period].append(current_response)

    result = JsonResponse(response)
    # # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Receivables_Turnover_Ratio(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    cash_flow = res["CASH FLOW"]
    statement_of_income = res["STATEMENT OF INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}

            # STATEMENT OF INCOME
            sales = float(
                statement_of_income[period][statement]["Sales"])

            # CASH FLOW
            accounts_receivable = float(
                cash_flow[period][statement]["Accounts Receivable"])

            current_response["{}".format(
                year)] = sales / accounts_receivable
            response[period].append(current_response)

    result = JsonResponse(response)
    # # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Payable_Turnover_Ratio(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    cash_flow = res["CASH FLOW"]
    statement_of_income = res["STATEMENT OF INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}

            # STATEMENT OF INCOME
            sales_cost = float(
                statement_of_income[period][statement]["Sales Cost"])

            # CASH FLOW
            accounts_payable = float(
                cash_flow[period][statement]["Accounts Payable"])

            current_response["{}".format(
                year)] = sales_cost/accounts_payable
            response[period].append(current_response)

    result = JsonResponse(response)
    # # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Inventory_Turnover_Ratio(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    balance_sheet = res["BALANCE SHEET"]
    statement_of_income = res["STATEMENT OF INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}

            # STATEMENT OF INCOME
            sales_cost = float(
                statement_of_income[period][statement]["Sales Cost"])

            # BALANCE SHEET
            inventory = float(
                balance_sheet[period][statement]["Inventory"])

            current_response["{}".format(
                year)] = sales_cost/inventory
            response[period].append(current_response)

    result = JsonResponse(response)
    # # result.headers.add('Access-Control-Allow-Origin', '*')

    return result




def get_Days_Inventory_Outstanding(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    balance_sheet = res["BALANCE SHEET"]
    statement_of_income = res["STATEMENT OF INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            if statement_of_income[period][statement] == {}:
                break

            # STATEMENT OF INCOME
            sales_cost = float(
                statement_of_income[period][statement]["Sales Cost"])

            # BALANCE SHEET
            inventory = float(
                balance_sheet[period][statement]["Inventory"])

            current_response["{}".format(
                year)] = abs(inventory/sales_cost * 365)
            response[period].append(current_response)

    result = JsonResponse(response)
    # # result.headers.add('Access-Control-Allow-Origin', '*')

    return result


def get_Days_Sales_Outstanding(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    cash_flow = res["CASH FLOW"]
    statement_of_income = res["STATEMENT OF INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            if statement_of_income[period][statement] == {}:
                break

            # STATEMENT OF INCOME
            sales = float(
                statement_of_income[period][statement]["Sales"])

            # CASH FLOW
            accounts_receivable = float(
                cash_flow[period][statement]["Accounts Receivable"])

            current_response["{}".format(
                year)] = abs(accounts_receivable/sales * 365)
            response[period].append(current_response)

    result = JsonResponse(response)
    # # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Days_Payable_Outstanding(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    cash_flow = res["CASH FLOW"]
    statement_of_income = res["STATEMENT OF INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            if statement_of_income[period][statement] == {}:
                break

            # STATEMENT OF INCOME
            sales_cost = float(
                statement_of_income[period][statement]["Sales Cost"])

            # CASH FLOW
            accounts_payable = float(
                cash_flow[period][statement]["Accounts Payable"])

            current_response["{}".format(
                year)] = abs(accounts_payable/sales_cost * 365)
            response[period].append(current_response)

    result = JsonResponse(response)
    # # result.headers.add('Access-Control-Allow-Origin', '*')

    return result


## here we used 3 financial statements (check it with Mazen)

def get_Operating_Cycle(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    cash_flow = res["CASH FLOW"]
    statement_of_income = res["STATEMENT OF INCOME"]
    balance_sheet = res["BALANCE SHEET"]


    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            if statement_of_income[period][statement] == {}:
                break

            # STATEMENT OF INCOME
            sales = float(
                statement_of_income[period][statement]["Sales"])
            sales_cost = float(
                statement_of_income[period][statement]["Sales Cost"])
            
            # BALANCE SHEET
            inventory = float(
                balance_sheet[period][statement]["Inventory"])

            # CASH FLOW
            accounts_receivable = float(
                cash_flow[period][statement]["Accounts Receivable"])

            current_response["{}".format(
                year)] = abs(accounts_receivable/sales * 365) + abs(inventory/sales_cost * 365)
            response[period].append(current_response)

    result = JsonResponse(response)
    # # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



## here we used 3 financial statements (check it with Mazen)

def get_Cash_Conversion_Cycle(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"_id": int(ticker)})

    cash_flow = res["CASH FLOW"]
    statement_of_income = res["STATEMENT OF INCOME"]
    balance_sheet = res["BALANCE SHEET"]
    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('-')[0]
            current_response = {}
            if statement_of_income[period][statement] == {}:
                break

            # STATEMENT OF INCOME
            sales = float(
                statement_of_income[period][statement]["Sales"])
            sales_cost = float(
                statement_of_income[period][statement]["Sales Cost"])
            
            # BALANCE SHEET
            inventory = float(
                balance_sheet[period][statement]["Inventory"])

            # CASH FLOW
            accounts_receivable = float(
                cash_flow[period][statement]["Accounts Receivable"])
            accounts_payable = float(
                cash_flow[period][statement]["Accounts Payable"])

            current_response["{}".format(
                year)] = (abs(accounts_receivable/sales * 365) + abs(inventory/sales_cost * 365)) - abs(accounts_payable/sales_cost * 365)
            response[period].append(current_response)

    result = JsonResponse(response)
    # # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



# comments  for later
# def comments(request,sectorVal,tickerVal):

    # Plowback ratio (retention)
    # retained earnings

    # Cash Dividend Payout Ratio = Cash Dividends / (Cash Flow from Operations – Capital Expenditures – Preferred Dividend Paid)
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
    # The golden rule of the balance sheet ratio
    # The working capital ratio
    # The permanent solvency ratio
    # The equity concentration ratio