from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import *
import json


# Create your python logic here.

def makeSectorList(sector):
    theSectorList=CompaniesGeneral.objects.filter(sector=sector)
    return theSectorList
def allCompanies():
    allCompanies=CompaniesGeneral.objects.all()
    return allCompanies
def isTheTickerThere(ticker,myList):
    for stock in myList:
        if stock['TICKER'] == ticker:
            return True
    return False
def filterTheStocks(filterObj):
    # Sector filter
    if filterObj['Sector']=='All':
        theCurrentStocks = allCompanies()
    else:
        theCurrentStocks = makeSectorList(filterObj['Sector'])
    # Price filter
    if filterObj['PRICE'] !='Any':
        theCurrentStocks=filterByPrice(theCurrentStocks,filterObj['PRICE'])
    # Market Cap filter
    if filterObj['MarketCap'] !='Any':
        theCurrentStocks=filterByMarketCap(theCurrentStocks,filterObj['MarketCap'])
    # P/B filter
    if filterObj['Pb'] !='Any':
        theCurrentStocks=filterByPb(theCurrentStocks,filterObj['Pb'])
    # P/E filter
    if filterObj['Pe'] !='Any':
        theCurrentStocks=filterByPe(theCurrentStocks,filterObj['Pe'])
    # Current Ratio filter
    if filterObj['CurrentRatio'] !='Any':
        theCurrentStocks=filterByCurrentRatio(theCurrentStocks,filterObj['CurrentRatio'])
    # Debt Ratio filter
    if filterObj['DebtRatio'] !='Any':
        theCurrentStocks=filterByDebtRatio(theCurrentStocks,filterObj['DebtRatio'])
    # Eps filter
    if filterObj['Eps'] !='Any':
        theCurrentStocks=filterByEps(theCurrentStocks,filterObj['Eps'])
    # Ebit filter
    if filterObj['Ebit'] !='Any':
        theCurrentStocks=filterByEbit(theCurrentStocks,filterObj['Ebit'])
    # Operating Eps filter
    if filterObj['OperatingEps'] !='Any':
        theCurrentStocks=filterByOperatingEps(theCurrentStocks,filterObj['OperatingEps'])
    # Dividend Yield filter
    if filterObj['DividendYield'] !='Any':
        theCurrentStocks=filterByDividendYield(theCurrentStocks,filterObj['DividendYield'])
    # Quick Ratio filter
    if filterObj['QuickRatio'] !='Any':
        theCurrentStocks=filterByQuickRatio(theCurrentStocks,filterObj['QuickRatio'])
    return theCurrentStocks

def filterByQuickRatio(theCurrentStocks,catVal):
    newStocksList=[]
    readyStocksList=[]
    if catVal =='High':
        for stock in QuickRatio.objects.all():
            if float(stock.value) > 3.00:
                newStocksList.append(stock)
    elif catVal =='Low':
        for stock in QuickRatio.objects.all():
            if float(stock.value) < 0.5:
                newStocksList.append(stock)
    else:
        for stock in QuickRatio.objects.all():
            if float(stock.value) >= 0.5 and float(stock.value) <= 3.00 :
                newStocksList.append(stock)
    for stock in theCurrentStocks:
        for x in newStocksList:
            if int(stock.ticker) == x.ticker and x.year.split('_')[0] == "2020":
                readyStocksList.append(stock)
    return readyStocksList
def filterByDividendYield(theCurrentStocks,catVal):
    newStocksList=[]
    readyStocksList=[]
    if catVal =='Positive':
        for stock in DividendYield.objects.all():
            if float(stock.value) > 0:
                newStocksList.append(stock)
    elif catVal =='High':
        for stock in DividendYield.objects.all():
            if float(stock.value) > 0.05:
                newStocksList.append(stock)
    elif catVal =='Very_High':
        for stock in DividendYield.objects.all():
            if float(stock.value) > 0.1:
                newStocksList.append(stock)
    else:
        for stock in DividendYield.objects.all():
            if float(stock.value) == 0:
                newStocksList.append(stock)
    for stock in theCurrentStocks:
        for x in newStocksList:
            if int(stock.ticker) == x.ticker and x.year.split('_')[0] == "2020":
                readyStocksList.append(stock)
    return readyStocksList
