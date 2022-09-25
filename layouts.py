import os
import PySimpleGUIQt as sg
from funcs import *

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

waybar_themes_array = os.listdir(f'{home_dir}/.swts/wbthemes')
sway_config_array = os.listdir(f'{home_dir}/.swts/swconfig')

waybar_layout = [  
	[
		sg.Text('Select a Theme to apply')
	],
	[
		sg.Combo(waybar_themes_array)
	],
	[
		sg.Text("", key="-WBOUTPUT-")
	],
	[
		sg.Button('Ok', key="-WBOKBTN-"), 
		sg.Button('Apply', key="-WBAPPLYBTN-"),
	] 
]

sway_config_layout = [
	[
		sg.Text('Select a Config to apply')
	],
	[
		sg.Combo(sway_config_array)
	],
	[
		sg.Text("", key="-SWOUTPUT-")
	],
	[
		sg.Button('Ok', key="-SWOKBTN-"), 
		sg.Button('Apply', key="-SWAPPLYBTN-"),
	] 
]



about_layout = [
	[
		sg.Text('SwTS')
	],
	[
		sg.Text('Change your Sway and Waybar theme in a easier way!')
	],
	[
		sg.Text('')
	],
	[
		sg.Text('Made by Brisolo32 in Brazil')
	]
]


tab_layout = [
	[
		sg.TabGroup(
			[
				[
					sg.Tab(
						"Waybar",
						waybar_layout,
						border_width=10,
						background_color='white',
					),
					sg.Tab(
						"Sway",
						sway_config_layout,
						border_width=10,
						background_color='white',
					),
					sg.Tab(
						"About",
						about_layout,
						border_width=10,
						background_color='white',
						element_justification='center'
					),
				]
			]
		)
	]
]