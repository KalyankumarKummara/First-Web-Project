from pydantic import BaseModel
from fastapi import FastAPI,Body, Request, File, UploadFile
class RenovationOfTemple(BaseModel):
    Phases:str
    District:str
    Constituency:str
    Mandal:str
    Village:str
    Colony:str
    Temple_age:int
    Phone_no:int
    Population:int
    Survey_no:str