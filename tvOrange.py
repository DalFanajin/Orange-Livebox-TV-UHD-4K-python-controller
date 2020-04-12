"""
Ce module permet de contrôler le décodeur TV orange via la ligne de commande Unix d'un système.
Il nécessite les modules suivants : requests, sys, getopt

Développé et testé pour le décodeur TV UHD 4K Orange :
	Modèle : Livebox Fibre
	Version de firmware : 1.12.16
	Version de firmware Orange : g0-f-fr)
	
Développé et tester sur un système connecté au même réseau local que le décodeur TV :
	Dans cet exemple, l'adresse IP de mon décodeur est fixe et son addresse locale est 192.168.1.12
	La variable globale 'URL' doit être modifiée pour accueillir l'addresse locale de votre décodeur.
	
Options :
	-h ou --help :
		Optionnel.
		Sans argument.
		Permet d'afficher cette docstring.
		
	-v ou --verbose :
		Optionnel.
		Sans argument.
		Permet d'afficher les informations écrites dans la console par la méthode 'printVerbose', utilisée pour afficher les informations de déroulement du programme.
		
	-o ou --operation :
		Obligatoire.
		Spécifie l'instruction à envoyer au décodeur TV.
		
		Valeurs possibles :
			[10] 	: affiche les informations système et l'état actuel du décodeur TV.
			[9]		: permet de se rendre sur une chaîne précise en indiquant un code EPG (Electronic Program Guide) en indiquant l'epg_id (-e ou --epg_id).
			[1]  	: permet de simuler l'appui d'une touche sur la télécommande en indiquant le mode (-m ou --mode) et la key (-k ou --key).
			
	-m ou --mode :
		Obligatoire si -o ou --operation est égal à '1'.
		Correspond au mode d'appui du bouton correspondant à la touche de la télécommande.
		
		Valeurs possibles :
			[0] : simule un appui court sur la touche de la télécommande (keyDown + keyUp)
			[1] : simule un appui sur la touche de la télécommande sans relache du bouton (keyDown)
			[2] : simule une relache du bouton de la touche de la télécommande (keyUp)
		
	-k ou --key :
		Obligatoire si -o ou --operation est égal à '1'.
		Correspond au 'code télécommande' du signal que l'on souhaite envoyer au décodeur TV.
		
		Valeurs connues possibles :
			[116] ou [POWER]: Simule la touche POWER : allume ou éteint le décodeur TV en fonction de son état
			[512] ou [0] 	: Simule la touche 0 de la télécommande
			[513] ou [1] 	: Simule la touche 1 de la télécommande
			[514] ou [2] 	: Simule la touche 2 de la télécommande
			[515] ou [3] 	: Simule la touche 3 de la télécommande
			[516] ou [4] 	: Simule la touche 4 de la télécommande
			[517] ou [5] 	: Simule la touche 5 de la télécommande
			[518] ou [6] 	: Simule la touche 6 de la télécommande
			[519] ou [7] 	: Simule la touche 7 de la télécommande
			[520] ou [8] 	: Simule la touche 8 de la télécommande
			[521] ou [9] 	: Simule la touche 9 de la télécommande
			[402] ou [CH+] 	: Simule la touche CH+ de la télécommande
			[403] ou [CH-] 	: Simule la touche CH- de la télécommande
			[115] ou [VOL+] : Simule la touche VOL+ de la télécommande
			[114] ou [VOL-] : Simule la touche VOL- de la télécommande
			[113] ou [MUTE] : Simule la touche MUTE de la télécommande
			[103] ou [UP] 	: Simule la touche HAUT de la télécommande
			[108] ou [DOWN] : Simule la touche BAS de la télécommande
			[105] ou [LEFT] : Simule la touche GAUCHE de la télécommande
			[116] ou [RIGHT]: Simule la touche DROITE de la télécommande
			[352] ou [OK] 	: Simule la touche OK de la télécommande
			[158] ou [BACK] : Simule la touche ARRIERE de la télécommande
			[139] ou [MENU] : Simule la touche MENU de la télécommande
			[164] ou [PAUSE]: Simule la touche PLAY/PAUSE de la télécommande
			[168] ou [FBWD] : Simule la touche RETOUR ARRIERE de la télécommande
			[159] ou [FFWD] : Simule la touche AVANCE RAPIDE de la télécommande
			[167] ou [REC] 	: Simule la touche ENREGISTRER de la télécommande
			[393] ou [VOD] 	: Simule la touche VOD de la télécommande
	
	-e ou --epg_id :
		Obligatoire si -o ou --operation est égal à '9'.
		Correspond au code EPG de la chaîne que le décodeur TV doit afficher.
		
		Valeurs connues possibles :
			
		

Un grand merci à tous les contributeurs du topic à cette addresse :
https://communaute.orange.fr/t5/TV-par-ADSL-et-Fibre/API-pour-commander-le-decodeur-TV-depusi-une-tablette/td-p/43443

Je suis loin d'être un expert des technologies utilisées par ce module : il peut présenter des erreurs, être incomplet, etc.
N'hésitez pas à le modifier, l'adapter, le partager, et l'utiliser quel que soit le contexte.

Je vous serais reconnaissant de me transmettre les éventuelles améliorations/corrections à y apporter sur le repository github : https://github.com/DalFanajin/Orange-Livebox-TV-UHD-4K-python-controller

Etant donné que le décodeur est exclusivement français, je n'ai pas prévu de traduction anglaise pour cette docstring : si elle est nécessaire, n'hésitez pas à me solliciter.
This decoder is a french product, so I didn't translate this docstring in english : do not hesitate to ask if you need a translation anyway.
"""

