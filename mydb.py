from country import Country
from user import User
from post import Post
from job import Job
from song import Song
from centering import Centering
from chercherimage import Chercherimage
from sing import Sing
class Mydb():
  def __init__(self):
    print("hello")
    self.Country=Country()
    self.Job=Job()
    self.User=User()
    self.Song=Song()
    self.Post=Post()
    self.Centering=Centering()
    self.Chercherimage=Chercherimage
    self.Sing=Sing()
