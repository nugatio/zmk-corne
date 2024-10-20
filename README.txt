ZMK config for corne split keyboard based on hands down neu virbranium v (Neu-vv)

keyboard: corne (https://github.com/foostan/crkbd)
firmware: zmk (https://zmk.dev/)
layout: hands down neu virbranium v (https://sites.google.com/alanreiser.com/handsdown/home/hands-down-neu#h.julmingx5jxo)


                          LAYOUT
     ╭─────────────────────╮ ╭─────────────────────╮
ESC  │  X   W   M   G   !? │ │ #$  .:  "'   J   B  │ VUP/PRV
Z    │  S   C   N   T   K  │ │ ,;   A   E   I   H  │ VM/PP
CAPS │  V   P   L   D   /* │ │ -+   U   O   Y   F  │ VDN/NXT
     ╰───────╮  Q   R  BSP │ │ SPC RET TAB ╭───────╯
             ╰─────────────╯ ╰─────────────╯


CONFIG CONTENTS
overview of all layers      > overview.txt
quick adjust settings       > setings.dtsi
main file                   > corne.keymap
key position names          > positions.dtsi
keymap/layout config        > keymap.dtsi
combo config                > combos.dtsi
behavior config             > behaviors.dtsi


HELPFUL INFORMATION
combo: combine multiple keypresses to output a different key
[https://zmk.dev/docs/keymaps/combos]

hold-tab: key will output the 'hold' behavior if it's held for a while, and output the 'tap' behavior when it's tapped quickly
[https://zmk.dev/docs/keymaps/behaviors/hold-tap]

mod-morph: invokes a different behavior depending on whether any of the specified modifiers are being held during the key press
[https://zmk.dev/docs/keymaps/behaviors/mod-morph]
