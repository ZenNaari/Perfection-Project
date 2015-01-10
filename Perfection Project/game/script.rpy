# You can place the script of your game in this file.

#colors
#4876FF - royalblue
#27408B - dark royal blue
#00FF7F - spring green
#4EEE94 - sea green
#00EEEE - cyan

image bg room = "room.jpg"

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image kat normal = "KatUNormal.png"

# Declare characters used by this game.
define z = Character('Zen')
define k = Character(_('Kat'), color = "#00EEEE" )


# The game starts here.
label start:
    
    scene bg room
    
    show kat normal
    with dissolve

    k "You've created a new Ren'Py game."

    k "Once you add a story, pictures, and music, you can release it to the world!"

    return
