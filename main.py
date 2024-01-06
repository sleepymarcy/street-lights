from microbit import *
from lib import update_display, lights, toggle_light


def main():
    while True:
        toggle_light("R")
        update_display()
        # sleep(5000)

        for i in range(5, 0, -1):
            display.show(i)
            sleep(1000)
        display.clear()

        toggle_light("Y")
        update_display()
        sleep(1000)
        toggle_light("Y")

        toggle_light("R")

        toggle_light("G")
        update_display()
        # sleep(5000)
        for i in range(5, 0, -1):
            display.show(i)
            sleep(1000)
        display.clear()
        toggle_light("G")

        toggle_light("Y")
        update_display()
        sleep(3000)
        toggle_light("Y")


main()
# mamy 4 opcje sygnalizacji świateł
# 1. za pomocą literek na display'u
# 2. za pomocą pojedyńczych ledów na display'u
# 3. za pomocą ustawionych wcześniej obrazków
#    (tablica która określa które ledy mają świecić i w jakim natężeniu)
# 4. na płytce stykowej używając ledów
