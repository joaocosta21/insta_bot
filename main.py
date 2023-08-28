from instagrapi import Client
from instagrapi.types import Usertag, Location
import config


cl = Client()
cl.login(config.username, config.password)

media_id = cl.media_id(cl.media_pk_from_url('https://www.instagram.com/p/CwSU0U4MZ4M/'))
comment = cl.media_comment(media_id, "@")
