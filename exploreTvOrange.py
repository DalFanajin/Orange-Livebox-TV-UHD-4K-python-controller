"""
Ce module me sert à explorer les possibilités de l'api. Il me permet de trouver à l'aveugle des modes, keys, epg_ids...
Il nécessite les modules suivants : requests, sys, getopt

Développé et testé pour le décodeur TV UHD 4K Orange :
	Modèle : Livebox Fibre
	Version de firmware : 1.12.16
	Version de firmware Orange : g0-f-fr)
	
Développé et tester sur un système connecté au même réseau local que le décodeur TV :
	Dans cet exemple, l'adresse IP de mon décodeur est fixe et son addresse locale est 192.168.1.12
	La variable globale 'URL' doit être modifiée pour accueillir l'addresse locale de votre décodeur.
	
Un grand merci à tous les contributeurs du topic à cette addresse :
https://communaute.orange.fr/t5/TV-par-ADSL-et-Fibre/API-pour-commander-le-decodeur-TV-depusi-une-tablette/td-p/43443

Je suis loin d'être un expert des technologies utilisées par ce module : il peut présenter des erreurs, être incomplet, etc.
N'hésitez pas à le modifier, l'adapter, le partager, et l'utiliser quel que soit le contexte.

Je vous serais reconnaissant de me transmettre les éventuelles améliorations/corrections à y apporter sur le repository github : https://github.com/DalFanajin/Orange-Livebox-TV-UHD-4K-python-controller

Etant donné que le décodeur est exclusivement français, je n'ai pas prévu de traduction anglaise pour cette docstring : si elle est nécessaire, n'hésitez pas à me solliciter.
This decoder is a french product, so I didn't translate this docstring in english : do not hesitate to ask if you need a translation anyway.
"""

# importing the requests library 
import requests, sys, getopt, time

# api-endpoint 
URL = "http://192.168.1.12:8080/remoteControl/cmd"

def explore_keys():
	for key in range(1,1000):
		print("On lance l'opération 1, appui simple, touche %s"%key)
		PARAMS = {'operation':1, 'key':key, 'mode':0} 
		
		r = requests.get(url = URL, params = PARAMS)
	
		getFullResult(r.json())
		
		waitForUser("Press enter to continue")
		
		print("On lance l'opération 1, appui long (200ms), touche %s"%key)
		print("On appuie")
		PARAMS = {'operation':1, 'key':key, 'mode':1} 
		
		r = requests.get(url = URL, params = PARAMS)
	
		getFullResult(r.json())
		
		time.sleep(0.2)
		
		print("On relache")
		PARAMS = {'operation':1, 'key':key, 'mode':2} 
		
		r = requests.get(url = URL, params = PARAMS)
	
		getFullResult(r.json())
		
		waitForUser("Press enter to continue")
		
def fast_explore_simple_keys_except_list():
	notin = [116,512,513,514,515,516,517,518,519,520,521,402,403,115,114,113,103,108,105,106,352,158,139,164,168,159,167,393,1,28,72,75,77,80,166,207,208,365,407,408,412,529,582]
	for key in range(1,1001):
		if key not in notin :
			print("On lance l'opération 1, appui simple, touche %s"%key)
			PARAMS = {'operation':1, 'key':key, 'mode':0} 
			
			r = requests.get(url = URL, params = PARAMS)
		
			getFullResult(r.json())
		
		
def explore_modes():
	for mode in range(1,1001):
		print("On lance l'opération %s"%mode)
		PARAMS = {'operation':mode} 
		
		r = requests.get(url = URL, params = PARAMS)
	
		if getFullResult(r.json()) == "ok":
			waitForUser("Press enter to continue")

def explore_epg_ids():
	#Bruteforcé jusqu'à 11000, à reprendre une nuit 
	for epg_id in range(11000,9999999999):
		epg_code = (10 - len(str(epg_id))) * '*' + str(epg_id)
		print("On lance la chaine d'EPG %s"%epg_code)
		PARAMS = {'operation':9, 'epg_id':epg_id,'uui':1} 
		
		loop = True
		
		while loop:
			r = requests.get(url = URL, params = PARAMS)
		
			if getFullResult(r.json()) == "ok":
				if waitForUser("Press enter to continue, some other key to try again") == '':
					loop = False
			
			else :
				loop = False
				
	
def getFullResult(data):
	resultCode = data['result']['responseCode'] 
	resultMessage = data['result']['message'] 
	resultData = data['result']['data'] 
	print("Code réponse:%s\nMessage:%s\nDonnées:%s"%(resultCode, resultMessage,resultData)) 
	return resultMessage

def waitForUser(text):
	return input(text)
	
if __name__ == "__main__":
	fast_explore_simple_keys_except_list()