def filterByOperatingEps(theCurrentStocks,catVal):
    newStocksList=[]
    readyStocksList=[]
    if catVal =='High':
        for stock in OperatingEps.objects.all():
            if float(stock.value) > 2.00:
                newStocksList.append(stock)
    elif catVal =='Low':
        for stock in OperatingEps.objects.all():
            if float(stock.value) < 0.00:
                newStocksList.append(stock)
    else:
        for stock in OperatingEps.objects.all():
            if float(stock.value) >= 0.00 and float(stock.value) <= 2.00 :
                newStocksList.append(stock)
    for stock in theCurrentStocks:
        for x in newStocksList:
            if int(stock.ticker) == x.ticker and x.year.split('_')[0] == "2020":
                readyStocksList.append(stock)
    return readyStocksList
def filterByEbit(theCurrentStocks,catVal):
    newStocksList=[]
    readyStocksList=[]
    if catVal =='Very_High':
        for stock in Ebit.objects.all():
            if int(stock.value) > 5000000000:
                newStocksList.append(stock)
    elif catVal =='High':
        for stock in Ebit.objects.all():
            if int(stock.value) >= 10000000 and int(stock.value) <= 5000000000 :
                newStocksList.append(stock)
    elif catVal =='Acceptable':
        for stock in Ebit.objects.all():
            if int(stock.value) >= 1000000 and int(stock.value) <= 10000000 :
                newStocksList.append(stock)
    elif catVal =='Low':
        for stock in Ebit.objects.all():
            if int(stock.value) >= -10000000 and int(stock.value) <= 0 :
                newStocksList.append(stock)
    else:
        for stock in Ebit.objects.all():
            if int(stock.value) < -10000000 :
                newStocksList.append(stock)
    for stock in theCurrentStocks:
        for x in newStocksList:
            if int(stock.ticker) == x.ticker and x.year.split('_')[0] == "2020":
                readyStocksList.append(stock)
    return readyStocksList
def filterByEps(theCurrentStocks,catVal):
    newStocksList=[]
    readyStocksList=[]
    if catVal =='High':
        for stock in Eps.objects.all():
            if float(stock.value) > 2.00:
                newStocksList.append(stock)
    elif catVal =='Low':
        for stock in Eps.objects.all():
            if float(stock.value) < 0.00:
                newStocksList.append(stock)
    else:
        for stock in Eps.objects.all():
            if float(stock.value) >= 0.00 and float(stock.value) <= 2.00 :
                newStocksList.append(stock)
    for stock in theCurrentStocks:
        for x in newStocksList:
            if int(stock.ticker) == x.ticker and x.year.split('_')[0] == "2020":
                readyStocksList.append(stock)
    return readyStocksList
def filterByDebtRatio(theCurrentStocks,catVal):
    newStocksList=[]
    readyStocksList=[]
    if catVal =='High':
        for stock in DebtRatio.objects.all():
            if float(stock.value) > 50.00:
                newStocksList.append(stock)
    elif catVal =='Low':
        for stock in DebtRatio.objects.all():
            if float(stock.value) < 10.00:
                newStocksList.append(stock)
    else:
        for stock in DebtRatio.objects.all():
            if float(stock.value) >= 10.00 and float(stock.value) <= 50.00 :
                newStocksList.append(stock)
    for stock in theCurrentStocks:
        for x in newStocksList:
            if int(stock.ticker) == x.ticker and x.year.split('_')[0] == "2020":
                readyStocksList.append(stock)
    return readyStocksList
def filterByCurrentRatio(theCurrentStocks,catVal):
    newStocksList=[]
    readyStocksList=[]
    if catVal =='High':
        for stock in CurrentRatio.objects.all():
            if float(stock.value) > 3.00:
                newStocksList.append(stock)
    elif catVal =='Low':
        for stock in CurrentRatio.objects.all():
            if float(stock.value) < 1.00:
                newStocksList.append(stock)
    else:
        for stock in CurrentRatio.objects.all():
            if float(stock.value) >= 1.00 and float(stock.value) <= 3.00 :
                newStocksList.append(stock)
    for stock in theCurrentStocks:
        for x in newStocksList:
            if int(stock.ticker) == x.ticker and x.year.split('_')[0] == "2020":
                readyStocksList.append(stock)
    return readyStocksList
