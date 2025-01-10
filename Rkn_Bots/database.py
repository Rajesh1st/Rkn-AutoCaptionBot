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
media_edits = db.media_edits  # New collection for media edit tracking

# Insert user data
async def insert(user_id):
    user_det = {"_id": user_id}
    try:
        await users.insert_one(user_det)
    except:
        pass

# Total User
async def total_user():
    user = await users.count_documents({})
    return user

# Total Channels
async def total_channels():
    channels = await chnl_ids.count_documents({})
    return channels

# Increment media edit count for a channel
async def increment_media_edit_count(channel_id):
    result = await media_edits.update_one(
        {'channel_id': channel_id},  # Find the channel by ID
        {'$inc': {'edit_count': 1}},  # Increment the media edit count
        upsert=True  # If the channel doesn't exist, create a new one with edit_count = 1
    )
    return result.modified_count > 0  # Return True if update was successful

# Get total media edits across all channels
async def get_total_media_edits():
    total_edits = await media_edits.aggregate([
        {"$group": {"_id": None, "total": {"$sum": "$edit_count"}}}
    ]).to_list(length=1)
    
    if total_edits:
        return total_edits[0]['total']
    return 0  # Return 0 if no media edits are found

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

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr
