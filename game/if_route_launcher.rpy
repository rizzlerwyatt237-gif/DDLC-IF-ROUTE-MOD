# DDLC IF ROUTE MOD launcher
# Classic DDLC / Ren'Py 6.99 compatibility.
#
# The classic DDLC main-menu screen doesn't reliably show config.overlay_screens.
# Redirect its built-in Start Game action to this mod's entry label instead.
# Remove this file to restore the original DDLC start flow.

init python:
    config.label_overrides["start"] = "if_route_mod_start"
