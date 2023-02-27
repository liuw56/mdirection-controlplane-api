from fastapi import APIRouter, Request
from api.models.Product import Product
import api.services.fireStore as fireStore
from firebase.firestore import connect_fb_db
from fastapi import FastAPI, Request, Response
router = APIRouter(
    prefix="/firestore",
    tags=["firestore"]
)
db, bucket  = connect_fb_db("serviceAccountKey.json")
@router.get("/allProducts")
def get_all_documents(response:Response):
    try:
        products = fireStore.get_all_documents(db,bucket)
        response.status_code = 200
        return products
    except:
        response.status_code = 500
        return {"Error":"Firestore Databse get documents error"}

@router.post("/productCreate")
def create_new_product(product:Product,response:Response):
    try:
        fireStore.create_new_product(db,product.dict())
        response.status_code =200
        return product
    except:
        response.status_code =400
        return {"Error":"Firestore Databse post documents error"}

@router.get("/relatedProduct/{source}")
def create_new_product(source: str,response:Response):
    try:
        productlist = fireStore.get_related_products(db,source)
        response.status_code = 200
        return productlist
    except:
        response.status_code =400
        return {"Error":"Firestore Databse get documents error"}

@router.get("/search/{keywords}")
def create_new_product(keywords: str,response:Response):
    try:
        productlist = fireStore.search_function(db,keywords)
        response.status_code = 200
        return productlist
    except:
        response.status_code =400
        return {"Error":"Firestore Databse get documents error"}



