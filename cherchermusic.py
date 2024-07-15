import requests
import urllib.request
from song import Song
from bs4 import BeautifulSoup
from chercherimage import Chercherimage
from unidecode import unidecode

class Cherchermusic():
    def __init__(self):
       self.someparams={"tbm":"isch"}
    def singularize(self,x):
       if x[-1] == "s":
           return x[0:-1]
       else:
         return x
    def searchcompos(self):
       html = requests.get("http://www.mp3classicalmusic.net/composerslist.htm", params=self.someparams)
       soup = BeautifulSoup(html.text, 'html.parser')
       malist=soup.select("a[href*=Composers]")
       for x in malist:
           #print(x)
           if x:
             xx=(str(x).split(">")[1].split("<")[0])
             if len(xx) > 0 and xx != ")":
               print(xx)
    def searchmusic(self):
       for x in list("azertyuiopmlkjhgfdsqwxcvbn"):
         html = requests.get("http://instrumentsdumonde.fr/az/instrument-"+x+".html", params=self.someparams)
         soup = BeautifulSoup(html.text, 'html.parser')
         malist=soup.select("[class=thumb]")
         #unidecode("instrument vnt")
         for x in malist:
             try:
               print(x)
               if x != "None" and x is not None and type(x).__name__ != "NoneType":
                   somesoup=(x["title"].split(":")[1])
                   if Song().getbyname(somesoup) is None:
                   #somesoup = str(x).split(">")[1].split("<")[0]
                     xx="http://instrumentsdumonde.fr/instrument/sons/"+self.singularize(unidecode(somesoup.strip().replace(" à","").replace(" ","_")))+".mp3"
                     print(xx)
                     opener=urllib.request.build_opener()
                     opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582')]
                     urllib.request.install_opener(opener)
                     filename=xx.split("/")[-1]
                     urllib.request.urlretrieve(xx, f'./uploads/'+filename)
                     pic=Chercherimage(somesoup).dlpic()
                     #print({"title":somesoup, "filename":filename})
                     Song().create({"artist":"artist","title":somesoup, "filename":filename,"image":pic["nom"]})
                   else:
                     print("exist deja")
               else:
                   print("uknhk")
             except:
               print("lettre"+str(x))

Cherchermusic().searchmusic()


