# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr

import motor.motor_asyncio
from config import Rkn_Bots

# Database connection setup
client = motor.motor_asyncio.AsyncIOMotorClient(Rkn_Bots.DB_URL)
db = client[Rkn_Bots.DB_NAME]
chnl_ids = db.chnl_ids
users = db.users

# Insert user data
async def insert(user_id):
    user_det = {"_id": user_id}
    try:
        await users.insert_one(user_det)
    except:
        pass

# Total user count
async def total_user():
    user = await users.count_documents({})
    return user

# Total channel count
async def total_channels():
    channels = await chnl_ids.count_documents({})
    return channels

# Get all users
async def getid():
    all_users = users.find({})
    return all_users

# Delete user
async def delete(id):
    await users.delete_one(id)

# Add or update button for a specific channel
async def addCap(chnl_id, button_data):
    dets = {"chnl_id": chnl_id, **button_data}
    await chnl_ids.insert_one(dets)

async def updateCap(chnl_id, button_data):
    await chnl_ids.update_one({"chnl_id": chnl_id}, {"$set": button_data})

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr
