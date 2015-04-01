label choice:

    stop music fadeout 1

    scene bg zencomp
    with fade

    menu:

        "What activity shall I pursue?"
    
        "Pursue music":
            $eve_story += 1
        
            if eve_story==1:
                call alpha
        
            if eve_story==2:
                call alpha
        
            if eve_story==3:
                call alpha
        
        "Get in shape":
            $kitty_story += 1
        
            if kitty_story==1:
                call kitty1
        
            if kitty_story==2:
                call alpha
        
            if kitty_story==3:
                call alpha
        
        "Just 'Relax'":
            $holly_story += 1
        
            if holly_story==1:
                call holly1
        
            if holly_story==2:
                call alpha
        
            if holly_story==3:
                call alpha
        
        "Skip to Kat's Chapter 3":
            call kat3