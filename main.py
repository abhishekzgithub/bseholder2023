import pandas as pd
import re

class PromoterNGroup(object):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    
    def get_data(self):
        all_cols=self.tree.find_class('TTRow_right')
        all_cols=[re.sub(r"[\s+|,]", "", i.text_content()) for i in all_cols]
        return all_cols
    
    def parse_category_shareholder_enity_type(self,column_name):
        category_of_shareholder=[]
        entity_type=[]
        for ele in range(0,len(column_name),2):
            category_of_shareholder.append(column_name[ele])
            entity_type.append(column_name[ele+1])
        return category_of_shareholder,entity_type

    def get_right_column_data(self):
        righ_data_xpath=self.tree.find_class('TTRow_left')
        right_data=[(i.text_content()).encode('ascii', 'ignore').decode("utf-8") for i in (righ_data_xpath)]
        category_of_shareholder,entity_type=self.parse_category_shareholder_enity_type(right_data)
        return category_of_shareholder,entity_type
    
    def set_data(self):
        datum=self.get_data()
        category_of_shareholder,entity_type=self.get_right_column_data()
        data={}
        j=1
        matrix_size=int(len(datum)/len(category_of_shareholder))
        for i in range(0,len(datum),matrix_size):
            data[j]=datum[i:i+matrix_size]
            j+=1
        df=pd.DataFrame(data).T
        df.insert(0,"Entity Type",entity_type)
        df.insert(0,"Category of shareholder",category_of_shareholder)
        return df
    
    def set_column_name(self):
        col_name=self.cols
        return col_name
    
    def final_result(self):
        df=self.set_data()
        df.columns=self.set_column_name()
        return df.replace(r'^\s*$', 0, regex=True)