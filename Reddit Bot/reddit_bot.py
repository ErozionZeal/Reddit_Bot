import praw
import config
import time


def bot_login():
  print('Logging in...')
  r = praw.Reddit(username = config.username,
              password = config.password,
              client_id = config.client_id,
              client_secret = config.client_secret,           user_agent = "ErozionZeal's Yang comment responder"
            )
  print('Logged in!')
  return r

def run_bot(r,comments_replied_to):
  print('Obtaining comments')
  count = 0 
  comments_replied_to_now = []
  for comment in r.subreddit('politics').comments(limit=500):
    if 'Bernie' in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
      comment.reply("Bernie may have been totally correct 10 years but we need a leader for the 21st century. Andrew Yang is who we'd need in this 21st century economy.")
      
      count += 1
      comments_replied_to.append(comment.id)
      with open("comments_replied_to.txt","a") as f:
          f.write(comment.id + '\n')
      comments_replied_to_now.append(comment.id)
  print('You have replied to '+ str(comments_replied_to_now))
  print('You have replied to '+str(count)+' comments')
  time.sleep(10)

def get_saved_comments():
  with open("comments_replied_to.txt",'r') as f :
    comments_replied_to = f.read()
    comments_replied_to = comments_replied_to.split("\n")
  return comments_replied_to

comments_replied_to = get_saved_comments()

while True:
  r = bot_login()
  run_bot(r,comments_replied_to)