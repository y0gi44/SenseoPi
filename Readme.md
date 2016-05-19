# Programme python Pour pilotage de la Senseo.

## Description.
	Des fois que le nom ne soit pas assez évocateur :-)
	J'ai une Senseo et j'ai décidé de la piloter par une raspberry pi.
	

### Lubie ou réel besoin.
	Bon certes au début on se dit, "oui, non mais faut pas exagérer", "Il y en a vraiment qui sont feignant". N'empêche que, c'est un peu comme les volets roulants électriques. 
	Au début on se dit, "pfff c'est du gadget", certaines mauvaises langue diront "j'y arrive très bien moi avec la manivelle !!"
	C'est pas faux, néanmoins, quand on n'a pas cette tâche à faire c'est toujours du temps de gagné :-) surtout quand on aime bien marmotter ou que l'on a des réveils difficiles.
	
### Genèse du projet.
	Dans notre ancien domicile, ma conjointe avait une cafetière à filtre. Et pour gagner du temps le matin, elle avait acheté un programmateur pour que le café soit prêt quand elle se réveillait.
	
	Après avoir emménagé ensemble, de mon côté j'avais une Senseo... petit problème, les programmateurs, ça ne marche pas sur une Senseo :-). Pas grave on fait sans.
	Mais bon, c'est vrai que se lever et avoir son petit café tout chaud prêt à déguster. C'est quand même sympa.
	Je me lance donc dans la recherche de personne ayant tenté ou même réussi à domotiser une Senseo. Google est mon amis et me montre ceci : http://www.domotique-info.fr/2014/09/domotiser-senseo/
	Pas mal mais bon acheter un contact Z-wave à 50/60€ c'est un peu cher et coté retour d'information sur la cafetière,  on n’a pas d'info.
	Grand fan de ces petits SOC que sont les raspberry, je me dis "Ohhh ça devrait pouvoir marcher ça.
	Je me mets en quête du plan de la carte de contrôle de la cafetière (trouvé, je vous ai copié l'image dans le répertoire doc) et d'un tuto sur : comment démonter une Senseo ... et la remonter pour qu'elle fonctionne à nouveau. Croyez-moi, en fonction du modèle, ce n'est pas toujours aussi évident qu'il n'y parait.
	
	
### Description
	Ce script python permet de piloter la cafetière mais aussi de l'interroger pour récupérer son statut (Eteint / Allumé en chauffe / Allumée prête / Allumée niveau d’eau insuffisant).
	
### Dépendance 
	Il vous faudra installer la librairie wiringpi, pour ça, google est votre ami :-)	

### Pré-requis
- une raspberry pi (le modèle de base suffit. je fais tourner ça sur une RPI A premier modele 256Mo de ram)
- une Senseo (pour les tests vous pouvez utiliser une breadboard avec des LED)
- 4 résistances
- du fil
- un fer à souder


### utilisation

usage : ./senseo.py [-h] | 1cup | 2cup | 4cup | status | pressPower | press1Cup | press2Cup
      status     : interroge la Senseo et retourne son état courant
      pressPower : appuie sur le bouton power
      press1Cup  : appuie sur le bouton 1 tasse
      press2Cup  : appuie sur le bouton 2 tasses
      1cup       : Scenario qui lance le café 1 tasse
      2cup       : Scenario qui lance le café 2 tasses
      4cup       : Scenario qui lance le café 4 tasses (2 x 2tasses)
            Note : Les scénarios allument la Senseo si celle ci est éteinte, et affichent un message d'erreur si le niveau d'eau est insuffisant

### webservice 
	Le programe python webserver.py est un copié/collé simple d'un tuto d'internet, un peu customisé pour lancer le programme de senseo lors d'un appel à l'url http://<monIp>:8001/senseo/action/<action>
	Les actions possibles sont 1cup.run, 2cup.run, 4cup.run, getStatus.
	
	Il se lance sans argument.
	Les chemins sont en dur, certes c'est pas super sexy mais bon ça a le mérite de fonctionner.
	
	Pourquoi faire un "webservice" ?, la réponse est simple, j'utilise le systeme de domotique Domoticz.
	J'ai créé des interrupteurs virtuels pour lancer les café 1 2 et 4 tasses cf capture_domoticz.png.
	Chaque interrupteur sous domitcz peu faire un appel http ou lancer un script quand celui ci passe à "on" ou à "off" .
	Et voilà.


### possibles Evolutions 
- Utiliser un ESP8226 wifi pour se passer du rapsberry pi qui à côté d'une cafetière est assez encombrant
- Ameliorer la sécurité du serveur Web python, (token, user/mdp ...  à voir)
