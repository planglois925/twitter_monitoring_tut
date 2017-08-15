import tweepy
from tweepy.streaming import StreamListener


def main():
    print "[] Twitter monitoring starting"

    # these are the values associated with the both the application and consumer
    ckey = ""
    csecret = ""
    atoken = ""
    asecret = ""


    #create the auth object leveraging the client key + client secret
    auth = tweepy.OAuthHandler(ckey, csecret)

    #set the application token + application secret to the new auth object
    auth.set_access_token(atoken, asecret)

    # now that we have our authentication set, we can connect  to the API
    api = tweepy.API(auth)

    # the listener the API
    listener = Listener(api)


    #when our powers combine, twitter allows us to connect!
    streamer = tweepy.Stream(auth=auth, listener=listener)
    print '[] Twitter successfully connected'

    #intrim use of track, we'll make sure this value is pulled down from a file in the final version

    track = ['test','awesome','hello','world']
    streamer.filter(track=track)





# we need to extend the listener class from Tweepy and build upon it
class Listener(StreamListener):

    def __init__(self, api=None):
        self.api = api or tweepy.API()

    #simple proof of concept
    def on_status(self, status):

        #json_data = json.loads(status)
        print '%s tweeted something' % status.user.name



if __name__ == '__main__':
    main()
