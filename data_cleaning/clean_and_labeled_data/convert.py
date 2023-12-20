import pandas as pd

df = pd.read_excel(r"C:\Users\Burak\Desktop\workspace\NLP4B_Football\data_cleaning\clean_and_labeled_data\Kaggle_clean_and_labeled.xlsx",index_col=0)

print(df)
#print(df.columns.values)




df.to_csv(path_or_buf=r"C:\Users\Burak\Desktop\workspace\NLP4B_Football\data_cleaning\clean_and_labeled_data\kaggle_clean_and_labeled.csv")