import requests
from chaine import Chaine
from bs4 import BeautifulSoup
import urllib.request
import urllib

class Chercherimage():
    def __init__(self,q):
       self.someparams={"q":q,"tbm":"isch"}
       print(q,"q")
    def search(self):
       html = requests.get("https://www.google.com/search", params=self.someparams)
       soup = BeautifulSoup(html.text, 'html.parser')
       malist=soup.select("img")
       malist.pop(0)
       wow=[]
       ye={}
       for k in malist:
           ye={}
           ye["src"]=k["src"]
           ye["q"]=self.someparams["q"]
           wow.append(ye)
       return wow
    def dlpic(self):
       ok=self.search()
       ok1=[]
       xx={"src":"","q":"","nom":""}
       if len(ok) > 0:
           xx=ok[0]
           opener=urllib.request.build_opener()
           opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582')]
           urllib.request.install_opener(opener)
           filename=xx["src"].split("/")[-1].split("?")[0]
           nom=Chaine().fichier(filename)
           urllib.request.urlretrieve(xx["src"], f'./uploads/'+nom)
           xx["nom"]=nom
           return xx
       else:
           return xx
           

