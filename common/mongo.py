from motor.motor_asyncio import AsyncIOMotorClient
from common.config import mongo_settings

client = AsyncIOMotorClient(mongo_settings.mongo_url)