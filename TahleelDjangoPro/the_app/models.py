from django.db import models
import pymongo

# Create your models here.

client = pymongo.MongoClient(
    "mongodb+srv://Mezo:Almazni2013@tadawul-test.wkg8i.mongodb.net/Tadawul?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")

