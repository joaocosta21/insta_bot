from instagrapi import Client
import config

cl = Client()
cl.login(config.username, config.password)

media_id = cl.media_id(cl.media_pk_from_url('https://www.instagram.com/p/BXyGGl8BhoK/'))
media = cl.user_info_by_username('koala.pt').dict()
accs = list(media.values())[0]
followers = list(cl.user_followers(accs))
# x = range(600)
# for i in x:
username = cl.username_from_user_id(followers[1])
print(username)
try:
    bot_account = cl.account_info()
except:
    cl.relogin()
comment = cl.media_comment(media_id, "@" + username)