def ReportsEntity(item) ->  dict:
    return {
        "id": str(["_id"]),
        "phases":item ["phases"],
        "District":item["District"],
       "Mandal":item["Mandal"],
       "Panchayat": item["Panchayat"],
       "Village":item["Village"],
      "Colony":item["Colony"],
     "Temple_Age":item["Temple_Age"],
     "Start_date":item["Start_date"],
     "End_date":item["End_date"],
     "Refered": item["Refered"]
    }
