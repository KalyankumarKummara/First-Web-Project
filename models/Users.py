from pydantic import BaseModel,EmailStr
from fastapi import FastAPI,Body, Request, File, UploadFile
class User(BaseModel):
    Username : str
    Email : EmailStr
    Password : str
    ConfirmPassword : str