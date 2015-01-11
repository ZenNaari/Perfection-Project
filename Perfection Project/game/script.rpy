# You can place the script of your game in this file.

#colors
#4876FF - royalblue
#27408B - dark royal blue
#00FF7F - spring green
#4EEE94 - sea green
#00EEEE - cyan

image bg room = "room.jpg"
image bg blur = "blurryroom.jpg"

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image kat normal color me = "KatUNormal.png"
image kat normal color away = "KatUNormal2.png"
image kat normal black me = "KatUNormal3.png"
image kat normal black away = "KatUNormal4.png"

image kat angry color me = "KatUAngry.png"
image kat angry color away = "KatUAngry2.png"
image kat angry black me = "KatUAngry3.png"
image kat angry black away = "KatUAngry4.png"
image kat angry color me teeth = "KatUAngry5.png"
image kat angry color away teeth = "KatUAngry6.png"
image kat angry black me teeth = "KatUAngry7.png"
image kat angry black away teeth = "KatUAngry8.png"

image kat smile color me = "KatUSmile.png"
image kat smile color away = "KatUSmile2.png"
image kat smile black me = "KatUSmile3.png"
image kat smile black away = "KatUSmile4.png"

# Declare characters used by this game.
define z = Character('Zen')
define k = Character(_('Kat'), color = "#00EEEE" )


# The game starts here.
label start:
    
    scene bg blur
    with dissolve

    "Aauughh."

    "I am so hungover."
    
    "What happened last night?"
    
    "I can hardly make out my surroundings."
    
    k "\"Aauugghh!\""
    
    "I can hear the hungover moans of a girl beside me"
    
    show kat angry black away teeth:
        right
    with dissolve
    
    k "\"What. The Fuck. Did we do last night?\""
    
    "I look around the room a little bit."
    
    "I can kinda see better now."
    
    "I find my wallet on my nightstand."
    
    "I open it."
    
    z "\"I have good reason to believe that nothing happened last night.\""
    
    show kat angry black me:
        right
    with dissolve
    
    "The girl looks over to my wallet"
    
    "She sees my unopened condom packet."
    
    k "\"Okay. But how can you be so sure?\""
    
    z "\"Well, for starters...\""
    
    scene bg room
    show kat angry black away:
        right
    with dissolve
    
    z "\"We're sleeping in separate beds.\""
    
    show kat normal black away:
        right
    with dissolve
    
    k "\"Hmmm.\""
    
    show kat normal black me:
        right
    with dissolve
    show kat normal black away:
        right
    with dissolve
    show kat normal black me:
        right
    with dissolve
    show kat normal black away:
        right
    with dissolve
    
    "She seems to be regaining her sight."
    
    show kat normal black away:
        right
        yalign 1.0
        linear .2 yalign 1.2
        linear .2 yalign 1.0
        linear .2 yalign 1.2
        linear .2 yalign 1.0


    
    "She starts patting herself around."
    
    "I think she's trying to see if she feels weird anywhere."
    
    "I think she realized for sure nothing happened."
    
    show kat angry black me
    with dissolve
    
    k "\"I don't really feel like analyzing anything right now.\""
    
    k "\"I'm going back to sleep.\""
    
    show kat normal black me
    with dissolve
    
    k "\"Go ahead and just leave me here.\""
    
    k "\"I can find my way home by myself.\""
    
    "She said in a pretty nonchalant way."
    
    "She sounds pretty independent."
    
    hide kat normal black me
    

    return
