label kat3:

    scene bg black
    with dissolve
    
    show expression Text(_("Kat's Chapter - Chapter 3"), size=50, yalign=0.5, xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve
    
    $renpy.pause(2, hard=True)
    
    hide text
    with dissolve
    
    play music "LongStroll.mp3" fadeout 1
    
    scene bg room
    with dissolve
    
    show kat away smile n color:
        hop2()
    with dissolve
    
    "It's been two months since Kat started living here."
    
    "And a month since we've been dating."
    
    "Honestly, everything is going well."
    
    "We've gotten into one major fight."
    
    "But that subsided pretty quickly."
    
    "Pretty quickly that I don't even want to call it a fight."
    
    "I guess that's one of the perks of dating a cool girl."
    
    "Even if you get in a fight about a major issue, things cool down pretty fast."
    
    "And there she is, just sitting down with her laptop."
    
    z "I'm going to the store, do we need anything?"
    
    show kat me
    with dissolve
    
    k "Hah!"
    
    z "What?"
    
    k "You said we."
    
    k "As if we're actually a couple."
    
    z "Are we actually a couple?"
    
    show kat away
    with dissolve
    
    k "You tell me."
    
    z "Well, if we are a couple, we're definitely not like any other couple."
    
    show kat me normal
    
    k "I'll disagree with that."
    
    z "Why so?"
    
    k "Well, for starters..."
    
    show kat me smile
    
    k "... we live together."
    
    "sigh"
    
    k "Couples eventually move in together right?"
    
    z "Couples normally move in together AFTER they're a couple."
    
    show kat away
    
    k "Makes no difference to me."
    
    "This girl."
    
    z "You'd make a great wife."
    
    k "No,{w} YOU{w} would make a great wife."
    
    z "I repeat, do we need anything from the store."
    
    show kat me normal
    
    k "You probably know what we need here."
    
    show kat me smile
    
    k "I won't say no to ice cream though."
    
    z "The ones with a cone?"
    
    k "You know what I like."
    
    z "Of course."
    
    z "I'm out then."
    
    k "See ya~"
    
    play sound "door.wav"
    
    scene bg black
    with dissolve
    
    $renpy.pause(2, hard=True)
    
    scene bg outside
    with dissolve
    
    "Let's see, I got noodles, bread, eggs..."
    
    "...and ice cream."
    
    "Looks like I got what I need."
    
    "Honestly, this girl."
    
    show ling away smile n:
        xalign -1.0 yalign 1.0
        linear 2 xalign 1.5
    
    "She used to always follow me around."
    
    "Now that we're dating it's like she doesn't feel the need to tag along with me."
    
    show ling away smile n flip:
        linear 2 xalign -0.5
    
    "Even if I'm just doing a little shopping."
    
    "Now I feel a little bit lonely."
    
    show ling away smile n:
        linear 1 xalign 0.5
    
    "But it's totally her fault."
    
    show ling me smile:
        hop()
    
    "She got me used to her following me around."
    
    "And now she just stops just like that."
    
    hide text
    
    show ling me mad
    
    "Hmph. How grateful."
    
    l "I said hey!"
    
    play sound "punch2.wav"
    
    show ling
    with hpunch
    
    z "Ow!"
    
    z "Hey, what are you-..."
    
    z "Oh."
    
    show ling me smile
    
    l "Remember me?"
    
    z "Ling!"
    
    z "How could I forget?!"
    
    z "I would never!..."
    
    l "Okay okay shut up. I get it."
    
    l "Still couldn't get over me after all this time huh?"
    
    z "Of course! I could never."
    
    z "How've you been doing?!"
    
    l "I'm alright I guess."
    
    l "And you?"
    
    z "Me?!"
    
    z "Great!"
    
    z "I'm doing great!"
    
    z "Even better now that you're here."
    
    show ling:
        hop()
        hop()
    
    l "Hahaha."
    
    l "Sweet as always aren't you?"
    
    z "Well, heh, you know me."
    
    l "I do."
    
    z "So what are you up to?"
    
    z "What brings you here?"
    
    stop music fadeout 1
    
    show ling away
    
    l "Hmm."
    
    show ling me
    with dissolve
    
    l "Okay, i'm going to be straightforward."
    
    z "Cuz you don't really know how to say it any other way."
    
    l "Exactly."
    
    show ling away normal:
        hop()
    
    l "Okay."
    
    "She sighs"
    
    show ling me smile
    with dissolve
    
    l "I came here looking for you."
    
    z "Me?"
    
    l "Yes, you."
    
    z "Why? Is there something you need me for?"
    
    l "I want you back."
    
    play music "RollinAt5.mp3"
    
    l "That's the best way to say it."
    
    "Pause."
    
    "This..."
    
    "This isn't happening."
    
    "Please tell me this isn't happening."
    
    show ling me normal
    with dissolve
    
    l "Zen? You okay?"
    
    z "Uh... Yeah! Yeah."
    
    l "Well?"
    
    z "I-it's just so sudden."
    
    l "Really?"
    
    l "That's something I thought you'd never say."
    
    z "Well, we grew up I guess."
    
    show ling me smile
    with dissolve
    
    l "Anyway, I'm moving into town."
    
    l "So I'll be seeing you around I guess."
    
    show kat me smile n color:
        xalign 1.5 yalign 1.0
        linear 1 xalign 1.0
    with dissolve
    
    show ling away normal
    with dissolve
    
    k "Hey Zen. What's taking you so..."
    
    show kat away normal
    with dissolve
    
    k "...long."
    
    "The tension suddenly rises."
    
    "You could tell that if I was dating any other girl, this air would be different."
    
    "But the fact that I happen to be dating Kat..."
    
    show kat mad
    with dissolve
    
    k "Who are you?"
    
    show ling mad
    with dissolve
    
    l "Who are 'you'?"
    
    k "I'm Zen's..."
    
    show kat me normal
    with dissolve
    
    k "Uhh..."
    
    l "Well, Zen is my..."
    
    show ling me normal
    with dissolve
    
    l "Um..."
    
    show ling mad
    
    show kat mad
    with dissolve
    
    l "God fucking damnit Zen."
    
    k "Why do you have to be so fucking complicated?"
    
    z "Uhh. I..."
    
    show kat away
    with dissolve
    
    k "I'm not dealing with this right now."
    
    show ling away
    with dissolve
    
    l "Neither am I."
    
    show kat me
    with dissolve
    
    k "Well, I'm going back..."
    
    show kat away
    with dissolve
    
    k "... to OUR apartment..."
    
    show kat me
    with dissolve
    
    k "... that WE share."
    
    jump choice