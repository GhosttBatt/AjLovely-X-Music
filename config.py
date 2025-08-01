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
STRING_SESSION = os.getenv("STRING_SESSION", "BQGP2BoAny3jHaKC1IiWLUMScYpYEXgPHmkXtz9M0CihxUGngp1cqNFuixfYyNNToLGVe4LOfqQPMEhZ1iAEbLgvRXJ7tR-IEeoGmaxFQ8M96zpxzYxYgPMQyOlJ84tS_eA4EGX8AUNQqow1RVpwU9fBLZiYzQ0Hfd1Lxo3r9hAM3CqHbEtvLvbOmcnI_X0bb8iqIsUcM2bPh8tB9M8lER9mbZz1ApxccwlG_x0Uu5nPqvD5_ze3x9IWQQ3pIngx5yGd0huDRGHLDPtEHzonIz8TCEv96rKfuXdrkif8fj1DeKXMhuxFGX29pWL3WlOCKFqneDtFM1GzYPGTovS0VYiIIjZmIQAAAAHAItULAA")
GROUP = os.getenv("GROUP", "HeartBeat_Fam")
CHANNEL = os.getenv("CHANNEL", "HeartBeat_Offi")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8209706073:AAH8stU0NeX1IoqTdfAzfVTBQVOzDU5nHDc")
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
