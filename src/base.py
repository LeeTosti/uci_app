import pandas as pd
from pathlib import Path

class Base:
    '''
    
    '''

    def __init__(self):
        self.get_data()
        self.clean_data()

    def get_data(self):
        folder_dir = f'{Path(__file__).parents[0]}/data'
        df_mat = pd.read_csv(f'{folder_dir}/student-mat.csv', delimiter= ';')
        df_por = pd.read_csv(f'{folder_dir}/student-por.csv', delimiter= ';')
        self.df = pd.concat([df_mat, df_por], axis=0)
        self.df = self.df.reset_index(drop=True)
        self.df.columns = self.df.columns.str.lower()
    
    def clean_data(self):
        boolean_values= {'yes': True, 'no': False}
        for col in self.df.columns:
            self.df[col] = self.df[col].replace(boolean_values)



if __name__ == '__main__':
    c = Base()
    print(c.df)