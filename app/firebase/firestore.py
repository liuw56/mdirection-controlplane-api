import firebase_admin
from firebase_admin import credentials, firestore, storage


def connect_fb_db(keyConfig):
    cred = credentials.Certificate(keyConfig)
    firebase_admin.initialize_app(cred, {'storageBucket': 'mdirectionbiotechweb.appspot.com'})
    db = firestore.client()
    bucket = storage.bucket()
    return db , bucket
