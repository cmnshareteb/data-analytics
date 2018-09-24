from textblob import TextBlob
import sys,tweepy


def percentage(part,whole):
    return 100*float(part)/float(whole)

consumerKey=""
consumerSecret=""
accessToken=""
accessTokenSecret=""

auth = tweepy.OAuthHandler(consumerKey,consumerSecret);
auth.set_access_token(accessToken,accessTokenSecret)
api =tweepy.API(auth)

searchTerm=raw_input("Enter keyword or hashtag to search:")
noOfTerms=int(raw_input("Enter no of tweets to analyse:"))

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



