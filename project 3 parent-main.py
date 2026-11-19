from microbit import *
import radio

radio.on()
radio.config(group=6)

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
