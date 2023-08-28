from instagrapi import Client
from instagrapi.types import Usertag, Location
import config


cl = Client()
cl.login(config.username, config.password)

media_id = cl.media_id(cl.media_pk_from_url('https://www.instagram.com/p/CwSU0U4MZ4M/'))
omment = cl.media_comment(media_id, "@" + username)
media = cl.user_info_by_username('koala.pt').dict()
accs = list(media.values())[0]
followers = cl.user_followers(accs).keys()
x = range(600)
for i in x:
    username = cl.username_from_user_id(followers[i])
    comment = cl.media_comment(media_id, "@" + username)