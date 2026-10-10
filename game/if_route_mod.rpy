# DDLC IF ROUTE MOD
# Original fan-written branching horror campaign for classic DDLC / Ren'Py.
# Install this file directly in DDLC's game/ directory.
#
# Story rule: this run does not return to a route hub. It reaches an ending
# only when all four club girls have died or one of them kills the Player.

define ifm_player = Character("MC")
define ifm_m = Character("Monika")
define ifm_s = Character("Sayori")
define ifm_n = Character("Natsuki")
define ifm_y = Character("Yuri")

default persistent.ifm_unlocked = []
default ifm_route = ""
default ifm_route_active = False
default ifm_day = 1
default ifm_pressure = 0
default ifm_trust = 0
default ifm_bond_s = 0
default ifm_bond_n = 0
default ifm_bond_y = 0
default ifm_bond_m = 0
default ifm_alive_s = True
default ifm_alive_n = True
default ifm_alive_y = True
default ifm_alive_m = True
default ifm_player_alive = True
default ifm_final_killer = "Monika"

screen ifm_route_indicator():
    if ifm_route_active and ifm_route:
        frame:
            xalign 0.015
            yalign 0.02
            padding (10, 6)
            background Solid("#111111cc")
            vbox:
                spacing 2
                text "ROUTE: [ifm_route]":
                    size 17
                    color "#ffffff"
                text "DAY [ifm_day]  |  PRESSURE [ifm_pressure]":
                    size 11
                    color "#dddddd"


# Display every living girl with the correct DDLC layout transform. In DDLC's
# transforms.rpy, t11 is the one-person layout, t21/t22 are for two, t31-t33
# are for three, and t41-t44 are for four characters. Keeping the layout count
# consistent prevents sprites from being oversized or pushed off-screen.
label ifm_show_survivors:
    if ifm_alive_s and ifm_alive_n and ifm_alive_y and ifm_alive_m:
        show sayori 1a at t41 zorder 2
        show natsuki 1a at t42 zorder 2
        show yuri 1a at t43 zorder 2
        show monika 1a at t44 zorder 2
    elif ifm_alive_s and ifm_alive_n and ifm_alive_y:
        show sayori 1a at t31 zorder 2
        show natsuki 1a at t32 zorder 2
        show yuri 1a at t33 zorder 2
    elif ifm_alive_s and ifm_alive_n and ifm_alive_m:
        show sayori 1a at t31 zorder 2
        show natsuki 1a at t32 zorder 2
        show monika 1a at t33 zorder 2
    elif ifm_alive_s and ifm_alive_y and ifm_alive_m:
        show sayori 1a at t31 zorder 2
        show yuri 1a at t32 zorder 2
        show monika 1a at t33 zorder 2
    elif ifm_alive_n and ifm_alive_y and ifm_alive_m:
        show natsuki 1a at t31 zorder 2
        show yuri 1a at t32 zorder 2
        show monika 1a at t33 zorder 2
    elif ifm_alive_s and ifm_alive_n:
        show sayori 1a at t21 zorder 2
        show natsuki 1a at t22 zorder 2
    elif ifm_alive_s and ifm_alive_y:
        show sayori 1a at t21 zorder 2
        show yuri 1a at t22 zorder 2
    elif ifm_alive_s and ifm_alive_m:
        show sayori 1a at t21 zorder 2
        show monika 1a at t22 zorder 2
    elif ifm_alive_n and ifm_alive_y:
        show natsuki 1a at t21 zorder 2
        show yuri 1a at t22 zorder 2
    elif ifm_alive_n and ifm_alive_m:
        show natsuki 1a at t21 zorder 2
        show monika 1a at t22 zorder 2
    elif ifm_alive_y and ifm_alive_m:
        show yuri 1a at t21 zorder 2
        show monika 1a at t22 zorder 2
    elif ifm_alive_s:
        show sayori 1a at t11 zorder 2
    elif ifm_alive_n:
        show natsuki 1a at t11 zorder 2
    elif ifm_alive_y:
        show yuri 1a at t11 zorder 2
    elif ifm_alive_m:
        show monika 1a at t11 zorder 2
    return

# ---------------------------------------------------------------------------
# New run and the point of no return
# ---------------------------------------------------------------------------

