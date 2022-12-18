import os
import re
import socket
import subprocess
from typing import List  # noqa: F401
from libqtile import layout, bar, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule
from libqtile.command import lazy
import qtile_bar

# Super key (windows key)
MOD_KEY = "mod4"

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

# Send a window to the other screen
# Set switch_group to true to also switch to that group on current screen
# Set switch_screen to False to stay on current screen
def window_to_other_screen(qtile, switch_group=False, switch_screen=True):
    i = qtile.screens.index(qtile.current_screen)
    # If we are on primary screen go to secondary screen
    if i < len(qtile.screens) - 1:
        other_screen_index = i + 1 
        group = qtile.screens[other_screen_index].group.name
    # Else go to primary screen
    else:
        other_screen_index = i - 1 
        group = qtile.screens[other_screen_index].group.name

    qtile.current_window.togroup(group, switch_group=switch_group)
    if switch_screen:
        qtile.cmd_to_screen(other_screen_index)


keys = [

# Most of our keybindings are in sxhkd file - except these

# SUPER + FUNCTION KEYS

    Key([MOD_KEY], "f", lazy.window.toggle_fullscreen()),
    Key([MOD_KEY], "q", lazy.window.kill()),

# SUPER + SHIFT KEYS

    Key([MOD_KEY, "shift"], "q", lazy.window.kill()),
    Key([MOD_KEY, "shift"], "r", lazy.restart()),

# QTILE LAYOUT KEYS
    Key([MOD_KEY], "n", lazy.layout.normalize()),
    Key([MOD_KEY], "space", lazy.next_layout()),

# CHANGE FOCUS
    Key([MOD_KEY], "Up", lazy.layout.up()),
    Key([MOD_KEY], "Down", lazy.layout.down()),
    Key([MOD_KEY], "Left", lazy.layout.left()),
    Key([MOD_KEY], "Right", lazy.layout.right()),
    Key([MOD_KEY], "k", lazy.layout.up()),
    Key([MOD_KEY], "j", lazy.layout.down()),
    Key([MOD_KEY], "h", lazy.layout.left()),
    Key([MOD_KEY], "l", lazy.layout.right()),


# SWITCH SCREEN FOCUS
    Key([MOD_KEY], "period", lazy.next_screen()),

# SWITCH WINDOW TO OTHER SCREEN
    Key([MOD_KEY, "shift"], "period", lazy.function(window_to_other_screen)),

# RESIZE UP, DOWN, LEFT, RIGHT
    Key([MOD_KEY, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([MOD_KEY, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([MOD_KEY, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([MOD_KEY, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([MOD_KEY, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([MOD_KEY, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([MOD_KEY, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([MOD_KEY, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),


# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([MOD_KEY, "shift"], "f", lazy.layout.flip()),

# FLIP LAYOUT FOR BSP
    Key([MOD_KEY, "mod1"], "k", lazy.layout.flip_up()),
    Key([MOD_KEY, "mod1"], "j", lazy.layout.flip_down()),
    Key([MOD_KEY, "mod1"], "l", lazy.layout.flip_right()),
    Key([MOD_KEY, "mod1"], "h", lazy.layout.flip_left()),

# MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([MOD_KEY, "shift"], "k", lazy.layout.shuffle_up()),
    Key([MOD_KEY, "shift"], "j", lazy.layout.shuffle_down()),
    Key([MOD_KEY, "shift"], "h", lazy.layout.shuffle_left()),
    Key([MOD_KEY, "shift"], "l", lazy.layout.shuffle_right()),

# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([MOD_KEY, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([MOD_KEY, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([MOD_KEY, "shift"], "Left", lazy.layout.swap_left()),
    Key([MOD_KEY, "shift"], "Right", lazy.layout.swap_right()),

# TOGGLE FLOATING LAYOUT
    Key([MOD_KEY, "shift"], "space", lazy.window.toggle_floating()),

# SWITCH KEYBOARD LAYOUT
    Key([MOD_KEY], "comma", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout.")

    ]



groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

# FOR AZERTY KEYBOARDS
#group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "section", "egrave", "exclam", "ccedilla", "agrave",]

#group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "0",]
group_labels = ["", "", "", "", "", "", "", "", "", "",]
#group_labels = ["Web", "Edit/chat", "Image", "Gimp", "Meld", "Video", "Vb", "Files", "Mail", "Music",]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall",]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([MOD_KEY], i.name, lazy.group[i.name].toscreen()),
        Key([MOD_KEY], "Tab", lazy.screen.next_group()),
        Key([MOD_KEY, "shift" ], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        Key([MOD_KEY, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])


def init_layout_theme():
    return {"margin":5,
            "border_width":2,
            "border_focus": "#5e81ac",
            "border_normal": "#4c566a"
            }

layout_theme = init_layout_theme()


layouts = [
    layout.MonadTall(margin=8, border_width=2, border_focus="ede732", border_normal="#4c566a"),
    layout.MonadWide(margin=8, border_width=2, border_focus="#5e81ac", border_normal="#4c566a"),
    layout.Matrix(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme)
]


# SCREEN AND BAR CONFIGURATION
widget_defaults = qtile_bar.get_widget_defaults()
screens = [
    Screen(top=bar.Bar(widgets=qtile_bar.get_widgets_screen1(), size=26, opacity=0.9)),
    Screen(top=bar.Bar(widgets=qtile_bar.get_widgets_screen2(), size=26, opacity=0.9))
]


# MOUSE CONFIGURATION
mouse = [
    Drag([MOD_KEY], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([MOD_KEY], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([MOD_KEY], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []

# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
# BEGIN

#########################################################
################ assign apps to groups ##################
#########################################################
# @hook.subscribe.client_new
# def assign_app_group(client):
#     d = {}
#     #####################################################################################
#     ### Use xprop fo find  the value of WM_CLASS(STRING) -> First field is sufficient ###
#     #####################################################################################
#     d[group_names[0]] = ["Navigator", "Firefox", "Vivaldi-stable", "Vivaldi-snapshot", "Chromium", "Google-chrome", "Brave", "Brave-browser",
#               "navigator", "firefox", "vivaldi-stable", "vivaldi-snapshot", "chromium", "google-chrome", "brave", "brave-browser", ]
#     d[group_names[1]] = [ "Atom", "Subl", "Geany", "Brackets", "Code-oss", "Code", "TelegramDesktop", "Discord",
#                "atom", "subl", "geany", "brackets", "code-oss", "code", "telegramDesktop", "discord", ]
#     d[group_names[2]] = ["Inkscape", "Nomacs", "Ristretto", "Nitrogen", "Feh",
#               "inkscape", "nomacs", "ristretto", "nitrogen", "feh", ]
#     d[group_names[3]] = ["Gimp", "gimp" ]
#     d[group_names[4]] = ["Meld", "meld", "org.gnome.meld" "org.gnome.Meld" ]
#     d[group_names[5]] = ["Vlc","vlc", "Mpv", "mpv" ]
#     d[group_names[6]] = ["VirtualBox Manager", "VirtualBox Machine", "Vmplayer",
#               "virtualbox manager", "virtualbox machine", "vmplayer", ]
#     d[group_names[7]] = ["Thunar", "Nemo", "Caja", "Nautilus", "org.gnome.Nautilus", "Pcmanfm", "Pcmanfm-qt",
#               "thunar", "nemo", "caja", "nautilus", "org.gnome.nautilus", "pcmanfm", "pcmanfm-qt", ]
#     d[group_names[8]] = ["Evolution", "Geary", "Mail", "Thunderbird",
#               "evolution", "geary", "mail", "thunderbird" ]
#     d[group_names[9]] = ["Spotify", "Pragha", "Clementine", "Deadbeef", "Audacious",
#               "spotify", "pragha", "clementine", "deadbeef", "audacious" ]
#     ######################################################################################
#
# wm_class = client.window.get_wm_class()[0]
#
#     for i in range(len(d)):
#         if wm_class in list(d.values())[i]:
#             group = list(d.keys())[i]
#             client.togroup(group)
#             client.group.cmd_toscreen(toggle=False)

# END
# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME



main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules, 
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='Arcolinux-welcome-app.py'),
    Match(wm_class='Arcolinux-tweak-tool.py'),
    Match(wm_class='Arcolinux-calamares-tool.py'),
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='Arandr'),
    Match(wm_class='feh'),
    Match(wm_class='Galculator'),
    Match(wm_class='arcolinux-logout'),
    Match(wm_class='xfce4-terminal'),
    Match(wm_class='pystopwatch')

],  fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "LG3D"
