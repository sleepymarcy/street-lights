from microbit import *

signal_state = {
    "R": "OFF",
    "Y": "OFF",
    "G": "OFF",
}


def main():
    # while True:
    #     handle_input()
    #     update_display()
    while True:
        signal_state["R"] = toggle_light(signal_state["R"])
        update_display()
        # sleep(5000)

        for i in range(5, 0, -1):
            display.show(i)
            sleep(1000)
        display.clear()

        signal_state["Y"] = toggle_light(signal_state["Y"])
        update_display()
        sleep(1000)
        signal_state["Y"] = toggle_light(signal_state["Y"])

        signal_state["R"] = toggle_light(signal_state["R"])

        signal_state["G"] = toggle_light(signal_state["G"])
        update_display()
        # sleep(5000)
        for i in range(5, 0, -1):
            display.show(i)
            sleep(1000)
        display.clear()
        signal_state["G"] = toggle_light(signal_state["G"])

        signal_state["Y"] = toggle_light(signal_state["Y"])
        update_display()
        sleep(3000)
        signal_state["Y"] = toggle_light(signal_state["Y"])


def update_display():
    if signal_state.get("R") == "ON":
        display.set_pixel(4, 0, 9)
        pin2.write_digital(1)
    else:
        display.set_pixel(4, 0, 0)
        pin2.write_digital(0)

    if signal_state.get("Y") == "ON":
        display.set_pixel(4, 2, 9)
        pin1.write_digital(1)
    else:
        display.set_pixel(4, 2, 0)
        pin1.write_digital(0)

    if signal_state.get("G") == "ON":
        display.set_pixel(4, 4, 9)
        pin0.write_digital(1)
    else:
        display.set_pixel(4, 4, 0)
        pin0.write_digital(0)


def handle_input():
    if button_a.was_pressed():
        signal_state["R"] = toggle_light(signal_state["R"])
    elif button_b.was_pressed():
        signal_state["G"] = toggle_light(signal_state["G"])
    elif pin_logo.is_touched():
        signal_state["Y"] = toggle_light(signal_state["Y"])
        sleep(200)


def toggle_light(light):
    if light == "ON":
        light = "OFF"
    else:
        light = "ON"
    return light


main()

# mamy 4 opcje sygnalizacji świateł
# 1. za pomocą literek na display'u
# 2. za pomocą pojedyńczych ledów na display'u
# 3. za pomocą ustawionych wcześniej obrazków
#    (tablica która określa które ledy mają świecić i w jakim natężeniu)
# 4. na płytce stykowej używając ledów
