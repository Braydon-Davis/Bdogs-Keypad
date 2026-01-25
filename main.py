from kmk.modules.encoder import EncoderHandler
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

encoder = EncoderHandler()
keyboard.modules.append(encoder)
encoder.pins = ((2,3),)
encoder.map = [
    (KC.VOLU, KC.VOLD)
]

# === DIRECT PINS (one key per pin) ===
keyboard.col_pins = (0, 1, 2, 3, 4, 5)
keyboard.row_pins = ()
keyboard.diode_orientation = DiodeOrientation.COLUMNS

# Map physical keys → logical order
keyboard.coord_mapping = [
    0, 1, 2, 3, 4, 5
]

# === KEY FUNCTIONS ===
keyboard.keymap = [
    [
        KC.MPRV,      # Key 1
        KC.MPLY,      # Key 2
        KC.MNXT,      # Key 3
        KC.DELETE,      # Key 4
        KC.E,      # Key 5
        KC.F       # Key 6
    ]
]

if __name__ == '__main__':
    keyboard.go()