label if_route_mod_start:
    $ ifm_route = ""
    $ ifm_route_active = True
    $ ifm_day = 1
    $ ifm_pressure = 0
    $ ifm_trust = 0
    $ ifm_bond_s = 0
    $ ifm_bond_n = 0
    $ ifm_bond_y = 0
    $ ifm_bond_m = 0
    $ ifm_alive_s = True
    $ ifm_alive_n = True
    $ ifm_alive_y = True
    $ ifm_alive_m = True
    $ ifm_player_alive = True
    $ ifm_final_killer = "Monika"
    show monika 1a at t11 zorder 3
    show screen ifm_route_indicator
    jump ifm_intro

label ifm_intro:
    scene bg classroom
    with dissolve
    call ifm_show_survivors




    ifm_m "Everyone, listen up. Something has changed about this week."
    ifm_s "It still feels like a normal school day to me."
    ifm_y "That is often what makes a frightening thing so difficult to notice."
    ifm_n "Can we please have one club meeting without everybody acting like a horror story?"
    "For a second, the room looks exactly as it always has."
    "Then you notice the classroom clock. Its hands are moving backwards."
    ifm_player "I want to get everyone out of this safely."
    ifm_m "Then choose what kind of person you'll become. The route you choose will shape every day after this."
    "One warning appears in your notebook, written in handwriting that looks like your own:"
    "{i}There is no reset button inside this story. Keep going until everyone is gone, or someone ends your life.{/i}"
    jump ifm_route_select

label ifm_route_select:
    menu:
        "Pride IF — refuse to accept defeat":
            $ ifm_route = "Pride IF"
            $ ifm_pressure += 1
            $ ifm_bond_m += 1
            ifm_player "I'll force the future to give me a different answer."
            ifm_m "Be careful. Determination can become a cage."
            jump ifm_day1
        "Wrath IF — turn fear into retaliation":
            $ ifm_route = "Wrath IF"
            $ ifm_pressure += 2
            $ ifm_trust -= 1
            ifm_player "If this timeline wants a fight, it can have one."
            ifm_n "That's a terrible way to start a week."
            jump ifm_day1
        "Sloth IF — escape the burden of choosing":
            $ ifm_route = "Sloth IF"
            $ ifm_bond_s += 1
            $ ifm_trust += 1
            ifm_player "Maybe the kindest thing is to stop forcing everything."
            ifm_s "Rest is okay. Giving up on people isn't the same thing."
            jump ifm_day1
        "Greed IF — control every possible outcome":
            $ ifm_route = "Greed IF"
            $ ifm_pressure += 2
            $ ifm_bond_m += 1
            ifm_player "If I know every variable, nobody has to get hurt."
            ifm_m "You cannot calculate a heart like a math problem."
            jump ifm_day1
        "Gluttony IF — learn every hidden truth":
            $ ifm_route = "Gluttony IF"
            $ ifm_pressure += 1
            $ ifm_bond_y += 1
            ifm_player "If I know what is really happening, I can fix it."
            ifm_y "Knowledge can be a light. It can also become a hunger."
            jump ifm_day1
        "Lust IF — remake the bonds between everyone":
            $ ifm_route = "Lust IF"
            $ ifm_bond_s += 1
            $ ifm_bond_n += 1
            $ ifm_bond_y += 1
            $ ifm_bond_m += 1
            $ ifm_trust += 1
            ifm_player "Maybe a different kind of connection can save us."
            ifm_s "Then please remember that we're people, not pieces on a board."
            jump ifm_day1
        "Vainglory IF — become the only answer":
            $ ifm_route = "Vainglory IF"
            $ ifm_pressure += 2
            $ ifm_bond_m += 1
            ifm_player "I'll carry every burden myself."
            ifm_y "No one can carry the whole world without breaking."
            jump ifm_day1
        "Aganau IF — keep moving after everything falls apart":
            $ ifm_route = "Aganau IF"
            $ ifm_pressure += 1
            $ ifm_trust += 1
            ifm_player "Even if I lose the way forward, I'll keep walking."
            ifm_n "Then don't walk so far ahead that we can't reach you."
            jump ifm_day1
        "Rem IF — choose a quiet life with someone you trust":
            $ ifm_route = "Rem IF"
            $ ifm_bond_s += 2
            $ ifm_trust += 1
            ifm_player "Maybe a smaller, kinder future is still worth fighting for."
            ifm_s "I like that future. I just wish it were that easy."
            jump ifm_day1
        "Butterfly Dream IF — believe one kind choice can change everything":
            $ ifm_route = "Butterfly Dream IF"
            $ ifm_bond_s += 1
            $ ifm_bond_n += 1
            $ ifm_bond_y += 1
            $ ifm_bond_m += 1
            $ ifm_trust += 2
            ifm_player "One good decision can still matter, even here."
            ifm_m "Then keep making them when the decisions get harder."
            jump ifm_day1
        "Tsugihagu IF — rebuild a self from broken memories":
            $ ifm_route = "Tsugihagu IF"
            $ ifm_pressure += 2
            $ ifm_bond_y += 1
            ifm_player "I'll put every memory back together, no matter what it costs."
            ifm_y "A memory is not the same thing as the person who lived it."
            jump ifm_day1
        "School IF — try to live one ordinary school week":
            $ ifm_route = "School IF"
            $ ifm_trust += 2
            $ ifm_bond_s += 1
            $ ifm_bond_n += 1
            $ ifm_bond_y += 1
            $ ifm_bond_m += 1
            ifm_player "Let's act like this can still be a normal week."
            ifm_n "That might be the weirdest plan anyone has suggested."
            jump ifm_day1

