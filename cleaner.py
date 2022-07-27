 #Data-Set-auto-cleaner
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df=pd.read_csv("mldata/roi.csv",encoding = "ISO-8859-1") 


def dupskate():

    
    dups=df.duplicated()
    dup=0
    dupn=-1
    dupx=''
    duplicated = list()
    for i in dups:
        dupn=dupn+1
        if i == True:
            dup=dup+1
            duplicated.append(dupn)
    duplicated_columns=df.iloc[duplicated,:]
    #df.drop_duplicates(inplace=True)
    #df.reset_index(inplace=True,drop=True)
    return duplicated_columns 





def void():
    
  
    columns_1=df.shape
    columns=int(columns_1[1]-1)
    z=""
    c="None"
    nrow = list()
    count=0
    for i in range(columns):
        count=count+1
        for x in df.index:
            if str(df.iloc[x,count]) =="nan":
                nrow.append(x)
                z=pd.DataFrame(nrow).drop_duplicates()
    z
    if len(z)<1:
        print("Zero Null")
    else:
            y=z.iloc[:,0]
            c=df.iloc[y,:]
    return c

