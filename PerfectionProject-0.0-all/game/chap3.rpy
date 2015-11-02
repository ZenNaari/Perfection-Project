label chap3:

    scene bg black
    with dissolve

    stop music fadeout 1
    
    play music "LongStroll.mp3" fadeout 1
    
    show expression Text(_("Chapter 3"), size=50, yalign=0.5, xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve
    
    $renpy.pause(2, hard=True)
    
    hide text
    with dissolve
    
    scene bg room
    with dissolve
    
    play sound "door.wav"
    
    show kat away smile n color:
        right
        hop2()
    with dissolve
    
    z "Hey."
    
    show kat me:
        hop2()
    
    k "Hey!"
    
    z "You settling in okay?"
    
    show kat away:
    with dissolve
    
    k "Sure am."
    
    "Kat continues to type away at her laptop on her bed."
    
    show kat me normal:
    with dissolve
    
    "Hm?"
    
    k "Where'd you come from?"
    
    z "Ah. I actually got myself wrapped around some extra curriculars."
    
    z "You know how that is."
    
    "Actually you probably don't."
    
    k "Hmm."
    
    play music "Marty.mp3" fadeout 1
    
    z "I should probably take a shower."
    
    show kat me angry
    
    k "NO!"
    
    show kat me angry:
        linear 0.5 center
    
    z "Huh?"
    
    "She quickly rolls out of bed and blocks me from entering the bathroom."
    
    z "What do you mean no?"
    
    show kat away mad
    
    k "Just. Not now."
    
    z "Huh?"
    
    show kat me angry
    
    k "Noooo!"
    
    "What the hell?"
    
    z "Are you hiding something in the bathroom?"
    
    show kat away mad
    
    k "No."
    
    z "Okay?"
    
    z "What's so important that you won't let me in the bathroom of my own home?"
    
    show kat me mad
    with dissolve
    
    "Ah."
    
    "That looked like it stung her a little."
    
    k "You don't need to take a shower!"
    
    z "What are you talking about?"
    
    z "Of course I need a shower."
    
    z "I mean look at me! I'm drenched in sweat!"
    
    show kat me smile
    with dissolve
    
    k "Yeah you are."
    
    z "What the fuck Kat?!"
    
    show kat me normal:
        hop()
    
    k "NOTHING!"
    
    z "You're not making any sense!"
    
    z "I mean you're a girl right?"
    
    z "Or at least a decent human being."
    
    "Actually given what I know about her I'm not sure that's true."
    
    show kat me mad:
    
    k "So?"
    
    z "So I should probably be sensitive to my roommate's sense of hygeine and do my responsibility to..."
    
    z "...well..."
    
    z "... clean... myself?"
    
    "Ugh, do I really have to say the weirdest shit?"
    
    k "That's not it."
    
    k "You're just cleaning yourself because you want to be clean."
    
    "What the fuck is this weird conversation about cleaning myself."
    
    "When did this become a philosophical debate?"
    
    z "So what if I'm cleaning myself because I want to be clean?"
    
    z "Isn't that like a pretty standard thing?"
    
    show kat away mad
    with dissolve
    
    "She's looking away, thinking for a second."
    
    show kat me
    with dissolve
    
    k "Cook."
    
    z "Huh?!"
    
    k "At least cook before getting in the shower!"
    
    z "Is that it? You're just that hungry?"
    
    show kat me smile:
        hop()
    
    k "YES!"
    
    "She said with great and odd enthusiasm."
    
    k "I'm hungry as shit!"
    
    z "Geez then just say that in the first place."
    
    "God this girl."
    
    z "Fine I'll cook something up."
    
    show kat:
        hop()
    
    k "SOUP!"
    
    z "What?"
    
    k "I want soup!"
    
    z "Ehh?"
    
    "Soup is not the best thing for me to cook right now."
    
    z "I don't want to cook soup, I might get sweat in it."
    
    show kat me mad:
         hop()
     
    k "You'll be fine."
    
    z "No I won't!"
    
    show kat me smile
    
    k "Then... ROAST!"
    
    z "We don't have anything fancy like ham or a whole chicken."
    
    z "And what the hell is up with your crazy food choices?!"
    
    show kat me mad
    
    k "Just make soup or something."
    
    z "I guess we can make chicken soup."
    
    z "We have potatoes, cabbage, lettuce..."
    
    z "Will chicken soup satisfy you madamme?"
    
    show kat me smile
    
    k "Oui oui monsieur!"
    
    z "Alright then."
    
    z "One chicken soup for the lady with the colorful hair."
    
    scene bg kitchen
    with wipeleft
    
    "Ugh."
    
    show kat away excited n color:
        xalign 1.6 yalign 3.0
        linear 1 xalign 1.35
    
    "Do I really have to put up with this?"
    
    "I seriously might get some sweat in the soup."
    
    "I don't want that."
    
    show kat:
        linear 1 xalign 1.25
    
    play sound "bubbles.wav"
    
    "Really, what a troublesome girl."
    
    "Wait."
    
    "Why am I taking orders from her?"
    
    "I mean, this is my home first."
    
    "No no. I shouldn't think like that."
    
    "But still."
    
    "As her equal roommate she should also share some of the cooking responsibilities."
    
    "I mean, if she wants soup and is hungry while i'm not here she should make it."
    
    "Huh."
    
    show kat normal:
        hop2()
    
    z "Kat?"
    
    show kat:
        linear 0.3 xalign 1.60
    
    z "You there?"
    
    z "Kat?"
    
    z "You okay?"
    
    k "Y-yeah! I-I'm fine!"
    
    k "You dork!"
    
    "Tch."
    
    play sound "bubbles.wav"
    
    "Calling me a dork when I'm slaving here over a pot of boiling water."
    
    "Maybe I should sweat in the food."
    
    show kat away excited:
        xalign 1.6 yalign 3.0
        linear 1 xalign 1.35
    
    "..."
    
    "No no. It's also going to be my food."
    
    show kat:
        linear 1 xalign 1.25
    
    show smoke
    with dissolve
    
    "Shit it's starting to get really hot."
    
    "Where's the ventilation?"
    
    "A window?"
    
    "Ugh."
    
    "It seems to be locked."
    
    "How do I open it?"
    
    show kat normal:
        hop2()
    
    z "Kat!"
    
    show kat:
        linear 0.3 xalign 1.60
    
    z "Did you do something with the ventilation?"
    
    k "O-o-of course not!"
    
    k "W-why would I even tamper around with that?"
    
    "I guess she has a point there."
    
    play sound "bubbles.wav"
    
    "Man she's acting strange today."
    
    "Time of the month?"
    
    "I don't know much about that."
    
    "Shouldn't she be acting more... well... angry?"
    
    "I guess she is a little mad."
    
    "Wait..."
    
    "Mad over what?"
    
    "She got mad at me for wanting to take a shower?"
    
    show kat away excited:
        xalign 1.6 yalign 3.0
        linear 1 xalign 1.35
    
    "Who the hell gets mad when their roommate wants to take a shower?"
    
    "It's supposed to be the other way around!"
    
    "*sigh*"
    
    "She's probably just being a weirdo."
    
    "Like she always is."
    
    "I guess I don't mind that."
    
    show kat:
        linear 1 xalign 1.25
    
    "Life is more fun when you know weird people."
    
    "I guess you can say I'm weird for thinking that."
    
    "Ah... towel!"
    
    "Why didn't I think of that before!"
    
    "I'll just wipe my face with a towel or something."
    
    "Let's see..."
    
    "..."
    
    "There's no kitchen towels."
    
    show kat normal:
        hop2()
    
    z "Kat!"
    
    show kat:
        linear 0.3 xalign 1.60
    
    z "Do you know where the kitchen towels are?"
    
    z "Did you wash them or something?"
    
    k "Y-yeah! YEAH! I did put them in the wash!"
    
    z "Did they look dirty?"
    
    z "I could have sworn that I put them in the wash recently"
    
    show kat:
        linear 1 right
        hop2()
    
    k "Sorry! I tried to cook something while you were away and failed!"
    
    z "Really?"
    
    k "Yeah!"
    
    z "What did you try to cook?"
    
    k "Uhh..."
    
    show kat me
    
    k "Soup?"
    
    z "Soup huh."
    
    k "I tried to make soup and failed."
    
    z "How?"
    
    show kat me mad
    with dissolve
    
    k "Stop asking!"
    
    k "I'm a little sensitive when it comes to housework."
    
    "You're probably just sensitive right now."
    
    "Well, I probably shouldn't be thinking like that."
    
    z "Soup's gonna be another hour."
    
    z "Now that it's cooking, i'll go take that shower now."
    
    show kat me angry:
        hop()
    
    k "NO!"
    
    z "Whyyy?"
    
    "I start to cry."
    
    "There's no point being reasonable anymore."
    
    "All I have left to do is beg."
    
    show kat away mad
    with dissolve
    
    k "Man up, you'll be fine."
    
    "I'm sure you're tougher than I am but it still stings when it comes from a girl."
    
    show kat:
        hop2()
    
    "I sit down."
    
    "What the hell is wrong with Kat today?"
    
    z "Why're you acting so weird all of a sudden?"
    
    show kat me
        
    k "Just,{w} whatever."
    
    z "Weirdo."
    
    k "Shut up."
    
    show kat away:
        hop()
        linear 0.5 xalign 1.75
    
    "And just like that she stands up and leaves the kitchen."
    
    "Ugh."
    
    "Who in the world has to suffer like this?"
    
    "Being forced to 'not' take a shower in his own home,"
    
    "after a long day's work."
    
    "It's just absurd."
    
    show kat me:
        linear 2 center
        hop2()
    
    "What's even more absurd is why the hell am I taking this shit from her?"
    
    k "Here."
    
    k "Play around with your laptop while wait."
    
    "Hm?"
    
    "It seems one thing is definitely clear."
    
    "She wants me to stay out of the shower."
    
    z "Thanks."
    
    show kat away smile:
        linear 1 right
        hop2()
    
    k "Sure."
    
    "..."
    
    "......"
    
    "........."
    
    z "Kat."
    
    show kat me
    
    k "Yeah?"
    
    z "Why're you still here?"
    
    show kat me mad
    
    k "I can't sit around my own home?"
    
    "I should really remember to talk to her as if she lives here."
    
    z "Nevermind."
    
    "I don't even know what to do with my laptop while she's sitting right there."
    
    "And sort of..."
    
    show kat me smile
    
    "... staring at me."
    
    z "You..."
    
    k "Yeah?"
    
    z "Wanna watch something while wait?"
    
    k "Sure."
    
    scene bg black
    with fade
    
    show expression Text(_("An hour later"), size=50, yalign=0.5, xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve
    
    $renpy.pause(2, hard=True)
    
    scene bg kitchen
    with fade
    
    show kat away smile n color:
        center
        hop2()
    with dissolve
    
    show smoke
    with dissolve
    
    show kat:
        linear 0.5 xalign 0.6
        linear 0.5 xalign 0.5
        linear 0.5 xalign 0.6
        linear 0.5 xalign 0.5
    
    "So we've been watching some random internet videos."
    
    "And right now I'm noticing that Kat is sitting awfully close to me."
    
    "Not that I mind but..."
    
    "It's almost as if she's trying to sit closer."
    
    "So of course I'm a little self conscious right now."
    
    "I'm all sweaty, and at this point I probably stink."
    
    play sound "bubbles.wav"
    
    "The smell of good soup is filling the air but..."
    
    show kat me
    with dissolve
    
    "She's really too close!"
    
    z "The soup seems ready huh?"
    
    show kat me normal
    
    k "Yep."
    
    "She pouts. As if disappointed."
    
    z "Guess I'll just turn it off and head to the shower now."
        
    hide smoke
    with dissolve
    
    show kat:
        hop()
    
    k "You won't eat it yet?"
    
    "She says as she gets up from her seat."
    
    z "I can't eat it yet when it's boiling hot."
    
    z "I'll wait for it to cool."
    
    z "And while I'm doing that."
    
    z "I'll take the shower you so loathe me wanting to do."
    
    show kat away
    with dissolve
    
    k "I guess."
    
    "She sighs."
    
    show kat me smile
    with dissolve
    
    k "I've been a little annoying today but..."
    
    k "Thanks for playing along."
    
    "More like, 'putting up with you.'"
    
    jump choice