import os
from libqtile import widget
import arcobattery

# COLORS FOR THE BAR
#Theme name : ArcoLinux Default
colors = [
    ["#2F343F", "#2F343F"], # color 0
    ["#2F343F", "#2F343F"], # color 1
    ["#c0c5ce", "#c0c5ce"], # color 2
    ["#fba922", "#fba922"], # color 3
    ["#3384d0", "#3384d0"], # color 4
    ["#f3f4f5", "#f3f4f5"], # color 5
    ["#cd1f3f", "#cd1f3f"], # color 6
    ["#62FF00", "#62FF00"], # color 7
    ["#6790eb", "#6790eb"], # color 8
    ["#a9a9a9", "#a9a9a9"] # color 9
] 

# WIDGETS FOR THE BAR

regular_font = "Ubuntu"
regular_font_size = 15
bold_font = "Ubuntu Bold"
clock_font_size = 17

home = os.path.expanduser('~')

def separator():
    return widget.Sep(
        linewidth = 1,
        padding = 10,
        foreground = colors[2],
        background = colors[1]
    )


widgets_list = [
    widget.GroupBox(
        font="FontAwesome",
        fontsize = 16,
        margin_y = 2,
        margin_x = 0,
        padding_y = 6,
        padding_x = 5,
        borderwidth = 2,
        disable_drag = True,
        active = colors[9], # Active means someting is on that workspace
        inactive = colors[5], # Inactive means no window is open on that workspace
        rounded = False,
        highlight_method = "line", # Draws line under groups that are on a screen 
        highlight_color = colors[3],
        this_current_screen_border = colors[6], # Color of the line under the group open on this screen for the current screen
        this_screen_border = colors[4], # Color of the group open on the other screen for the current screen
        other_current_screen_border = colors[6], # Color of the line under the group open on this screen for the other screen
        other_screen_border = colors[4], # Color of the line under the group open on the other screen for the other screen
        foreground = colors[2],
        background = colors[1]
    ),
    separator(),
    widget.CurrentLayout(
        font = bold_font,
        fontsize = regular_font_size,
        foreground = colors[5],
        background = colors[1]
    ),
    separator(),
    widget.WindowName(
        font=regular_font,
        fontsize = regular_font_size,
        foreground = colors[5],
        background = colors[1],
    ),
    separator(),
    widget.ThermalSensor(
        font = regular_font,
        fontsize = regular_font_size,
        foreground = colors[5],
        foreground_alert = colors[6],
        background = colors[1],
        metric = True,
        padding = 3,
        threshold = 80
    ),
    separator(),
    widget.OpenWeather(
       location="Montreal, CA",
       format="{location_city}: {temp} °{units_temperature}, {weather_details}",
       font = regular_font,
       fontsize = regular_font_size,
       background = colors[1]
    ),
    separator(),
    arcobattery.BatteryIcon(
        padding=0,
        scale=0.7,
        y_poss=2,
        theme_path=home + "/.config/qtile/icons/battery_icons_horiz",
        update_interval = 5,
        background = colors[1]
    ),
    separator(),
    widget.TextBox(
        font="FontAwesome",
        text="  ",
        foreground=colors[3],
        background=colors[1],
        padding = 0,
        fontsize=16
    ),
    widget.Clock(
        foreground = colors[5],
        background = colors[1],
        fontsize = clock_font_size,
        font = regular_font,
        format="%Y-%m-%d - %H:%M"
    ),
    separator(),
    widget.KeyboardLayout(
        configured_keyboards=['us', 'ca'],
        font = regular_font,
        fontsize = regular_font_size,
        background = colors[1]
    ),
    separator(),
    widget.Systray(
        background=colors[1],
        icon_size=22,
        padding = 6
    )
]


def get_widgets_screen1():
    return widgets_list[:]

def get_widgets_screen2():
    # Remove systray and extra separator
    return widgets_list[:-2]

def get_widget_defaults():
    return dict(
        font="Noto Sans",
        fontsize = 12,
        padding = 2,
        background=colors[1]
    )
