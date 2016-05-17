# Programme python Pour pilotage de la Senseo.

## Description.
	Des fois que le nom ne soit pas assez évocateur :-)
	J'ai une Senséo et j'ai décidé de la piloter par une raspberry pi.
	

### Lubie ou reel besoin.
	Bon certe au début on se dit, "oui, non mais faut pas exagérer", "Il y en a vraiment qui sont feignant". N'epeche que, c'est un peu comme les volet roulant électrique. 
	Au début on se dit, "pfff c'est du gadget", certaines mauvaises langue diront "j'y arrive très bien moi avec la manivelle !!"
	C'est pas faux, néanmoins, quand on n'a pas cette tache à faire c'est toujours du temps de gagné :-) surtout quand on aime bien marmotter ou que l'on a des réveils difficiles.
	
### génèse du projet.
	Dans notre aincien domicile, ma conjointe avait une cafetière à filtre. Et pour gagner du temps le matin, elle avait acheté un programmateur pour que le café soit prêt quand elle se réveillait.
	
	Après avoir enménagé ensemble, de mon coté j'avais une senséo... petit problème les programmateur, ça ne marche pas sur une senseo :-). Pas grave on fait sans.
	Mais bon, c'est vrai que se lever et avoir son petit café tout chaud prêt à déguster. C'est quand même sympa.
	Je me lance donc dans la recherche de personne ayant tenté ou même réussi à domotiser une senseo. Google est mon amis et me montre ceci : http://www.domotique-info.fr/2014/09/domotiser-senseo/
	Pas mal mais bon acheter un contact Zwave à 50/60€ c'est un peu cher et coté retour d'information sur la cafetiere,  on a pas d'info.
	Grand fan de ces petits SOC que sont les raspberry, je me dis "Ohhh ça devrait pouvoir marcher ça.
	Je me met en quête du plan de la carte de controle de la cafetiere (trouvé, je vous ai copié l'image dans le repertoire doc) et d'un tuto sur : comment démonter une senso ... et la remonter pour qu'elle fonctionne à nouveau. croyez moi, en fonction du modèle, c'est pas toujours aussi évident qu'il n'y parait.
	
	
### Description
	Ce script python permet de piloter la cafetiere mais aussi de l'interroger pour récupérer son statut.
	
### Dépendance 
	Il vous faudra installer la librairie wiringpi, pour ça, google est votre ami :-)	

### Pré-requis
- une raspberry pi (le modele de base suffit. je fais tourner ça sur une RPI A premier modele 256Mo de ram)
- une senseo (pour les tests vous pouvez utiliser une breadboard avec des LED)
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

