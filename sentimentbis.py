from typing import Counter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import tweepy
import pandas as pd
import matplotlib.pyplot as plt

#twitter api keys
auth = tweepy.OAuthHandler('XkKqFcDqgkZf6SbYgiLI30DBE', 'HWlmy0hBfszrQ0voWEWoUrwnU4oxQ5uVONbFSvT2WXIXHvjzV4')
auth.set_access_token('1050988734634749952-rTwT4cw1tquyJi8m8Fpw6vfoORnpH9', 'yt3YQgC8T0gs7XLBYYTlw4dUhVoit0tRIs2JlIbmDTvK0')

#function to run sentiment analysis. This function accepts a string
def sentiment_scores(sentence):

	sid_obj = SentimentIntensityAnalyzer()

	#gives sentiment analysis score
	sentiment_dict = sid_obj.polarity_scores(sentence)
	#prints the said score
	print("Overall sentiment dictionary is : ", sentiment_dict)
	print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
	print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
	print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")

	print("Sentence Overall Rated As", end = " ")
	#returns if the sentence was negative, neutral or positive
	if sentiment_dict['compound'] >= 0.05 :
		return("Positive")

	elif sentiment_dict['compound'] <= - 0.05 :
		return("Negative")

	else :
		return("Neutral")
#inputs the number of tweets to analyse
number_tweets = input("How many tweets do you want to analyse? ")

api = tweepy.API(auth,wait_on_rate_limit=True)
#declatre lists to use later
list1 = [None] * int(number_tweets)
list2 = [None] * int(number_tweets)
count = 0 	#count variable
keyphrase = input("For what do you want to run analysis? ")		#input a keyphrase to analyze
#setting for the analysis
for tweet in tweepy.Cursor(api.search_tweets,q=keyphrase,Counter=10,
                           lang="en",
                           since="2017-04-03").items(int(number_tweets)):
    print (tweet.created_at, tweet.text)
    list1[count] = tweet.text.encode('utf-8')
    list2[count] = sentiment_scores(str(list1[count]))
    count +=1
#print precentage of neutral, negative or positive tweets
print("\n% of neutral tweets: ", list2.count("Neutral")/int(number_tweets)*100, "%")
print("% of negative tweets: ", list2.count("Negative")/int(number_tweets)*100, "%")
print("% of positive tweets: ", list2.count("Positive")/int(number_tweets)*100, "%")


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
data = [list2.count("Neutral"), list2.count("Negative"), list2.count("Positive")]
names = ["Neutral", "Negatives", "Positive"]
# Creating plot
fig = plt.figure(figsize =(10, 7))
plt.pie(data, labels = names)
plt.show()
