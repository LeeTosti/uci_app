from pathlib import Path
import streamlit as st
import sys
import os
import pandas as pd


sys.path.insert(0, os.path.join(Path(__file__).parents[1]))

from mongo_connection import MongoConnection

grades = MongoConnection

df = pd.DataFrame(list(grades.student_grades.find()))

st.header('Grade Page')
st.write('''
         This page will search the database for grades by period.

         You will need to select the period to retrieve the corresponding grade.
         '''
         )

