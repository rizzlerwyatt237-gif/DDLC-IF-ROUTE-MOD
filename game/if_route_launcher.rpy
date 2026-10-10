# IF ROUTE MOD launcher.
# Adds a small button to the Ren'Py overlay so the route story can be started
# without replacing DDLC's normal start label or main menu.

init python:
    if "if_route_mod_launcher" not in config.overlay_screens:
        config.overlay_screens.append("if_route_mod_launcher")

screen if_route_mod_launcher():
    if main_menu:
        textbutton "IF ROUTE MOD":
            xalign 0.5
            yalign 0.94
            action Start("if_route_mod_start")