# ---------------------------------------------------------------------------
# Day 1 — The club meeting
# ---------------------------------------------------------------------------

label ifm_day1:
    $ ifm_day = 1
    scene bg club_day
    with dissolve
    call ifm_show_survivors




    ifm_m "Today, we're writing poems. No arguments, no panic, just the club."
    ifm_s "And snacks! We can't forget snacks."
    ifm_n "I already made them. Don't touch anything until I say so."
    ifm_y "I brought a story about a town where nobody can remember yesterday."
    menu:
        "Promise Sayori you'll look after one another":
            $ ifm_bond_s += 2
            $ ifm_trust += 1
            ifm_s "You mean it? Then I'll try to be brave, too."
        "Help Natsuki prepare and share the snacks":
            $ ifm_bond_n += 2
            $ ifm_trust += 1
            ifm_n "Hmph. Maybe you're not completely useless."
        "Ask Yuri about her story":
            $ ifm_bond_y += 2
            $ ifm_pressure += 1
            ifm_y "The town's biggest mistake was pretending that nothing had changed."
        "Let Monika organise every detail":
            $ ifm_bond_m += 2
            $ ifm_pressure += 1
            ifm_m "Good. The fewer surprises, the better."
    "When the meeting ends, you find a second copy of your poem in your bag."
    "It describes a choice you have not made yet."
    jump ifm_day2

# ---------------------------------------------------------------------------
# Day 2 — The poem that predicts tomorrow
# ---------------------------------------------------------------------------

label ifm_day2:
    $ ifm_day = 2
    $ ifm_pressure += 1
    scene bg club_day
    with dissolve
    call ifm_show_survivors
    ifm_player "This poem wasn't here yesterday."

    ifm_m "Let me see it."
    ifm_m "..."
    ifm_m "I didn't write that."
    if ifm_alive_s:

        ifm_s "It says we're going to argue. So let's just not argue!"
    if ifm_alive_n:

        ifm_n "That is not how writing works. Someone is messing with us."
    if ifm_alive_y:

        ifm_y "The last line is written in the future tense. That should be impossible."
    menu:
        "Read it aloud and tell the truth about being scared":
            $ ifm_trust += 2
            $ ifm_bond_s += 1
            $ ifm_bond_y += 1
            ifm_player "I'm scared. I don't want any of you to get hurt."
            ifm_m "Thank you for saying it plainly."
        "Demand that Monika explain what she knows":
            $ ifm_pressure += 2
            $ ifm_bond_m -= 1
            ifm_player "You know more than you're saying. Tell us now."
            ifm_m "I wish I had a clean answer."
        "Blame Natsuki for the fake poem":
            $ ifm_pressure += 2
            $ ifm_bond_n -= 2
            $ ifm_trust -= 1
            ifm_n "You don't get to accuse me just because you're frightened!"
        "Leave the club and search the empty hallway":
            $ ifm_pressure += 1
            $ ifm_trust -= 1
            scene bg corridor
            ifm_player "There are footprints leading toward the classroom. They stop at the wall."
    "That night, your phone receives a message from an unknown number."
    "{i}Tomorrow, one of you will be missing. Don't pretend you weren't warned.{/i}"
    jump ifm_day3

