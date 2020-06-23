#!/bin/python3
# 1. open xlsx to pandas
# 2. get all user/repository
# 3. find all right and wrong user and repos
# 4. if right, get all file ,count four dir and two file(readme & summary)
# 5. reserved for continue.

from github import Github
import pandas as pd
import numpy as np
import re

df=pd.read_excel('data/data.xlsx',sheet_name='Sheet1',header=1,index=False)

df=df.drop_duplicates(subset=['姓名'],keep='last')
for i,row in df.iterrows():
    if(re.search("^git.*git$",row['项目地址'])):
        continue 
    else:
        print(row['姓名']+':'+row['项目地址'])



