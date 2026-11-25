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

def ecart_mouvement():
    plus_grand = 0
    for _ in range(5):                    # 5 mesures en 0,1 s
        x, y, z = accelerometer.get_values()
        ecart = abs(math.sqrt(x*x + y*y + z*z) - 1000)
        if ecart > plus_grand:
            plus_grand = ecart
        sleep(20)
    return plus_grand

def classer_mouvement(ecart):
    '''0 = calme, 1 = agite, 2 = tres agite'''
    if ecart < SEUILS_MOUVEMENT[0]:
        return 0
    if ecart < SEUILS_MOUVEMENT[1]:
        return 1
    return 2

def bilan_mouvement(comptes):
    '''E = endormi, A = agite, T = tres agite'''
    total = sum(comptes)
    if comptes[0] >= 0.9 * total:
        return "E"
    if comptes[2] >= 0.25 * total:
        return "T"
    return "A"

