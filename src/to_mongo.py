from base import Base
import pymongo
import os
from dotenv import load_dotenv
import certifi

class ToMongo(Base):
    '''
    
    '''

    def __init__(self):
        Base.__init__(self)
        load_dotenv()
        self.__mongo_url = os.getenv('MONGO_URL')
        self.client = pymongo.MongoClient(self.__mongo_url, tlsCAFile=certifi.where())
        #database
        self.db = self.client.db 
        #collection
        self.student_grades = self.db.student_grades
   

    def upload_one_by_one(self):
        for i in self.df.index:
            self.student_grades.insert_one(self.df.loc[i].to_dict())

    def upload_collection(self):
        self.student_grades.insert_many([self.df.to_dict()])

    def drop_collection(self):
        self.db.student_grades.drop()

if __name__ == '__main__':
    c = ToMongo()
    print('You are connected!')
    c.drop_collection()
    print('Previous Collections Dropped')
    c.upload_one_by_one()
    print('Successfully Uploaded All Grades to MongoDB')
        
