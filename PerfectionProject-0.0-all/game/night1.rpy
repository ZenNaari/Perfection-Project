label night1:
    
    show expression Text(_("8PM"), size=50, yalign=0.5, xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve
    
    $renpy.pause(2, hard=true)
    
    hide text
    with dissolve
    
    scene bg room
    with fade
    
    play sound "ring.wav"
    
    $renpy.pause(2, hard=true)
    
    play sound "beep.wav"
    
    z "Yo."
    
    c "Hey man."
    
    c "Going drinkin' tonight?"
    
    z "Just a little, yeah."
    
    z "I had a weird day."
    
    z "I need to unwind."
    
    z "You joining me?"
    
    c "Yeah sure."
    
    z "Something happen at the club?"
    
    c "Not really. I just want to spend time with ya."
    
    z "We see each other almost everyday."
    
    c "Whatever man. Let's find you a girl tonight."
    
    z "Shut up. I don't need that."
    
    c "Anyway, see you there."
    
    z "Yeah, kay."
    
    play sound "beep.wav"
    
    "Ugh. I had a tiring day."
    
    "Anyway, I need to drink."
    
    "That vodka ain't gonna drink itself."
    
    scene bg black
    with fade
    
    $renpy.pause(2, hard=true)
    
    
    
    return
    