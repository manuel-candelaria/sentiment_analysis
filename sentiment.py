#pip install TextBlob

#import TextBloob
from textblob import TextBlob

text = "Susana made me angree"

obj = TextBlob(text)


#return the sentiment of text by returnting a value between -1 and 1
sentiment = obj.sentiment.polarity

print(text)
print(sentiment)