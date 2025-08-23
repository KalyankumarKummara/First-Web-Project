from fastapi import APIRouter
from models.Login import LoginUser
import bcrypt
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
DB = myclient["InternshipManagement"]
mycol = DB["Users"]

login_router = APIRouter()

@login_router.post("/Login")
async def user_login(request: LoginUser):
    username = request.Username
    password = request.Password.encode()
    
    user_data = mycol.find_one({"Username": username}, {"_id": 0})
    if not user_data:
        return {"message": "Invalid credentials", "status": "failed"}

    hashed_password = user_data["Password"].encode()
    if bcrypt.checkpw(password, hashed_password):
        return {"message": "Login successful", "status": "success"}
    else:
        return {"message": "Invalid credentials", "status": "failed"}
