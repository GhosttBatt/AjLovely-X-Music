import random
import string
import os
from os import getenv
import time
import pymongo
from telethon import TelegramClient, events, Button
from pyrogram import Client, filters
from thumbnails import *
from fonts import *

# Use getenv for all sensitive/configurable values
API_ID = os.getenv("API_ID","26204186")
API_HASH = os.getenv("API_HASH", "c277a7f93583f68d0fdfdcb68f5fc6c0")
STRING_SESSION = os.getenv("STRING_SESSION", "BQGP2BoAP4JT-5wna5L_Z1nareUi02O8FEyUUn4VmOSrh71vWKcJoqazyJ4_LmSMMKR-9V7-3_QLUUa0YP02Nctpdu0v4ZdqiE-KldC1NtGYVloBBxF0lXMHlSGXstx5crc19uDGrnJiTs809TF70PkewPb9iHSp1mfTGI0nY-uzhJHgoKiyLlUgjWsLnDuNw66RQo2TrbAiNK0ZtGj1qfe7dTDYF0FFrh4gK7DkWck3B7KeGNNfEred5YRUOPTHp0OEq28cwNGHQNI6nVrdqDLDnZNV1xAtXhVoyTYYiZ12-tDjblYm8PX9l72JJluqvpyG7Pjarp8AAmc3WlPaqOWZJ32_YQAAAAHAItULAA")
GROUP = os.getenv("GROUP", "HeartBeat_Fam")
CHANNEL = os.getenv("CHANNEL", "HeartBeat_Offi")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8209706073:AAGayoWtC1Dqch1UbjAj8_-fo3GCbMrmZmI")
OWNER_ID = int(os.getenv("OWNER_ID", "8099828972"))
LOGGER_ID = os.getenv("LOGGER_ID", "2275616383")
mongodb = os.getenv("MONGODB_URI", "mongodb+srv://ghosttbatt:Ghost2021@ghosttbatt.ocbirts.mongodb.net/?retryWrites=true&w=majority")
# Working directory
ggg = os.getcwd()

# Initialize data structures
# Track start time
StartTime = time.time()

# Set up MongoDB connection
mongo_client = pymongo.MongoClient(mongodb)
db = mongo_client['voice']
user_sessions = db['user_sessions']
collection = db["users"]
