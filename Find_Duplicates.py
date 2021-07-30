import pymongo
import collections

client = pymongo.MongoClient(
    "mongodb+srv://Mezo:Almazni2013@tadawul-test.wkg8i.mongodb.net/Tadawul?retryWrites=true&w=majority")
mydb = client["Tadawul_v3"]

sectors = ['Communication_Services', 'Consumer_Discretionary', 'Consumer_Staples',
           'Energy', 'Financials', 'Health_Care', 'Industrials', 'Information_Technology',
           'Materials', 'Real_Estate', 'Utilities']

for sector in sectors:
    current_res = []
    mycol = mydb[sector]
    res = mycol.find({}, {"TICKER": 1})
    for x in res:
        current_res.append(x['TICKER'])

    print(f"Duplicates in {sector}")
    print([item for item, count in collections.Counter(
        current_res).items() if count > 1])
