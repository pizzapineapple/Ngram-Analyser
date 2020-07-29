import praw
from parsing import redditPass
import time

reddit = praw.Reddit(client_id="xpfNZWognqQokg",
                    client_secret="d5bW-geWORiEwWLizSb12PcM0-k",
                    user_agent="NGram Collector")

subredditName = "uwaterloo"
subreddit = reddit.subreddit(subredditName)
post = subreddit.hot(limit=1)


for submission in post :
    flattenedComments = submission.comments.list()
    #print(submission.comments)
    #print("Type         " + str(type(flattenedComments)))

moreCommentsTime = 0

for comment in flattenedComments :
    #print(comment.body)
    try :
        if(comment.body.strip() != "[deleted]") :
            redditPass(comment.body, comment.id, comment.score, int(comment.created_utc), None)
           
        """
            atributes to send forward:
                a refrence to lookup on reddit
                that its from reddit
                the actual ngrams
                score
                comment from date
                parent comment ids

                groupable data:
                    text
                    source -- reddit implied

                object data:
                    score
                    date
                    commment id
        """

    except AttributeError :
    #   print("\r")
        #print("\r")
        #print("more comments " + str(type(flattenedComments)))
        #print("\r")
        runtime = time.time()
        # print(type(time.time()))
        flattenedComments = comment.comments
        moreCommentsTime += (runtime - time.time())
        # print("More Comments")
        #type(flattenedComments)
        #print(flattenedComments)

print(moreCommentsTime)


#textParser = parser
