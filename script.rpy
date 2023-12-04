# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define gordon = Character("Gordon Hobbs")
define n = Character("Voice")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    n "April 12th, 1926, 8:15pm. The Beacon Island lighthouse off the shore of Folly Point, Massachusetts, ceased to cast its light over the region’s dangerous rocky waters about 15 minutes ago."

    n "As a result, the SS Essex County, a mixed passenger and cargo vessel on which you are all traveling to Rockport, has foundered on the rocks and incurred considerable damage to its hull. The ship is sinking, and the crew hurries you toward one of the many small rowboats acting as the ship’s lifeboats."

    # This ends the game.

    return
