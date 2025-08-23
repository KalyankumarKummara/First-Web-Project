def NewTempleEntity(item) ->  dict:
    return {
        "id": str(["_id"]),
        "phases":item ["phases"],
        "District":item["District"],
        "Constituency":item["Constituency"],
       "Mandal":item["Mandal"],
       "Village":item["Village"],
      "Colony":item["Colony"],
      "documents":item["documents"],
      "Phone_no":item["Phone_no"],
      "Population":item["Population"],
      "survey_no":item["survey_no"]

    }