def filterByPe(theCurrentStocks,catVal):
    newStocksList=[]
    readyStocksList=[]
    if catVal =='High':
        for stock in Pe.objects.all():
            if float(stock.value) > 50.00:
                newStocksList.append(stock)
    elif catVal =='Low':
        for stock in Pe.objects.all():
            if float(stock.value) < 15.00:
                newStocksList.append(stock)
    else:
        for stock in Pe.objects.all():
            if float(stock.value) >= 15.00 and float(stock.value) <= 50.00 :
                newStocksList.append(stock)
    for stock in theCurrentStocks:
        for x in newStocksList:
            if int(stock.ticker) == x.ticker and x.year.split('_')[0] == "2020":
                readyStocksList.append(stock)
    return readyStocksList
def filterByPb(theCurrentStocks,catVal):
    newStocksList=[]
    readyStocksList=[]
    if catVal =='High':
        for stock in Pb.objects.all():
            if float(stock.value) > 5.00:
                newStocksList.append(stock)
    elif catVal =='Low':
        for stock in Pb.objects.all():
            if float(stock.value) < 1.00:
                newStocksList.append(stock)
    else:
        for stock in Pb.objects.all():
            if float(stock.value) >= 1.00 and float(stock.value) <= 5.00 :
                newStocksList.append(stock)
    for stock in theCurrentStocks:
        for x in newStocksList:
            if int(stock.ticker) == x.ticker and x.year.split('_')[0] == "2020":
                readyStocksList.append(stock)
    return readyStocksList
def filterByMarketCap(theCurrentStocks,catVal):
    newStocksList=[]
    readyStocksList=[]
    if catVal =='Mega':
        for stock in Marketcap.objects.all():
            if int(stock.marketcap) >= 200000000000 :
                newStocksList.append(stock)
    elif catVal =='Nano':
        for stock in Marketcap.objects.all():
            if int(stock.marketcap) <50000000:
                newStocksList.append(stock)
    elif catVal =='Large':
        for stock in Marketcap.objects.all():
            if int(stock.marketcap) >= 10000000000 and int(stock.marketcap) <= 200000000000 :
                newStocksList.append(stock)
    elif catVal =='Mid':
        for stock in Marketcap.objects.all():
            if int(stock.marketcap) >= 2000000000 and int(stock.marketcap) <= 10000000000 :
                newStocksList.append(stock)
    elif catVal =='Small':
        for stock in Marketcap.objects.all():
            if int(stock.marketcap) >= 300000000 and int(stock.marketcap) <= 2000000000 :
                newStocksList.append(stock)
    else:
        print("Entered the Microooo!!!!!!")
        for stock in Marketcap.objects.all():
            if int(stock.marketcap) >= 50000000 and int(stock.marketcap) <= 300000000 :
                newStocksList.append(stock)
    for stock in theCurrentStocks:
        for x in newStocksList:
            if int(stock.ticker) == x.ticker :
                readyStocksList.append(stock)
    return readyStocksList
def filterByPrice(theCurrentStocks,catVal):
    newStocksList=[]
    if catVal =='High':
        for stock in theCurrentStocks:
            if int(stock.price) >100:
                newStocksList.append(stock)
    elif catVal =='Low':
        for stock in theCurrentStocks:
            if int(stock.price) <50:
                newStocksList.append(stock)
    else:
        for stock in theCurrentStocks:
            if int(stock.price) >= 50 and int(stock.price) <=100:
                newStocksList.append(stock)
    return newStocksList

def findComByTicker(Sector,Ticker):
    tadawul_db = client["Tadawul_v3"]
    sectorList = tadawul_db[Sector]
    company = sectorList.find_one({"TICKER": int(Ticker)})
    return company

def isItCorrectSearch(searchData):
    if int(searchData) <= 9999:
        return True
    else:
        return False

# def getMC(sectorVal,tickerVal):
#     # sector = sectorVal
#     # ticker = tickerVal
#     # tadawul_db = client["Tadawul_v3"]
#     # mycol = tadawul_db[sector]
#     # res = mycol.find_one({"TICKER": int(ticker)})

#     # price = float(res["PRICE"])
#     # shares = int(res["ISSUED_SHARES"])
#     # result= (price * shares)


#     return Marketcap.objects.get(ticker=)
def getInvestments(tickerVal):
    # ALLc=allCompanies()
    result={}
    for c in allCompanies():
        if int(c['TICKER']) == int(tickerVal):
            result=c['BALANCE_SHEET']['ANNUALLY']['2020_12_31']['Investments']
    return result
def getDepreciation(tickerVal):
    ALLc=allCompanies()
    result={}
    for c in ALLc:
        if int(c['TICKER']) == int(tickerVal):
            result=c['STATEMENT_OF_INCOME']['ANNUALLY']['2020_12_31']['Depreciation']
    return result
def getNetIncome(tickerVal):
    ALLc=allCompanies()
    result={}
    for c in ALLc:
        if int(c['TICKER']) == int(tickerVal):
            result=c['CASH_FLOW']['ANNUALLY']['2020_12_31']['Net_Income']
    return result

# def removeDuplicates(cuurentStocksList):
#     newStocksList = []
#     for stock in cuurentStocksList:
#         if not isTheTickerThere(stock['TICKER'],newStocksList):
#             newStocksList.append(stock)
#     return newStocksList



# Create your views here.

def main(request):
    filterObj = {
    'Sector': 'All',
    'PRICE': 'Any',
    'MarketCap': 'Any',
    'Pb': 'Any',
    'Pe': 'Any',
    'CurrentRatio': 'Any',
    'DebtRatio': 'Any',
    'Eps': 'Any',
    'Ebit': 'Any',
    'OperatingEps': 'Any',
    'DividendYield': 'Any',
    'QuickRatio': 'Any'
    } 
    request.session['filterObj'] = filterObj
    return redirect('filter/Sector/catagory/All')
def searchT(request):
    if request.method =='POST':
        if isItCorrectSearch(request.POST['search']):
            company=CompaniesGeneral.objects.filter(ticker=request.POST['search'])
            if company:
                context ={
                    'correctSearch': True,
                    'thereIsResult':True,
                    'result':company,
                }
                return render(request, 'searchResults.html',context)
            else:
                context ={
                    'correctSearch': True,
                    'thereIsResult':False
                }
                return render(request, 'searchResults.html',context)
        else:
            context ={
                'correctSearch': False,
                'thereIsResult':False
            }
            return render(request, 'searchResults.html',context)

def filterView(request,filterVal,catVal):
    filterObj=request.session['filterObj'] 
    filterObj[filterVal]=catVal
    request.session['filterObj'] =filterObj
    cuurentStocksList =filterTheStocks(request.session['filterObj'] )
    context={
        'cuurentStocksList':cuurentStocksList,
        'isScreener':True,
    }
    return render(request, 'main.html',context)


def stockPage(request,sectorVal,tickerVal):
    stock=findComByTicker(sectorVal,int(tickerVal))
    dividend=0
    dividendAvg=0
    if sectorVal != 'Financials':
        x=DividendYield.objects.get(ticker=tickerVal, year='2020_12_31')
        dividend=x.value
        s=DividendIndustryAverage.objects.get(sector=sectorVal, year='2020_12_31')
        dividendAvg=s.Average
    # print("yesssssssssssssss")
    # print(dividend)
    # print(dividendAvg)
    context={
        'dividend':dividend,
        'dividendAvg':dividendAvg,
        'stock':stock,
        'isStock':True,
        'MC':Marketcap.objects.filter(ticker=tickerVal),
    }
    return render(request, 'stockPage.html',context)

# Create your API formulas
# def newDividendAvrgForSector(request,sectorVal):
#     sectorList=makeSectorList(sectorVal)
#     sectorDividendList=[]
#     # put all sector dividends in one place
#     for c in sectorList:
#         for d in DividendYield.objects.all():
#             if c.ticker == d.ticker and d.year == '2020_12_31':
#                 sectorDividendList.append(d.value)
#     # add them all 
#     sum=0
#     for d in sectorDividendList:
#         sum=+d
#     avg=sum/len(sectorDividendList)
#     newAvg= DividendIndustryAverage.objects.create(sector= sectorVal,year='2020_12_31',Average=avg)
#     newAvg.save()
#     return redirect('/')
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