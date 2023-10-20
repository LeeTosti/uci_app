#import pandas as pd
#from pathlib import Path
#from base import Base
#from to_mongo import ToMongo
#import re
#import spacy
#from sklearn.pipeline import make_pipeline
#from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.neighbors import NearestNeighbors
#import pickle
#
#folder_dir = f"{Path(__file__).parents[0]}/data"
#
#Base().df.to_csv(f'{folder_dir}/merged_students.csv', index=False)
#print('Saved Student Records Data to CSV File')
#
#ToMongo().drop_collection()
#print('Successfully Dropped all Items in Collection')
#ToMongo().upload_one_by_one()
#print('Successfully Updated Collection with New Data')
#
#df = pd.read_csv(f'{folder_dir}/merged_students.csv', low_memory=False)
#print('Created the DataFrame object')
#
##No null values or empty strings so no values need to be dropped
##Data has already been clead so no need for regex to remove non alpha numeric
#
#df['lemmas'] = lemmas

