input.onButtonPressed(Button.A, function () {
    if (Spieler < 8) {
        Spieler += 1
    }
    basic.showNumber(Spieler)
})
radio.onReceivedString(function (receivedString) {
    serial.writeString("" + (receivedString.split("_")))
    if ("FWD_1" == receivedString) {
        basic.showLeds(`
            # # # # .
            # # # # .
            # . . . .
            . . . . .
            . . . . .
            `)
    }
    if ("RWD_1" == receivedString) {
        basic.showLeds(`
            . . . . .
            # # # . .
            # # # # #
            # # # # #
            . . . . .
            `)
    }
})
input.onButtonPressed(Button.B, function () {
    if (Spieler > 1) {
        Spieler += -1
    }
    basic.showNumber(Spieler)
})
let Spieler = 0
Spieler = 1
radio.setGroup(1)
basic.forever(function () {
	
})
