from textblob import TextBlob
import sys,tweepy
import matplotlib.pyplot as plt

def percentage(part,whole):
    return 100*float(part)/float(whole)

consumerKey="yWKMZj6LwwjwT3LM7ZSYlJmAd"
consumerSecret="QY0lK9dBMdz7FtexOEkFQCwJZcsLSNVIlnVITG5J1rlB9DeDwC"
accessToken="843384274153865216-uVQBeGYb1GkGmHgViJmDyLNg7ycGLge"
accessTokenSecret="XHg6OiWwlx9R0uCDU34sscZ16lqhpzmaLQWB2hhCtTfWX"

auth = tweepy.OAuthHandler(consumerKey,consumerSecret);
auth.set_access_token(accessToken,accessTokenSecret)
api =tweepy.API(auth)

searchTerm= input("Enter keyword or hashtag to search:")
noOfTerms = int(input("Enter no of tweets to analyse:"))

tweets = tweepy.Cursor(api.search,q=searchTerm,lang="English").items(noOfTerms)

positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
    #print(tweet.text)
    analysis=TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if(analysis.sentiment.polarity == 0 ):
        neutral +=1
    elif (analysis.sentiment.polarity < 0):
        negative +=1
    elif (analysis.sentiment.polarity > 0.00):
        positive +=1

positive = percentage(positive,noOfTerms)
negative = percentage(negative,noOfTerms)
neutral = percentage(neutral,noOfTerms)
polarity = percentage(polarity,noOfTerms)

positive = format(positive,'.2f')
negative = format(negative,'.2f')
neutral = format(neutral,'.2f')

print("How people are reacting on "+searchTerm+" by analyzing "+str(noOfTerms)+" tweets")

if(polarity == 0.00):
    print("Neutral")
elif (polarity < 0.00):
    print("Negative")
elif(polarity > 0.00):
    print("Positive")

labels = ['Positive ['+str(positive)+'%]','Neutral ['+str(neutral)+'%]','Positive ['+str(negative)+'%]']
sizes = [positive,neutral,negative]
colours = ['yellowgreen','gold','red']

patches,texts = plt.pie(sizes,colours,startanagle=90)
plt.legend(patches,labels,loc="best")
plt.title("How people are reacting on "+searchTerm+" by analyzing "+str(noOfTerms)+" tweets")
plt.axis('equal')
plt.tight_layout()
plt.show()

