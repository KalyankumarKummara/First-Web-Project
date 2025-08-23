from pydantic import BaseModel
from fastapi import FastAPI,Body, Request, File, UploadFile
class BhajanaMandhiralu(BaseModel):
    Phases:str
    District:str
    Documents:str
    Constituency:str
    Mandal:str
    Village:str
    Colony:str
    Phone_no:int
    Population:int
    Survey_no:str