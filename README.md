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
	
## Options :

*-h ou --help :
   Optionnel.
   Sans argument.
   Permet d'afficher cette docstring.
		
*-v ou --verbose :
		Optionnel.
		Sans argument.
		Permet d'afficher les informations écrites dans la console par la méthode 'printVerbose', utilisée pour afficher les informations de déroulement du programme.
		
*-o ou --operation :
   Obligatoire.
   Spécifie l'instruction à envoyer au décodeur TV.
   
   Valeurs possibles :
   |Valeur|Description|
   |10|affiche les informations système et l'état actuel du décodeur TV|
   |9|permet de se rendre sur une chaîne précise en indiquant un code EPG (Electronic Program Guide) en indiquant l'epg_id (-e ou --epg_id)|
   |1|permet de simuler l'appui d'une touche sur la télécommande en indiquant le mode (-m ou --mode) et la key (-k ou --key)|
			
*-m ou --mode :
   Obligatoire si -o ou --operation est égal à '1'.
   Correspond au mode d'appui du bouton correspondant à la touche de la télécommande.
   
   Valeurs possibles :
   |0|simule un appui court sur la touche de la télécommande (keyDown + keyUp)|
   |1|simule un appui sur la touche de la télécommande sans relache du bouton (keyDown)|
   |2|simule une relache du bouton de la touche de la télécommande (keyUp)|
   
*-k ou --key :
   Obligatoire si -o ou --operation est égal à '1'.
   Correspond au 'code télécommande' du signal que l'on souhaite envoyer au décodeur TV.
   
   Valeurs connues possibles :
   [Voir la liste des keys : le code donné à l'option peut être la valeur de la colonne CODE_INT ou CODE_STR.](https://github.com/DalFanajin/Orange-Livebox-TV-UHD-4K-python-controller/blob/master/keys.md)
	
*-e ou --epg_id :
   Obligatoire si -o ou --operation est égal à '9'.
   Correspond au code EPG de la chaîne que le décodeur TV doit afficher.
   
   Valeurs connues possibles :
   [Voir la liste des epg_ids : le code donné à l'option peut être la valeur de n'importe quelle colonne.](https://github.com/DalFanajin/Orange-Livebox-TV-UHD-4K-python-controller/blob/master/epg_ids.md)
		

[Un grand merci à tous les contributeurs du topic à cette addresse.](https://communaute.orange.fr/t5/TV-par-ADSL-et-Fibre/API-pour-commander-le-decodeur-TV-depusi-une-tablette/td-p/43443)

Je suis loin d'être un expert des technologies utilisées par ce module : il peut présenter des erreurs, être incomplet, etc.
N'hésitez pas à le modifier, l'adapter, le partager, et l'utiliser quel que soit le contexte.

[Je vous serais reconnaissant de me transmettre les éventuelles améliorations/corrections à y apporter sur le repository github.](https://github.com/DalFanajin/Orange-Livebox-TV-UHD-4K-python-controller)

Etant donné que le décodeur est exclusivement français, je n'ai pas prévu de traduction anglaise pour cette docstring : si elle est nécessaire, n'hésitez pas à me solliciter.
This decoder is a french product, so I didn't translate this docstring in english : do not hesitate to ask if you need a translation anyway.