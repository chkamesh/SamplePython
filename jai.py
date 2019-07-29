#!/usr/bin/env python
# coding: utf-8

# In[2]:


"jai"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

#D:\python\Prob\UserIdToGenderTrain.csv
#D:\python\Prob\UserIdToGenderTest.csv
#D:\python\Prob\UserIdToUrl\part-00000
#D:\python\Prob\Urls_Json_Data.txt

UserIdToGenderTrainKey='UserIdToGenderTrain.csv'
UserIdToGenderTestKey='UserIdToGenderTest.csv'
UrlsJsonDataKey='Urls_data.txt'
Part1='UserIdToUrl\part-00003'

TrnFile=pd.read_csv(UserIdToGenderTrainKey)
TstFile=pd.read_csv(UserIdToGenderTestKey)

#UrlsJsonDataFile=pd.read_json(UrlsJsonDataKey)
#UserIdToGenderTrain.head()



def readFile(fileName,countLines):
    i=0
    df=pd.DataFrame()
    with open(fileName,'rb') as f:
        for line in f.readlines():
            i=i+1
            if i==2:
                df=pd.DataFrame((line.decode("utf-8")).split(','))
            if i > 2:
                stArr=(line.decode("utf-8")).split(',')
                print(stArr)
                df=df.append(stArr)
                if i == countLines:
                  break
    return df

GenderTrainDf=pd.DataFrame(TrnFile)
GenderTestDf=pd.DataFrame(TstFile)

TrnUserIdsLst=GenderTrainDf['userid'].values
TrnGenderLst=GenderTrainDf['gender'].values
TstUserIdsLst=GenderTestDf['userid'].values
print(readFile(Part1,10))

def removeFromSpecialChar(item):
    itemExt=item
    print(itemExt)
    if '(' in item:
        itemExt=itemExt[:itemExt.find('(')]
        print(itemExt)
    if '.' in item:
        itemExt=itemExt[:itemExt.find('.')]
        print(itemExt)
    if '[' in item:
        itemExt=itemExt[:itemExt.find('[')]
        print(itemExt)
    return itemExt
df.applymap(removeFromSpecialChar)
#unique_test_data=test_data.drop_duplicates(subset=None, keep='first', inplace=False)
#unique_test_data_cleaned= [w.replace('\r', ' ') for w in unique_test_data_cleaned]