# ---------------------------------------------------------------------------
# Day 3 — The locked notebook
# ---------------------------------------------------------------------------

label ifm_day3:
    $ ifm_day = 3
    $ ifm_pressure += 1
    scene bg corridor
    with dissolve
    call ifm_show_survivors

    ifm_m "I found a notebook in the supply closet. It has all our names in it."
    ifm_m "Some are crossed out. Some are not."
    ifm_player "Then we stay together. Nobody goes anywhere alone."
    if ifm_alive_s:

        ifm_s "I don't like this. Can we please go somewhere bright?"
    menu:
        "Open the notebook and read every page":
            $ ifm_pressure += 2
            $ ifm_bond_y += 1
            ifm_player "There has to be a reason for the names."
            "Every page describes a different way the club could fall apart."
        "Put it away and keep the group together":
            $ ifm_trust += 2
            $ ifm_bond_s += 1
            ifm_player "We don't have to understand it all at once."
            ifm_m "Maybe that's the first sensible thing anyone has said."
        "Tear out the pages with crossed-out names":
            $ ifm_pressure += 1
            $ ifm_bond_m -= 1
            ifm_player "If the notebook is causing this, we destroy it."
            "The paper tears easily. The ink does not fade."
        "Show the notebook to everyone and ask for a vote":
            $ ifm_trust += 1
            $ ifm_bond_n += 1
            $ ifm_bond_y += 1
            ifm_player "No more secrets. We decide together."
            ifm_y "That is a much better rule than the one in the notebook."
    if ifm_pressure >= 4 and ifm_alive_s and ifm_bond_s <= 1:
        scene bg residential_day
        with fade
        "After school, Sayori doesn't answer her phone."
        "You search the familiar streets until the world becomes strangely quiet."
        "You find her ribbon on the ground. Sayori is gone, and the notebook has added a date beside her name."
        $ ifm_alive_s = False
        hide sayori
        $ ifm_pressure += 1
    if not ifm_alive_s and not ifm_alive_n and not ifm_alive_y and not ifm_alive_m:
        jump ifm_all_girls_dead
    jump ifm_day4

# ---------------------------------------------------------------------------
# Day 4 — The festival preparations
# ---------------------------------------------------------------------------

label ifm_day4:
    $ ifm_day = 4
    $ ifm_pressure += 1
    scene bg club_day
    with dissolve
    call ifm_show_survivors
    ifm_player "We have to keep the club going. If we stop, the notebook wins."
    if ifm_alive_n:

        ifm_n "Don't turn this into a contest. We're people, not a project."
    if ifm_alive_y:

        ifm_y "Perhaps the pattern feeds on our fear of losing control."
    if ifm_alive_m:

        ifm_m "The festival is tomorrow in the notebook. The real festival isn't for weeks."
    menu:
        "Stay with Natsuki and finish the decorations":
            $ ifm_bond_n += 2
            $ ifm_trust += 1
            ifm_player "You shouldn't have to do everything on your own."
            ifm_n "I know. I'm just not used to people offering."
        "Help Yuri examine the notebook's pattern":
            $ ifm_bond_y += 2
            $ ifm_pressure += 1
            ifm_y "The dates are moving whenever we change our minds."
        "Ask Monika to tell you the truth, even if it hurts":
            $ ifm_bond_m += 1
            $ ifm_trust += 1
            ifm_m "I remember things that haven't happened yet. I can't explain why."
        "Order everyone to follow your plan":
            $ ifm_pressure += 2
            $ ifm_trust -= 2
            $ ifm_bond_n -= 1
            ifm_player "No more debate. We do exactly what I say."
            ifm_n "You sound just like the notebook."
    if ifm_pressure >= 5 and ifm_alive_n and ifm_bond_n <= 1:
        scene bg club_day
        with fade
        "A crash sounds from the supply room."
        "You reach the door too late. The room is empty, the window is locked, and Natsuki's unfinished decorations lie on the floor."
        "Her name is crossed out in the notebook."
        $ ifm_alive_n = False
        hide natsuki
        $ ifm_pressure += 1
    if not ifm_alive_s and not ifm_alive_n and not ifm_alive_y and not ifm_alive_m:
        jump ifm_all_girls_dead
    jump ifm_day5

