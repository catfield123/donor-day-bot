from aiogram.fsm.storage.mongo import MongoStorage
from common.mongo import client
from common.config import mongo_settings

user_fsm_storage = MongoStorage(client=client, 
                           db_name=mongo_settings.FSM_DB, 
                           collection_name="user_fsm_states",
                           )