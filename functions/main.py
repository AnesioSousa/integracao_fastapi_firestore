# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
"""Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app

 initialize_app()
#
#
 @https_fn.on_request()
 def on_request_example(req: https_fn.Request) -> https_fn.Response:
     return https_fn.Response("Hello world!")
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials, firestore

# Inicialize o Firebase Admin SDK
cred = credentials.Certificate("../seminarioppedu-54c2d-firebase-adminsdk-rtg8o-4ae2fc1484.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str
    birthdate: str = ""
    cpf: str

@app.post("/users/", response_model=dict)
async def create_user(user: User):
    try:
        user_ref = db.collection('users').document(str(user.id))
        user_ref.set(user.dict())
        return {"message": "User created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/users/", response_model=list)
async def get_users():
    try:
        users_ref = db.collection('users')
        docs = users_ref.stream()
        users = [doc.to_dict() for doc in docs]
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
