from fastapi import FastAPI, Request, Response
from api.models.Product import Product
def get_all_documents(db,bucket) -> list:
    products = []
    try:
        productsInfo = db.collection('productDetail').get()
        for product in productsInfo:
            productinfo = product.to_dict()
            products.append(productinfo)
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
        keywords = keywords.lower()
        products = []
        productsInfo = db.collection('productDetail').get()
        for product in productsInfo:
            product = product.to_dict()
            print(product)
            if "ID" in product and keywords in product["ID"].lower():
                products.append(product)
            elif "source" in product and keywords in product["source"].lower():
                products.append(product)
            elif "description" in product and keywords in product["description"].lower():
                products.append(product)
            elif "enSpecies" in product and keywords in product["enSpecies"].lower():
                products.append(product)
            elif "sequence" in product and keywords in product["sequence"].lower():
                products.append(product)
        print(products)
        return products
    except:
        raise BaseException
def search_pdf_link(db,bucket,filename):
    PdfList = bucket.list_blobs(prefix="ProductPDF")
    for pdf in PdfList:
        if pdf.name.lower() == f"ProductPDF/{filename}.pdf".lower():
            pdf.make_public()
            pdfurl = pdf.public_url
            print(filename,pdf.name)
            db.collection('productDetail').document(filename).update({"pdfurl": pdfurl})
            print(filename, pdf.name)
            return True
    return False
