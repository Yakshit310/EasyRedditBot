import praw
import config

def bot_login():
    r = praw.Reddit(username = config.username,
        password = config.password,
        client_id = config.client_id,
        client_secret = config.client_secret,
        user_agent = "NOOBCyPhER's dog comment responder v0.1")

    return r

def run_bot(r):
    print("obtainng 25 comments ....")
    for comment in r.subreddit("test").comments(limit=25):
        if "dog" in comment.body:
            print('"String with "dog" found"')
            comment.reply("I also love dog! [Here](https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=1.00xw:0.669xh;0,0.190xh&resize=1200:*) is an image of one!")

r = bot_login()

run_bot(r)