from instagrapi import Client
import config

cl = Client()
cl.login(config.username, config.password)

#get media via link
media_id = cl.media_id(cl.media_pk_from_url('https://www.instagram.com/p/BXyGGl8BhoK/'))
#get username via string
media = cl.user_info_by_username('koala.pt').dict()
accs = list(media.values())[0]
#get follower list
followers = list(cl.user_followers(accs))
# x = range(600)
# for i in x:
username = cl.username_from_user_id(followers[1])
print(username)
#check if you are still logged if not relog
try:
    bot_account = cl.account_info()
except:  # bad programming habit
    cl.relogin()
#finally comment
comment = cl.media_comment(media_id, "@" + username)