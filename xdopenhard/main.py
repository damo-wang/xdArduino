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
import git

df=pd.read_excel('data/data.xlsx',sheet_name='Sheet1',header=1,index=False)

df=df.drop_duplicates(subset=['姓名'],keep='last')
count1=0
count2=0
for i,row in df.iterrows():
    if(re.search("^git.*git$",row['仓库地址'])):
        print(str(row['序号'])+row['姓名']+':'+row['仓库地址']+' OK')
        repo=git.Repo.clone_from(url=row['仓库地址'],to_path=row['姓名'])        
        count1=count1+1
        continue 
    else:
        print(str(row['序号'])+row['姓名']+':'+row['仓库地址'])
        count2=count2+1
print('合格:', count1,'人')
print('不合格:', count2,'人')
