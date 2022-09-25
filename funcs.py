import os

home_dir = os.environ['HOME']

def replace_waybar_theme(val):
	os.system(f"rm -rf {home_dir}/.config/waybar/*")
	os.system(f"cp -r {home_dir}/.swts/wbthemes/{val}/* {home_dir}/.config/waybar/")

def replace_sway_config(val):
	os.system(f"rm -rf {home_dir}/.config/sway/*")
	os.system(f"cp -r {home_dir}/.swts/swconfig/{val}/* {home_dir}/.config/sway/")	