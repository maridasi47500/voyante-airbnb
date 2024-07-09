import json
from fichier import Fichier
from musicalinstrument import Musicalinstrument
dbPays=Musicalinstrument()
x=json.loads(Fichier("./","music.json").lire())
for pays in x["instruments"]:
    name=""
    unicode=""
    
    try:
        name=pays["name"]
    except:
        name=""
    try:
        unicode=pays["icon"]
    except:
        unicode=""
    dbPays.create({"name":name,"unicode":unicode})
