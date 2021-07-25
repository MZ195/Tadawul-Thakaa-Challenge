from django.shortcuts import render,redirect
from django.http import JsonResponse,request
from .models import client


# Create your views here.
# def cleanSector(sector):
#     print("intered cleanSector"]
#     print(sector)
#     tadawul_db = client["Tadawul_v3"]
#     mycol = tadawul_db[sector]
#     res = list(mycol.find({}))
#     listOfCompanies=[]
#     for company in res:
#         company["id"] = company["TICKER"]
#         del company["TICKER"]
#         company["AUTHORIZED_CAPITAL"] = company["AUTHORIZED_CAPITAL (SAR)"]
#         del company["AUTHORIZED_CAPITAL (SAR)"]
#         company["ISSUED_SHARES"] = company["ISSUED_SHARES"]
#         del company["ISSUED_SHARES"]
#         company["PAID_CAPITAL"] = company["PAID_CAPITAL (SAR)"]
#         del company["PAID_CAPITAL (SAR)"]
#         listOfCompanies.append(company)
#     return listOfCompanies
def returnAllCompanies(Communication_Services_Sector,Consumer_Discretionary_Sector,Consumer_Staples_Sector,
    Energy_Sector,Financials_Sector,Health_Care_Sector,Industrials_Sector,Information_Technology_Sector,Materials_Sector,
    Real_Estate_Sector,Utilities_Sector):
    allCompanies=[]
    for com in Communication_Services_Sector:
        allCompanies.append(com)
    for com in Consumer_Discretionary_Sector:
        allCompanies.append(com)
    for com in Consumer_Staples_Sector:
        allCompanies.append(com)
    for com in Energy_Sector:
        allCompanies.append(com)
    for com in Financials_Sector:
        allCompanies.append(com)
    for com in Health_Care_Sector:
        allCompanies.append(com)
    for com in Industrials_Sector:
        allCompanies.append(com)
    for com in Information_Technology_Sector:
        allCompanies.append(com)
    for com in Materials_Sector:
        allCompanies.append(com)
    for com in Real_Estate_Sector:
        allCompanies.append(com)
    for com in Utilities_Sector:
        allCompanies.append(com)
    return allCompanies
def sortByPrice(allCompanies):
    n = len(allCompanies)
    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            # company["PRICE"]
            if allCompanies[j]["PRICE"] < allCompanies[j + 1]["PRICE"] :
                allCompanies[j], allCompanies[j + 1] = allCompanies[j + 1], allCompanies[j]
    return allCompanies
def makeSectorList(sector):
    tadawul_db = client["Tadawul_v3"]
    mycol=tadawul_db[sector]
    theSectorList = list(mycol.find({}))
    return theSectorList
def allComs():
    Communication_Services_Sector = makeSectorList("Communication_Services")
    Consumer_Discretionary_Sector = makeSectorList("Consumer_Discretionary")
    Consumer_Staples_Sector = makeSectorList("Consumer_Staples")
    Energy_Sector = makeSectorList("Energy")
    Financials_Sector = makeSectorList("Financials")
    Health_Care_Sector = makeSectorList("Health_Care")
    Industrials_Sector = makeSectorList("Industrials")
    Information_Technology_Sector = makeSectorList("Information_Technology")
    Materials_Sector = makeSectorList("Materials")
    Real_Estate_Sector = makeSectorList("Real_Estate")
    Utilities_Sector = makeSectorList("Utilities")
    allCompanies=returnAllCompanies(Communication_Services_Sector,Consumer_Discretionary_Sector,Consumer_Staples_Sector,
    Energy_Sector,Financials_Sector,Health_Care_Sector,Industrials_Sector,Information_Technology_Sector,Materials_Sector,
    Real_Estate_Sector,Utilities_Sector)
    return sortByPrice(allCompanies)
def main(request):
    return redirect('/sector/All')

def sector(request,sectorVal):
    tadawul_db = client["Tadawul_v3"]
    if sectorVal == "All":
        all=allComs()
        context ={"allCompanies": all}
        return render(request, 'main.html',context)
    else:
        all=makeSectorList(sectorVal)
        context ={"allCompanies": all}
        return render(request, 'main.html',context)
