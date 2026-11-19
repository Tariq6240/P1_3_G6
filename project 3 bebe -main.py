from microbit import *
import radio

radio.on()
radio.config(group=6)

def decrypter(message):
    resultat = ""
    for caractere in message:
        resultat += chr(ord(caractere) - 1)
    return resultat

display.show(Image.HOUSE)

while True:
    message = radio.receive()

    if message:
        champs = message.split("|")

        if len(champs) == 3:
            type_message = champs[0]
            longueur = champs[1]
            contenu = champs[2]

            if len(contenu) == int(longueur):
                contenu_decrypte = decrypter(contenu)

                if type_message == "LED":

                    if contenu_decrypte == "ON":
                        display.set_pixel(2, 2, 9)

                    elif contenu_decrypte == "OFF":
                        display.clear()

                elif type_message == "IMG":

                    if contenu_decrypte == "HEART":
                        display.show(Image.HEART)

                    elif contenu_decrypte == "SAD":
                        display.show(Image.SAD)