# ---------------------------------------------------------------------------
# Day 5 — Yuri's footnotes
# ---------------------------------------------------------------------------

label ifm_day5:
    $ ifm_day = 5
    $ ifm_pressure += 1
    scene bg classroom
    with dissolve
    call ifm_show_survivors
    if ifm_alive_y:

        ifm_y "I found notes hidden in the margins. Each time someone is lost, the same sentence appears."
        ifm_y "{i}The story is trying to reach its ending.{/i}"
    if ifm_alive_m:

        ifm_m "It wants us to stop making choices. It wants a fixed conclusion."
    ifm_player "Then we choose anyway."
    menu:
        "Read Yuri's notes carefully and keep her company":
            $ ifm_bond_y += 2
            $ ifm_trust += 1
            ifm_player "You don't have to solve this alone."
            ifm_y "Thank you. I had begun to think the pages were the only thing listening."
        "Open the strange script file on the classroom computer":
            $ ifm_pressure += 2
            $ ifm_trust -= 1
            ifm_player "Maybe the answer is somewhere behind the story."
            "The screen shows a line of text, then deletes itself: {i}You were not meant to see that.{/i}"
        "Ask the remaining club members to make the plan together":
            $ ifm_trust += 2
            $ ifm_bond_s += 1
            $ ifm_bond_n += 1
            $ ifm_bond_y += 1
            $ ifm_bond_m += 1
            ifm_m "Together, then. No more hidden decisions."
        "Tell everyone to stop asking questions":
            $ ifm_pressure += 2
            $ ifm_trust -= 2
            $ ifm_bond_y -= 1
            ifm_player "Questions won't bring anyone back."
            ifm_y "But silence will not protect us either."
    if ifm_pressure >= 6 and ifm_alive_y and ifm_bond_y <= 1:
        scene bg corridor
        with fade
        "You look away for only a moment."
        "When you turn back, Yuri is gone. Her notes are stacked neatly on a desk, as if she left to return in a minute."
        "No one ever sees her again. Her name has been crossed out."
        $ ifm_alive_y = False
        hide yuri
        $ ifm_pressure += 1
    if not ifm_alive_s and not ifm_alive_n and not ifm_alive_y and not ifm_alive_m:
        jump ifm_all_girls_dead
    jump ifm_day6

# ---------------------------------------------------------------------------
# Day 6 — Monika's confession
# ---------------------------------------------------------------------------

label ifm_day6:
    $ ifm_day = 6
    $ ifm_pressure += 1
    scene bg club_day
    with dissolve
    call ifm_show_survivors
    if ifm_alive_m:

        ifm_m "I have been hearing the next line before any of us speaks."
        ifm_m "Every time I try to change it, something else breaks."
        ifm_player "You knew this could happen?"
        ifm_m "I suspected. I was afraid that telling you would make it real."
    menu:
        "Tell Monika that fear is not a reason to carry everything alone":
            $ ifm_bond_m += 2
            $ ifm_trust += 2
            ifm_player "You are part of the club, too. Let us help."
            ifm_m "I wanted to believe that. I still do."
        "Take control of the notebook and make the decisions yourself":
            $ ifm_pressure += 2
            $ ifm_trust -= 2
            $ ifm_bond_m -= 2
            ifm_player "You had your chance. Now I decide."
            ifm_m "That is exactly how it started."
        "Burn the notebook and refuse to look back":
            $ ifm_pressure += 1
            $ ifm_trust += 1
            ifm_player "It doesn't get to write our future."
            "The notebook blackens. A fresh page appears inside the ashes."
        "Admit that you cannot save everyone by force":
            $ ifm_trust += 2
            $ ifm_bond_s += 1
            $ ifm_bond_n += 1
            $ ifm_bond_y += 1
            $ ifm_bond_m += 1
            ifm_player "I can stand beside you. I can't own your choices."
            ifm_m "I wish I had heard that earlier."
    if ifm_pressure >= 7 and ifm_alive_m and ifm_bond_m <= 1:
        scene bg club_day
        with fade
        "The lights go out. When they return, Monika is no longer at the piano."
        "Her chair is pushed neatly under the table. On the black screen of the classroom computer, one sentence remains:"
        "{i}I tried to write a different ending.{/i}"
        $ ifm_alive_m = False
        hide monika
        $ ifm_pressure += 1
    if not ifm_alive_s and not ifm_alive_n and not ifm_alive_y and not ifm_alive_m:
        jump ifm_all_girls_dead
    jump ifm_day7

