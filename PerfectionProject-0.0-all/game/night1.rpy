label night1:
    
    show expression Text(_("8PM"), size=50, yalign=0.5, xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve
    
    $renpy.pause(2, hard=True)
    
    hide text
    with dissolve
    
    scene bg room
    with fade
    
    play sound "ring.wav"
    
    $renpy.pause(2, hard=True)
    
    play sound "beep.wav"
    
    z "Yo."
    
    c "Hey man."
    
    c "Are we going drinkin' tonight?"
    
    z "Yeah."
    
    z "I had a weird day."
    
    z "I need to unwind."
    
    c "Cool, cool."
    
    c "Let's find you a girl tonight."
    
    z "Shut up."
    
    c "Anyway, see you there."
    
    z "Yeah, kay."
    
    play sound "beep.wav"
    
    "Ugh. I had a tiring day."
    
    "Anyway, I need to drink."
    
    "It ain't gonna drink itself."
    
    play sound "door.wav"
    
    scene bg black
    with fade
    
    $renpy.pause(2, hard=True)
    
    scene bg counter
    with fade
    
    play music "AcidJazz.mp3"
    
    "I usually come here early."
    
    "Mainly because it's dark and quiet."
    
    "Sometimes there's a nice show on the tv."
    
    "This is a sports bar after all."
    
    "I'm not into sports or anything, but the local MMA fights are broadcasted here."
    
    "There's a stage for music nights."
    
    "It's a pretty chill place."
    
    "But it's usually quiet here."

    "Why you ask?"
    
    "Because this is Beachside!"
    
    "There are plenty of bars and clubs to choose from."
    
    "The last place anyone wants to go for a more fun time is the bar in school."
    
    "But of course, the occasional university teams hang around here."
    
    "There's a stage, so comedians and musicians perform here during their nights."
    
    "So there is an element that makes this place fun on it's own."
    
    "Not to mention, it's close to the dorms."
    
    "You can say that this is a pretty chill place to hang out."
    
    "But not really to have fun."
    
    bar "Hey Zen."
    
    z "Oh hey."
    
    bar "She's here again."
    
    z "So I see."
    
    play sound "beer.wav"
    
    bar "Here's your beer."
    
    z "I'll need this, thanks."
    
    "Okay, so a little bit of context."
    
    "I believe everyone has that one person who's kinda sorta obsessed with them."
    
    "You were nice to them one time, and the next thing you know, they're always there."
    
    "To me... that person is."
    
    show mary me excited n:
        xalign -0.5 yalign 1.0
        linear 1 xalign 0.0
    with dissolve
    
    "Mary..."
    
    m "Hey Zen!"
    
    z "Heyy..."
    
    show mary me smile
    
    m "What's up? How are you? I haven't seen you since Friday."
    
    "We don't need to see each other everyday."
    
    show mary:
        linear 1 xalign 0.25
        hop2()
    
    "She makes herself comfortable beside me."
    
    play sound "drink.wav"
    
    "I'm gonna have to finish half the bottle for this conversation."
    
    z "I'm alright I guess. Same as always."
    
    m "Meet anybody new?"
    
    "..."
    
    z "Yeah, yeah I did. Met a few people the past few days."
    
    m "That's cool.{w} That's cool."
    
    "I can see her trying hard not to look like she's prying in too much."
    
    "Which just make things even weirder."
    
    z "What about you?"
    
    show mary me normal
    
    m "Huh?"
    
    z "What have you been doing?"
    
    show mary away normal
    
    m "Uhh..."
    
    show mary me normal
    
    m "You know, homework. Projects."
    
    show mary me smile
    
    m "Also been hanging around here."
    
    "Despite her looks, she's actually an average student."
    
    "And this will make me sound like a douche."
    
    "But the reason why she hangs out here is because I come here."
    
    "She's not good with talking to people."
    
    "I mean, I'm not Mr. Charismatic or anything."
    
    "But I helped her out once in during some class."
    
    "And ever since then, she's been sitting beside me here, making small talk."
    
    m "Hey, you know."
    
    z "Mhm?"
    
    m "I've been seeing this girl with weird colors on her hair."
    
    show mary me excited
    
    m "Have you seen her?"
    
    m "She looks pretty weird."
    
    z "Yeah. I've seen her."
    
    z "She's kind of a weirdo."
    
    if kat_love > 0:
        z "But she's pretty fun."
    
    else:
        z "But she's a nice person."
    
    show mary me normal
    
    m "Oh."
    
    m "So you know her?"
    
    z "One of the people I've newly met. Yeah."
    
    show mary away normal
    
    m "So uhh."
    
    show mary me normal
    
    m "What do you think of her hair?"
    
    z "It's pretty cool."
    
    z "I like it."
    
    show mary away mad
    
    m "I see."
        
    "I try to pretend not to notice."
    
    "Cuz you see."
    
    "Mary used to have normal black hair."
    
    "And I had a conversation with her about girls who dye their hair."
    
    "And the very next day, she bleached it."
    
    "Hence her current hair color."
    
    "I mean, it's kinda okay. I guess."
    
    "But I don't really want to compliment her in particular because of it."
    
    show mary me
    
    "Looks like she can't get rid of her upset face."
    
    play sound "drink.wav"
    
    "Gonna use this opportunity to drink."
    
    show mary me normal
    
    m "How's your drink?"
    
    z "Beer tastes awful as always."
    
    play sound "drink.wav"
    
    m "Yet you always chug one down like it's nothing."
    
    z "Well, nobody likes the taste of beer."
    
    z "We like the effects of alcohol."
    
    z "Speaking of which, you should order something every now and then."
    
    show mary me mad
    
    m "I order stuff."
    
    z "You should order a drink for once."
    
    z "I mean, you are at a bar."
    
    show mary me normal
    
    m "Uhh."
    
    "One of the reasons why I can't stand Mary is because she decided that the part of her day she chose to see me everyday is at the bar at this time."
    
    "And she doesn't even order a drink."
    
    "At best she'll order some fries or something."
    
    "It's just disrespectful to the bar."
    
    "Woah."
    
    "Did I really just have one beer?"
    
    "Chris and Kat are going to make fun of me later."
    
    m "Uhh."
    
    "Mary checks her watch."
    
    m "I guess it's about time I get back to the dorms."
    
    z "Sure."
    
    show mary me smile
    
    m "I'll see ya tomorrow if you're here."
    
    "You wish."
    
    show mary away smile:
        hop()
        linear 2 xalign 0.75
    
    "And she makes her way out."
    
    "When suddenly."
    
    play sound "door.wav"
    
    show kat away normal n color:
        xalign 2.0 yalign 1.0
        linear 2 xalign 1.25
    with dissolve
    
    show mary away mad
    with dissolve
    
    "Kat appears from the door."
    
    show mary me mad
    
    "Mary takes one good look at her."
    
    show mary away mad
    
    m "Excuse me."
    
    show mary:
        linear 2 xalign 2.5
    
    play sound "door.wav"
    
    "And makes her way out."
    
    show kat me normal:
        linear 1 xalign 1.0
        hop2()
    
    k "Yeesh."
    
    k "What's that bitch's problem?"
    
    z "Nothing. Probably had a stressful day."
    
    k "You know her?"
    
    z "Kinda sorta."
    
    play sound "door.wav"
    
    show chris smile:
        xalign -0.5 yalign 1.0
        linear 2 xalign 0.0
        hop2()
    with dissolve
    
    c "Hey."
    
    c "I just saw Mary come outside."
    
    c "Something happen?"
    
    z "Yeah, she cray cray."
    
    c "Crazy for you yeah?"
    
    z "I guess"
    
    if kat_love>0:
        "Kinda weird talking about this with Kat."
    
    k "So who's she?"
    
    c "Some girl Zen met once."
    
    c "She's crazy for him."
    
    c "Kinda like you."
    
    show kat away mad
    with dissolve
    
    k "Shut up."
    
    c "Well, she's probably more crazy for him."
    
    show kat away angry
    
    k "I said shut up already."
    
    show kat me mad
    
    k "Zen's just an interesting guy."
    
    if kat_love>0:
        "Ouch."
    
    z "Well I am pretty interesting, some might say."
    
    show kat away mad
    
    k "I haven't met an interesting guy for a long time."
    
    k "A{w} long{w} time."
    
    z "Okay then,{w} we'll have beers over here."
    
    bar "Yes sir."
    
    play sound "drink.wav"
    
    "As soon as the beer arrives, Kat just gulps one down easy."

    show chris normal
    
    c "Woaah."
    
    z "Yeah, woaah."
    
    show kat me mad
    
    k "What?"
    
    c "Only girl we know who drinks like that is Gale."
    
    show kat away normal
    
    k "I don't know why you're surprised."
    
    k "I mean, I did drink a lot the other night."
    
    k "More than you even."
    
    show chris smile
    
    c "Yeah{w} right."
    
    show kat away mad
    
    k "I did."
    
    c "But I think we can all agree that Zen barfed first."
    
    show kat me smile
    
    k "Yeah he did."
    
    "I did?"
    
    z "Hey, I never drink that heavily."
    
    z "I think that night was the first time I've ever drank that much."
    
    z "Gimme a break."
    
    c "He was like."
    
    c "\"Bro. Bro. I can't drink anymore.\""
    
    c "I was just there like, \"What?!\""
    
    z "I remember that."
    
    c "You wuss."
    
    c "You should be able to drink more than that."
    
    play sound "drink.wav"
    
    scene bg booth
    with fade
    
    show chris smile:
        left
        hop2()
    with dissolve
    
    show kat me smile n color:
        right
        hop2()
    with dissolve
    
    z "And then Chris was like..."
    
    show chris normal
    
    z "\"We'll just go to the new basement from the old basement.\""
    
    c "Dude..."
    
    play sound "drink.wav"
    
    show bg booth
    with fade
    
    z "And then, our friend released this wild chicken at us."
    
    show chris smile
    
    c "And Zen ran like one."
    
    z "Broo."
    
    play sound "drink.wav"
    
    show kat me normal
    with fade
    
    c "So Kat, how many guys have you dated?"
    
    show kat away mad
    with dissolve
    
    k "A few..."
    
    c "A few?"
    
    k "Yes. A few. Now shut up."
    
    play sound "drink.wav"
    
    show kat me smile
    with fade
    
    z "I don't really want to be richie rich or anything."
    
    z "But I want to have enough money to do what I want."
    
    c "This guy."
    
    c "C'mon, one more!"
    
    z "No! No! I've had enough!"
    
    show kat normal away
    
    k "C'mon Chris, we have a...{w} we have a day tomorrow."
    
    show chris normal
    
    c "But nothing interesting happened yet!"
    
    z "Shut up! Let's go home."
    
    z "I need some candy."
    
    show kat me smile:
        hop2()
    
    k "Here's some gum."
    
    z "Perfect! Thank you."
    
    c "Why do you need gum?"
    
    z "It takes away the taste of alcohol."
    
    show chris smile
    
    c "Pussy."
    
    z "Shut up."
    
    stop music fadeout 1
    
    show white
    with dissolve
    
    z "Uhh... woah..."
    
    show kat me normal
    
    k "Are you okay?"
    
    show chris normal
    
    c "Bro? Dude. Are you kidding me?"
    
    show bg black
    with fade
    
    "Shit."
    
    "I've never blacked out over a few beers before."
    
    "And now I'm in this weird state of mind."
    
    "Something weird is going on."
    
    "Is it because I drank too much the other night?"
    
    play sound "door.wav"
    
    "Did someone drug me?"
    
    "Hmm..."
    
    "I don't see any reason for Chris to drug me."
    
    "Kat?"
    
    "..."
    
    play sound "brake.wav"
    
    "This is getting scary."
    
    "Is Kat some crazy bitch who's after my organs or something?"
    
    "That sucks."
    
    play sound "punch.wav"
    
    "Ow."
    
    "Someone hit me."
    
    
    
    return
    