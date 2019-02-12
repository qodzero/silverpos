from pymongo import MongoClient
from random import randint

client = MongoClient()
db = client.silverpos
stocks = db.stocks

def purchase_product():
    codes = []
    for product in stocks.find():
        codes.append(product['product_code'])

    with open('products_purchase.csv','w') as f:
        f.write('Product_Code,Purchased\n')
        for day in range(1,31):
            for code in codes:
                purchased = randint(0,47)
                line = ','.join([str(code),str(purchased)])
                f.write(line+'\n')
    return len(codes)

purchase_product()