# You can place the script of your game in this file.

#colors
#4876FF - royalblue
#27408B - dark royal blue
#00FF7F - spring green
#4EEE94 - sea green
#00EEEE - cyan


init:
    image bg room = "bg/room.jpg"
    image bg kitchen = "bg/kitchen.jpg"
    image bg blur = "bg/blurryroom.jpg"
    image bg black = "bg/black.jpg"
    image bg katcomp = "bg/katcomp.jpg"
    image bg katcomp gray = im.Grayscale("bg/katcomp.jpg")
    image bg zencomp = "bg/zencomp.jpg"
    image bg club = "bg/club.jpg"
    image bg taxi = "bg/taxi.jpg"
    image bg lakecamp = "bg/campus2.jpg"
    image bg beachcamp = "bg/campus.JPG"
    image bg gym = "bg/gym.jpg"
    image bg gym1 = "bg/gym1.JPG"
    image bg dorm = "bg/room2.jpg"
    image bg class = "bg/classroom.jpg"
    image bg cafe = "bg/cafe.jpg"
    image bg counter = "bg/counter.jpg"
    image bg booth = "bg/booth.jpg"
    image bg outside = "bg/outside.jpg"
    
    image white = "bg/white.png"
    
    image smoke = "smoke.png"

    # Declare images below this line, using the image statement.
    # eg. image eileen happy = "eileen_happy.png"

    # ~~~~~~~~~~~~images of Kat in underwear~~~~~~~~~~~~
    image kat me normal u color = "kat/Underwear/MeNormal.png"
    image kat away normal u color = "kat/Underwear/AwayNomral.png"

    image kat me mad u color = "kat/Underwear/MeMad.png"
    image kat away mad u color = "kat/Underwear/AwayMad.png"
    
    image kat me angry u color = "kat/Underwear/MeAngry.png"
    image kat away angry u color = "kat/Underwear/AwayAngry.png"

    image kat me smile u color = "kat/Underwear/MeSmile.png"
    image kat away smile u color = "kat/Underwear/AwaySmile.png"
    
    image kat me excited u color = "kat/Underwear/MeExcited.png"
    image kat away excited u color = "kat/Underwear/AwayExcited.png"
    
    image kat me excited u black = "kat/BUnderwear/MeExcited.png"
    image kat away excited u black = "kat/BUnderwear/AwayExcited.png"
    
    image kat me smile u black = "kat/BUnderwear/MeSmile.png"
    image kat away smile u black = "kat/BUnderwear/AwaySmile.png"
    
    image kat me normal u black = "kat/BUnderwear/MeNormal.png"
    image kat away normal u black = "kat/BUnderwear/AwayNormal.png"
    
    image kat me mad u black = "kat/BUnderwear/MeMad.png"
    image kat away mad u black = "kat/BUnderwear/AwayMad.png"
    
    image kat me angry u black = "kat/BUnderwear/MeAngry.png"
    image kat away angry u black = "kat/BUnderwear/AwayAngry.png"


    image kat me normal u color flip = im.Flip("kat/Underwear/MeNormal.png", horizontal=True)
    image kat away normal u color flip = im.Flip("kat/Underwear/AwayNormal.png", horizontal=True)

    image kat me smile u color flip = im.Flip("kat/Underwear/MeSmile.png", horizontal=True)
    image kat away smile u color flip = im.Flip("kat/Underwear/AwaySmile.png", horizontal=True)

    # ~~~~~~~~~~~images of Kat in normal clothes~~~~~~~~~~~~~~~~~
    image kat me normal n color = "kat/Normal/MeNormal.png"
    image kat away normal n color = "kat/Normal/AwayNormal.png"

    image kat me mad n color = "kat/Normal/MeMad.png"
    image kat away mad n color = "kat/Normal/AwayMad.png"
    
    image kat me angry n color = "kat/Normal/MeAngry.png"
    image kat away angry n color = "kat/Normal/AwayAngry.png"

    image kat me smile n color = "kat/Normal/MeSmile.png"
    image kat away smile n color = "kat/Normal/AwaySmile.png"
    
    image kat me excited n color = "kat/Normal/MeExcited.png"
    image kat away excited n color = "kat/Normal/AwayExcited.png"
    
    image kat me excited n black = "kat/BNormal/MeExcited.png"
    image kat away excited n black = "kat/BNormal/AwayExcited.png"
    
    image kat me normal n black = "kat/BNormal/MeNormal.png"
    image kat away normal n black = "kat/BNormal/AwayNormal.png"
    
    image kat me mad n black = "kat/BNormal/MeMad.png"
    image kat away mad n black = "kat/BNormal/AwayMad.png"
    
    image kat me angry n black = "kat/BNormal/MAngry.pnge"
    image kat away angry n black = "kat/BNormal/AwayAngry.png"
    
    image kat me smile n black = "kat/BNormal/MeSmile.png"
    image kat away smile n black = "kat/BNormal/AwaySmile.png"
    
    # ~~~~~~~~~~~~images of Kat in Dress~~~~~~~~~~~~~~~~~~~~~~~~~~~
    image kat angry me black d = "kat/BDress/MeAngry.png"
    
    image kat normal d black me = "kat/BDress/MeNormal.png"
    
    #~~~ images of Gale
    image gale smile = "GaleNSmile.png"
    image gale normal = "GaleNNormal.png"
    
    #~~~ images of Chris
    image chris smile = "chris/ChrisNSmile.png"
    image chris normal = "chris/ChrisNNormal.png"
    
    #~~~ images of Holly
    image holly me smile n = "holly/HollySmileMe.png"
    image holly away smile n = "holly/HollySmileAway.png"
    image holly me teeth n = "holly/HollyTeethMe.png"
    image holly away teeth n = "holly/HollyTeethAway.png"
    
    #~~~ images of Kitty
    image kitty me smile n = "kitty/KittyMeSmileN.png"
    image kitty away smile n = "kitty/KittyAwaySmileN.png"
    image kitty me normal n = "kitty/KittyMeNormalN.png"
    image kitty away normal n = "kitty/KittyAwayNormalN.png"
    image kitty me teeth n = "kitty/KittyMeAngryN.png"
    image kitty away teeth n = "kitty/KittyAwayAngryN.png"
    image kitty me angry n = "kitty/KittyMeMadN.png"
    image kitty away angry n = "kitty/KittyAwayMadN.png"
    image kitty me excited n = "kitty/KittyMeExitedN.png"
    image kitty away excited n = "kitty/KittyAwayExitedN.png"
    
    #~~~ images of Mary
    image mary me smile n = "mary/MaryMeSmileN.png"
    image mary away smile n = "mary/MaryAwaySmileN.png"
    image mary me normal n = "mary/MaryMeNormalN.png"
    image mary away normal n = "mary/MaryAwayNormalN.png"
    image mary me mad n = "mary/MaryMeMadN.png"
    image mary away mad n = "mary/MaryAwayMadN.png"
    image mary me excited n = "mary/MaryMeExcitedN.png"
    image mary away excited n = "mary/MaryAwayExcitedN.png"
    
    #~~~ images of Sherman
    image sherman smile = "sherman/ShermanSmile.png"
    image sherman normal = "sherman/ShermanNormal.png"
    
    #~~~images of Ling
    image ling me smile n = "ling/LingMeSmileN.png"
    image ling me normal n = "ling/LingMeNormalN.png"
    image ling me mad n = "ling/LingMeMadN.png"
    image ling me angry n = "ling/LingMeAngryN.png"
    
    image ling away smile n = "ling/LingAwaySmileN.png"
    image ling away normal n = "ling/LingAwayNormalN.png"
    image ling away mad n = "ling/LingAwayMadN.png"
    image ling away angry n = "ling/LingAwayAngryN.png"
    
    image ling away smile n flip = im.Flip("ling/LingAwaySmileN.png", horizontal=True)
    
