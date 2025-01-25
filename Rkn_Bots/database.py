# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr

import motor.motor_asyncio
from config import Rkn_Bots

client = motor.motor_asyncio.AsyncIOMotorClient(Rkn_Bots.DB_URL)
db = client[Rkn_Bots.DB_NAME]
chnl_ids = db.chnl_ids
users = db.users
banned_users = db.banned_users  # New collection for banned users

# Insert user data
async def insert(user_id):
    user_det = {"_id": user_id}
    try:
        await users.insert_one(user_det)
    except:
        pass

# Total Users
async def total_user():
    user = await users.count_documents({})
    return user

# Total Channels
async def total_channels():
    channels = await chnl_ids.count_documents({})
    return channels

async def getid():
    all_users = users.find({})
    return all_users

async def delete(id):
    await users.delete_one(id)

async def addCap(chnl_id, caption):
    dets = {"chnl_id": chnl_id, "caption": caption}
    await chnl_ids.insert_one(dets)

async def updateCap(chnl_id, caption):
    await chnl_ids.update_one({"chnl_id": chnl_id}, {"$set": {"caption": caption}})

# Ban a user
async def ban_user(user_id):
    user = {"_id": user_id}
    try:
        await banned_users.insert_one(user)
    except:
        pass

# Unban a user
async def unban_user(user_id):
    await banned_users.delete_one({"_id": user_id})

# Check if a user is banned
async def is_banned(user_id):
    user = await banned_users.find_one({"_id": user_id})
    return user is not None
