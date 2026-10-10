# DDLC IF ROUTE MOD
# Original fan-written route framework inspired by alternate-timeline fiction.
# Install into the game/ directory of a compatible DDLC/Monika After Story-style
# Ren'Py mod project or a DDLC Mod Template project.

define ifm_player = Character("Player")
define ifm_m = Character("Monika")
define ifm_s = Character("Sayori")
define ifm_n = Character("Natsuki")
define ifm_y = Character("Yuri")

default ifm_unlocked = []
default ifm_route = ""
default ifm_route_active = False

screen ifm_route_indicator():
    if ifm_route_active and ifm_route:
        frame:
            xalign 0.015
            yalign 0.02
            padding (10, 5)
            background Solid("#111c")
            text "ROUTE: [ifm_route]":
                size 18
                color "#ffffff"

init python:
    if "ifm_route_indicator" not in config.overlay_screens:
        config.overlay_screens.append("ifm_route_indicator")

label if_route_mod:
    $ ifm_route_active = False
    scene black
    with dissolve
    centered "DDLC IF ROUTE MOD"
    "A branching alternate-timeline fan story inspired by the IF-route concept of Re:Zero."
    jump ifm_hub

label if_route_mod_start:
    jump if_route_mod

label ifm_hub:
    $ ifm_route_active = False
    scene black
    with dissolve
    ifm_m "Welcome to the IF Route Archive."
    ifm_m "Every choice can create a different timeline."
    menu:
        "Start a new timeline":
            jump ifm_choose
        "Replay an unlocked route" if len(ifm_unlocked) > 0:
            jump ifm_replay
        "Leave the archive":
            return

label ifm_choose:
    ifm_player "Which path should I take?"
    menu:
        "Pride IF — Refuse to give up":
            $ ifm_route = "Pride IF"
            jump ifm_pride
        "Wrath IF — Strike back":
            $ ifm_route = "Wrath IF"
            jump ifm_wrath
        "Sloth IF — Take the easy way":
            $ ifm_route = "Sloth IF"
            jump ifm_sloth
        "Greed IF — Control every outcome":
            $ ifm_route = "Greed IF"
            jump ifm_greed
        "Gluttony IF — Take what you cannot bear to lose":
            $ ifm_route = "Gluttony IF"
            jump ifm_gluttony
        "Lust IF — Rewrite the bonds between everyone":
            $ ifm_route = "Lust IF"
            jump ifm_lust
        "Vainglory IF — Become the answer":
            $ ifm_route = "Vainglory IF"
            jump ifm_vainglory
        "School IF — A different school day":
            $ ifm_route = "School IF"
            jump ifm_school

label ifm_pride:
    $ ifm_route_active = True
    scene black
    ifm_m "You decided that losing was unacceptable."
    ifm_player "Then I'll keep going. Even if everyone tells me to stop."
    ifm_s "But what if your determination hurts someone?"
    menu:
        "Push forward anyway":
            ifm_m "That's the Pride timeline."
            ifm_player "I will be the one who decides what happens."
        "Admit you need help":
            ifm_s "Maybe refusing to lose doesn't mean refusing everyone."
            ifm_player "Maybe this timeline can change."
    jump ifm_finish

label ifm_wrath:
    $ ifm_route_active = True
    scene black
    ifm_player "If nobody will protect the club, I will."
    ifm_y "Protection can become another word for control."
    menu:
        "Confront everyone":
            ifm_player "Then let them know I won't back down."
        "Lower your guard":
            ifm_n "You don't have to fight every battle."
    jump ifm_finish

label ifm_sloth:
    $ ifm_route_active = True
    scene black
    ifm_s "You could just leave everything alone."
    ifm_player "Maybe that's easier."
    menu:
        "Walk away":
            ifm_m "The timeline continues without you."
        "Turn back":
            ifm_player "No. I can't pretend I didn't see it."
    jump ifm_finish

label ifm_greed:
    $ ifm_route_active = True
    scene black
    ifm_m "You want every possibility to end the way you choose."
    ifm_player "If I plan enough, nobody has to get hurt."
    menu:
        "Control everything":
            ifm_m "And what happens when something refuses to be controlled?"
        "Accept uncertainty":
            ifm_player "I can't save every possible future."
    jump ifm_finish

label ifm_gluttony:
    $ ifm_route_active = True
    scene black
    ifm_y "What makes someone themselves? Their memories? Their choices?"
    ifm_player "If I knew everything, maybe I could fix everything."
    menu:
        "Take the memories":
            ifm_y "Knowledge can become another kind of hunger."
        "Leave them untouched":
            ifm_player "Some things shouldn't belong to me."
    jump ifm_finish

label ifm_lust:
    $ ifm_route_active = True
    scene black
    ifm_s "What if every relationship in the club changed?"
    ifm_player "Then we'd have to learn who we are all over again."
    menu:
        "Rewrite the bonds":
            ifm_m "A completely different timeline begins."
        "Keep the bonds":
            ifm_player "Changing people isn't the same as saving them."
    jump ifm_finish

label ifm_vainglory:
    $ ifm_route_active = True
    scene black
    ifm_m "You believe you can become the answer to every problem."
    ifm_player "Someone has to be the hero."
    menu:
        "Take the role":
            ifm_m "Then everyone will look to you."
        "Reject the pedestal":
            ifm_player "I'm just one person."
    jump ifm_finish

label ifm_school:
    $ ifm_route_active = True
    scene black
    ifm_s "Welcome to a completely different school day!"
    ifm_n "No ominous timelines. Hopefully."
    ifm_y "That sounded ominous."
    menu:
        "Enjoy the normal day":
            ifm_player "Let's just have fun."
        "Look for the anomaly":
            ifm_m "You noticed it too, didn't you?"
    jump ifm_finish

label ifm_finish:
    if ifm_route not in ifm_unlocked:
        $ ifm_unlocked.append(ifm_route)
    $ ifm_route_active = False
    scene black
    with fade
    centered "{size=+12}[ifm_route]{/size}\n\nTIMELINE RECORDED"
    "Route unlocked: [ifm_route]"
    "The choice is now saved in this playthrough."
    jump ifm_hub

label ifm_replay:
    scene black
    "Unlocked timelines:"
    $ replay_choice = None
    python:
        replay_choice = renpy.display_menu([(r, r) for r in ifm_unlocked])
    if replay_choice == "Pride IF":
        $ ifm_route = replay_choice
        jump ifm_pride
    if replay_choice == "Wrath IF":
        $ ifm_route = replay_choice
        jump ifm_wrath
    if replay_choice == "Sloth IF":
        $ ifm_route = replay_choice
        jump ifm_sloth
    if replay_choice == "Greed IF":
        $ ifm_route = replay_choice
        jump ifm_greed
    if replay_choice == "Gluttony IF":
        $ ifm_route = replay_choice
        jump ifm_gluttony
    if replay_choice == "Lust IF":
        $ ifm_route = replay_choice
        jump ifm_lust
    if replay_choice == "Vainglory IF":
        $ ifm_route = replay_choice
        jump ifm_vainglory
    if replay_choice == "School IF":
        $ ifm_route = replay_choice
        jump ifm_school
    jump ifm_hub