# importing the requests library 
import requests, sys, getopt

# initialisation de la 
VERBOSE = False

# api-endpoint 
URL = "http://192.168.1.12:8080/remoteControl/cmd"

def main(argv):	
	opts, args = checkArgs(argv)
	
	operation, key, mode = getFlagsAndValues(opts)
	
	checkIfArgsAreEmpty(args)
	
	# parametres d'url
	PARAMS = {'operation':operation, 'key':key, 'mode':mode} 
	
	# sending get request and saving the response as response object 
	r = requests.get(url = URL, params = PARAMS)
	
	getFullResult(r.json())
	
def createAndSendRequest(operation,mode,key,epg_id):
	
	

def getFullResult(data):
	resultCode = data['result']['responseCode'] 
	resultMessage = data['result']['message'] 
	resultData = data['result']['data'] 
	printVerbose("Code réponse:%s\nMessage:%s\nDonnées:%s"%(resultCode, resultMessage,resultData)) 
	
def checkArgs(argv):
	global VERBOSE
	
	try:                                
		opts, args = getopt.getopt(argv, "hvo:k:m:e:", ["help", "verbose", "operation=", "key=", "mode=","epg_id="])
		
		for flag, value in opts:
			if flag in ('-v', '--verbose'):
				VERBOSE = True
		
		return opts, args
		
	except getopt.GetoptError:
		printError('Argument(s) invalide(s)')
		exitTvOrange()
		
def getFlagsAndValues(opts):
	for flag, value in opts:
		printVerbose("%s:%s"%(flag,value))
		
		if flag in ('-o', '--operation'):
			operation = value
			
		elif flag in ('-k', '--key'):
			key = value
		
		elif flag in ('-m', '--mode'):
			mode = value
		
		elif flag in ('-e', '--epg_id'):
			epg_id = value
		
		elif flag in ('-h', '--help'):
			exitTvOrange()
		
	return '01','115','0'
	
def checkIfArgsAreEmpty(args):
	if len(args) != 0:
		printError('Argument(s) invalide(s)')
		exitTvOrange()

def exitTvOrange():
	usage()
	sys.exit(2)
	
def usage():
	print(__doc__)
	
def printVerbose(text):
	if VERBOSE:
		print("\033[1;34;40m%s\033[0m"%text)
		
def printError(text):
	print("\033[1;31;40m%s\033[0m"%text)

if __name__ == "__main__":
	main(sys.argv[1:])