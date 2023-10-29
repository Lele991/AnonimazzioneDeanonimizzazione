# -*- coding: utf-8 -*-

from funzioni import *

# inizializzazione processo di operazione da effettuare
print("- Per Anonimizzare il file digita 1\n- Per Deanonimizzare il file digita 0")
anonimizzazione = input("Processo da eseguire: ") # richiesta all'utente se vuole anonimizzare i file json oppure deanonimizzarli
anonimizzazione = True if anonimizzazione == "1" else False
    
nameFile1 = input("Inserisci il nome primo file: ") # esempio: logs_anonimizzato_1.json oppure logs_1.json
nameFile2 = input("Inserisci il nome secondo file: ") # esempio: logs_anonimizzato_2.json oppure logs_2.json 

# se è un processo di deanonimizzazione chiedo all'utente come si chiama il file
# con gli uuid assegnati ad ogni nome presente nei file
if not anonimizzazione:
    nameFile3 = input("Inserisci il nome del file con le utenze: ") # esempio: utenza.json
    dataFile3 = loadJson(nameFile3)
    for datas in dataFile3:
        listName.append(tuple([datas[0], datas[1]]))

# caricamento dei dati dai file json
dataFile1 = loadJson(nameFile1)
dataFile2 = loadJson(nameFile2)
        

# anonimizzazione o deanonimizzazione per il campo "Nome completo dell'utente" dei file inseriti in precedenza
replaceNameID(dataFile1, anonimizzazione)
replaceNameID(dataFile2, anonimizzazione)

# stampa dei nominativi con l'uuid assegnato
print("Nominativi presenti: " + ", ".join([str(str(name[1]) + " ("+str(name[0])+")") for name in listName]))

# rimozione campo "Utente coinvolto"
deleteKey(dataFile1, 2)
deleteKey(dataFile2, 2)

# salvataggio dei dati nei file json
saveJson(dataFile1, 'logs_1.json')
saveJson(dataFile2, 'logs_2.json')
saveJson(listName, 'utenza.json')