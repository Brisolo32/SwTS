#!/usr/bin/python
import PySimpleGUIQt as sg
import os
from funcs import *
from layouts import *

sg.LOOK_AND_FEEL_TABLE['Native'] = {
    'BACKGROUND': sg.COLOR_SYSTEM_DEFAULT,
    'TEXT':       sg.COLOR_SYSTEM_DEFAULT,
    'INPUT':      sg.COLOR_SYSTEM_DEFAULT,
    'TEXT_INPUT': sg.COLOR_SYSTEM_DEFAULT,
    'SCROLL':     sg.COLOR_SYSTEM_DEFAULT,
    'BUTTON':    (sg.COLOR_SYSTEM_DEFAULT, sg.COLOR_SYSTEM_DEFAULT),
    'PROGRESS':   sg.DEFAULT_PROGRESS_BAR_COLOR,
    'BORDER': 1,
    'SLIDER_DEPTH': 0,
    'PROGRESS_DEPTH': 0,
}

sg.theme('Native')

window = sg.Window('SwTS', tab_layout, size=(290, 4))
while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED:
		break

	# Events for Waybar Layout
	if event == '-WBOKBTN-':
		replace_waybar_theme(values[0])
		break
	if event == '-WBAPPLYBTN-':
		replace_waybar_theme(values[0])

		window['-WBOUTPUT-'].update(
			'\nPress MOD+Shift+C to Restart Sway\nor kill waybar and start it up again'
		)

	# Events for Sway Layout
	if event == '-SWOKBTN-':
		replace_sway_config(values[1])
		break
	if event == '-SWAPPLYBTN-':
		replace_sway_config(values[1])

		window['-SWOUTPUT-'].update(
			'\nPress MOD+Shift+C to Restart Sway\nor log off and log on again'
		)
window.close()