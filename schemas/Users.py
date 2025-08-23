def UserEntity(item) ->  dict:
    return {
        "id": str(["_id"]),
        "Username":item["Username"],
        "Email": item["Email"],
        "Password": item["Password"],
        "ConfirmPassword": item["ConfirmPassword"]
    }