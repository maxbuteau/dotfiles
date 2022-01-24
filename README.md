# Install on your Linux system
To install my dot files on your system, run the following command:

```
curl -Lks https://bit.ly/3JV95oP | /bin/bash
```
If there are conflicting files, they will not be copied. Please either move them or delete them.

## The Software I Use
### Browsers
* google-chrome-stable
* firefox
### Communication
* thunderbird
* discord
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
* install lib32-intel for steam
* optimus-manager-qt (for the icon, set driver to intel and tearfree to yes to avoid screen tearing)
### Other
* nitrogen
* dmenu
* galculator
* picom
* sxhkd
* nbfc (notebook fan control), some good configs:
    * Asus Zenbook UX430UQ
    * Asus Zenbook UX430UA
    * Asus ROG G752VS
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


