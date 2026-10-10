# DDLC IF ROUTE MOD

A Ren'Py-based DDLC fan mod inspired by the alternate-timeline / IF-route idea of **Re:Zero**.

## What this is

This is an actual `.rpy` mod source project. It adds a branching IF-route story to a compatible DDLC installation without replacing DDLC's normal `start` label.

### Included routes

- Pride IF
- Wrath IF
- Sloth IF
- Greed IF
- Gluttony IF
- Lust IF
- Vainglory IF
- School IF

Each route has choices and two possible conclusions. Completing a route records it persistently and enables the route archive.

## Installation

This repository is a **DDLC mod source project**, not a redistribution of DDLC itself.

1. Obtain a legitimate copy of DDLC.
2. Back up the DDLC `game` folder.
3. Download this repository.
4. Copy **both** files from this repository's `game/` folder into your DDLC `game/` folder:
   - `if_route_mod.rpy`
   - `if_route_launcher.rpy`
5. Start DDLC.
6. On the DDLC main menu, look for the **IF ROUTE MOD** button near the bottom-center of the screen.
7. Click it. The mod should begin with the IF Route introduction.

The launcher is an overlay screen, so it does not require replacing DDLC's original `script.rpy` or `start` label. Ren'Py supports overlay screens through `config.overlay_screens`. See the official Ren'Py documentation for configuration details.

## How to verify it works

A successful installation should show **IF ROUTE MOD** on the main menu. Clicking it should show:

> Something feels different today.

Then choose **Follow the choice that feels right**. You should see all eight IF routes.

Choose any route, finish it, and return to the archive. The route is recorded in persistent data so it remains available after restarting the game.

If the button does not appear, make sure both `.rpy` files are directly inside DDLC's `game/` folder and not inside another nested folder.

## Development

Main story source:

`game/if_route_mod.rpy`

Launcher:

`game/if_route_launcher.rpy`

Ren'Py compiles `.rpy` files automatically when the game starts. The project intentionally does not include DDLC or Re:Zero copyrighted game assets.

## Route design

The routes are separate alternate timelines rather than simply renamed versions of the seven deadly sins. The goal is to capture the *idea* of IF-route storytelling while using original fan-written scenes.

## Credits

DDLC is created by Team Salvato.

Re:Zero is created by Tappei Nagatsuki and its respective rights holders.

This is an unofficial fan project and is not affiliated with Team Salvato or the creators/rightsholders of Re:Zero.
