from pydantic import BaseModel
from fastapi import FastAPI,Body, Request, File, UploadFile
class NewTempleConstruction(BaseModel):
    Phases:str
    District:str
    Constituency:str
    Mandal:str
    Village:str
    Colony:str
    Documents:str
    Phone_no:int
    Population:int
    Survey_no:str