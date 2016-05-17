#!/usr/bin/python

import wiringpi as GPIO
import sys
import os

# Import des modules
import time

duree1Cup = 20
duree2Cup = 40

pinPwr  = 0
pin1Cup = 2
pin2Cup = 3
pinLed  = 4


def init():

    GPIO.wiringPiSetup()  
    GPIO.pinMode(pinLed, 0) # sets WP pin 6 to input  
    GPIO.pinMode(pinPwr, 1) 
    GPIO.pinMode(pin1Cup, 1) 
    GPIO.pinMode(pin2Cup, 1) 
    # mise à 1 de tous les boutons
    GPIO.digitalWrite(pinPwr, GPIO.GPIO.HIGH)
    GPIO.digitalWrite(pin1Cup, GPIO.GPIO.HIGH)
    GPIO.digitalWrite(pin2Cup, GPIO.GPIO.HIGH)


def pressButton( btn):
    GPIO.digitalWrite(btn, GPIO.GPIO.LOW)
    time.sleep(0.2)
    GPIO.digitalWrite(btn, GPIO.GPIO.HIGH)

# fonction qui retourn vrai si la pin n'est pas dans le statut "not_wanted" pendant plus de nbSecondes
def pinIs(pin, statusNotWanted, nbSec):
    # initialisation compteur
    i = 0
    while True :
        time.sleep(0.1)
        # lecture de la pin
        if (GPIO.digitalRead(pin) == statusNotWanted):
            return False
        i = i+1
        if (i > nbSec*10):
            return True 

# fonction qui retourne la durée en millisecondes entre deux clinottement
def pinBlinkInterval(pin, Timeout):
    # initialisation compteur
    startTime = getStartTime()
    
    initPinState = GPIO.digitalRead(pin)
    startCounting=False
    firstPulse = False
    pulse = 0
    ## récupération d'un cycle
    while True :
        # gestion du timeout
        if ( isTimeoutExpired(startTime, Timeout) ):
            return -1
            
        #time.sleep(0.01)
        # lecture de la pin
        if (startCounting == False ):
            if (GPIO.digitalRead(pin) != initPinState):
                startCounting = True
                pulse = getStartTime()
        else:
            if (firstPulse == False):
                if (GPIO.digitalRead(pin) == initPinState):
                    firstPulse = True
            if (firstPulse and GPIO.digitalRead(pin) != initPinState):
                return getStartTime() - pulse

def getSenseoStatus():
    if (senseoIsUp() ):
        msg = 'Allumée'
        
        # détermination de l'état de la senseo
        pulse = pinBlinkInterval(pinLed, 3)
        if (pulse < 0):
            msg = msg+' - prete a servir'
        else:
            #print 'Pulse time : {}'.format(pulse)
            if (pulse > 0.5):
                msg = msg+' - En Chauffe'
            else:
                msg = msg+" - Niveau d'eau insuffisant"
        return msg
    else:
        return  'Eteint'
                    
def senseoIsUp():
    # La senseo est allumée si la broche de la LED n'est pas allumé pendant plus de 2 secondes
    if (pinIs(pinLed, 1, 2)):
        return False
    else:
        return True

def senseoIsReady():
    # La senseo est allumée si la broche de la LED n'est pas allumé pendant plus de 2 secondes
    if (pinIs(pinLed, 0, 2)):
        return True
    else:
        return False

def getStartTime():
    return time.time()

    
def isTimeoutExpired(startTime, timeout):
    if ( (int(time.time()) - int(startTime)) > timeout ):
        return True
    else:
        return False
    
    
def waitForTemperatureReady(timeout):
    startTime = getStartTime()
    print 'Debut attente {}'.format(startTime )
    while True :
        # gestion du timeout
        if ( isTimeoutExpired(startTime, timeout) ):
            return False
        if (pinIs(pinLed, 0, 2)):
            print ''
            return True
        else:
            sys.stdout.write(".")
            sys.stdout.flush()

def voiceMessage(msg):
    # votre commande de notification vers un serveur de TTS.
    cmd = "monclientTTS -m X.X.X.X -p yyyy -txt '"+msg+"'"
    print 'Cmd = {}'.format(cmd)
    # décommenter la ligne suivante si vous en avez un :-)
    #os.system(cmd)


def lancerUnDoubleCafe():
    print 'Attente Temperature OK'
    if (waitForTemperatureReady(120)):
        print 'Lancement du café'
        pressButton(pin2Cup)
        time.sleep(duree2Cup)
        return True
    else:
        return False

