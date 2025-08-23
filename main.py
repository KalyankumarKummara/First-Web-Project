from typing import Union
from fastapi import FastAPI, Body, Request, File, UploadFile
from fastapi import Form
from pydantic import BaseModel
from datetime import date
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes.BhajanaMandhiralu import user
from routes.NewTempleConstruction import user1
from routes.RenovationOfTemple import user2
from routes.Users import user3
from routes.Reports import user4
from routes.Login import UserLogin

app = FastAPI()
app.include_router(user)
app.include_router(user1)
app.include_router(user2)
app.include_router(user3)
app.include_router(user4)
app.include_router(UserLogin)




app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")



@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("Login.html", {"request": request})


@app.get("/Register", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("Register.html", {"request": request})


@app.get("/BhajanaMandhiralu", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("BhajanaMandhiralu.html", {"request": request})


@app.get("/NewTempleConstruction", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("NewTempleConstruction.html", {"request": request})


@app.get("/RenovationOfTemple", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("RenovationOfTemple.html", {"request": request})


@app.get("/Reports", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("Reports.html", {"request": request})


@app.get("/Login", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("Login.html", {"request": request})


@app.post("/uploadfile/")
async def Upload_file(file: UploadFile):
    return {"filename": file.filename}


if __name__ =="__main__":
    app.run()