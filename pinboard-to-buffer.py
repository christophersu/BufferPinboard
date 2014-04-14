import pinboard
import PinboardCredentials
import BufferCredentials
from datetime import date, timedelta

p = pinboard.open(token=PinboardCredentials.PINBOARD_API_TOKEN)
# posts = p.posts(fromdt=p["last_updated"]) # only get content since last run
pastdays = date.today() - timedelta(3)
posts = p.posts(fromdt=pastdays)
print posts

from pprint import pprint as pp
from colorama import Fore
from buffpy.models.update import Update
from buffpy.managers.profiles import Profiles
from buffpy.managers.updates import Updates
from buffpy.api import API

token = BufferCredentials.BUFFER_APP_TOKEN

api = API(client_id=BufferCredentials.BUFFER_CLIENT_ID,
          client_secret=BufferCredentials.BUFFER_CLIENT_SECRET,
          access_token=token)

profile = Profiles(api=api).filter(service='twitter')[0]
print profile.updates.pending