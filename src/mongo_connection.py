from dotenv import load_dotenv
import pymongo
import os
import certifi

class MongoConnection:
    def __init__(self):
        load_dotenv()
        self.__mongo_url = os.getenv('MONGO_URL')
        self.client = pymongo.MongoClient(self.__mongo_url, tlsCAFile=certifi.where())
        self.db = self.client.db 
        self.student_grades = self.db.student_grades

if __name__ == '__main__':
    c = MongoConnection()
    print('You are connected!')