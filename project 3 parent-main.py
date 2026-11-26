from microbit import *
import radio

radio.on()
radio.config(group=6)
doses = [30, 60, 90, 120, 150]
index_dose = 1          
total = 0
nb_biberons = 0
TYPE_BRUIT = "05"   



SEUILS_BRUIT = (40, 100)       
                     
          
MESURES_BRUIT = 10              
DUREE_MUSIQUE = 60000    


def confirmer_reset():
    
    #vider la memoire 
    global total, nb_biberons
    display.show("?")
    button_a.was_pressed()  
    button_b.was_pressed()   #cela sert pour vider la memoire 
    debut = running_time()
    
    
    while running_time() - debut < 5000:
        if button_a.was_pressed():   #remet tout a 0, si 5 seconde sont ecoukle
            total = 0
            nb_biberons = 0
            display.show(Image.YES)
            sleep(1000)
            display.clear()
            return
        if button_b.was_pressed():  #sort de la boucke sans rien effacer
            break
        sleep(50)
    
    display.show(Image.no)  #atteint si 5secondes sont ecouler ou bien on appuie sur b 
    sleep(800)
    display.clear()


display.scroll(str(doses[index_dose]))

while True:
    a = button_a.was_pressed()
    b = button_b.was_pressed()

    
    if a or b:
        sleep(150)
        a = a or button_a.was_pressed()    #si ona 2 boutton qui sont presse il va voir si il ya 150ms qui separe les 2
        b = b or button_b.was_pressed()

    if a and b:
        confirmer_reset()
    elif a:
        total += doses[index_dose]
        nb_biberons += 1
        display.show(Image.YES)
        sleep(500)
        display.scroll(str(total))
    elif b:
        index_dose = (index_dose + 1) % len(doses) #on ajoute 1 et on fait une division pour passer a la prochaine dose  
        display.scroll(str(doses[index_dose]))  #afficher la dose 
    elif pin_logo.is_touched():
        display.scroll(str(total))
        display.scroll("x" + str(nb_biberons)) #on affiche le nombre de dose de lait 

    sleep(50)

def crypter(message):
    resultat = ""
    for caractere in message:
        resultat += chr(ord(caractere) + 1)
    return resultat

def envoyer(type_message, commande):
    contenu_crypte = crypter(commande)
    message = type_message + "|" + str(len(contenu_crypte)) + "|" + contenu_crypte
    radio.send(message)

display.show(Image.HEART)

while True:
    if button_a.was_pressed():
        envoyer("LED", "ON")
        display.show(Image.YES)

    if button_b.was_pressed():
        envoyer("LED", "OFF")
        display.show(Image.NO)

    if accelerometer.was_gesture("shake"):
        envoyer("IMG", "HEART")
        display.show(Image.HEART)

    sleep(100)
# Imports go at the top
from microbit import *
doses = [30, 60, 90, 120, 150]
index_dose = 0          
total = 0
nb_biberons = 0


def confirmer_reset():
    
    #vider la memoire 
    global total, nb_biberons
    display.show("?")
    button_a.was_pressed()  
    button_b.was_pressed()   #cela sert pour vider la memoire 
    debut = running_time()
    
    
    while running_time() - debut < 5000:
        if button_a.was_pressed():   #remet tout a 0, si 5 seconde sont ecoukle
            total = 0
            nb_biberons = 0
            display.show(Image.YES)
            sleep(1000)
            display.clear()
            return
        if button_b.was_pressed():  #sort de la boucke sans rien effacer
            break
        sleep(50)
    
    display.show(Image.NO)  #atteint si 5secondes sont ecouler ou bien on appuie sur b 
    sleep(800)
    display.clear()


display.scroll(str(doses[index_dose]))

while True:
    a = button_a.was_pressed()
    b = button_b.was_pressed()

    
    if a or b:
        sleep(150)
        a = a or button_a.was_pressed()    #si ona 2 boutton qui sont presse il va voir si il ya 150ms qui separe les 2
        b = b or button_b.was_pressed()

    if a and b:
        confirmer_reset()
    elif a:
        total += doses[index_dose]
        nb_biberons += 1
        display.show(Image.YES)
        sleep(500)
        display.scroll(str(total))
    elif b:
        index_dose = (index_dose + 1) % len(doses) #on ajoute 1 et on fait une division pour passer a la prochaine dose  
        display.scroll(str(doses[index_dose]))  #afficher la dose 
    elif pin_logo.is_touched():
        display.scroll(str(total))
        display.scroll("x" + str(nb_biberons)) #on affiche le nombre de dose de lait 

    sleep(50)



while True:
    display.show(Image.HEART)
    sleep(1000)
    display.scroll('Hello')
    
def traiter_message():
    recu = recevoir()
    if recu and recu[0] == TYPE_ETAT:
        lettre = recu[1]
        if lettre == "T":
            display.show("T")
            music.play(ALARME)
            sleep(1000)
        elif lettre == "E" or lettre == "A":
            display.show(lettre)
            sleep(1500)
        display.clear()
    elif recu and recu[0] == TYPE_BRUIT:
        if recu[1] == "C" or recu[1] == "M" or recu[1] == "F":
            display.show(recu[1])        # bruit autour du bebe
            sleep(1500)
            display.clear()
