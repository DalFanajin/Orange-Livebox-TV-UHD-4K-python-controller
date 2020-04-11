# Orange-Livebox-TV-UHD-4K-python-controller

Ce module permet de contrôler le décodeur TV orange via la ligne de commande Unix d'un système.
Il nécessite les modules suivants : requests, sys, getopt

Développé et testé pour le décodeur TV UHD 4K Orange :
	Modèle : Livebox Fibre
	Version de firmware : 1.12.16
	Version de firmware Orange : g0-f-fr)
	
Développé et tester sur un système connecté au même réseau local que le décodeur TV :
	Dans cet exemple, l'adresse IP de mon décodeur est fixe et son addresse locale est 192.168.1.12
	La variable globale 'URL' doit être modifiée pour accueillir l'addresse locale de votre décodeur.
	
Arguments :
	-h ou --help :
		Optionnel.
		Permet d'afficher cette docstring.
		
	-v ou --verbose :
		Optionnel.
		Permet d'afficher les informations écrites dans la console par la méthode 'printVerbose', utilisée pour afficher les informations de déroulement du programme.
		
	-o ou --operation :
		Obligatoire.
		
		Spécifie l'instruction à envoyer au décodeur TV.
		
		Valeurs possibles :
			10 : affiche les informations système et l'état actuel du décodeur TV.
			1  : permet de simuler l'appui d'une touche ou d'une série d'une touche sur la télécommande.
			
	-m ou --mode :
		Ne peut pas être utilisé si -o ou --operation est égal à '10'.
		Obligatoire si -o ou --operation est égal à '01'.
		
		Correspond au mode d'appui du bouton correspondant à la touche de la télécommande.
		
		Valeurs possibles :
			0 : simule un appui court sur la touche de la télécommande (keyDown + keyUp)
			1 : simule un appui sur la touche de la télécommande sans relache du bouton (keyDown)
			2 : simule une relache du bouton de la touche de la télécommande (keyUp)
		
	-k ou --key :
		Ne peut pas être utilisé si -o ou --operation est égal à '10'.
		Obligatoire si -o ou --operation est égal à '1'.
		
		Correspond au 'code télécommande' du signal que l'on souhaite envoyer au décodeur.
		
		Valeurs possibles :
			
		

Un grand merci à tous les contributeurs du topic à cette addresse :
https://communaute.orange.fr/t5/TV-par-ADSL-et-Fibre/API-pour-commander-le-decodeur-TV-depusi-une-tablette/td-p/43443

Je ne suis pas un expert sur les expert sur les technologies utilisées par ce module : il peut présenter des erreurs, être incomplet, etc.
N'hésitez pas à le modifier, l'adapter, le partager, et l'utiliser quel que soit le contexte.

Je vous serais reconnaissant de me transmettre les éventuelles améliorations/corrections à y apporter sur le repository github : 

Etant donné que le décodeur est exclusivement français, je n'ai pas prévu de traduction anglaise pour cette docstring : si elle est nécessaire, n'hésitez pas à me solliciter.
This decoder is a french product, so I didn't translate this docstring in english : do not hesitate to ask if you need a translation anyway.
