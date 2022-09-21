#!/usr/bin/python
import PySimpleGUIQt as sg
import os

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

themesArray = os.listdir(os.environ['HOME'] + '/wbthemes')

layout = [  
	[
		sg.Text('Select a Theme to apply')
	],
	[
		sg.Combo(themesArray)
	],
	[
		sg.Text("", key="-OUTPUT-")
	],
	[
		sg.Button('Ok'), 
		sg.Button('Apply'),
		sg.Button('About')
	] 
]

window = sg.Window('SwTS', layout, size=(290, 4))
while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED:
		break
	if event == 'Ok':
		break
	if event == 'Apply':
		os.system(f"rm -rf {os.environ['HOME']}/.config/waybar/*")
		os.system(f"cp -r {os.environ['HOME']}/wbthemes/{values[0]}/* {os.environ['HOME']}/.config/waybar/")

		window['-OUTPUT-'].update('\nPress MOD+Shift+C to Restart Sway\nor kill waybar and start it up again')
	if event == 'About':
		sg.Popup('Made by Brisolo32\nLicensed under the MIT License')
window.close()
