# DDLC IF ROUTE MOD

A Ren'Py fan mod with original alternate-timeline routes inspired by the IF-route concept.

## Included routes

- Pride IF
- Wrath IF
- Sloth IF
- Greed IF
- Gluttony IF
- Lust IF
- Vainglory IF
- School IF

## Install from GitHub

This repository contains mod scripts only. It does **not** include or redistribute DDLC's original game files.

1. Use a legally obtained copy of classic DDLC compatible with Ren'Py 6.99.
2. Back up the DDLC installation's `game/` folder.
3. Open this repository's `game/` folder.
4. Copy `if_route_mod.rpy` and `if_route_launcher.rpy` directly into DDLC's `game/` folder. Do not copy the repository folder itself.

The layout should be:

```text
DDLC/
  game/
    if_route_mod.rpy
    if_route_launcher.rpy
    ...the existing DDLC files...
```

## Launching the mod

The mod uses the existing **Start Game** button as its entry point. This avoids injecting a custom main-menu overlay, which is unreliable with classic DDLC's older Ren'Py screen setup. Press **Start Game** to enter the IF Route Archive and choose one of the eight routes.

To restore the original DDLC start flow, remove `if_route_launcher.rpy` from the `game/` folder (you can leave `if_route_mod.rpy` in place).

## Troubleshooting

- If DDLC does not start, remove both added `.rpy` files to restore the unmodified game, then check the full traceback in `traceback.txt`.
- If the game starts normally but the mod does not appear, confirm both files are directly inside `DDLC/game/`, not inside a nested repository folder.
- If there is a Ren'Py error, share the complete error screen or the contents of `traceback.txt`, including the line number and exception.

## Notes and credits

This mod expects the character-independent dialogue API and background names supplied by a classic DDLC installation. It uses no bundled DDLC art/audio. DDLC is by Team Salvato; Re:Zero and its characters/world are owned by their respective rights holders. This is an unofficial fan project and is not affiliated with them.
