
from microbit import *

total = 0
nb_doses = 0

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
            display.clear()
            return

        if button_b.was_pressed():
            break

        sleep(50)

    display.show(Image.NO)
    sleep(800)
    display.clear()


while True:

    a = button_a.was_pressed()
    b = button_b.was_pressed()

    if a or b:
        sleep(150)
        a = a or button_a.was_pressed()
        b = b or button_b.was_pressed()

    if a and b:
        confirmer_reset()

    elif a:
        if total < 150:
            total += 30
            nb_doses += 1
            display.show(Image.YES)
            sleep(500)
            display.scroll(str(total)+"ml")
        else:
            display.show(Image.NO)
            sleep(500)

    elif b:
        display.scroll("x"+str(nb_doses))

    sleep(50)

