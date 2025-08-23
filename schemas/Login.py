def LoginEntity(item) ->  dict:
    return {
        "id": str(["_id"]),
        "Username": item["Username"],
        "Password": item["Password"]
    }