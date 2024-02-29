from os import getenv
import pandas as pd
from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database():
    def __init__(self):
        # gathering URL with mongodb code
        load_dotenv()
        url = getenv('DB_URL')
        # connect to MongoDB with url and select bandersnatch project
        self.database = MongoClient(url, tlsCAFile=where())["Bandersnatch"]
        # go to the monsters collection in the database
        self.collection = self.database.get_collection("monsters")

    def seed(self, amount):
        # create a list to hold monsters
        monster_list = []

        # populate the list with as many monsters specified in amount
        for i in range(0, amount):
            monster = Monster()
            monster_list.append(monster.to_dict())

        # insert the list into the collection
        self.collection.insert_many(monster_list)

    def reset(self):
        # delete all the entries in the collection
        self.collection.delete_many({})

    def count(self) -> int:
        # count entries in the collection
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        # make the collection into a DataFrame
        return pd.DataFrame(list(self.collection.find()))

    def html_table(self) -> str:
        # adjusting start index to one for more friendly interface
        db = self.dataframe()
        db.index = range(1, len(db) +1 )
        # transform the dataframe that pulls from MongoDB into an HTML table
        return db.to_html()
