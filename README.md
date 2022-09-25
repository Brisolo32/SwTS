# SwTS
A theme changer for Waybar (Now supporting Sway configs!)

### How it works

It overrides the current config with the one selected using the app, there is no need to add something to the waybar or sway configs

### How to use it

- Create a new directory in `~` called `.swts` and inside there create 2 dirs `wbthemes` and `swconfig`
    - On `wbthemes` you will put your waybar themes
    - On `swconfig` you will put your sway configs
    - All of the configs need to be separated by folders with a specific name
      - Ex: `~/.swts/wbthemes/CoolTheme/...`
      - Another Ex: `~/.swts/swconfig/DefaultConfig/...`

### How to convert your current config/theme into a usable one

- If you haven't done it yet, read "How to use it"
- Make a new dir inside `~/.swts/wbthemes` or `~/.swts/swconfig` with the name of your theme
- Done

if you want you can download a precompiled binary and put it into `/usr/bin/` 
