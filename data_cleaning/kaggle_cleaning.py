import pandas as pd

def concate(words):
    res = ''
    l = len(words)
    for i in range (l):
        if res == '':
            res = words[i]
        else:
            res = res + ' ' + words[i]
    return res

pd.set_option('display.max_colwidth', None)
#pd.set_option('max_columns', None)

df = pd.read_csv(r"C:\Users\aliki\Desktop\NLP\cleaned_kaggle.csv")
hate_speech = df[df["hate_speech"] != 0]

tweets = df["tweet"].to_string(index=False)
#print(tweets)
sentences = tweets.split("\n")
#print(sentences)
clear_tweets = []
for sentence in sentences:
    words = sentence.split(" ")
    #print("words", words)

    if 'RT' in words:
        words.remove("RT")
    if '\"' in words:
        words.remove("\"")
    if '\'\'' in words:
        words.remove('')
    
    
    #print("sentence", sentence)
    for word in words:
        #word = word.encode(encoding='utf-8')
        #print(word)
        if '@' in word:
            words.remove(word)
            break
            
        if len(word) != 0 and (word[0] == "@" or word[0] == "&" or word[0:4] == 'http' or word[0:5] == "hymns"):
            #print("REMOVEEEE   ", word)
            words.remove(word)
        for i in range(len(word)):
            if word[i] != '!':
                break
            if i == len(word) - 1:
                words.remove(word)
    
    clear_tweet = concate(words)
    clear_tweets.append(clear_tweet)
    #words = tweet
    
df_clear = pd.DataFrame(clear_tweets)

    
#print(df_clear)

df["tweet"] = df_clear
df=df.loc[:,'count':'tweet']
print(df)

df.to_excel(excel_writer=r"C:\Users\aliki\Desktop\NLp\aaaaaa.xlsx")