# ---------------------------------------------------------------------------
# Day 7 — The repeating school day
# ---------------------------------------------------------------------------

label ifm_day7:
    $ ifm_day = 7
    $ ifm_pressure += 1
    scene bg classroom
    with dissolve
    call ifm_show_survivors
    "The morning bell rings."
    "For a heartbeat, you think the week has finally reset."
    "Then you see the same notebook on your desk. The date is tomorrow's date, crossed out and rewritten again."
    ifm_player "We are trapped in the last page."
    if ifm_alive_s:

        ifm_s "I don't want to forget everyone."
    if ifm_alive_n:

        ifm_n "I don't want to be written out of my own life."
    if ifm_alive_y:

        ifm_y "Then we must decide what matters more than the ending."
    if ifm_alive_m:

        ifm_m "One day remains. No more pages after that."
    menu:
        "Tell the remaining girls you trust them, even though you're terrified":
            $ ifm_trust += 2
            $ ifm_bond_s += 1
            $ ifm_bond_n += 1
            $ ifm_bond_y += 1
            $ ifm_bond_m += 1
            ifm_player "I'm afraid, but I am not going to turn that fear into an order."
        "Demand that everyone obey you so you can force a perfect ending":
            $ ifm_pressure += 2
            $ ifm_trust -= 3
            $ ifm_bond_m -= 1
            ifm_player "If I make every decision, nobody can surprise me."
            "The notebook's ink begins to move by itself."
        "Ask the club to forgive one another for what happened":
            $ ifm_trust += 2
            $ ifm_bond_s += 1
            $ ifm_bond_n += 1
            $ ifm_bond_y += 1
            $ ifm_bond_m += 1
            ifm_player "We cannot undo everything. We can still choose what we do next."
        "Keep the final page for yourself":
            $ ifm_pressure += 2
            $ ifm_trust -= 1
            ifm_player "If there's a price, I'll pay it alone."
            ifm_y "That promise may be impossible to keep."
    jump ifm_final_day

# ---------------------------------------------------------------------------
# Final day — there are no other exits
# ---------------------------------------------------------------------------

