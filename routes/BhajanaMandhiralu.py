from fastapi import APIRouter, Request, UploadFile,File
from models.BhajanaMandhiralu import BhajanaMandhiralu


import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
DB = myclient["Project"]
mycol = DB["BhajanaMandhircol"]
mandalcol = DB["Mandals"]


user = APIRouter()


@user.post("/BhajanaMandhiralu")
async def create_user(request: BhajanaMandhiralu):
    Phases = request.Phases
    District = request.District
    Documents = request.Documents
    Constituency = request.Constituency
    Mandal = request.Mandal
    Village = request.Village
    Colony = request.Colony
    Phone_no = request.Phone_no
    Population = request.Population
    Survey_no = request.Survey_no

    data = {
        "Phases": Phases,
        "District":  District,
        "Documents": Documents,
        "Constituency": Constituency,
        "Mandal":  Mandal,
        "Village": Village,
        "Colony": Colony,
        "Phone_no": Phone_no,
        "Population": Population,
        "Survey_no": Survey_no
    }
    mycol.insert_one(data)
    return "Success"


@user.post("/GetMandals")
async def GetMandalsByDistrict(request: Request):
    data = await request.json()
    districts = data["Districts"]
    mandal_list = []

    for district in districts:
        mandals_data = mandalcol.find({"District": district}, {"_id": 0})
        mandal_list.extend([m["Mandal"] for m in mandals_data])

    return {"mandallist": mandal_list}


@user.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    with open("D:\Requested Documents/" + file.filename, "wb") as f:
        f.write(contents)
    print(file.filename)
    return {"filename": file.filename}


 