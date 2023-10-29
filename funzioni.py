import json
import string
import random
import os

listName = []

# verifico e nel caso creo la directory data che conterrà i file elaborati da caricare e da salvare
if not os.path.exists("data"):
    os.makedirs("data")

# recupero il path in cui è presente il file python eseguito
dirname = os.path.dirname(os.path.abspath(__file__)) + "\\data\\"

# funzione di caricamento del file json
def loadJson(nameFile):
    file = open(dirname + nameFile)
    dataFile = json.load(file)
    file.close()
    return dataFile

# funzione di salvataggio del file json
def saveJson(dataFile, nameFile):
    with open(dirname + nameFile, 'w') as f:
        json.dump(dataFile, f, indent=2)

# funzione per generare l'uuid di lunghezza di 6 caratteri (caratteri e numeri) con ultimo valore un progressivo
def generateUUID(progressivo, lung=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(lung)) + str("-" + str(progressivo))

# funzione per eliminare elemento nella posizione specificata in tutte le strutture
def deleteKey(data, key):
    for datas in data:
        del datas[key]

# funzione per verificare se esiste già un UUID al nominativo (nel caso lo restituisce) oppure
# se deve deanonimizzare restituisce nominativo assegnato al UUID che sta verificando
def existID(nome, anonimizzazione):
    idx = None
    for nomeX in listName:
        if nome in nomeX[1] or nome in nomeX[0]:
            idx = nomeX[0] if anonimizzazione else nomeX[1]
            break
    return idx

# funzione per anonimizzare / deanonimizzare del campo "Nome completo dell'utente" 
def replaceNameID(data, anonimizzazione):
    idx = 1
    index = len(listName) if len(listName) > 0 else 1 # verifico id di partenza
        
    for datas in data:
        progressivo = existID(datas[1], anonimizzazione)
        if progressivo == None:
            progressivo = generateUUID(idx) # genero il mio uuid oppure lo recupero se mi trovo nella fase di deanonimizzazione
            if anonimizzazione:
                listName.append(tuple([progressivo, datas[1]])) #salva la lista dei nomi e il loro identificativo
            idx += 1
        datas[1] = progressivo