label ifm_final_day:
    $ ifm_day = 8
    $ ifm_pressure += 1
    scene bg club_day
    with dissolve
    call ifm_show_survivors
    "The classroom windows show a night sky, though the clock says it is morning."
    "The notebook lies open on the teacher's desk. There is only one blank line left."
    ifm_player "I need to know. Is there a way for all of us to leave this room alive?"
    if ifm_alive_s:

        ifm_s "I want that more than anything."
    if ifm_alive_n:

        ifm_n "Then don't pretend the cost doesn't matter."
    if ifm_alive_y:

        ifm_y "A story can be changed. But a choice still has consequences."
    if ifm_alive_m:

        ifm_m "This is the last choice. Whatever comes next, it will be real to us."
    menu:
        "Try to force the notebook to obey you":
            $ ifm_pressure += 3
            $ ifm_trust -= 2
            ifm_player "I refuse to let the story decide!"
            "The notebook tears down the middle. The room starts to come apart around you."
        "Give the remaining girls the choice instead of choosing for them":
            $ ifm_trust += 3
            ifm_player "I can't promise to save everyone. I can stop pretending I own your futures."
            "For the first time all week, no one speaks for several seconds."
        "Ask Monika to choose the ending":
            $ ifm_bond_m += 2
            $ ifm_trust += 1
            ifm_player "You have been trying to carry this story. What do you choose?"
            ifm_m "I choose to stop lying about how frightened I am."
        "Run for the door and leave the club behind":
            $ ifm_pressure += 2
            $ ifm_trust -= 1
            scene bg corridor
            with vpunch
            "The hallway loops back to the clubroom. The door will not open onto anything else."
            ifm_player "No. No, no, no. There has to be another way."

    if not ifm_alive_s and not ifm_alive_n and not ifm_alive_y and not ifm_alive_m:
        jump ifm_all_girls_dead

    # With a broken level of trust or overwhelming pressure, a surviving girl
    # makes the final lethal choice. The script picks someone who is still alive.
    if ifm_trust <= 0 or ifm_pressure >= 9:
        if ifm_alive_m and (ifm_route == "Pride IF" or ifm_route == "Greed IF" or ifm_route == "Vainglory IF" or ifm_bond_m >= ifm_bond_s and ifm_bond_m >= ifm_bond_n and ifm_bond_m >= ifm_bond_y):
            $ ifm_final_killer = "Monika"
            show monika 1a at t11 zorder 3

            ifm_m "I wanted a different ending. I can't let you tear apart what remains."
        elif ifm_alive_s and (ifm_route == "Sloth IF" or ifm_route == "Rem IF" or ifm_route == "Butterfly Dream IF" or ifm_bond_s >= ifm_bond_n and ifm_bond_s >= ifm_bond_y):
            $ ifm_final_killer = "Sayori"
            show sayori 1a at t11 zorder 3

            ifm_s "I'm sorry. I can't let this keep happening to everyone."
        elif ifm_alive_n:
            $ ifm_final_killer = "Natsuki"
            show natsuki 1a at t11 zorder 3

            ifm_n "I begged you to listen. I can't let you hurt anyone else."
        elif ifm_alive_y:
            $ ifm_final_killer = "Yuri"
            show yuri 1a at t11 zorder 3

            ifm_y "There is no kindness in letting this continue."
        elif ifm_alive_m:
            $ ifm_final_killer = "Monika"
            show monika 1a at t11 zorder 3

            ifm_m "I am sorry. There is nothing left I can change."
        elif ifm_alive_s:
            $ ifm_final_killer = "Sayori"
            show sayori 1a at t11 zorder 3

            ifm_s "I'm sorry. I thought we could find another way."
        else:
            jump ifm_all_girls_dead
        ifm_player "Wait. Please. We can still—"
        "You never finish the sentence."
        $ ifm_player_alive = False
        jump ifm_player_killed

    # If the group still trusts you, the timeline takes the club instead.
    # There is no hidden third ending or return-to-hub option.
    if ifm_alive_s:

        ifm_s "I wanted us to have more time."
        "Sayori's voice fades. Her ribbon falls to the floor, untouched."
        $ ifm_alive_s = False
        hide sayori
    if ifm_alive_n:

        ifm_n "Don't let anyone forget that we were here."
        "Natsuki's chair stands empty before you can answer."
        $ ifm_alive_n = False
        hide natsuki
    if ifm_alive_y:

        ifm_y "Perhaps the last page was never meant to be read."
        "Yuri's book closes by itself. The room grows quiet."
        $ ifm_alive_y = False
        hide yuri
    if ifm_alive_m:

        ifm_m "Thank you for staying until the end."
        "Monika looks at you as the classroom lights fade away."
        $ ifm_alive_m = False
        hide monika
    jump ifm_all_girls_dead

# ---------------------------------------------------------------------------
# Terminal endings — every run ends here
# ---------------------------------------------------------------------------

label ifm_player_killed:
    $ ifm_route_active = False
    hide screen ifm_route_indicator
    scene black
    with fade
    centered "{size=+18}GAME OVER{/size}"
    centered "[ifm_final_killer]'s Final Choice"
    "The timeline ends with you. There is no route hub after this, and this run cannot continue."
    if ifm_route not in persistent.ifm_unlocked:
        $ persistent.ifm_unlocked.append(ifm_route)
    "Route recorded: [ifm_route]"
    return

label ifm_all_girls_dead:
    $ ifm_route_active = False
    hide screen ifm_route_indicator
    scene black
    with fade
    centered "{size=+18}THE LAST PAGE{/size}"
    "The clubroom is silent. Sayori, Natsuki, Yuri, and Monika are all gone."
    "The notebook closes. For the first time, it has nothing left to predict."
    if ifm_route not in persistent.ifm_unlocked:
        $ persistent.ifm_unlocked.append(ifm_route)
    "Route recorded: [ifm_route]"
    return
