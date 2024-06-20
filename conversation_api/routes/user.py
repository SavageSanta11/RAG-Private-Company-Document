from fastapi import APIRouter
from models.user import User 
# from config.db import conn 
from config.db import collection_name 
from schemas.user import serializeDict, serializeList
from bson import ObjectId
from typing import Dict
user = APIRouter() 

@user.get('/')
async def find_all_users():
    return serializeList(collection_name.local.user.find())

# @user.get('/{id}')
# async def find_one_user(id):
#     return serializeDict(conn.local.user.find_one({"_id":ObjectId(id)}))


# CREATING A NEW USER
@user.post('/')
async def create_user(user: User):
    collection_name.local.user.insert_one(dict(user))
    return serializeList(collection_name.local.user.find())



#ADDING NEW MESSAGE TO USER
@user.post('/{email}/add-message')
async def add_message_to_user(email: str, message: Dict[str, str]):
    # Find the user by email
    user = collection_name.local.user.find_one({"email": email})
    if user:

        if 'message' in user:

            if message not in user['message']:
            
                user['message'].append(message)
        else:

            user['message'] = [message]
        
        # Update the user document with the new or updated 'message' list
        collection_name.local.user.update_one({"email": email}, {"$set": {"message": user['message']}})
        return {"message": "Message added successfully"}
    else:
        return {"message": "User not found"}


#getting all messages
#http://localhost:8000/aishu@gmail.com/messages/
# @user.get('/{email}/messages')
# async def get_user_messages(email: str):
#     # Find the user by email
#     user = collection_name.local.user.find_one({"email": email})
#     if user:
#         # Check if the 'message' field exists in the user document
#         if 'message' in user:
#             # Return the list of messages for the user
#             return {"messages": user['message']}
#         else:
#             return {"message": "No messages found for the user"}
#     else:
#         return {"message": "User not found"}
    

@user.get('/{email}/messages')
async def get_user_messages(email: str):
    # Find the user by email
    user = collection_name.local.user.find_one({"email": email})
    if user:
        # Check if the 'message' field exists in the user document
        if 'message' in user:
            # Exclude the first message and return the remaining messages
            messages = user['message'][1:]
            return {"messages": messages}
        else:
            return {"message": "No messages found for the user"}
    else:
        return {"message": "User not found"}


#getting recent 5 messages
@user.get('/{email}/recent-messages')
async def get_recent_messages(email: str):
    # Find the user by email
    user = collection_name.local.user.find_one({"email": email})
    if user:
        # If the 'message' field is present
        if 'message' in user:
            # Get the last 5 messages
            messages = user['message'][1:]
            recent_messages = messages[-5:]
            return {"recent_messages": recent_messages}
        else:
            return {"message": "No messages found for this user"}
    else:
        return {"message": "User not found"}



#DELETING USER
@user.delete('/{email}')
async def delete_user(email: str):
    # Find the user by email and delete it
    deleted_user = collection_name.local.user.find_one_and_delete({"email": email})
    if deleted_user:
        return {"message": f"User with email {email} has been deleted successfully"}
    else:
        return {"message": f"User with email {email} not found"}

