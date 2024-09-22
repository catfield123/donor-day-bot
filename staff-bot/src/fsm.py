from aiogram.fsm.storage.mongo import MongoStorage
from common.mongo import client
from common.config import mongo_settings

staff_fsm_storage = MongoStorage(client=client, 
                           db_name=mongo_settings.FSM_DB, 
                           collection_name="staff_fsm_states",
                           )