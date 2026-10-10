# DDLC IF ROUTE MOD
# Original fan-written route framework inspired by alternate-timeline fiction.
# Install into the game/ directory of a compatible DDLC/Monika After Story-style
# Ren'Py mod project or a DDLC Mod Template project.

label if_route_mod_start:
    scene bg club_day
    with dissolve

    s "Something feels different today."
    m "Different?"
    s "Like we're standing at the beginning of a story we've already lived."
    n "The thought should have been impossible."
    n "But somehow, it felt familiar."

    $ if_route_mod_setup()

    if persistent.if_route_mod_completed:
        jump if_route_hub

    menu:
        "Follow the choice that feels right":
            jump if_route_choice
        "Turn away from the strange feeling":
            jump if_route_normal_intro

label if_route_normal_intro:
    n "For one quiet afternoon, nobody questioned anything."
    s "Maybe not every story needs to be complicated."
    m "That's a nice thought."
    n "But the strange feeling never completely disappeared."
    n "THE END — THE UNCHOSEN TIMELINE"
    return

label if_route_choice:
    m "If you could change one decision you've already made... would you?"

    menu:
        "Refuse to accept anyone else's rules":
            $ if_route_mod_set_route("pride")
            jump if_route_pride
        "Protect everyone, even if they hate you for it":
            $ if_route_mod_set_route("wrath")
            jump if_route_wrath
        "Stop fighting and choose the quiet life":
            $ if_route_mod_set_route("sloth")
            jump if_route_sloth
        "Make every possible outcome work":
            $ if_route_mod_set_route("greed")
            jump if_route_greed
        "Learn everything, even what should remain unknown":
            $ if_route_mod_set_route("gluttony")
            jump if_route_gluttony
        "Put every relationship above the original story":
            $ if_route_mod_set_route("lust")
            jump if_route_lust
        "Become the person everyone believes you should be":
            $ if_route_mod_set_route("vainglory")
            jump if_route_vainglory
        "Treat this like an ordinary school day":
            $ if_route_mod_set_route("school")
            jump if_route_school

label if_route_hub:
    scene bg club_day
    with dissolve
    m "Welcome back to the IF Route Archive."
    m "Every route is a different answer to the same question: what happens when one choice changes everything?"

    menu:
        "Pride IF":
            jump if_route_pride
        "Wrath IF":
            jump if_route_wrath
        "Sloth IF":
            jump if_route_sloth
        "Greed IF":
            jump if_route_greed
        "Gluttony IF":
            jump if_route_gluttony
        "Lust IF":
            jump if_route_lust
        "Vainglory IF":
            jump if_route_vainglory
        "School IF":
            jump if_route_school
        "Leave the archive":
            return

label if_route_pride:
    scene bg club_day
    with dissolve
    m "Pride IF."
    n "You decide that nobody gets to write your future for you."
    s "You don't have to prove you're stronger than everyone else."
    m "Maybe I do."
    n "Every warning becomes a challenge. Every disagreement becomes evidence that you must be right."
    menu:
        "Admit that you were wrong":
            n "For the first time, the timeline bends without breaking."
            n "Pride does not disappear. It becomes something you can control."
            jump if_route_good_end
        "Double down":
            n "The club becomes a stage, and everyone else becomes an audience."
            n "When nobody is left to argue with, victory feels exactly like loneliness."
            jump if_route_dark_end

label if_route_wrath:
    scene bg club_day
    with dissolve
    m "Wrath IF."
    n "You decide that protecting people means deciding who deserves your trust."
    y "You can't keep treating every disagreement like a threat."
    n "But fear is persuasive when it calls itself protection."
    menu:
        "Lower your guard":
            n "You finally tell the others what you were afraid would happen."
            n "They don't fix everything. They simply stay."
            jump if_route_good_end
        "Trust nobody":
            n "The walls become taller. Then thicker. Then permanent."
            n "You protected everyone from danger by becoming the danger nobody could reach."
            jump if_route_dark_end

label if_route_sloth:
    scene bg residential_day
    with dissolve
    m "Sloth IF."
    n "You choose the path with the least resistance."
    s "Maybe that's not always a bad thing."
    n "For a while, it isn't."
    n "Homework waits. Problems wait. Tomorrow waits."
    menu:
        "Get up and face tomorrow":
            n "Rest becomes recovery instead of escape."
            jump if_route_good_end
        "Stay where nothing can change":
            n "The timeline doesn't end with a catastrophe."
            n "It simply stops moving."
            jump if_route_dark_end

