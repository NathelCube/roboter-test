def on_button_pressed_a():
    global Spieler
    if Spieler < 8:
        Spieler += 1
    basic.show_number(Spieler)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    serial.write_string("" + str((receivedString.split("_"))))
    if "FWD_1" == receivedString:
        basic.show_leds("""
            # # # # .
                        # # # # .
                        # . . . .
                        . . . . .
                        . . . . .
        """)
    if "RWD_1" == receivedString:
        basic.show_leds("""
            . . . . .
                        # # # . .
                        # # # # #
                        # # # # #
                        . . . . .
        """)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global Spieler
    if Spieler > 1:
        Spieler += -1
    basic.show_number(Spieler)
input.on_button_pressed(Button.B, on_button_pressed_b)

Spieler = 0
Spieler = 1
radio.set_group(1)

def on_forever():
    pass
basic.forever(on_forever)