def lancerUnCafe():
    print 'Attente Temperature OK'
    if (waitForTemperatureReady(120)):
        print 'Lancement du café'
        pressButton(pin1Cup)
        time.sleep(duree1Cup)
        return True
    else:
        return False

def usage():
    print 'usage : '+sys.argv[1]+' [-h] | 1cup | 2cup | 4cup | status | pressPower | press1Cup | press2Cup '
    print '      status     : interroge la Senseo et retourne son état courant '
    print '      pressPower : appuie sur le bouton power '
    print '      press1Cup  : appuie sur le bouton 1 tasse '
    print '      press2Cup  : appuie sur le bouton 2 tasses '
    print '      1cup       : Scenario qui lance le café 1 tasse '
    print '      2cup       : Scenario qui lance le café 2 tasses '
    print '      4cup       : Scenario qui lance le café 4 tasses (2 x 2tasses) '
    print '            Note : Les scénarios allument la Senseo si celle ci est éteinte, et affichent un message d\'erreur si le niveau d\'eau est insuffisant'


if (len(sys.argv) > 1):
    argument = sys.argv[1]
    # cas de la demande d'un café court
    print 'Argument : ',argument
    
    if (argument == '1cup' or argument == '2cup' or argument == '4cup' or argument == "status" or argument == "pressPower" or argument == "press1Cup" or argument == "press2Cup" ):
        print 'Initialisation du GPIO'
        init()
        
        if(argument == "status"):
            print "La senseo est au statut : {}".format( getSenseoStatus())
            
        if(argument == "pressPower"):
            pressButton(pinPwr)
            print "Appui sur le bouton power de la senseo "
        
        if(argument == "press1Cup"):
            pressButton(pin1Cup)
            print "Appui sur le bouton 1 Tasse de la senseo "
        
        if(argument == "press2Cup"):
            pressButton(pin2Cup)
            print "Appui sur le bouton 2 Tasses de la senseo "
            
        if (argument == '1cup' or argument == '2cup' or argument == '4cup') :

            if(senseoIsUp() == False):
                voiceMessage('Allumage de la Saine séo')
                print 'Allumage de la cafetiere ...'
                # Allumage de la cafetiere
                pressButton(pinPwr)

            # Test du statut de la Senseo
            statut = getSenseoStatus()
            print "Statut de la senseo {}".format(statut)
            if(statut == "Allumée - Niveau d'eau insuffisant"):
                voiceMessage("Le niveau do est insuffisant") 
                voiceMessage("Extinction de la Saine séo") 
                pressButton(pinPwr)
                sys.exit(1)
          
            
            if (argument == '1cup'):
                # si le retour est OK en moins de 2 minutes on lance le Café !!!!
                if (lancerUnCafe()):
                    voiceMessage('Votre café est pres') 
                    print 'Arret de la cafetiere'
                    pressButton(pinPwr)
                else:
                    voiceMessage('Il y a un problème avec la cafetière, extinction') 
                    pressButton(pinPwr)

            if (argument == '2cup'):
                # si le retour est OK en moins de 2 minutes on lance le Café !!!!
                if (lancerUnDoubleCafe()):
                    voiceMessage('Votre café est pres') 
                    print 'Arret de la cafetiere'
                    pressButton(pinPwr)
                else:
                    voiceMessage('Il y a un problème avec la cafetière, extinction') 
                    pressButton(pinPwr)
                    
            if (argument == '4cup'):
                # si le retour est OK en moins de 2 minutes on lance le Café !!!!
                if (lancerUnDoubleCafe()):
                    statut = getSenseoStatus()
                    if(statut == "Allumée - Niveau d'eau insuffisant"):
                        voiceMessage("Le niveau do est insuffisant") 
                        voiceMessage("Extinction de la Saine séo") 
                        pressButton(pinPwr)
                        sys.exit(1)
                        
                    if (lancerUnDoubleCafe()):
                        voiceMessage('Votre café est pres') 
                        print 'Arret de la cafetiere'
                        pressButton(pinPwr)
                    else:
                        voiceMessage('Il y a un problème avec la cafetière, extinction') 
                        pressButton(pinPwr)
                else:
                    voiceMessage('Il y a un problème avec la cafetière, extinction') 
                    pressButton(pinPwr)
        
    else:
        print "Argument inconnu"
        sys.exit(2)

                
else:
    print 'Erreur , un argument est attendu'
    sys.exit(3)
    
sys.exit(0)


