import firebase_admin
from firebase_admin import credentials, firestore

def connect_fb_db(keyConfig):
    cred = credentials.Certificate(keyConfig)
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db