from fastapi import APIRouter,Request,UploadFile,File
from models.NewTempleConstuction import NewTempleConstruction


import pymongo 
myclient= pymongo.MongoClient("mongodb://localhost:27017/")
DB = myclient["Project"]
mycol= DB["NewTempleConstructioncol"]
mandalcol= DB["Mandals"]


user1 = APIRouter()
@user1.post("/NewTempleConstruction")
async def create_user(request:NewTempleConstruction):
    Phases = request.Phases
    District = request.District
    Constituency = request.Constituency
    Mandal= request.Mandal
    Village = request.Village
    Colony = request.Colony
    Documents   = request.Documents
    Phone_no   = request.Phone_no
    Population = request.Population
    Survey_no   = request.Survey_no

    data = {
        "Phases": Phases,
        "District":  District ,
        "Constituency": Constituency ,
        "Mandal":  Mandal,
        "Village": Village,
        "Colony": Colony ,
        "Documents ": Documents ,
        "Phone_no": Phone_no  ,
        "Population": Population ,
        "Survey_no": Survey_no
    }
    mycol.insert_one(data)
    return "Success"
    


@user1.post("/FetchMandals")
async def GetMandalsByDistrict(request: Request):
    data = await request.json()
    districts = data["Districts"]
    mandal_list = []

    for district in districts:
        mandals_data = mandalcol.find({"District": district}, {"_id": 0})
        mandal_list.extend([m["Mandal"] for m in mandals_data])

    return {"mandallist": mandal_list}


@user1.post("/uploadDocument")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    with open("D:\Requested Documents/" + file.filename, "wb") as f:
        f.write(contents)
    print(file.filename)
    return {"filename": file.filename}

    
    