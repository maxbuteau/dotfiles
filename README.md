# Install on your Linux system
To install my dot files on your system, run the following command:

```
curl -Lks https://bit.ly/3JV95oP | /bin/bash
```
If there are conflicting files, they will not be copied. Please either move them or delete them.

# Troubleshooting
When updating your system, errors related to arch linux keyring can generally be fixed by first running:
```
sudo pacman -S archlinux-keyring
```

## The Software I Use
### Browsers
* google-chrome-stable
* firefox
### Communication
* thunderbird
* discord (use the flatpak version, seems to get rid of the lag on arch linux)
* zoom
### File Managers
* pcmanfm
* vifm
### Window Managers
* qtile
### Terminal Emulators
* alacritty
### Development
* vim
* neovim
* nodejs
* npm
### Office Work
* Libre Office
* Evince
* Latex
### Virtual Machines
* VirtualBox
### Media
* Spotify
* VLC
* Gimp
* Mirage
### Graphics
* xf86-video-intel
* nvidia
* install mesa-utils
* optimus-manager
    * Setting ```dynamic_power_management=fine``` and setting graphics to hybrid seems to give a good result (in /etc/optimus-manager/optimus-manager.conf) 
* install lib32-intel for steam
* optimus-manager-qt (for the icon, set driver to intel and tearfree to yes to avoid screen tearing)
### Other
* nitrogen
* dmenu
* galculator
* picom
* sxhkd
* starship (command line prompt)
* nbfc (notebook fan control), some good configs:
    * Asus Zenbook UX430UQ
    * Asus Zenbook UX430UA
    * Asus ROG G752VS
* betterlockscreen (used with arcolinux-logout, might want to remove that)
    * Pressing space to wake from sleep registers as first character, so look into it or press shift
### Hardware Specific
* Trackpad (in /etc/X11/xorg.conf.d/30-touchpad.conf)
```
Section "InputClass"
    Identifier "touchpad"
    Driver "libinput"
    MatchIsTouchpad "on"
    Option "Tapping" "on"
    Option "NaturalScrolling" "true"
EndSection
```
