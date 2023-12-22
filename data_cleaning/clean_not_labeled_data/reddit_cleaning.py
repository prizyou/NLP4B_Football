import pandas as pd


input_file_and_path = r'C:\Users\aliki\Desktop\NLP\redditComments_Ali.csv'
file_encoding = 'utf8'        # set file_encoding to the file encoding (utf8, latin1, etc.)
input_fd = open(input_file_and_path, encoding=file_encoding, errors = 'backslashreplace')
df = pd.read_csv(input_fd)

#df = pd.read_csv(filepath_or_buffer=r'C:\Users\aliki\Desktop\NLP\redditComments_Ali.csv')
 

pd.set_option('display.max_colwidth', None)
#df.style.set_properties(**{'text-align': 'left'})

df.columns = ['index', 'comment']

#print(df.columns.values)
#print('SSSSSSSSSSSSS')
#print(df.head(10))
#print('DDDDDDDDDDDDDDDDDD')
#df = df[df.iloc[15]]
#print(type(df))

new_list = []
tweets = df["comment"].to_string(index=False)
#print(tweets)
sentences = tweets.split("\n")
for sentence in sentences:
    new_list.append(sentence)
  
    
print(new_list)
df = pd.DataFrame(new_list)
    #sentence = sentence.encode('ASCII')

df.to_excel('AAAA.xlsx')