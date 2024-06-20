def userEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "email":item["email"],
        "message":item["message"],
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]
#Best way

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}


# def serializeDict(a) -> dict:
#     # Convert the ObjectId to str
#     serialized_dict = {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}
    
#     # Check if the 'message' field is present and not empty
#     if 'message' in serialized_dict and isinstance(serialized_dict['message'], list):
#         # Serialize each message dictionary in the list
#         serialized_dict['message'] = [serializeDict(msg) for msg in serialized_dict['message']]
    
#     return serialized_dict

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]