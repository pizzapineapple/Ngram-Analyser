import praw
from parsing import redditPass
import time

reddit = praw.Reddit(client_id="xpfNZWognqQokg",
                    client_secret="d5bW-geWORiEwWLizSb12PcM0-k",
                    user_agent="NGram Collector")

def setLoad(*args) :
    subredditName = args[0]
    method = args[1]
    size = args[2]

    subreddit = reddit.subreddit(subredditName)

    if method == "hot": 
        post = subreddit.hot(limit=size)
    elif method == "top": 
        post = subreddit.top(limit=size)
    elif method == "new": 
        post = subreddit.new(limit=size)
    else: 
        return None #an invalid format type was specified

    for submission in post :
        flattenedComments = submission.comments.list()
        #print(submission.comments)
        #print("Type         " + str(type(flattenedComments)))

    moreCommentsTime = 0

    for comment in flattenedComments :
        # print(comment.body)
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
            runtime = time.time()
            flattenedComments = comment.comments
            moreCommentsTime += (runtime - time.time())
        break
    # print(moreCommentsTime)


    #textParser = parser
