# DDLC IF ROUTE MOD

A Ren'Py/DDLC fan mod containing original alternate-timeline IF routes.

## Included routes

- Pride IF
- Wrath IF
- Sloth IF
- Greed IF
- Gluttony IF
- Lust IF
- Vainglory IF
- School IF

## Install directly from this GitHub repository

This repository contains the mod scripts only. It does **not** redistribute DDLC's original game files.

1. Use a legally obtained DDLC installation that supports `.rpy` mod scripts.
2. Open DDLC's installation folder.
3. Open its `game` folder.
4. From this repository, open the `game` folder.
5. Copy these two files directly into DDLC's `game` folder:
   - `if_route_mod.rpy`
   - `if_route_launcher.rpy`
6. Do **not** copy the entire GitHub repository folder into `DDLC/game/`.

Correct layout:

```text
DDLC/
  game/
    if_route_mod.rpy
    if_route_launcher.rpy
    ...existing DDLC files...
```

## Start the mod

The launcher adds an **IF ROUTE MOD** button to DDLC's main menu. Clicking it starts the `if_route_mod_start` label.

The mod uses DDLC's existing character definitions/assets through its own character objects and uses DDLC background names. Route unlocks are stored with Ren'Py `persistent` data so they survive restarting the game.

## If it still errors

Send the **complete Ren'Py error screen**, especially the file name, line number, and error message. Do not send only the first line; the traceback tells us exactly which GitHub script needs fixing.

## Legal / credits

This is an unofficial fan project. DDLC and its original assets belong to Team Salvato. Re:Zero and its original characters/world belong to their respective rights holders. This repository contains original fan-written code and does not include their copyrighted game assets.
