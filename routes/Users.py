from fastapi import APIRouter
from models.Users import User
import bcrypt
import pymongo 
myclient= pymongo.MongoClient("mongodb://localhost:27017/")
DB = myclient["Project"]
mycol= DB["Usercol"]
user3 = APIRouter()
@user3.post("/Register")
async def create_user(request:User):
    Username = request.Username
    Email = request.Email 
    Password = request.Password.encode()  # Encoding the Password before Hashing
    ConfirmPassword = request.ConfirmPassword.encode()
    # Hashing the Password
    hashedPassword = bcrypt.hashpw(Password,bcrypt.gensalt())
    hashedConfirmPassword = bcrypt.hashpw(ConfirmPassword,bcrypt.gensalt())
    data ={
        "Username" : Username,
        "Email" : Email,
        "Password" : hashedPassword.decode(),
        "ConfirmPassword" : hashedConfirmPassword.decode()
    }
    mycol.insert_one(data)
    return "Success"