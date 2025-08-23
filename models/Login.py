from pydantic import BaseModel
from fastapi import FastAPI,Request
class LoginUser(BaseModel):
    Username : str
    Password : str