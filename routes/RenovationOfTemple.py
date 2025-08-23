from fastapi import APIRouter,Request
from models.RenovationOfTemple import RenovationOfTemple


import pymongo 
myclient= pymongo.MongoClient("mongodb://localhost:27017/")
DB = myclient["Project"]
mycol= DB["RenovationOfTemplecol"]
mandalcol= DB["Mandals"]

user2 = APIRouter()
@user2.post("/RenovationOfTemple")
async def create_user(request:RenovationOfTemple):
    Phases = request.Phases
    District = request.District
    Constituency = request.Constituency
    Mandal= request.Mandal
    Village = request.Village
    Colony = request.Colony
    Temple_age = request.Temple_age
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
        "Temple_age":Temple_age ,
        "Phone_no": Phone_no  ,
        "Population": Population ,
        "Survey_no": Survey_no
    }
    mycol.insert_one(data)
    return "Success"

    
@user2.post("/Mandals")
async def GetMandalsByDistrict(request: Request):
    data = await request.json()
    districts = data["Districts"]
    mandal_list = []

    for district in districts:
        mandals_data = mandalcol.find({"District": district}, {"_id": 0})
        mandal_list.extend([m["Mandal"] for m in mandals_data])

    return {"mandallist": mandal_list}