#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = '359150678-DAyroyYOpYkqLiCaNIok2M9KoY2fj1C4fxBO5v6R'
access_token_secret = 'zhTmAekrR0hcX4yfV4mRLVx1OQZMuIikj3dTvtfzghjAZ'
consumer_key = 'RE9RJs5c3zQ8yhLCZQCKlVglT'
consumer_secret = 'iA5ElxRl9JWm4wYDntSI2UxT56Yp6SpcDkAJ40EoDvMMFnWkfK'

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'ferguson'
    stream.filter(track=['ferguson'])