label if_route_greed:
    scene bg club_day
    with dissolve
    m "Greed IF."
    n "You refuse to accept a future where anyone has to lose."
    m "Then I'll find a way for everybody to win."
    n "One plan becomes ten. Ten become a hundred."
    n "Soon, every person is a variable and every conversation is a calculation."
    menu:
        "Accept that some things cannot be controlled":
            n "You stop trying to own every possible future."
            jump if_route_good_end
        "Control every variable":
            n "You get exactly what you wanted: a perfect plan."
            n "Nobody is happy inside it."
            jump if_route_dark_end

label if_route_gluttony:
    scene bg club_day
    with dissolve
    m "Gluttony IF."
    n "You become obsessed with knowing every hidden answer."
    y "Some memories aren't yours to take."
    n "But curiosity can become hunger."
    menu:
        "Stop reading the lives of others":
            n "You choose people over information."
            jump if_route_good_end
        "Keep consuming every secret":
            n "Names blur. Memories overlap."
            n "You know everything except which thoughts are truly yours."
            jump if_route_dark_end

label if_route_lust:
    scene bg club_day
    with dissolve
    m "Lust IF."
    n "In this timeline, connection becomes the force that changes the story."
    s "Then let's stop pretending people are pieces on a board."
    n "Friendship, affection, jealousy, and trust pull the timeline in directions nobody predicted."
    menu:
        "Respect everyone's choice":
            n "Love becomes something freely given instead of something possessed."
            jump if_route_good_end
        "Force the perfect relationship":
            n "The perfect relationship becomes a cage."
            jump if_route_dark_end

label if_route_vainglory:
    scene bg club_day
    with dissolve
    m "Vainglory IF."
    n "You become obsessed with the version of yourself that everyone else applauds."
    s "Who are you when nobody is watching?"
    n "The question hurts more than any insult."
    menu:
        "Answer honestly":
            n "You let the mask fall."
            jump if_route_good_end
        "Become the perfect version":
            n "The applause never stops. Neither does the performance."
            jump if_route_dark_end

label if_route_school:
    scene bg club_day
    with dissolve
    n "School IF."
    n "No world-ending prophecy. No impossible destiny. Just a clubroom after classes."
    s "Honestly? I could get used to this."
    menu:
        "Enjoy the ordinary day":
            n "For once, the alternate timeline is allowed to be happy."
            jump if_route_good_end
        "Look for the hidden timeline":
            n "Even an ordinary school day can hide a door."
            n "You open it."
            jump if_route_archive_end

label if_route_good_end:
    scene bg club_day
    with dissolve
    n "The timeline changes, but it doesn't have to destroy everything."
    m "Maybe an IF route isn't about finding the correct answer."
    m "Maybe it's about seeing what every answer costs."
    $ if_route_mod_complete()
    n "ROUTE CLEAR — HOPEFUL TIMELINE"
    jump if_route_archive_end

label if_route_dark_end:
    scene bg club_day
    with dissolve
    n "The choice has consequences."
    n "The timeline continues without you seeing what could have happened differently."
    $ if_route_mod_complete()
    n "ROUTE CLEAR — BROKEN TIMELINE"
    jump if_route_archive_end

label if_route_archive_end:
    scene bg club_day
    with dissolve
    m "The route has been recorded."
    m "You can return to the archive and see another possibility."
    menu:
        "Return to IF Route Archive":
            jump if_route_hub
        "End this session":
            return

init python:
    def if_route_mod_setup():
        if not hasattr(persistent, "if_route_mod_completed"):
            persistent.if_route_mod_completed = False
        if not hasattr(persistent, "if_route_mod_routes"):
            persistent.if_route_mod_routes = []

    def if_route_mod_set_route(route_name):
        persistent.if_route_mod_current = route_name

    def if_route_mod_complete():
        persistent.if_route_mod_completed = True
        route_name = getattr(persistent, "if_route_mod_current", "unknown")
        routes = getattr(persistent, "if_route_mod_routes", [])
        if route_name not in routes:
            routes.append(route_name)
        persistent.if_route_mod_routes = routes
