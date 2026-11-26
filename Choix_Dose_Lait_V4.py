from microbit import *

total = 0
nb_doses = 0


# Affiche le volume total et le nombre de doses
def afficher_bilan():
    display.scroll(str(total) + "ml x" + str(nb_doses))


# Attend que le doigt soit retire du logo
def attendre_relachement_logo():
    while pin_logo.is_touched():
        sleep(50)


# Remise a zero avec confirmation
def confirmer_reset():
    global total, nb_doses

    display.show("?")

    button_a.was_pressed()
    button_b.was_pressed()

    debut = running_time()

    while running_time() - debut < 5000:

        if button_a.was_pressed():
            total = 0
            nb_doses = 0

            display.show(Image.YES)
            sleep(1000)
            return

        if button_b.was_pressed():
            break

        sleep(50)

    display.show(Image.NO)
    sleep(800)


# Saisie manuelle d'un volume
def encoder_volume():
    global total, nb_doses

    V = ""
    n = 0

    button_b.was_pressed()
    display.show(n)

    while True:

        # Selection du chiffre
        if button_a.was_pressed():
            n = (n + 1) % 10
            display.show(n)

        # Validation du chiffre
        if button_b.was_pressed():
            V += str(n)
            display.scroll(V)
            n = 0
            display.show(n)

        # Confirmation du volume
        if pin_logo.is_touched():
            attendre_relachement_logo()

            if V != "" and int(V) > 0:

                volume = int(V)

                # Verification de la limite de 150 ml
                if total + volume <= 150:
                    total += volume
                    nb_doses += 1

                    display.show(Image.YES)
                    sleep(500)

                else:
                    display.show(Image.NO)
                    sleep(800)

            else:
                display.show(Image.NO)
                sleep(800)

            return

        sleep(50)


# Affichage initial
afficher_bilan()


while True:

    a = button_a.was_pressed()
    b = button_b.was_pressed()

    # Detection de deux boutons presses ensemble
    if a or b:
        sleep(150)
        a = a or button_a.was_pressed()
        b = b or button_b.was_pressed()

    if a and b:
        confirmer_reset()

    elif b:
        encoder_volume()

    elif pin_logo.is_touched():
        afficher_bilan()

    sleep(50)