# Define some transistions
define slideright = CropMove(0.3, "slideright")
define slideleft = CropMove(0.3, "slideleft")

define slideawayright = CropMove(0.3, "slideawayright")
define slideawayleft = CropMove(0.3, "slideawayleft")

define wiperight = CropMove(0.5, "wiperight")
define wipeleft = CropMove(0.5, "wipeleft")

# Declare characters used by this game.
define z = Character('Zen')
define k = Character(('Kat'), color = "#00EEEE", show_side_image=Image("kat/Kat_Side.png", xalign=0.0, yalign=1.0) )
define kb = Character(('Kat'), color = "#00EEEE", show_side_image=Image("kat/Katb_Side.png", xalign=0.0, yalign=1.0) )

define c = Character(('Chris'), color = "#EE0000", show_side_image=Image("chris/chris_side.png", xalign=0.0, yalign=1.0))
define h = Character(('Holly'), color = "#FFFF00", show_side_image=Image("holly/Holly_side.png", xalign=0.0, yalign=1.0))
define ki = Character(('Kitty'), color = "#800000", show_side_image=Image("kitty/Kitty_Side.png", xalign=0.0, yalign=1.0))
define m = Character(('Mary'), color = "#00FF7F", show_side_image=Image("Mary/Mary_side.png", xalign=0.0, yalign=1.0))
define l = Character(('Ling'), color = "#00FF00", show_side_image=Image("Ling/Ling_side.png", xalign=0.0, yalign=1.0))

define he = Character(('Henry'), color = "#3D9140")
define sh = Character(('Sherman'), color = "#3D9140", show_side_image=Image("sherman/Sherman_side.png", xalign=0.0, yalign=1.0))

define cab = Character('Cab Driver')
define pro = Character('Professor')
define bar = Character('Bartender')

transform hop():
    linear .2 yalign 1.2
    linear .2 yalign 1.0
    
transform hop2():
    linear .2 yalign 1.7
    linear .2 yalign 1.5
    

init:
    $day = 0
    $night = 0
    $kat_love = 0
    $kitty_story = 0
    $kitty_love = 0
    $holly_story = 0
    $holly_love = 0
    $eve_story = 0
    $eve_love = 0

# The game starts here.
label start:

    play music "CoolVibes.mp3"
    
    scene bg black
    with fade
    show expression Text(_("Sunday 9am"), size=30, yalign=0.5, xalign=0.5, drop_shadow=(2, 2)) as text
    $ renpy.pause (2, hard=True)
        
    scene bg blur
    with fade

    "Aauughh."

    "I am so hungover."
    
    "What...{w} happened last night?"
    
    "Where...{w} the fuck am I?"
    
    kb "Aauugghh!"
    
    "I can hear the hungover moans of a girl beside me"
    
    show kat away angry u black:
        right
    with dissolve
    
    kb "What...{w} The Fuck...{w} Did we do last night?"
    
    "I look around the room a little bit."
    
    "I can kinda see better now."
    
    "I find my wallet on my nightstand."
    
    "I open it."
    
    z "I have good reason to believe that nothing happened last night."
    
    show kat me mad black u
    with dissolve
    
    "The girl looks over to my wallet"
    
    "She sees my unopened condom packet."
    
    kb "Okay. But how can you be so sure?"
    
    z "Well, for starters..."
    
    scene bg room
    show kat me mad u black:
        right
    with dissolve
    
    z "We're on separate beds."
    
    show kat away normal u black
    with dissolve
    
    kb "Hmmm."
    
    show kat me normal u black
    with dissolve
    show kat away normal u black
    with dissolve
    
    "She seems to be regaining her sight."
    
    show kat away normal u black:
        hop()
        hop()
    
    "She starts patting herself around."
    
    "I think she's trying to see if she feels weird anywhere."
    
    "I think she realized for sure nothing happened."
    
    show kat me mad u black
    with dissolve
    
    kb "I don't really feel like analyzing anything right now."
    
    kb "I'm going back to sleep."
    
    show kat me normal u black
    with dissolve
    
    kb "Go ahead and just leave me here."
    
    kb "I can find my way home by myself."
    
    "She sounds pretty independent."
    
    "I like that."
    
    hide kat normal black away
    with dissolve
    
    "Well, I better look around and see what I can discover about last night."
    
    "If I know my friends, they probably blacked out drunk on top of each other somewhere."
    
    play sound "door.wav"
    
    show bg black
    with fade
    show expression Text(_("About an hour and a half later"), size=30, yalign=0.5, xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve
    $ renpy.pause (2, hard=True)
    hide text
    show bg room
    with fade
    $ renpy.pause (1, hard=True)
        
    show kat away angry u black:
        right
    with dissolve
    $ renpy.pause (1, hard=True)
    
    kb "Uugh."
    
    show kat me normal u black
    with dissolve
    show kat away normal u black
    with dissolve
    
    kb "Hmm."
    
    kb "So he left huh?"
    
    kb "Well, I did tell him to leave."
    
    show kat me normal u black
    with dissolve
    show kat away normal u black
    with dissolve
    
    show kat away normal u black:
        hop()
        
    kb "Hm? What's this?"

    show kat away normal u black:
        right
        linear .2 xalign 0.5
        
    kb "He left his wallet here."

    scene bg black
    with fade
    show expression Text(_("Flashback, few weeks ago."), size=30, yalign=0.5, xalign=0.5, drop_shadow=(2, 2)) as text
    $ renpy.pause (2, hard=True)
    hide text
    
    scene bg katcomp
    with fade
    
    show kat away normal u color flip
    with dissolve
    
    kb "C'mon internet, show me something interesting."
        
    show kat me normal u color flip:
    with dissolve
    show kat away normal u color flip:
    with dissolve
    show kat me normal u color flip:
    with dissolve

        
    show kat away smile u color flip:
        hop()
    with dissolve
        
    kb "Ooh. What's this?"
    
    "What Your Condom Says About Your Personality."
    
    show kat away smile u color flip:
        hop()
    
    kb "Sounds interesting. Good job internet."

    scene bg black
    with fade
    $ renpy.pause (2, hard=True)
    
    scene bg room
    with fade
    
    show kat away excited u black:
        center
        hop()
        hop()
    with dissolve
    
    kb "Heh heh heh"
    
    play sound "door.wav"
    
    "So I just got back from the convenience store."
    
    "Just to see this girl chuckling, probably about my choice in condoms."
    
    "I knew I shouldn't have left my wallet in here."
    
    "I just kinda wanted to leave something here to tell her that I didn't leave."
    
    "Of course, I took my money and cards with me, just in case."
    
    show kat me smile u black
    with dissolve
    
    show kat me smile u black:
        hop()
    
    kb "Oh hey."
    
    show kat me excited u black:
        hop()
        hop()
    kb "Heh heh heh."
    
    "I'm not sure if I'm regretting this."
    
    z "So uhh, I bought some food."
    
    kb "And you like blowjobs too."
    
    "That came out of nowhere."
    
    z "I'm going to cook hotdogs and eggs."
    
    kb "And you like getting your hotdog and eggs sucked."
    
    "I fell into that one."
    
    z "Did Chris tell you about that?"
    
    kb "Nope. Just a guess."
    
    "I'm confused."
    
    z "I'm going to start cooking."
    
    kb "Alright then."
    
    scene bg kitchen
    with wipeleft
    
    show kat me smile u black:
        xalign 2.0 yalign 1.0
        linear .5 xalign 0.5
        linear .5 yalign 1.5
    
    play sound "cooking.wav"
    
    z "So I found out some stuff about what happened last night."
    
    show kat me normal u black
    
    kb "Yeah"
    
    z "I've been looking for an apartment lately."
    
    z "When we got drunk last night, I got a call from an apartment guy."
    
    z "And he asked if I'd like to swing by to check out the apartment the next day."
    
    z "Us being drunk and looking for a place to hangout, we were like, 'Hell yeah! Let's go to the place now!'"
    
    kb "That seems plausible."
    
    z "The rest of the night, couldn't figure out."
    
    z "I was just able to figure out that part while looking at the messages on my phone."
    
    kb "So... why am I the only one here then?"
    
    z "Dunno. The others probably went somewhere else."
    
    kb "Where are we exactly anyway?"
    
    z "About 20 minutes away from my campus."
    
    z "Yours is is about 10 minutes away."
    
    show kat away normal u black
    with dissolve
    
    kb "Hmm..."
    
    kb "This is a pretty good place."
    
    show kat me smile u black
    with dissolve
    
    kb "I wish I could stay here with you."
    
    z "Why not?"
    
    "I said on reflex."
    
    show kat me normal u black
    with dissolve
    
    kb "Why not?"
    
    "We hit an awkward pause."
    
    "I barely even know this girl."
    
    "All I remember was that she was Gale's friend."
    
    "And we partied last night."
    
    "I kinda sorta remember not liking her."
    
    hide kat
    
    show bg club
    with wipeleft
    
    show kat angry me black d
    with dissolve
    
    show white behind kat
    with dissolve
    
    "She had this judging stare."
    
    "I could tell she didn't want to be there."
    
    "I didn't want to be there either."
    
    "She wore this skimpy dress."
    
    show kat angry black me d:
        linear .5 right
    
    show gale smile
    with dissolve
    
    "And I knew that Gale probably forced it on her."
    
    hide gale
    hide white
    
    hide kat
    
    show bg kitchen
    with wiperight
    
    show kat me normal u black:
        xalign 0.5 yalign 1.5
    with dissolve
    
    "Which raises plenty of questions."
    
    "Why is she wearing my shorts?"
    
    "That obviously isn't my tanktop, but she definitely wasn't wearing one last night."
    
    kb "You know,"
    
    show kat me smile u black
    
    kb "I think I'm going to like you."
    
    "And that just raises even more questions."
    
    z "What makes you think that?"
    
    play sound "serve.wav"
    
    "I ask her while serving breakfast."
    
    show kat away smile u black:
        hop2()
        hop2()
    
    kb "First of all, this breakfast is great."
    
    show kat me smile u black:
    
    z "Thank you."
    
    kb "You're good at figuring stuff out, something I'm pretty bad at."
    
    "I am studying Computer Science."
    
    "Analyzing code was my specialty."
    
    kb "And judging by your choice of condoms, you're probably a thoughtful and sensitive person."
    
    show kat me smile u black:
        hop2()
        hop2()
    
    kb "Heh heh."
    
    z "You got that from a fruit-flavored condom?"
    
    show kat me smile u black:
        hop2()
        hop2()
    
    kb "Heh heh. Hyeah."
    
    z "Totally ignoring the fact that I left my wallet here to ensure you that I'm coming back."
    
    show kat me normal u black
    
    kb "Well yeah. Okay. There's that too."
    
    z "Can you recall anything from last night?"
    
    kb "If I did I would tell you anything I know."
    
    z "You wanna call Chris and Gale?"
    
    kb "Not really."
    
    z "Why not? Who knows what sort of crazy shit we did last night."
    
    kb "I'm enjoying spending time with you right now."
    
    kb "I kinda feel like that's gonna end if we call them."
    
    "O-kay. Wow."
    
    z "You're being dramatic."
    
    z "You're friends with Gale. She'll probably drag you along to another party."
    
    kb "Not likely."
    
    kb "I don't know Gale that much."
    
    kb "I just kinda live across the hall from her."
    
    kb "She probably asked me to come along cuz I wouldn't judge her for getting back with Chris."
    
    z "Really?"
    
    kb "Yeah."
    
    z "Then we're on the same boat."
    
    kb "Hm?"
    
    z "Well, Chris is my best friend. {p}But I'm really not the type of guy who goes to parties a lot."
    
    kb "You seem like one."
    
    z "That's just because Chris gussied me up."
    
    z "He even made me cut my hair and dye it brown just for last night."
    
    z "He said,{p}if you want to get a girl with colored hair, you should color your hair as well."
    
    kb "You like girls who color their hair?"
    
    z "Weird fetish. Yeah."
    
    show kat smile
    with dissolve
    
    kb "I really think I'm going to like you Zen."
    
    z "Thank you. I guess."
    
    kb "It's been one crazy night."
    
    kb "For some reason, I'm wearing your shorts. And I don't think you're a pervert despite it."
    
    "She knew?!"
    
    kb "Promise me this."
    
    "I'm not obligated to promise you anything."
    
    z "Yeah?"
    
    show kat normal
    with dissolve
    
    kb "Try not figure out what happened last night."
    
    kb "I'm pretty sure we did something stupid and we didn't even sleep together."
    
    "Well, technically we did."
    
    kb "If we learn the details of last night, it's going to be weird."
    
    show kat smile
    with dissolve
    
    kb "The fact that I'm here with you alone means that Drunk Kat found something special in you."
    
    kb "The important part is we had fun and I made a new friend."
    
    "Weirdo"
    
    z "T-thanks. I guess."
    
    kb "You probably want to live alone, or with Chris."
    
    kb "So I won't try insist to live here."
    
    kb "But if you're looking for a roomate, I would love that."
    
    z "Uhh, okay then."
    
    stop music fadeout 1
    
    hide kat
    with dissolve
    
    show bg black
    with fade
    
    
    
    show expression Text(_("30 minutes later."), size=30, yalign=0.5, xalign=0.5, drop_shadow=(2, 2)) as text
    $ renpy.pause(2, hard=True)
    hide text
    
    scene bg taxi
    with fade
    
    show kat smile me black n:
        xalign 1.0 yalign 1.5
    with dissolve
    
    play music "LongStroll.mp3"
    
    kb "See ya."
    
    z "Aight."
    
    show kat smile me black n:
        linear .2 xalign 2.0
    
    "So I just dropped off Kat to her dorm here at Beach Uni."
    
    "She's a fun girl, definitely weird."
    
    "I'm kinda sorta into that."
    
    "But there's just something about her that's kinda...{w} off."
    
    "She told me not to figure out what happened last night."
    
    "Could she have remembered something about last night?"
    
    "If so, then she lied to me."
    
    "Hmm..."
    
    "Probably not."
    
    "She told me not to analyze what happened last night."
    
    "But it's kinda hard not to."
    
    "That is, after all, my specialty."
    
    "Something that will help me in the future."
    
    cab "Where to kid?"
    
    z "Lake Uni, Lakeside Dorm."
    
    "Gale and Kat study here at Beach Uni."
    
    "Chris and I study at Lake Uni."
    
    "There's two towns in the area."
    
    "Lakeside and Beachside."
    
    "They built these two universities at the town border."
    
    "Well, it's not much of a border."
    
    "Just a back-to-back sign that says...{p}\'Welcome to Lakeside Town\' and{p}\'Welcome to Beachside Town\'"
    
    "It's pretty cool to have two universities next to each other."
    
    "You meet more people."
    
    "They have sort of a rivalry going on."
    
    "But they're essentially sister schools."
    
    "Something about the Mayors' daughters being best friends."
    
    "That's how the story goes anyway."
    
    "Lakeside is known for the Great Lake."
    
    "Beachside is known for, well, having a beach."
    
    "It's cold this time of year, so people visit the Lake more."
    
    "I however prefer going to the beach during the cold season."
    
    "And the cool water of the Great Lake is perfect for the hot season."
    
    "It's something about balance."
    
    "Well, to me anyway."
    
    "And it's not like I ever visit those places frequently."
    
    "I enjoy moments like this when I can be alone with my thoughts."
    
    "You could say that I'm kind of an introverted person."
    
    "But if an introvert frequents going to the bar and making conversation{w} then I'm not sure what to call myself."
    
    "Guess you can say I'm kinda weird."
    
    "I can only distract myself from last night's events for so long."
    
    play sound "ring.wav"
    
    "Hmm...?"
    
    "It's a call from Chris."
    
    "I better pick this up."
    
    play sound "beep.wav"
    
    c "Hey man!"
    
    z "Hey dude. Where are you?"
    
    c "I'm at the apartment with Gale."
    
    z "What apartment?"
    
    stop music
    
    c "The apartment here at Lakeside."
    
    play music "Rollinat5.mp3"
    
    z "Wait what?"
    
    c "Yeah, I can't find you anywhere."
    
    c "Is Kat there with you?"
    
    z "I just dropped her off at Beachside Uni."
    
    c "Nice."
    
    z "Wait no, nothing happened."
    
    c "What?"
    
    z "Wait wait, shut up for a second."
    
    z "What do you mean you're at Lakeside?"
    
    c "I mean we were drunk last night, and we were looking for a place to crash."
    
    z "Okay."
    
    c "Your apartment guy called you up and asked if you wanted to see the apartment here."
    
    z "But, I woke up at an apartment in Beachside."
    
    c "What the hell are you doing in Beachside?"
    
    z "I don't know! I'm only realizing it now!"
    
    z "Do you remember anything?"
    
    c "Just that part,{w} and a some more fun parts at the end."
    
    "This doesn't add up."
    
    "Why did I wake up at an apartment in Beachside?"
    
    c "Dude, you okay?"
    
    z "Yeah,{w} yeah,{w} I'll be fine."
    
    c "So, uhh, I'll text you the address."
    
    z "Yeah, sounds good."
    
    c "Alright, see ya here."
    
    z "Kay."
    
    play sound "beep.wav"
    
    "Okay, let's try to recall the events of last night."
    
    "Chris and Gale are having one of their on again off again dates...{w} which mostly takes place in clubs."
    
    "Chris invited me,{w} and Gale invited her friend, Kat."
    
    "Kat said she wasn't really close with Gale."
    
    "Gale is a pretty friendly girl, so maybe she thinks differently about her."
    
    "Otherwise Gale wouldn't invite Kat."
    
    "But Kat did say that Gale invited her so that she wouldn't be judged while we're out there."
    
    scene bg club
    with wipeleft
    
    show gale smile at left
    
    show chris smile:
        xalign 1.2 yalign 1.0
    
    show kat normal d black me
    with dissolve
    
    "We got in the club Saturday night 9pm."
    
    show kat angry me black d
    with dissolve
    
    "Kat was stressed out."
    
    play sound "beer.wav"
    
    "And I guess after that is when the drinking started."
    
    show white
    with dissolve
    
    "And this is where everything started to get hazy"
    
    play sound "ring.wav"
    
    "At some point I was called by my apartment guy."
    
    "He asked if we'd like to swing by the apartment."
    
    "I'm guessing we needed a place to crash."
    
    "Chris said the apartment we were asked to check out was at Lakeside."
    
    scene bg room
    with wipeleft
    
    show kat me normal u black
    with dissolve
    
    "But I woke up with Kat at an apartment in Beachside."
    
    
    "Uugh."
    
    
    scene bg taxi
    with wiperight
    
    "Okay. This is starting to hurt my head a little bit."
    
    "Wait."
    
    "I could solve a lot of questions by calling the apartment guy."
    
    stop music fadeout 0.5
    
    "His number is in my log."
    
    "..."
    
    show expression Text(_("Try not figure out what happened last night."), size=25, yalign=0.5, xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve
    $ renpy.pause (2, hard=True)
    hide text
    with dissolve
    
    "..."
    
    play music "LongStroll.mp3" fadeout 1
    
    "You know what."
    
    "I analyze everything all the time."
    
    "I should just chill."
    
    "I woke up next to a cute girl today."
    
    "We enjoyed time together this morning."
    
    "We became friends."
    
    "Kat was right."
    
    "Whatever happened last night isn't important."
    
    "What matters is what happened now."
    
    "Instead of calling the apartment guy, I'm calling Kat."
    
    play sound "beep.wav"
    
    "She gave me her number a while ago."
    
    play sound "call.wav"
    
    $renpy.pause(5, hard=True)
    
    kb "Aauugghh!{w} Who the fuck is this?!{w} Some people are trying to FUCKING SLEEP!"
    
    "Aah! My ear!"
    
    "It's like she's shouting through a megaphone."
    
    z "uuh..."
    
    "I lower my voice"
    
    z "hey...{w} this is zen..."
    
    kb "Oh,{w} hey Zen, sup?"
    
    "Suddenly, a mood change appears."
    
    z "uhh..."
    
    kb "Sorry about that, I get really cranky when I try to sleep."
    
    kb "Don't feel bad about it."
    
    z "O-kay."
    
    kb "You know, normally, guys wait 3 days before they call a girl they just met, not 3 minutes."
    
    "She's kinda talkative on the phone."
    
    "She starts yawning."
    
    kb "You have yet to say anything you know."
    
    kb "Did you just call to give me your number?"
    
    z "Uh... sorry... yeah..."
    
    kb "Alright then."
    
    kb "Look, I really want to go back to sleep."
    
    kb "I'm guessing you're still frozen from when I yelled at you."
    
    kb "So I'll hang up now."
    
    play sound "beep.wav"
    
    "Well... that went well."
    
    play sound "brake.wav"
    
    "God, I am so stupid."
    
    cab "Here we are kid."
    
    z "Oh hey thanks."
    
    "I'll just text Chris that I'm not going there."
    
    "Besides, I like the apartment I just woke up in."
    
    "Two beds for hookups, a desk for my computer, enough space for a small flatscreen."
    
    "Shower bathroom. And the place comes with it's own stove."
    
    "I can afford that."
    
    "Taxi doesn't cost much to get to school."
    
    "It was a great find."
    
    scene bg black
    with fade
    
    $ renpy.pause (1, hard=True)
    
    scene bg lakecamp
    with fade
    
    "Welcome To Lakeside Dormitory"
    
    "That's what's written on the entrance."
    
    "Lakeside is pretty okay."
    
    "I'm not really in on the buzz at school but, from what I know, Lakeside has more intelligent people than Beachside."
    
    "On the other hand, Beachside has more fun people."
    
    "More sports, more events, more parties."
    
    "Us Lakesiders however are more, well, artsy."
    
    "We offer more food for the mind, better and more practical teaching methods, higher passing rates, shaping the leaders of tomorrow."
    
    "Future Doctors, Artisans, and Scientists study here."

    "It's a little hard to understand."
    
    "But these details aren't very important."
    
    "It's just the constant monologue I have in my head."
    
    "Analyzing stuff is my specialty."
    
    "Welp, here I am."
    
    play sound "door.wav"
    
    scene bg black
    with fade
    
    $ renpy.pause(1,hard=True)
    
    scene bg dorm
    with fade
    
    "And here's my dorm."
    
    "I don't have a lot of things to pack up."
    
    "I pretty much came for my laptop and a few clothes."
    
    "I've done the paperwork ahead of time already."
    
    "Good for you Zen. Good for you."
    
    "Ugh."
    
    "The place stinks of man."
    
    "While it's partially my fault, most of the blame has to be with Chris."
    
    "Lord knows how many girls he's taken here."
    
    "And lord knows how many times I've had to spend outside my dorm just to let them have their fun."
    
    "So Kat was kinda wrong about me wanting to be roommates with Chris again."
    
    play sound "door.wav"
    
    show chris smile
    with dissolve
    
    c "Hey!"
    
    "Speak of the devil."
    
    z "Yo."
    
    c "You're really moving out huh."
    
    z "Yup."
    
    "Mostly because I hardly live here given your history with women."
    
    "You're probably wondering what a douche like Chris is doing in Lakeside instead of Beachside."
    
    "Well, it's because he can be serious about his future."
    
    "He does study diligently,{w} but he never fails to make time for having fun."
    
    "I guess that's why we're best friends."
    
    z "Sorry man, but we just can't live together."
    
    show chris normal
    
    c "I understand bro."
    
    c "I'm gonna miss you."
    
    z "And I wish I could say the same to you."
    
    z "We'll both be happier this way."
    
    show chris smile
    
    c "We'll still see each other right?"
    
    z "Of course we will. We have a few same classes."
    
    "Our conversations tend to be a little gay through tough times."
    
    c "You promise?"
    
    z "Okay man, I'm not playing anymore."
    
    show chris normal
    
    c "Do you have to be like that."
    
    z "I do enjoy our bromantic conversations but, not right now man."
    
    show chris smile
    
    c "That's fine."
    
    show chris normal
    
    c "Real talk."
    
    c "So why don't you want to know more about the details of last night."
    
    z "I decided that it was too confusing to think about."
    
    show chris smile
    
    c "That's hardly like you."
    
    z "I know."
    
    c "Did Kat seduce you into her spell?"
    
    z "I dunno what you're talking about."
    
    c "We should all go out again."
    
    "..."
    
    "I start to smile a stupid grin."
    
    z "Yeah. Sure."
    
    c "Hmm."
    
    c "So. Do you like her?"
    
    z "Huh?"
    
    menu:
        c "Kat. Do you like her?"
    
        "Yeah. Sure.":
            $ kat_love += 1
            z "Yeah. Sure."
            z "She's quirky, weird. Independent and attached at the same time."
            z "I kinda like that."
            c "That's cool."
        
        "Nahh.":
            z "Naah."
            z "She's an interesting person."
            z "But she's not in like, 'my scope'."
            z "You could say she's a fun friend."
            c "I see."
        
    
    c "Anyway, I'll see what I can do."
    
    show chris normal
    
    c "Hey, you do remember that you were with us right?"
    
    z "What do you mean?"
    
    c "You and Kat were with us in Lakeside."
    
    c "As far as I can remember."
    
    z "Huh?"
    
    z "That hardly makes any sense."
    
    c "I'm positive you were with us last night."
    
    c "You even drunkenly said something about bed rules."
    
    z "I did?"
    
    "That sounds like something I would say if I was drunk."
    
    c "Dunno where you two disappeared to."
    
    z "Well, thanks for the info. But I'm trying my best not to think about it."
    
    show chris smile
    
    c "Suit yourself."
    
    z "Anyway, I'm gonna go try and get cozy at my new place."
    
    z "You wanna come with?"
    
    c "I would love to, but I got a thing."
    
    z "Well, I'm done here."
    
    z "Guess I'll be seeing you tomorrow."
    
    c "Take care man."
    
    z "See ya."
    
    play sound "door.wav"
    
    scene bg lakecamp
    with dissolve
    
    "Goodbye Lakeside Dorm!"
    
    "Thanks for giving me a temporary place to live."
    
    "But apparently my best friend just happens to be someone who is unliveable with."
    
    scene bg taxi
    with dissolve
    
    "I wonder what it's like to live with Kat?"
    
    if kat_love > 0:
        "It would be a little awkard."
    
    "She does seem like a fun girl."
    
    "I guess I'm a little reluctant about living with her because I don't know her enough yet."
    
    "I'll try to get to know her this semester."
    
    $renpy.pause(0.5, hard=True)
    
    scene bg room
    with dissolve
    
    $renpy.pause(0.5, hard=True)
    
    "Welp. Here I am."
    
    "You know, you'd think a move like this would take longer."
    
    "But this place is just 20 minutes away."
    
    "That's like what? An episode of a sitcom."
    
    "I should watch an episode of a sitcom on my way to class."
    
    "Guess I should set up my computer."
    
    show bg zencomp
    with wipeleft

    "Fits perfectly."
    
    "I don't know about other people, but I prefer smaller spaces."
    
    "I don't like it cramped of course."
    
    "But I like places where there's just enough space to move around."
    
    "Well, class starts again tomorrow."
    
    "I should probably do something over the semester."
    
    "There are plenty of fun things to do."
    
    "Of course, these can be sorta tedious."
    
    "But I do feel compelled to do something aside school over the semester."
    
    "It's been a while since I've played the piano."
    
    "There are song lyrics I've written down I haven't played."
    
    "Maybe I should spend some time on that."
    
    "But man..."
    
    "I'm out of shape."
    
    "That's no surprise, I do spend a lot of time in front of the computer."
    
    "It would be a very healthy decision to get some exercise."
    
    "The gym at Beachside Uni has pretty good equipment."
    
    "But you know what."
    
    "Nothing beats extra time staying at home."
    
    "I actually do have a guy to call whenever I need to 'unwind.'"
    
    "I have a new apartment, there's plenty of windows."
    
    "This place is perfect to have a few 'sessions.'"
    
    "Security doesn't seem too tight."
    
    "This IS Beachside."
    
    "I might as well have some of my own fun."
    
    jump choice
    
    jump alpha

    return
