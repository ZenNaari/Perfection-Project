label eve1:

    "Nothing says fun and productive than making music."
    
    "I actually have basic know-how of the common band instruments."
    
    "So I can be placed anywhere a band might need me."
    
    "Drums, Bass, Guitar."
    
    "I am more experienced with a piano keyboard."
    
    "I also know how to use electronic sounds and pedals."
    
    "I can also sing."
    
    "Or more like, I'm not afraid to sing."
    
    "Back in highschool my classmates begged me to be the lead singer."
    
    "Not because I'm a good singer,{w} but because I'm not ashamed to be on center stage."
    
    "I've been singing a lot on my own since then."
    
    "And I've also written a few songs."
    
    "Made my own riffs and pieces."
    
    "Nothing impressive, just simple things."
    
    "But I guess I could use this opportunity to become better at it."
    
    scene bg black
    with fade
    
    call classday
    
    show expression Text(_("4PM"), size=50, yalign=0.5, xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve
    
    $renpy.pause(2, hard=True)
    
    hide text
    with dissolve
    
    scene bg lakecamp
    with fade
    
    play music "AirportLounge.mp3"
    
    "Out of class, and now looking for the music room."
    
    "I've actually never been to the music room."
    
    "In fact, it was only recently that I knew there was a music room."
    
    "Well, Lakeside has an orchestral room."
    
    "But it was only a few days ago when I heard there was a light music room."
    
    "I'd be more comfortable playing in a band."
    
    "Plus that sounds more fun that sitting around playing some classical music with some fancy instrument."
    
    "Not saying classical music isn't fun though."
    
    scene bg hall3
    with fade
    
    "I overheard some rumors around school."
    
    "Something about a blue fairy..."
    
    "... and how she only smiles when music is playing."
    
    "I guess every school needs its seven wonders or whatever."
    
    "I've seen a few posters hung over school about band members wanted."
    
    "Also has directions to where the music room is."
    
    "And that's where I'm heading."
    
    "Whoop"
    
    play sound "punch.wav"
    
    scene bg hall3
    with hpunch
    
    "Ow."
    
    guy "Watch it!"
    
    z "Sorry."
    
    "A guy bumped into me from where I was headed."
    
    stop music fadeout 1
    
    "Did he just come from the music room?"
    
    "I guess he was, cuz here it is."
    
    play sound "door.wav"
    
    scene bg mroom
    with fade
    
    show eve away smile
    with dissolve
    
    play music "Retro.mp3"
    
    "As I open the door, the first thing I see is a woman in front of me."
    
    "Happily playing on the bass."
    
    "Rocking out like nobody's looking."
    
    "Actually I don't even think she knows I just came in."
    
    "She's probably listening to music while playing."
    
    "I guess I'll just listen for a little bit."
    
    "It's a cool song."
    
    "Even though I can only hear the bass."
    
    "I wonder how long it'll take until she notices I'm here."
    
    "I guess it's a good time for me to interrupt."
    
    z "Hello?"
    
    "Of course she doesn't hear me."
    
    z "Hi!"
    
    "This time I wave my hand in front of her."
    
    show eve:
        linear 1 right
        linear 2 left
        linear 1 center
    
    "As I did, she began to spin around."
    
    "Conveniently avoiding my gestures."
    
    "Leaving me in a rather awkward stance."
    
    "Without thinking I pat her on the head."
    
    stop music fadeout 1
    
    show eve:
        hop()
    
    $renpy.pause(0.5, hard=True)
    
    show eve me normal
    with dissolve
    
    z "Hi?"
    
    "She looks at me for a second."
    
    scene bg black
    with fade
    
    call night
    
    jump choice