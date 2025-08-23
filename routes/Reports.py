from fastapi import APIRouter,Request,Form
from typing import List ,Optional,Union,Any
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")


import pymongo 
myclient= pymongo.MongoClient("mongodb://localhost:27017/")
DB = myclient["Project"]
mycol= DB["BhajanaMandhircol"]
mandalcol= DB["Mandals"]


user4 = APIRouter()
@user4.post("/Reports")
async def GetApplicationsByDistrict(request: Request, District: List[str] = Form(default=None), Mandal: List[str] = Form(default=None)):
    context = {"request": request}
    ReportsData = []

    for d in District:
        if not Mandal:
            Data = mycol.find({"District": d}).sort("_id", 1)
            for i in Data:
                data = {"District": d, "request_data": i}
                ReportsData.append(data)
        else:
            for m in Mandal:
                Data = mycol.find({"District": d, "Mandal": m}).sort("_id", 1)
                for i in Data:
                    data = {"District": d, "Mandal": m, "request_data": i}
                    ReportsData.append(data)

    c = bool(ReportsData)
    return templates.TemplateResponse('Reports.html', {"ReportsData": ReportsData, "District": District, "Mandal": Mandal, "c": c, **context})
   

@user4.post("/MandalData")
async def GetMandalsByDistrict(request: Request):
    data = await request.json()
    districts = data["Districts"]
    mandal_list = []

    for district in districts:
        mandals_data = mandalcol.find({"District": district}, {"_id": 0})
        mandal_list.extend([m["Mandal"] for m in mandals_data])

    return {"mandallist": mandal_list}


