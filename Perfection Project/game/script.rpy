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

image kat normal = "KatUNormal.png"
image kat normal2 = "KatUNormal2.png"
image kat normal3 = "KatUNormal3.png"
image kat normal4 = "KatUNormal4.png"

image kat angry = "KatUAngry.png"
image kat angry2 = "KatUAngry2.png"
image kat angry3 = "KatUAngry3.png"
image kat angry4 = "KatUAngry4.png"
image kat angry5 = "KatUAngry5.png"
image kat angry6 = "KatUAngry6.png"
image kat angry7 = "KatUAngry7.png"
image kat angry8 = "KatUAngry8.png"

image kat smilel = "KatUSmile.png"
image kat smile2 = "KatUSmile2.png"
image kat smile3 = "KatUSmile3.png"
image kat smile4 = "KatUSmile4.png"

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
    
    show kat angry8
    with dissolve
    
    k "\"What. The Fuck. Did we do last night?\""
    
    "I look around the room a little bit."
    
    "I can kinda see better now."
    
    "I find my wallet on my nightstand."
    
    "I open it."
    
    z "\"I have good reason to believe that nothing happened last night.\""
    
    show kat angry3
    
    "The girl looks over to my wallet"
    
    "She sees my unopened condom packet."
    
    k "\"Okay. But how can you be so sure?\""
    
    z "\"Well, for starters...\""
    
    scene bg room
    show kat angry3
    with dissolve
    
    z "\"We're sleeping in separate beds.\""
    
    show kat normal4
    with dissolve
    
    k "\"Hmmm.\""
    

    return
