import pandas as pd
import emoji
#import sklearn
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel(r'c:\Users\aliki\Desktop\NLP\model\labeled_data.xlsx')

print(df.head())

#Demojizing
demojized = []
for i in df.index:
    demojized.append(emoji.demojize(df['comment'][i]))
    
df['comment'] = demojized

df.to_csv(path_or_buf=r'c:\Users\aliki\Desktop\NLP\model\labeled_normalized_data.csv')
