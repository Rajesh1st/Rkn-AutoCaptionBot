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

# insert user data
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

# Add this new function to count edited messages globally
async def increment_edit_count(chnl_id):
    await chnl_ids.update_one(
        {"chnl_id": chnl_id},
        {"$inc": {"edited_count": 1}},  # Increment by 1 each time a message is edited
        upsert=True  # If channel doesn't exist, it will be created
    )

# Function to get total number of edits for all channels
async def total_edits():
    total_edits = await chnl_ids.aggregate([
        {"$group": {"_id": None, "total_edits": {"$sum": "$edited_count"}}}
    ]).to_list(length=1)  # This will return the total edited message count
    return total_edits[0]["total_edits"] if total_edits else 0


# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr
