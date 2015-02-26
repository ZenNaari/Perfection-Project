label kitty1:

    "Alright then."
    
    "I've decided to start getting fit."
    
    "Time to workout."
    
    "Maybe even join a sport."
    
    "Yeah."
    
    "That sounds like a fun idea."
    
    "I should join a sport."
    
    "I'll let it come to me."
    
    "For now, I'll just do a few warmups."
    
    show bg zencomp
    with hpunch
    
    show bg
    with vpunch
    
    "A few situps..."
    
    show bg
    with hpunch
    
    show bg
    with hpunch
    
    "...One pushup..."
    
    show bg
    with vpunch
    
    "Oh god."
    
    "I need to work on my pushups."
    
    "Well, that's a good start."
    
    "I'll see what I can do tomorrow."
    
    stop music fadeout 1
    
    scene bg black
    with fade
    
    call classday
    
    show expression Text(_("4PM"), size=50, yalign=0.5, xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve
    
    $renpy.pause(2, hard=True)
    
    hide text
    with dissolve
    
    scene bg beachcamp
    with fade
    
    play music "AirportLounge.mp3"
    
    "So I just got out of class..."
    
    "and I decided to walk from LSU to BSU."
    
    "And I...{w} am terribly exhausted."
    
    "This was not a very good idea."
    
    "At the very least, the sea breeze is keeping me cool."
    
    "It's the cold season, I have that to thank."
    
    "But at this rate, I might really pass out."
    
    "Hm?"
    
    show kitty away smile n:
        xalign 1.0 yalign 1.0
        linear 1 xalign 0.5
    with dissolve
    
    "A girl with dyed red hair appears from behind me."
    
    "Effortlessly jogging around the campus it seems."
    
    "Although I think I spotted her on my way here."
    
    "I think she passed me about 4 times by now."
    
    "I do have to admit that the way from LSU to BSU is perfect for jogging."
    
    "Lots of nature to admire, clear blue skies."
    
    show kitty me
    with dissolve
    
    "Ah, she's looking at me."
    
    "She probably recognizes me from my walk here."
    
    show kitty me excited
    with dissolve
    
    show kitty:
        hop()
    
    "Huh?"
    
    show kitty away:
        linear 0.5 xalign 0.0
    
    $renpy.pause(0.1,hard=False)
    
    hide kitty
    with dissolve
    
    stop music fadeout 5
    
    "She gave me a condescending look before running off."
    
    "Ugh, this is making me hate myself."
    
    "I probably shouldn't even go to the gym."
    
    "I mean look at me, I am absolutely exhausted."
    
    "While a girl jogged about 4 laps around me!"
    
    "And not the wimpy kind of jogging too."
    
    "I mean the really bring your knees up high jogging."
    
    "Guess I'll go home."
    
    "I'm not that far from the street."
    
    "I could just turn around and get a cab."
    
    "Hm?"
    
    ki "Hey!"
    
    show kitty me smile n
    with dissolve
    
    ki "Wanna join the MMA Club?"
    
    play music "Breakdown.mp3"
    
    show expression Text(_("Kitty's Chapter - Chapter 1"), size=50, yalign=0.5, xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve
    
        
    $renpy.pause(3, hard=True)
    
    hide text
    with dissolve
    
    z "Huh?"
    
    z "What makes you think I wanna join that?"
    
    ki "You look like the kind of person who would benefit from it."
    
    ki "It's a fun way to exercise and get in shape."
    
    z "Real reason?"
    
    show kitty me angry
    with dissolve
    
    ki "Damn."
    
    "I kinda sorta saw through that."
    
    "These things like sports clubs recruit new members so that they get more money from the school."
    
    ki "Am I really that readable?"
    
    z "Nope. It's just because it's me."
    
    show kitty me normal
    
    ki "What do you mean?"
    
    z "Nevermind. Just know that I'm good at stuff like that."
    
    ki "So you're not gonna join huh?"
    
    "I'm not sure how to respond to that."
    
    show kitty away angry
    
    ki "Damn."
    
    show kitty me normal
    
    ki "Well, if you ever change your mind. Just try to find me."
    
    show kitty away
    
    z "Wait."
    
    "I stupidly replied."
    
    show kitty me
    
    ki "Hm?"
    
    z "What if I am interested?"
    
    ki "But you just said a while ago..."
    
    z "That's not a good way to recruit members."
    
    "Apparently, that's the reason why I replied."
    
    "I was just annoyed at the way she tried to recruit me."
    
    z "If you're going to recruit people then you should convince them more."
    
    z "Not just give up at the first sign of rejection."
    
    ki "Uhm. Okay?"
    
    z "You're in the MMA club right?"
    
    z "Think about it like...{w} going for the knockout punch while you're rocked."
    
    "I actually watch the Supreme Fighting Championship(SFC)."
    
    z "Have you seen the Johnson vs. Lawly title fight last week?"
    
    ki "Yeah. What about it?"
    
    z "Johnson was the light heavyweight champion."
    
    ki "And he lost to Lawly."
    
    z "But Johnson never gave up."
    
    z "He kept trying to attempt that takedown."
    
    z "Even though he lost the fight, he didn't just stand there circling the octagon like most fighters do."
    
    z "He was tired, he knew he had less points, he knew Lawly was gonna be the new champion."
    
    z "But he stuck in there anyway, and he kept trying to get that takedown."
    
    "I'm not sure if I worded it right."
    
    "I sound boring while I described one of the best fights in SFC history."
    
    ki "I see..."
    
    show kitty me smile
    
    ki "You should join the MMA club."
    
    ki "I don't know what it is, but you look like the kind of guy who's perfect for it."
    
    z "Now you're just flattering me."
    
    "I mean look at me, I'm a sweating pig."
    
    ki "At least I didn't give up."
    
    z "I guess."
    
    ki "So, will you join the MMA club?"
    
    "Well. I did come all the way here to get in shape."
    
    "I do watch SFC fights very often."
    
    "Why the hell not?"
    
    "It actually does sound like a fun way to get in shape."
    
    "My apartment isn't that far from here."
    
    "Maybe I could even jog there."
    
    "..."
    
    "No. No I can't."
    
    "But I guess I'll give it a shot."
    
    z "Sure. I'll try it out."
    
    show kitty me excited
    
    ki "Yess!"
    
    ki "Another step closer to the SFC!"
    
    z "Wait."
    
    show kitty me normal
    
    ki "Hm?"
    
    z "Don't tell me you're actually aiming to be in the SFC."
    
    ki "Why shouldn't I?"
    
    ki "And why should you object?"
    
    ki "You're the one who told me not to give up."
    
    "She got me there."
    
    z "Alright, alright. I'll shut up."
    
    z "Good to see such high hopes."
    
    show kitty me smile
    
    ki "Good then."
    
    z "So what exactly is your plan?"
    
    show kitty me normal
    
    ki "What plan?"
    
    z "Surely you have a plan if you want to fight in the SFC."
    
    ki "Uh..."
    
    ki "Fight, win.{w} Keep fighting and winning?"
    
    "My goodness."
    
    "How hopeful can you get."
    
    z "Have you entered any local MMA fights?"
    
    show kitty me smile
    
    ki "YES!"
    
    z "How did it go?"
    
    ki "I won 2 fights by KO."
    
    "Woah."
    
    "That is impressive."
    
    "The women's division usually win by submissions."
    
    "Arm bars, choke holds, things like that."
    
    "A woman with knockout power."
    
    "Now that's something."
    
    z "So I'm guessing you're a boxer."
    
    ki "Yes."
    
    z "Any other skills?"
    
    ki "I throw a few kicks when I need to."
    
    "Her speech is so simple, it sounds primitive."
    
    "She's got quite the foreign accent on her."
    
    "At least she can understand me."
    
    "But so far, judging by our conversation, we are still pretty out-of-sync."
    
    "This is the equivalent of a relationship moving waay too fast."
    
    stop music fadeout 1
    
    ki "Wanna go to the gym?"
    
    z "Oh yeah. Sure."
    
    ki "Alright then."
    
    ki "By the way, I'm Kitty."
    
    z "Zen."
    
    scene bg gym1
    with irisout
    
    show kitty away smile n:
        xalign 1.5 yalign 1.0
        linear 1 xalign 0.5
    
    play music "HoneyBee.mp3" fadeout 1
    
    ki "Here we are."
    
    play sound "boxing.wav"
    
    "Hm."
    
    "It's mostly boxing equipment in here."
    
    "I guess that's not surprising."
    
    "Given that she claims she is a boxer."
    
    z "So, who else is in the MMA club."
    
    show kitty me
    
    ki "Just us, for now."
    
    "..."
    
    z "What?!"
    
    show kitty me normal
    
    ki "The boxing club is more popular."
    
    ki "I have a hard time getting members because of them."
    
    "Ugh."
    
    z "So if I didn't meet you today, I would have been recruited by them."
    
    show kitty me angry
    with dissolve
    
    "She crosses her brows at me."
    
    "Of course she's upset."
    
    z "Sorry about that."
    
    z "So, what do we do now?"
    
    show kitty me normal
    
    ki "Uhh..."
    
    ki "Train more and get more members I guess."
    
    z "Plain and simple. Then our goal is to get two other people to join us."
    
    z "Alright, our goal is to get one more boy and another girl for you."
    
    show kitty me angry
    
    ki "I can fight boys."
    
    "I'm not going to doubt that."
    
    "But since we're talking about MMA, there's going to be a lot of clinching, takedown, wrestling."
    
    show kitty me excited:
        linear .5 yalign 2.0
    
    "Which means a lot of touching..."
    
    play sound "ruff.wav"
    
    show bg
    with hpunch
    
    z "Woah woah!"
    
    "Kitty puts one arm in between my legs."
    
    "Another around my neck."
    
    "And the next thing I know, I'm up in the air, being held by two thin but incredibly powerful arms."
    
    z "What are you doing?! What are you doing?!"
    
    ki "See, I can carry you easily."
    
    z "Shit shit shit! Put me down!"
    
    ki "Okay."
    
    show kitty
    with hpunch
    
    z "Woah woah woah WAIT!"
    
    show kitty:
        linear .2 yalign 1.0
    with vpunch
    
    play sound "fall.wav"
    
    show bg
    with hpunch
    
    z "Agh!"
    
    "She threw me to the ground."
    
    show kitty:
        linear .2 yalign 2.0
    with vpunch
    
    "And she mounts me at half guard."
    
    ki "I'm pretty strong no?"
    
    "I'm a pretty heavy guy."
    
    "So there's no doubting her strength."
    
    z "Ow. Yes. Yes. Okay okay."
    
    show kitty:
        linear .2 yalign 1.0
    with vpunch
    
    "I struggle to get back up."
    
    z "Ugh."
    
    z "Look, Kitty. I know you're strong enough to beat up guys."
    
    ki "That's right!"
    
    z "Yeah."
    
    z "But let's just make it our goal to get one boy and girl by the end of the semester."
    
    show kitty me smile
    
    ki "Sounds good."
    
    z "I think the best thing to do right now is to observe the boxing club."
    
    show kitty me angry
    with dissolve
    
    "Her thick brows cross again."
    
    "She must really hate the boxing club."
    
    ki "Fine."
    
    z "We'll just find out what kind of programs they're doing and we'll do the same thing."
    
    ki "Okay."
    
    z "So..."
    
    z "Where's the boxing club?"
    
    stop music fadeout 1
    
    ki "It's in the other room."
    
    ki "Over here."
    
    scene bg gym
    with wipeleft
    
    show kitty away angry n:
        xalign 1.5 yalign 1.0
        linear 1 xalign 1.0
    
    play music "WahGameLoop.mp3" fadeout 1
    
    ki "Here's the stupid boxing club."
    
    "Hmm. Not bad."
    
    "My main concern would be that there's an octagon in a boxing club."
    
    "We're gonna need to use that octagon."
    
    "There's about 6 or 7 people in here."
    
    "They all look like real contenders."
    
    "I'm going to guess that they actually play boxing for the school."
    
    "Considering that boxing is a big sport loved by many, 7 people should already give a huge payout."
    
    "Whereas even if we get 7 people in local fights, it'll just barely give us any profit."
    
    "Kitty's knockout power should be able to get lots of attention."
    
    "Ah..."
    
    "A big dark senior looks in our direction."
    
    show sherman smile:
        xalign -0.5 yalign 1.0
        linear 1 xalign 0.0
    
    sh "Hey there. Who are you, new bloods?"
    
    show sherman normal
    with dissolve
    
    sh "Oh, it's you."
    
    ki "Fuck you Sherman."
    
    sh "How many times do I have to tell you, there's no girls on this team."
    
    "Ah."
    
    "Now I get it."
    
    ki "And how many times do I have to ask, why not?"
    
    "The big guy looks at me."
    
    sh "And who's this fat kid?"
    
    sh "Is he your bitch?"
    
    "Fat kid, I'm perfectly fine with."
    
    "Calling me a bitch is a totally different thing."
    
    "Nevertheless I keep my cool with raised eyebrows."
    
    z "Hi, nice to meet you, my name is Zen."
    
    ki "He joined the MMA club."
    
    show sherman smile
    
    sh "Hah. So you finally got someone to join that ghost town of a club?"
    
    sh "I would congratulate you, but this wimp doesn't even look like he can last 10 minutes on a treadmil."
    
    "Okay. That was clever."
    
    "Because I really can't last 10 minutes on a treadmil without slowing down."
    
    "Just keep your cool Zen. Keep your cool."
    
    ki "He's got what it takes."
    
    show kitty me
    
    ki "I can see it."
    
    "I want to say thank you but even I don't see it."
    
    "Anyway, we're here for a different reason."
    
    "So I'm going to butt in the conversation now."
    
    z "Hey man, look I'm sorry about this."
    
    show sherman normal
    
    sh "This doesn't concern you bro."
    
    sh "This idiot here is the one who started it."
    
    "I can totally see that to be the case."
    
    z "First of all, this started to concern me when you called me a bitch."
    
    z "Second of all, we just want to observe the club for a little bit."
    
    z "We don't want to disturb you or anything."
    
    z "We just want follow your club's example."
    
    "See. That went well."
    
    "There's an advantage to being the diplomat here."
    
    show sherman:
        linear 0.5 xalign 0.5
    
    stop music fadeout 1
    
    "Huh?"
    
    play sound "punch2.wav"
    
    scene bg black
    
    $renpy.pause(1,hard=True)
    
    ki "You fucker!"
    
    play sound "punch.wav"
    
    $renpy.pause(0.5,hard=True)
    
    play sound "punch2.wav"
    
    "Ugh."
    
    "That guy had me."
    
    "I forgot something important."
    
    "I forgot that there are people who exist who you just can't have diplomacy with."
    
    sh "Little bitch!"
    
    play sound "punch2.wav"
    
    $renpy.pause(0.5,hard=True)
    
    play sound "punch.wav"
    
    "There are two ways to deal with people like this."
    
    "Either you turn your back and ignore them."
    
    play music "ThereItIs.mp3" fadeout 1
    
    "Or you talk back using the form of body language everyone understands."
    
    scene bg gym
    with fade
    
    show kitty away angry n:
        xalign 0.6 yalign 1.0
    with dissolve
    
    show sherman normal:
        xalign 0.4 yalign 1.0
    with dissolve
    
    show kitty:
        linear 0.2 xalign 0.7
        linear 0.2 xalign 0.6
    with hpunch
    
    play sound "punch.wav"
    
    $renpy.pause(0.2,hard=True)
    
    show sherman:
        linear 0.2 xalign 0.3
        linear 0.2 xalign 0.4
    with hpunch
    
    play sound "punch2.wav"
    
    "Ugh."
    
    "I get up on my feet."
    
    "I blacked out for a second there."
    
    "Oh god, my face hurts."
    
    "My hands won't stop making a fist."
    
    "There's only one thing on my mind right now."
    
    show kitty me normal:
        linear 0.2 xalign 1.0
    with dissolve
    
    "I push Kitty aside."
    
    ki "Hey!"
    
    "I lean my left side forward with my fists up."
    
    show sherman:
        linear 0.2 xalign 0.2
    
    "Sherman backs up a little."
    
    "I can see it."
    
    "He thinks he can land a stepping straight."
    
    "And here it comes."
    
    show sherman:
        linear 0.2 xalign 0.5
    
    $renpy.pause(0.2, hard=True)
    
    play sound "punch2.wav"
    
    show sherman:
        linear 0.2 xalign 0.2 yalign 6.0
    with hpunch
    
    z "Ohh god my hand!"
    
    z "Shit shit shit."
    
    z "That hurt."
    
    z "Auugh!"
    
    z "Shit that hurt."
    
    show kitty:
        linear 0.3 xalign 0.6
    
    ki "Are you okay?"
    
    z "Of course I'm fucking okay!"
    
    z "I just knocked the fuck out of a renowned boxer!"
    
    z "I feel fucking great!"
    
    ki "Well, you aren't wearing any gloves."
    
    z "Still..."
    
    z "Oh god this fucking hurts."
    
    z "I think I cut my knuckles with that one."
    
    "I timed everything perfectly and landed a powerful counter right hook."
    
    "All those shadow boxing and sparring sessions with Chris payed off."
    
    "I aimed for his jaw."
    
    "My knuckles slid across his bony jaw upon impact."
    
    "So my knuckles got scraped."
    
    "I can never ever pull that off again."
    
    show kitty away
    
    ki "Shit."
    
    ki "He's out cold."
    
    "He used a dangerous move on me."
    
    "He thought he could pull it off cuz I look like a wimp."
    
    "When actually I'm no stranger to the ocassional bar fight."
    
    "Not to mention, a couple of times when Chris banged a girl and got into some boyfriend trouble."
    
    "So if Sherman used a different punch on me, this whole thing would have been different."
    
    "Still, that was totally uncalled for."
    
    show kitty me smile
    
    ki "See."
    
    z "Huh?"
    
    ki "I knew you have what it takes."
    
    "A few street fights and suddenly 'I have what it takes.'"
    
    "How convenient."
    
    "The other boxers looked at us with impressed faces."
    
    show kitty me normal
    
    ki "Hey, let's go back."
    
    z "Ah okay."
    
    "She clearly doesn't like being here."
    
    stop music fadeout 1
    
    "But I think she was happy about what happened."
    
    
    
    scene bg gym1
    with wiperight
    
    play music "Honeybee.mp3" fadeout 1
    
    show kitty me smile n:
        xalign 0.0 yalign 1.0
        linear 2 xalign 0.5
    with dissolve
    
    ki "That was cool."
    
    ki "I knew you had it in you."
    
    "My hand still hurts."
    
    z "How many times have you said that now?"
    
    ki "I'll keep saying it until you believe me."
    
    z "Look here."
    
    show kitty me normal
    
    ki "Hm?"
    
    z "After fighting that guy, I just realized that I'm probably not suited for this."
    
    ki "What do you mean?"
    
    z "I mean, look at me."
    
    z "I'm a wreck."
    
    z "I get so easily exhausted."
    
    z "I tried to be the nice guy first before I thought of resorting to violence."
    
    show kitty me smile
    
    ki "Idiot."
    
    ki "Fighting is not about being agressive."
    
    z "I know that."
    
    show kitty me normal
    
    ki "Shut up, I'm talking."
    
    "Ah."
    
    ki "Listen."
    
    ki "I'm not the best at putting words together."
    
    ki "But there's something about you that I can sense."
    
    show kitty me smile
    
    ki "You're going to be a great fighter."
    
    "..."
    
    z "Thanks."
    
    z "That,{w} that motivated me a little."
    
    z "Yeah."
    
    z "I'm going to be a great fighter!"
    
    ki "Anyway, let's call it a day."
    
    z "I guess so."
    
    show kitty me excited
    with dissolve
    
    ki "You better work on your cardio."
    
    ki "You'll be a useless fighter if you can't even walk from LSU to here without panting like a pig."
    
    z "Alright alright."
    
    z "And you, don't forget to recruit other people."
    
    ki "Gotcha."
    
    stop music fadeout 1
    
    scene bg black
    with fade
    
    call night1
    
    jump choice
    
    