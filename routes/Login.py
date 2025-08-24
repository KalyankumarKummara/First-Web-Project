from fastapi import APIRouter
from models.Login import LoginUser
import bcrypt
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://kalyan:Kalyankumar%40123@cluster0.sur1pof.mongodb.net/")
DB = myclient["Project"]
mycol = DB["Usercol"]

UserLogin = APIRouter()

@UserLogin.post("/Login")
async def UserAccount(request: LoginUser):
    try:
        # Find user in database
        user_data = mycol.find_one({"Username": request.Username})
        
        if not user_data:
            return {"status": "Error", "detail": "User not found"}
        
        # Verify password
        if bcrypt.checkpw(request.Password.encode(), user_data["Password"].encode()):
            return {"status": "Success"}
        else:
            return {"status": "Error", "detail": "Invalid password"}
            
    except Exception as e:
        return {"status": "Error", "detail": str(e)}