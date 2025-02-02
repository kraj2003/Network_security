import os
import sys
import json
import certifi
from dotenv import load_dotenv
load_dotenv()

mongo_db_url= os.getenv("MONGO_DB_URL_KEY")

print(mongo_db_url)
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from Network_security.logging.logger import logging
from Network_security.exception.exception import NetworkSecurityException

class network_data_ext():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def csv_to_json(self,filepath):
        try:
            data=pd.read_csv(filepath)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records

        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def insert_data_toMongo(self,records,database,collections):
        try:
            self.database=database
            self.collection=collections
            self.records=records
            self.mongoclient=pymongo.MongoClient(mongo_db_url)
            self.database=self.mongoclient[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e,sys)

if __name__=="__main__":
    File_Path="Network_data\phisingData.csv"
    DATABASE="khushirajpurohit617"
    Collection="Network_data"
    networkobj=network_data_ext()
    records=networkobj.csv_to_json(filepath=File_Path)
    print(records)
    no_of_records=networkobj.insert_data_toMongo(records,database=DATABASE,collections=Collection)
    print(no_of_records)
