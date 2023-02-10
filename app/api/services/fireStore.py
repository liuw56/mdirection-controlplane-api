from fastapi import FastAPI, Request, Response
from api.models.Product import Product
def get_all_documents(db) -> list:
    products = []
    try:
        productsInfo = db.collection('productDetail').get()
        for product in productsInfo:
            products.append(product.to_dict())
            return products
    except:
        raise Exception("FireStore get Error")

def create_new_product(db,productInfo:Product):
    try:
        db.collection('productDetail').document(productInfo["ID"]).set(productInfo)
    except:
        raise Exception("FireStore post Error")

def get_related_products(db,source):
    try:
        products = []
        productsInfo = db.collection('productDetail').where("source","==",source).get()
        for product in productsInfo:
            products.append(product.to_dict())
        return products
    except:
        raise BaseException

def search_function(db,keywords):
    try:
        products = []
        productsInfo = db.collection('productDetail').get()
        for product in productsInfo:
            product = product.to_dict()
            print(product)
            if keywords in product["ID"]:
                products.append(product)
            elif keywords in product["source"]:
                products.append(product)
            elif keywords in product["description"]:
                products.append(product)
            elif keywords in product["enSpecies"]:
                products.append(product)
            elif keywords in product["sequence"]:
                products.append(product)
        print(products)
        return products
    except:
        raise BaseException