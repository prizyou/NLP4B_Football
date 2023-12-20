import pandas as pd 

df = pd.read_excel(r'C:\Users\aliki\Desktop\NLP\reddit_clean_not_labeled.xlsx', index_col=0)

print(df.columns.values)

df.to_csv(r'C:\Users\aliki\Desktop\NLP\aaaaaa.csv')