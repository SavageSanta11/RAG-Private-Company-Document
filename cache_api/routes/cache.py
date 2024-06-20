from fastapi import APIRouter
from models.cache import CacheEntry , UpdateModel
# from config.db import conn 
from config.db import collection_name 
from schemas.cache import serializeDict, serializeList
from routes.utils import get_chunk_id_least_accessed
from bson import ObjectId
from typing import Dict
cache = APIRouter() 

# endpoints
# get question given chunk id           - get_question
# get top 5  frequently asked questions
# add question to the cache             - cache_entry
# remove question                       - delete_cache_entry

# GET ALL CACHE INFO
@cache.get('/')
async def get_all_cache_entries():
    return serializeList(collection_name.local.user.find())

# GET SPECIFIC CACHE ENTRY
@cache.get('/get')
async def get_cache_entry(chunk_id: str, new_access_time: float):
    cache_entry = collection_name.local.user.find_one({"chunk_id": chunk_id})
    if cache_entry:
        cache_entry.pop("_id")
        return cache_entry
    else:
        return {"message": "Cache entry was not found"}

# RETURN FAQs
@cache.get('/faq')
async def get_freq_questions():
    data = serializeList(collection_name.local.user.find())

    sorted_data = sorted(data, key=lambda x: x['entry_info']['freq'], reverse=True)

    # Get the top 5 dictionaries with the highest 'freq' value
    top_5_dicts = sorted_data[:5]
    for d in top_5_dicts:
        d.pop("_id")
    return top_5_dicts
    
# CREATING A NEW CACHE ENTRY
@cache.post('/create')
async def add_cache_entry(cache_entry: CacheEntry):
    collection_name.local.user.insert_one(dict(cache_entry))

    total_entries = serializeList(collection_name.local.user.find())
    print(len(total_entries))
    if len(total_entries) > 10:
        least_accessed_cache_entry = get_chunk_id_least_accessed(total_entries)
        deleted_cache_entry = collection_name.local.user.find_one_and_delete({"chunk_id": least_accessed_cache_entry})
        print(f"Least recently used cache entry with chunk_id '{least_accessed_cache_entry}' has been deleted")
        return {"message": "New cache entry has been created", "size_limit_flag": True, "removed_chunk_id": least_accessed_cache_entry}
    return {"message": "New cache entry has been created and an old one has been removed", "size_limit_flag": False}

# UPDATING A CACHE ENTRY
@cache.post('/update')
async def add_cache_entry_frequency(update_entry: UpdateModel):
    chunk_id = update_entry.chunk_id
    new_access_time = update_entry.new_access_time

    cache_entry = collection_name.local.user.find_one({"chunk_id": chunk_id})
    if cache_entry:
        curr_info = cache_entry['entry_info']
        curr_info['freq'] += 1
        curr_info['last_access_time'] = new_access_time
        collection_name.local.user.update_one({"chunk_id": chunk_id}, {"$set": {"entry_info": curr_info}})
        cache_entry = collection_name.local.user.find_one({"chunk_id": chunk_id})
        cache_entry.pop("_id")
        return {"cache_entry": cache_entry}
    else:
        return {"message": "Cache entry could not be found"}

#DELETING CACHE ENTRY
@cache.delete('/delete')
async def delete_cache_entry(chunk_id: str):
    # Find the user by email and delete it
    deleted_user = collection_name.local.user.find_one_and_delete({"chunk_id": chunk_id})
    if deleted_user:
        return {"message": f"Cache entry with chunk_id '{chunk_id}' has been deleted successfully"}
    else:
        return {"message": f"Cache entry with chunk_id '{chunk_id}' not found"}

