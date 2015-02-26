label holly1:

    "It's been awhile since I've called my guy."
    
    "I'll see if I can get some 'stuff' from him."
    
    play sound "beep.wav"
    
    play sound "call.wav"
    
    $renpy.pause(5,hard=True)
    
    he "H-Hello?"
    
    z "Yo. Henry! Sup man?"
    
    he "Heyy...{w} who's this?"
    
    z "Bro. Read the name on the phone."
    
    he "Oh heyy! Zen! Been a while man."
    
    z "Yeah man."
    
    he "Need me to hook you up with stuff?"
    
    z "I'd love that man."
    
    he "Alright alright. Just text me the details and I'll head over there."
    
    z "Cool man. Cool."
    
    play sound "beep.wav"
    
    "That went well."
    
    "Every man is entitled to their own vice."
    
    "That's what I believe."
    
    "Life's too short to not try things."
    
    "Thus led me to this."
    
    "Compared to my friends, I'm not that social."
    
    "I frequent the bar, like once or twice a week."
    
    "But Chris is a nightclub VIP."
    
    "Or at least he's treated like one."
    
    "He doesn't have a card or anything."
    
    "But because he parties there a lot,{w} not to mention he's the party animal who makes things fun,{w} he gets preferred treatment."
    
    "But here's the weird thing."
    
    "I like smoking my weed."
    
    "Most of my friends haven't even tried it."
    
    "So some of my friends think I'm cooler than them."
    
    "But I think that being 'cool' comes down to your popularity, personality, and charisma."
    
    "At best, I think I have the personality."
    
    "Then again I do have mixed feelings about my personality."
    
    "You see."
    
    "This."
    
    "This whole analytical thing."
    
    "I actually like being analytical."
    
    "However, another way of saying that is,{w} 'I think too much.'"
    
    "Which can be a burden at times."
    
    scene bg room
    with fade
    
    "I guess what I'm saying is."
    
    "I need a break from observing everything every now and then."
    
    "It's an advantageous trait, yes."
    
    "But I acknowledge the fact that I need a break from all that."
    
    "Thinking too much makes me exhausted."
    
    "Sometimes I end up worrying about things I shouldn't be worried about."
    
    "I'm gonna close my eyes a little bit."
    
    scene bg black
    with fade
    
    "I met Henry about a year ago."
    
    "However, I started smoking around the second semester of freshman year."
    
    "We were in the same English class, and we were seated next to each other."
    
    "We made a lot of jokes."
    
    "For example, the teacher once asked,{p}'Name something that you do everyday.'"
    
    "Next thing you know, there go Henry and I whispering the song,{p} 'Smoke weed everyday.'"
    
    "I don't know much about the guy."
    
    "Only that he was actually a supplier and the stuff he gets are gooood."
    
    play sound "knock.wav"
    
    stop music
    
    "Hm?"
    
    "Here already?"
    
    "That was rather quick."
    
    "Oh right, he lives at Beachside."
    
    "That took me a while to realize."
    
    "Guess he knows this place better than I do."
    
    scene bg room
    with fade
    
    scene bg kitchen
    with wipeleft
    
    play sound "knock.wav"
    
    z "Yeah yeah! I'm here. I'm here."
    
    play sound "door.wav"
    
    play music "Montego.mp3" fadeout 5
    
    show holly me smile n:
        xalign -0.25 yalign 1.0
        linear 5 xalign 0.0
        hop()
        hop()
    with dissolve
    
    $renpy.pause(2, hard=True)

    show expression Text(_("Holly's Chapter - Chapter 1"), size=50, yalign=0.5, xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve
    
        
    $renpy.pause(3, hard=True)
    
    hide text
    with dissolve
    
    h "heyy."
    
    "..."
    
    "I don't know this girl."
    
    "A blonde girl with braids just entered my home."
    
    "But okay context clues."
    
    show holly:
        hop()
    
    h "Is it like, okay if I sit down?"
    
    z "Of course. Go ahead."
    
    h "Cool."
    
    show holly away:
        linear 1 xalign 0.2
    
    "The girl slowly walks toward the chair."
    
    show holly me
    with dissolve
    show holly away
    with dissolve
    
    "Now she's looking around."
    
    show holly me
    with dissolve
    show holly away
    with dissolve
    
    show holly:
        linear 1 xalign 0.5
    
    $renpy.pause(1)
    
    "She made it to the chair."
    
    show holly me:
        linear 1 yalign 1.5
    
    "She sits down slowly, probably trying not to fall."
    
    h "Duude."
    
    h "Your place is like,{w} so{w} cool."
    
    show holly away
    with dissolve
    
    h "There's like, windows over there."
    
    show holly me
    with dissolve
    
    h "Hey, mind if I smoke one in here."
    
    play sound "door.wav"
    
    "I close the door before anyone notices anything."
    
    z "Uhm."
    
    show holly:
        hop2()
    
    h "No no. It's okay if you don't want."
    
    z "I don't believe we've met."
    
    show holly:
        hop2()
        hop2()
    
    h "Oh! OH! That's right!"
    
    h "I'm Holly,{w} Henry's little sis."
    
    "Okay?"
    
    show holly:
        hop2()
        hop2()
    
    "She's taking something out of her pocket."
    
    "It's a joint."
    
    h "C'mon, I walked all the way here."
    
    z "I didn't say no."
    
    h "Oh?"
    
    z "Yeah, let's blaze it."
    
    z "You first."
    
    h "Sure."
    
    show holly away
    with dissolve
    
    play sound "smoke.wav"
    
    
    "She takes the first hit while I open up the windows."
    
    show holly me:
        hop2()
    
    "She's handing me the joint while holding her breath."
    
    play sound "smoke.wav"
    
    z "Forgive me if I cough, it's been a while."
    
    show holly:
        hop2()
        hop2()
     
    "She shakes her head as if saying no problem."
     
    "It's been a while so I should go ahead and have a big one."
    
    play sound "smoke.wav"
    
    $renpy.pause (2, hard=True)
    
    "7... {w}8...{w}9..."
    
    z "*cough*! *cough*!"
    
    show holly me teeth
    with dissolve
    
    h "Hahaha!"
    
    "She laughs at me coughing and smoke comes out of our mouths."
    
    show smoke
    with dissolve       
    
    z "Hey! I held a big one in for 9 seconds."
    
    h "Yeah, you're too pussy to get to 10."
    
    show holly away smile
    with dissolve
    
    play sound "smoke.wav"
    
    "I hand her the joint and she sucks on it."
    
    z "Nice nice."
    
    show holly me
    with dissolve
    
    "She hands it to me again."
    
    play sound "smoke.wav"
    
    $renpy.pause (2, hard=True)
    
    show holly me teeth
    with dissolve
    
    h "8...{w} 9... {w} 10!"
    
    h "Yay! You did it!"
    
    "This time I smoothly exhale."
    
    z "Yeahh."
    
    z "Woah."
    
    z "This is good stuff."
    
    show holly me smile
    
    h "Yeahh duude."
    
    h "This is imported shit right here."
    
    z "Oh right. Yeah Uh..."
    
    z "Before I forget, uhh. My uhh... my stuff?"
    
    h "Oh yeah yeah. Here."
    
    z "And here you go."
    
    "She hands me a bag and I hand her the money."
    
    h "Is it okay if I chill here for a while?"
    
    z "Yeah yeah, sure sure."
    
    "Ahh... I love this feeling."
    
    "My body is relaxed."
    
    "I feel like I have no cares in the world."
    
    show holly away
    with dissolve
    
    h "Hey, what's in the other room?"
    
    z "I got two beds in there."
    
    show holly me
    
    h "Awesome!"
    
    h "Can I lie down on it?"
    
    z "Sure sure."
    
    scene bg room
    with wiperight
    
    show holly away smile n:
        xalign -0.5 yalign 1.0
        linear 1 xalign 0.0
    
    h "Woaah."
    
    h "This place is so cool."
    
    "She passes me the joint."
    
    play sound "smoke.wav"
    
    z "Yeah. It is."
    
    show holly:
        linear 1 xalign 1.0
        hop2()
    
    "She finds her way to the second bed and plops herself right on it."
    
    show holly me
    
    h "Dude dude."
    
    z "Yeah?"
    
    h "Your bed...{w} is like... {w} soft... {w} and hard...{w} at the same time."
    
    show holly me teeth
    with dissolve
    
    h "It's perfect!"
    
    z "Thanks."
    
    "I hand it to her."
    
    show holly away smile
    with dissolve
    
    play sound "smoke.wav"
    
    $renpy.pause (2, hard=True)
    
    show holly me
    with dissolve
    
    "She hands it to me while holding her breath and nods her head."
    
    "Guess the last hit is mine."
    
    play sound "smoke.wav"
    
    $renpy.pause (2, hard=True)
    
    "She spreads her arms out on the bed, laying on her back."
    
    "She opens her mouth and slowly lets the smoke come out on its own."
    
    "I do the same."
    
    show smoke
    with dissolve
    
    z "This is good stuff."
    
    h "Yes. Yes it is."
    
    "I throw away the filter in the trash."
    
    h "Hey."
    
    z "Hm?"
    
    h "Why do you have two beds?"
    
    z "The apartment came with two beds."
    
    z "Although I haven't paid for furnishing."
    
    z "So a guy might come over and take it sometime."
    
    h "I see."
    
    z "But I'm planning to keep it."
    
    h "Oh? Why?"
    
    z "Uhh..."
    
    h "You a player?"
    
    z "No. No."
    
    z "I like to visit the bar every now and then."
    
    h "And pick up chicks?"
    
    z "No. No... {w} Not always."
    
    show holly me teeth
    with dissolve
    
    h "Heheheh."
    
    show holly me smile
    with dissolve
    
    h "Hey."
    
    z "Hm?"
    
    h "Hug me."
    
    show holly:
        linear 1 xalign 0.5
        hop2()
    
    "She sat up and stretched her arms."
    
    z "Uh..."
    
    h "No no. Go ahead. Hug me."
    
    "I was too high to think it over."
    
    "I wanted a hug."
    
    "I came closer and embraced her."
    
    h "Mmmm."
    
    h "Hugging feels nice."
    
    "I was enjoying the hug too much to say anything."
    
    "She pulls me down on the bed over her."
    
    h "You're so huggable."
    
    h "You're my huggaballoo."
    
    h "Mmmm."
    
    h "But you're heavy."
    
    h "Switch."
    
    show holly:
        hop()
    
    "She lies down on top of me, hugging me hard."
    
    "I can feel her breasts resting on my chest."
    
    show holly:
        hop()
    
    "She buries her face on the bed."
    
    show holly:
        hop()
        hop()
    
    "And again."
    
    show holly:
        hop()
        hop()
        hop()
    
    "And some more."
    
    h "Dude!"
    
    h "You gotta try putting your face on your bed!"
    
    h "Just slap it in there and motorboat the bed."
    
    "I look at the bed."
    
    "Then I look at her chest."
    
    "I can't help it, I'm a guy."
    
    h "Woah woah. No."
    
    h "Put your head on the bed first."
    
    show holly teeth
    with dissolve
    
    h "If you can resist the softness of your bed then you can motorboat me."
    
    z "Uhh... okay..."
    
    "I bury my face on the bed as told."
    
    show bg
    with hpunch
    
    show bg
    with hpunch
    
    "My goodness."
    
    "Was my bed really this soft?"
    
    "I continue motorboating my bed."
    
    show bg
    with hpunch
    
    show bg
    with hpunch
    
    h "Hahahaha!"
    
    "Holly laughs at me before continuing to motorboat the bed with me."
    
    show bg
    with hpunch
    
    show bg
    with hpunch
    
    show holly smile:
        hop2()
        hop2()
    with dissolve

    "At this point, we're both face down on the same bed."
    
    "Just shaking our heads and feeling the fabric slide across our faces."
    
    "I suddenly stop."
    
    "I suddenly want to feel the fabric of Holly's jacket."
    
    "Too high to think about it, I allow my hand to wander her sleeve."
    
    show holly teeth:
        hop2()
    with dissolve
    
    h "Ah. What is this?"
    
    z "Your jacket...{w} is so soft."
    
    show holly smile:
        hop2()
    with dissolve
    
    h "Really?"
    
    show holly:
        hop2()
        hop2()
    
    h "Oh yeah! It does."
    
    z "Woah."
    
    h "Woah."
    
    z "Dude, my hand."
    
    show holly teeth:
        hop2()
        hop2()
    
    h "Hahahaha!"
    
    h "No! No!"
    
    h "Don't talk about your hand!"
    
    z "My hand...{w} is amazing."
    
    z "Look at your hand."
    
    show holly:
        hop2()
    
    h "No!!!"
    
    z "Here's my hand."
    
    "I show her my hand,{w} and she starts laughing."
    
    show holly:
        hop2()
        hop2()
        hop2()
    
    h "HAHAHAHA!"
    
    h "Nuuu!"
    
    h "Not the hand!"
    
    "I laugh at her resisting my hand."
    
    z "HAHAHA!"
    
    "My stomach hurts."
    
    z "Hey hey."
    
    show holly smile
    with dissolve
    
    h "What?"
    
    z "Can I touch your hair?"
    
    "..."
    
    show holly teeth:
        hop2()
        hop2()
    with dissolve
    
    "We both laugh at the stupid request."
    
    h "I wanna touch your hair too!"
    
    show holly smile:
        hop2()
        hop2()
    
    "She starts messing up my hair."
    
    "I start fondling her hair as well"
    
    h "Dude your hair is so messy."
    
    h "It's like, straight and wavy."
    
    h "Feels so nice."
    
    z "Your braids feel weird."
    
    z "Feels nice, but weird."
    
    h "Does it feel weird?"
    
    z "Yeah it does feel weird."
    
    h "Weird."
    
    z "Yeah weird."
    
    show holly teeth:
        hop2()
    with dissolve
    
    h "Stop saying weird!"
    
    z "But your hair feels weird"
    
    show holly:
        hop2()
        hop2()
    
    h "HAHAHAHA!"
    
    h "Stop it!"
    
    z "Okay."
    
    show holly smile
    with dissolve
    
    "I put my hands down."
    
    "..."
    
    h "Actually I like it when you touch my hair."
    
    z "I like it when you touch my hair."
    
    show holly teeth
    with dissolve
    
    h "Yay! Hair!"
    
    z "Yay! Hair!"
    
    show holly smile
    with dissolve
    
    "From our hair, we start touching each other's faces."
    
    h "Your cheeks are so squishy!"
    
    z "You skin is so smooth."
    
    "I touch her lips."
    
    z "And your lips are so cute."
    
    h "Mmm."
    
    show holly teeth
    with dissolve
    
    h "Wanna kiss?"
    
    z "Is it okay?"
    
    show holly smile
    with dissolve
    
    h "That's like, the weirdest reply to the question."
    
    "I chuckle."
    
    "But I really do want to kiss her."
    
    z "I want to kiss you."
    
    h "Okay. C'mere then."
    
    show holly smile:
        hop2()
    with dissolve
    
    h "Mwahh."
    
    "She gives me a light peck before I start giggling at her sound effect."
    
    z "What kind of sound effect is that?"
    
    show holly teeth
    with dissolve
    
    h "Dunno."
    
    show holly smile
    with dissolve
    
    h "Hey, that felt good."
    
    h "Let's do it again."
    
    z "Okay."
    
    show holly:
        hop2()
    
    "We kiss again."
    
    "This time a long one."
    
    z "You feeling weird?"
    
    h "Not really."
    
    h "Feels nice to kiss."
    
    z "Yeah it does."
    
    h "Something wrong?"
    
    menu:
        h "You have a girlfriend or something?"
    
        "Yeah... something.":
            h "Aww, that's a shame."
    
        "Nop.":
            $holly_love += 1
            h "Aww, little lonely guy."
        
    h "C'mere I want to hug you more."
    
    "This may sound weird but..."
    
    "I am enjoying this."
    
    "I've never gotten high alone with a girl before."
    
    "It's usually just me, or with other friends."
    
    "Or I eat a space cake and go to class."
    
    "The sensation of wanting to hug and kiss is normal for me."
    
    "I didn't know others felt like that."
    
    z "You know."
    
    h "Hmm?"
    
    z "I read an article that lovers should smoke weed together more."
    
    h "Lovers?"
    
    "..."
    
    z "Sorry."
    
    h "No no, that's fine."
    
    h "Honest mistake."
    
    h "I mean, we were just hugging and kissing right now."
    
    z "Don't mind if I say something weird?"
    
    h "Hmm?"
    
    z "I've always wanted to get high with a girl."
    
    h "Oh yeah, you don't see a lot of girls like me."
    
    h "I mean, there are plenty."
    
    h "But you don't see a lot."
    
    z "Yeah, that's right."
    
    h "So you never got high with a girl?"
    
    z "I went to a party with my friend once."
    
    z "I ate a space cake because I didn't feel like drinking."
    
    h "Uhuh."
    
    z "I was able to talk to a girl that time."
    
    z "But she thought I was weird."
    
    show holly teeth
    with dissolve
    
    h "You didn't talk about your hand did you?"
    
    z "I did."
    
    h "HAHAHA!"
    
    show holly smile
    with dissolve
    
    h "No wonder."
    
    h "If that was me, even if I was sober I woulda laughed."
    
    show holly away
    with dissolve
    
    h "This is what makes weed different from drinking."
    
    z "Yeah!"
    
    "..."
    
    "We stare at the wall."
    
    z "Are you going out with anyone?"
    
    show holly me
    with dissolve
    
    h "Not really."
    
    h "There's this guy who likes me."
    
    h "But he kinda scares me."
    
    show holly me teeth
    with dissolve
    
    h "But you're a huggaballoo."
    
    show holly me smile
    with dissolve
    
    h "From now on you are my huggaballoo."
    
    h "My cutie huggaballoo."
    
    h "Now hug me huggaballoo."
    
    "I embrace her as told."
    
    show holly me teeth
    with dissolve
    
    h "Hahaha!"
    
    h "Feels so nice to hug my huggaballoo."
    
    show holly me smile
    with dissolve
    
    h "Oh right, you wanted to motorboat me right?"
    
    z "Yeah."
    
    show holly away
    with dissolve
    
    h "Hmm..."
    
    show holly me
    with dissolve
    
    h "Alright, you can."
    
    h "Because you're my huggaballoo."
    
    "Yess."
    
    z "Okay then, allow me."
    
    "I proceed to bury my face under her breasts."
    
    "I didn't want my face to touch the zipper."
    
    show bg
    with hpunch
    
    z "Mmm."
    
    show holly me teeth
    with dissolve
    
    h "Hahaha~."
    
    h "That felt funny."
    
    show bg
    with hpunch
    
    show bg
    with hpunch
    
    show holly me smile
    with dissolve
    
    h "Does it feel good?"
    
    z "Yeah. I'm happy now."
    
    h "I'm happy that my huggaballoo is happy."
    
    hide smoke
    with dissolve
    
    "At this point we were almost sober."
    
    show holly away
    with dissolve
    
    h "Oh my, look at the time."
    
    show holly me:
        hop()
    with dissolve
    
    h "I better go now."
    
    z "Oh right yeah."
    
    scene bg kitchen
    with wipeleft
    
    show holly me smile n
    with moveinright
    
    play sound "door.wav"
    
    "I open the door for her as we exchange numbers."
    
    h "One more for the road?"
    
    z "Yes please."
    
    show holly:
        hop()
    
    "She puts her face against mine and share the last kiss for today."
    
    "Mmm?"
    
    show holly me teeth:
        hop()
    with dissolve
    
    h "Little bit of tongue for ya."
    
    "She licks her lips after saying."
    
    h "You're my huggaballoo okay?"
    
    h "Call me."
    
    z "I will."
    
    h "Enjoy your stuff."
    
    show holly:
        linear 2 xalign -2.0
    
    "That was nice."
    
    "Today... Today was a good day."
    
    scene bg room
    with wiperight
    
    stop music fadeout 1
    
    "I'll roll one before calling it a day."
    
    play sound "smoke.wav"
    
    $renpy.pause(2, hard=True)
    
    show bg black
    with fade
    
    call classday
    
    jump choice
    
    return