def get_market_cap(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    price = float(res["PRICE"])
    shares = int(res["ISSUED_SHARES"])

    response = {}
    response["MarketCap"] = (price * shares)

    result = JsonResponse(response)

    return result

def get_EPS(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    shares = int(res["ISSUED_SHARES"])
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('_')[0]
            current_response = {}
            net_income = float(
                statement_of_income[period][statement]["Net_Income"])
            current_response["{}".format(year)] = net_income/shares
            response[period].append(current_response)

    result = JsonResponse(response)
    # # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Operating_EPS(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    statement_of_income = res["STATEMENT_OF_INCOME"]
    shares = int(res["ISSUED_SHARES"])

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('_')[0]
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

    result = JsonResponse(response)
    # # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_EBIT(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('_')[0]
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

    result = JsonResponse(response)
    # # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_EBITDA(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('_')[0]
            current_response = {}
            total_income = float(
                statement_of_income[period][statement]["Total_Income"])
            admin_marketing_expenses = float(
                statement_of_income[period][statement]["Admin_and_Marketing_Expenses"])
            current_response["{}".format(
                year)] = total_income-admin_marketing_expenses
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Non_Current_Assets(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('_')[0]
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

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Current_Assets(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('_')[0]
            current_response = {}
            current_assets = float(
                balance_sheet[period][statement]["Current_Assets"])
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

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('_')[0]
            current_response = {}
            shareholders_equity = float(
                balance_sheet[period][statement]["Shareholders_Equity"])
            total_liabilities_and_shareholder_equity = float(
                balance_sheet[period][statement]["Total_Liabilities_and_Shareholder_Equity"])
            current_response["{}".format(
                year)] = total_liabilities_and_shareholder_equity - shareholders_equity
            response[period].append(current_response)

    result = JsonResponse(response)

    return result



def get_Cash_Change(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    cash_flow = res["CASH_FLOW"]

    response = {}

    for period in cash_flow:
        response['{}'.format(period)] = []
        for statement in cash_flow[period]:
            year = statement.split('_')[0]
            current_response = {}
            cash_at_end = float(
                cash_flow[period][statement]["Cash_at_End_of_Period"])
            cash_at_begining = float(
                cash_flow[period][statement]["Cash_at_Begining_of_Period"])
            current_response["{}".format(
                year)] = cash_at_end - cash_at_begining
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Book_Value(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]
    shares = int(res["ISSUED_SHARES"])

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('_')[0]
            current_response = {}
            shareholders_equity = float(
                balance_sheet[period][statement]["Shareholders_Equity"])
            current_response["{}".format(
                year)] = shareholders_equity/shares
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Dividends_Per_Share(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    statement_of_income = res["STATEMENT_OF_INCOME"]
    shares = int(res["ISSUED_SHARES"])

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('_')[0]
            current_response = {}
            cash_dividends = float(
                statement_of_income[period][statement]["Cash_Dividends"])
            current_response["{}".format(
                year)] = abs(cash_dividends/shares)
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_PE(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

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
            year = statement.split('_')[0]
            current_response = {}
            net_income = float(
                statement_of_income[period][statement]["Net_Income"])
            current_response["{}".format(
                year)] = price / (net_income/shares)
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Operating_Profit_Multiple(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

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
            year = statement.split('_')[0]
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

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_PB(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

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
            year = statement.split('_')[0]
            current_response = {}
            shareholders_equity = float(
                balance_sheet[period][statement]["Shareholders_Equity"])
            current_response["{}".format(
                year)] = price / (shareholders_equity/shares)
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_PS(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

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
            year = statement.split('_')[0]
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

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('_')[0]
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

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Dividend_Yield(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

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
            year = statement.split('_')[0]
            current_response = {}

            cash_dividends = float(
                statement_of_income[period][statement]["Cash_Dividends"])

            current_response["{}".format(
                year)] = abs(cash_dividends/shares)/price * 100
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Payout_Ratio(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    shares = int(res["ISSUED_SHARES"])
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('_')[0]
            current_response = {}

            cash_dividends = float(
                statement_of_income[period][statement]["Cash_Dividends"])
            net_income = float(
                statement_of_income[period][statement]["Net_Income"])
            current_response["{}".format(
                year)] = abs(cash_dividends/shares) / (net_income/shares) * 100
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Operating_Profit_Margin(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('_')[0]
            current_response = {}

            total_income = float(
                statement_of_income[period][statement]["Total_Income"])
            admin_marketing_expenses = float(
                statement_of_income[period][statement]["Admin_and_Marketing_Expenses"])
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

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('_')[0]
            current_response = {}

            net_income = float(
                statement_of_income[period][statement]["Net_Income"])
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

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    capital = int(res["PAID_CAPITAL (SAR)"])
    balance_sheet = res["BALANCE_SHEET"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('_')[0]
            current_response = {}

            shareholders_equity = float(
                balance_sheet[period][statement]["Shareholders_Equity"])

            current_response["{}".format(
                year)] = shareholders_equity/capital * 100
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Debt_Ratio(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('_')[0]
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

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Debt_to_Equity(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('_')[0]
            current_response = {}

            shareholders_equity = float(
                balance_sheet[period][statement]["Shareholders_Equity"])
            total_liabilities_and_shareholder_equity = float(
                balance_sheet[period][statement]["Total_Liabilities_and_Shareholder_Equity"])

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

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]
    cash_flow = res["CASH_FLOW"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('_')[0]
            current_response = {}

            # CASH FLOW STATEMENT
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

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Cash_Ratio(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]
    cash_flow = res["CASH_FLOW"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('_')[0]
            current_response = {}

            # CASH FLOW STATEMENT
            cash_at_end = float(
                cash_flow[period][statement]["Cash_at_End_of_Period"])

            # BALANCE_SHEET
            current_liabilities = float(
                balance_sheet[period][statement]["Current_Liabilities"])

            current_response["{}".format(
                year)] = cash_at_end/current_liabilities
            response[period].append(current_response)

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_ROA(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('_')[0]
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

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_ROTA(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('_')[0]
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

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_ROE(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in balance_sheet:
        response['{}'.format(period)] = []
        for statement in balance_sheet[period]:
            year = statement.split('_')[0]
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

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result





def get_Asset_Turnover_Ratio(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('_')[0]
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

    result = JsonResponse(response)
    # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Net_Fixed_Asset_Turnover_Ratio(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('_')[0]
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

    result = JsonResponse(response)
    # # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Equity_Turnover_Ratio(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('_')[0]
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

    result = JsonResponse(response)
    # # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Receivables_Turnover_Ratio(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    cash_flow = res["CASH_FLOW"]
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('_')[0]
            current_response = {}

            
            sales = float(
                statement_of_income[period][statement]["Sales"])

            # CASH FLOW
            accounts_receivable = float(
                cash_flow[period][statement]["Accounts_Receivable"])

            current_response["{}".format(
                year)] = sales / accounts_receivable
            response[period].append(current_response)

    result = JsonResponse(response)
    # # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Payable_Turnover_Ratio(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    cash_flow = res["CASH_FLOW"]
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('_')[0]
            current_response = {}

            # STATEMENT OF INCOME
            sales_cost = float(
                statement_of_income[period][statement]["Sales_Cost"])

            # CASH FLOW
            accounts_payable = float(
                cash_flow[period][statement]["Accounts_Payable"])

            current_response["{}".format(
                year)] = sales_cost/accounts_payable
            response[period].append(current_response)

    result = JsonResponse(response)
    # # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Inventory_Turnover_Ratio(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('_')[0]
            current_response = {}

            # STATEMENT OF INCOME
            sales_cost = float(
                statement_of_income[period][statement]["Sales_Cost"])

            # BALANCE_SHEET
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

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    balance_sheet = res["BALANCE_SHEET"]
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('_')[0]
            current_response = {}
            if statement_of_income[period][statement] == {}:
                break

            # STATEMENT OF INCOME
            sales_cost = float(
                statement_of_income[period][statement]["Sales_Cost"])

            # BALANCE_SHEET
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

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    cash_flow = res["CASH_FLOW"]
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('_')[0]
            current_response = {}
            if statement_of_income[period][statement] == {}:
                break

            # STATEMENT OF INCOME
            sales = float(
                statement_of_income[period][statement]["Sales"])

            # CASH FLOW
            accounts_receivable = float(
                cash_flow[period][statement]["Accounts_Receivable"])

            current_response["{}".format(
                year)] = abs(accounts_receivable/sales * 365)
            response[period].append(current_response)

    result = JsonResponse(response)
    # # result.headers.add('Access-Control-Allow-Origin', '*')

    return result



def get_Days_Payable_Outstanding(request,sectorVal,tickerVal):
    sector = sectorVal
    ticker = tickerVal

    tadawul_db = client["Tadawul_v3"]
    mycol = tadawul_db[sector]
    res = mycol.find_one({"TICKER": int(ticker)})

    cash_flow = res["CASH_FLOW"]
    statement_of_income = res["STATEMENT_OF_INCOME"]

    response = {}

    for period in statement_of_income:
        response['{}'.format(period)] = []
        for statement in statement_of_income[period]:
            year = statement.split('_')[0]
            current_response = {}
            if statement_of_income[period][statement] == {}:
                break

            # STATEMENT OF INCOME
            sales_cost = float(
                statement_of_income[period][statement]["Sales_Cost"])

            # CASH FLOW
            accounts_payable = float(
                cash_flow[period][statement]["Accounts_Payable"])

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
            year = statement.split('_')[0]
            current_response = {}
            if statement_of_income[period][statement] == {}:
                break

            # STATEMENT OF INCOME
            sales = float(
                statement_of_income[period][statement]["Sales"])
            sales_cost = float(
                statement_of_income[period][statement]["Sales_Cost"])
            
            # BALANCE_SHEET
            inventory = float(
                balance_sheet[period][statement]["Inventory"])

            # CASH FLOW
            accounts_receivable = float(
                cash_flow[period][statement]["Accounts_Receivable"])

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
            year = statement.split('_')[0]
            current_response = {}
            if statement_of_income[period][statement] == {}:
                break

            # STATEMENT OF INCOME
            sales = float(
                statement_of_income[period][statement]["Sales"])
            sales_cost = float(
                statement_of_income[period][statement]["Sales_Cost"])
            
            # BALANCE_SHEET
            inventory = float(
                balance_sheet[period][statement]["Inventory"])

            # CASH FLOW
            accounts_receivable = float(
                cash_flow[period][statement]["Accounts_Receivable"])
            accounts_payable = float(
                cash_flow[period][statement]["Accounts_Payable"])

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

    # Cash_Dividend Payout Ratio = Cash_Dividends / (Cash Flow from Operations – Capital Expenditures – Preferred Dividend_Paid)
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