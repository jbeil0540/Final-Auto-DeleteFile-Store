#(©)CodeXBotz

import pymongo, os
from config import DB_URI, DB_NAME

dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]
user_data = database['users']

async def present_user(user_id : int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)
    
async def add_user(user_id: int):
    await user_data.update_one({'_id': user_id}, {"$set": {'_id': user_id}}, upsert=True)
    return

async def full_userbase():
    user_docs = user_data.find()
    user_ids = [doc['_id'] for doc in user_docs]
    print(f"Fetched users: {user_ids}")  # Debug log
    return user_ids

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return
