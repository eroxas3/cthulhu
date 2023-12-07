# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define gordon = Character("Gordon Hobbs")
define n = Character("Voice")
define sailor = Character("Captain of the SS Essex County")
define monster = Character("Unknown Creature")

# Set Gordon Hobb's skill levels

$ spot_hidden = 65
$ first_aid = 30
$ medicine = 35
$ fighting_brawl = 55
$ listen = 20
$ mech_repair = 50
$ stealth = 50
$ swim = 60
$ dodge = 40
$ elec_repair = 50
$ firearms_handgun = 50
$ hit_points = 12
$ sanity = 65
$ pilot_boat = 74
$ zoology = 38
$ int = 65
$ str = 85
$ dex = 75
$ pow = 65
$ painting = 21

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene stormy sea


    # These display lines of dialogue.

    gordon "I am a Special Agent for the Bureau of Investigation. My current assignment in this godforsaken hell hole is keeping an eye out for any illegal activity conducted along the popular east coast shipping routes."
    gordon "So far, there's not been much to report, with the exception of one unmarked vessel spotted passing Rockport during a storm in early February, which seems to have vanished without a trace."
    gordon "A fellow undercover agent and friend, Michael Turner, has been stationed up on Beacon Island under the name Michael Turner. What better place to keep an eye on passing ships than from a lighthouse?"
    gordon "He got a message to me that he'd uncovered some sort of evidence of smuggling, but he didn't go into any details. He also asked to meet me in Rockport tomorrow morning, so here I am, on a late boat heading for our rendesvous."
    gordon "I really hope he's found something that would signal an end to my time here. This whole region gives me the creeps. Maybe it's just my imagination; maybe I've just been involved intoo many weird cases in the past."
    gordon "Ah, it's probably nothing. But if it is, why do I always get the feeling I'm being watched whenever I'm on the water?"


    n "April 12th, 1926, 8:15pm. The Beacon Island lighthouse off the shore of Folly Point, Massachusetts, ceased to cast its light over the region’s dangerous rocky waters about 15 minutes ago."
    n "As a result, the SS Essex County, a mixed passenger and cargo vessel on which you are traveling to Rockport, has foundered on the rocks and incurred considerable damage to its hull. The ship is sinking, and the crew hurries you toward one of the many small rowboats acting as the ship’s lifeboats."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show sailor

    sailor "Your best bet is to aim for Beacon Island."
    sailor "I doubt you'll make the mainland as a storm is brewing. You should have just enough time to reach the island before it hits."

    #hide sailor

    n "Then, without another word, they shove you off into the dark, churning waters. All you hve to guide you is the small light shining at the base of the lighthouse's towering silhoutte."

    n "As you brave the roaring waters, your rowboat hits something hard in the dark waters. Twisted metal has become lodged on a nearby sandbank, while yet more lurks just below the surface."
    n "Can you find out any information about this? Please roll for Spot Hidden."

    # Displays the dice roll results

    $ roll_result = renpy.random.randint(1,100)
    $ damage_result = renpy.random.randint(1,3)
    $ roll_result6 = renpy.random.randint(1,6)

    if roll_result <= 65:
        jump success_scene1
    else:
        jump failure_scene1

    label success_scene1:
        n "Success! You see that there are no identifying marks on the metal, and judging by the relatively small number of barnacles and lack of deterioration, it obviously hasn't been here for very long."
        n "You also realize that the metal may be part of a ship, although you can't recall hearing of a wreck around here for quite some time. Strange."
        jump second_scene

    label failure_scene1:
        n "Failure! Due to the intensity of the waves and your overall shakiness, you fail to obtain any information from the metal."
        jump second_scene

    label second_scene:
        n "Can you get yourself out of the wreckage? Please roll for Pilot Boat."
    if roll_result <= 74:
        jump success_scene2
    else:
        jump failure_scene2

    label success_scene2:
        n "Success! You manage to dislodge the rowboat from the wreckage without crashing into nearby rocks. You arrive at the island safely."
        jump sthird_scene

    label failure_scene2:
        n "Failure! You try to force the rowboat out of the wreckage, but you end up damaging the boat. You fall off. Roll for Swim as you now have to swim to the island."
    if roll_result <= 60:
        jump sthird_scene
    else:
        jump fthird_scene

    label sthird_scene:
        n "You get to the island quicker and stop on the small pier and dock."
        n "As you arrive, you hear a faint churning of machinery nearby."
        jump fourth_scene

    label fthird_scene:
        n "You are able to get yourself out from under the water. However, the intensity of the waves has knocked the wind out of you. Roll 1D3 for damage."
     #damage_result
        n "You wash up on the island on the sandbank near the dock. As you arrive, you hear a faint churning of machinery nearby."
        jump fourth_scene

    label fourth_scene:
        n "What is that sound? Roll for Mechanical or Electrical Repair."
    if roll_result <= 50:
        jump sfifth_scene
    else:
        jump fifth_scene

    label sfifth_scene:
        n "You are able to pick up that the sound suggests an electric generator nearby."
        n "You see a path going south. As you walk through the path, you can't help but feel like you are being watched."
        jump sixth_scene

    label fifth_scene:
        n "It doesn't sound like anything to you."
        n "You see a path going south. As you walk through the path, you can't help but feel like you are being watched."
        jump sixth_scene

    label sixth_scene:
        n "You come across the lighthouse cottage entrance, with its front door slightly ajar, and a steady glow can be seen coming from within. The path continues around to the back of the lighthouse."
        n "As you inspect the entrance, you see small, muddy, animal-like footprints in the front of the main cottage door. Beneath these are distinct boot prints."
        n "Does this species seem familiar to you? Roll Zoology."
    if roll_result <= 38:
        n "Success! You took a few zoology classes in the Academy, and you recognize the small footprints as duck-like in nature. However, there is something unusual about these footprints, as if they may be from an as yet unidentified species."
        jump seventh_scene
    else:
        n "They simply look animal-like to you. You don't know more information about the footprints."
        jump seventh_scene

    label seventh_scene:
    n "The ocean grows rougher as the storm the sailors warned you about begins to roll through. Rain begins to patter down from the sky. You notice that the footprints are slowly disappearing, as the rain is making tracking impossible."
    n "You see that the animal-like footprints came along the path from the direction of the thicket; boot prints lead from the cottage's front into the trees. As they are underneath, the booth prints must have been made first."
    n "Do you want to follow the footprints?"
    menu:
        "Yes, I do.":
            jump choice1_yes
        "No, I don't.":
            jump choice1_no

    label choice1_no:
        n "Where do you want to go next?"
    menu:
        "Cottage.":
            jump choice_cottage
        "Further south.":
            jump choice_south
        "Sheds.":
            jump choice_sheds

    label choice1_yes:
        n "As you walk through the thicket, the feeling of being watched is further intensified. You catch your breath. As a federal agent, situations like this should not phase you."
        n "Eventually, you stumble across a hideously mangled body - that of Michael Turner. It is a bloody mess; his innards have been dragged from his body, slashed, and trampled into the dirt. Besides the corpse lies a shattered lantern. It is evident he died recently."
        n "This is your friend. You lose [roll_result6] sanity."
    if roll_result6 > 5:
        n "You are in pieces. You suffer a temporary sanity break as you mourn your friend who's been violently murdered. All you want is to leave this place."
        gordon "I can't take this anymore. This place. You people. I'm going, and there's nothing you can do to stop me!"
        gordon "Who is that?"
        #*gunshot*
        n "Game over. Restart."
        return

    else:
        n "Although you feel deep sadness for your friend's death, your experiences in the field has desensitized you to death. You dust yourself off and swear that you will avenge your fellow agent."
        jump thicket_scene1

    label thicket_scene1:
        n "See if you can find out any information from his body. Roll for Medicine."
    if roll_result <= 35:
        n "Success! Your basic medicine training in the Academy allowed you to infer that Turner was probably torn apart by some kind of animal, as there are odd teeth and claw marks on the body. He also appears to have died very recently; within the last hour, in fact."
    else:
        n "Failure! Although you are proficient in medicine, you are too shaken to be able to conduct an accurate autopsy."
        jump thicket_scene2
    if roll_result >= 7:
        n "Extreme success! You, by some miracle, find small needles embedded deep into his skin. It appears to be some sort of animal spine, and are quite probably poisonous. Your training has allowed you to identify possible poisonous weapons that can be used against you."

    label thicket_scene2:
        n "On his body is an empty concealed holster and a Bureau of Investigation badge. A six-bullet revolver lies tangled in his innards, with its chamber only having five live bullets remaining along with one empty shell casing."
        n "Whatever attacked Turner, he only had the chance to get off one round before it dropped him."
        n "You have two choices: Go and explore further south or return to the path."
    menu:
        "Explore further south.":
            jump choice_south
        "Return to the path.":
            jump choice_path

    label choice_south:
        n "You continue along the well-trodden path south through the forest and find another worn-out pier. Tied to it is a yellow-painted rowboat. The lights of a small town can be seen in the distance, and some of Rockport's famous granite quarries can be spotted to the south-west."
        n "There is no way out of this island as long as the storm is raging on. You are stuck here."
        jump choice_path

    label choice_path:
        n "As you make your way out of the thicket, you return to the footpath you followed upon arriving on the island."
        n "The footpath soon branches. One leads back to the cottage and the other leads to two sheds - a smaller shed where you can hear the same churning of machinery earlier and a larger one."
        n "Go back to the cottage or explore the sheds?"
    menu:
        "Go back to the cottage.":
            jump choice_cottage
        "Explore the sheds.":
            n "Which shed do you want to check out first?"
            jump choice_sheds

    label choice_sheds:

    menu:
        "Smaller shed.":
            jump choice_workshop
        "Larger shed.":
            jump choice_generator1

    label choice_generator1:
        n "You open the door to the shed. You can see that it contains a running electric generator containing gas and firewood."
        n "You also notice that there is a leak in the generator shed's roof. Raindrops spatter through it onto the electrical equipment below."
        n "You do not have the necessary materials to repair the roof. Maybe you should check the other shed?"
        jump choice_sheds2

    label choice_sheds2:

    menu:
        "Smaller shed.":
            jump choice_workshop2
        "Larger shed.":
            jump choice_generator2

    label choice_workshop:
        n "You open the door to the shed. This shed looks obviously like a workshop. There's mechanical parts, a workbench, all that."
        n "There is a hammer, along with nails and corrugated iron sheets, as well as numerous scredrivers and chisels."
        n "Do you want to grab these?"
    menu:
        "Yes.":
            jump choice_yes2
        "No.":
            jump choice_no2

    label choice_workshop2:
        n "You open the door to the shed. This shed looks obviously like a workshop. There's mechanical parts, a workbench, all that."
        n "Most importantly, there is also a hammer, along with nails and corrugated iron sheets that can be used to fix the generator."
        n "Do you want to grab these?"
        menu:
            "Yes.":
                jump choice_generator2

    label choice_generator2:
        n "You have the necessary tools to fix the generator. However, do you even know how to fix generators? (Hard Mechanical Repair to succeed)"
        jump choice_generator4

    label choice_generator4:
    if roll_result <= 25:
        n "Success! You are able to fix the generator! Mr. Handyman!"
        jump choice_cottage
    else:
        n "You failed. Might as well go to the cottage, the rain is only getting worse."
        jump choice_cottage

    label choice_sheds3:
    menu:
        "Smaller shed.":
            jump choice_workshop
        "Larger shed.":
            jump choice_generator1

    label choice_no2:
        jump choice_sheds3

    label choice_yes2:
        jump choice_generator3

    label choice_generator3:
        n "You open the door to the larger shed. You can see that it contains a running electric generator containing gas and firewood."
        jump choice_generator2

    label choice_cottage:
        n "You make your way into the cottage. The rain is getting worse, after all."
        n "You fully open the door. Beyond the partially open front door, a hallway leads to the cottage's four rooms, two on each of the wide passageway."
        n "At the end of the hallway is a winding staircase leading to the lighthouse's service room. Although all of the rooms appear to be fitted with electric light bulbs, only the study's lights are currently turned on."
        n "The first thing you notice is the three coat hooks by the door, only one of which currently has a well-worn jacket hanging from it. Two pairs of rain boots stand in a shallow tray just beneath the coat hooks; there is space for another pair, while a pair of indoor shoes sits beside the tray."
        n "Two oil lanterns hang from hooks next to the oilskin; there is also an empty hook, suggesting one lamp is missing."
        n "Do you see anything else in the hallway? Roll a Spot Hidden."
    if roll_result <= 65:
        n "You see two bullets lodged in the hallway floor."
        jump eighth_scene

    label eighth_scene:
        n "Can you find more information about the bullets? Roll Handgun."
    if roll_result <= 50:
        n "The bullets were fired from someone positioned a couple of steps up the winding stairwell."
    else:
        n "Failure! You fail to find out more information about the bullets."
        jump ninth_scene

    label ninth_scene:
        n "You also see spattered blood leading from the the door farther left to the stairs, where three large golden coins lie discarded on the floor."
        n "Which room do you want to investigate first?"
    menu:
        "1 (door closest to you on the left)":
            jump choice_study
        "2 (door closest to you on the right)":
            jump choice_bunkroom
        "3 (door farther on the left)":
            jump choice_kitchen
        "4 (door farther on the right)":
            jump choice_larder

    label choice_study:
        n "You open the door to what looks like a study. It contains three armchairs, located in roughly the center of the room. In addition to the hall doorway, there is another door leading to the third, bloodied room."
        n "In terms of furniture, besides the armchairs, there is a table to the left of the hall door and a roll-writing desk on the outer wall, close to the other door. Both have their own chair next to them. The one by the writing desk currently lies on the floor."
        n "Can you deduce more information from this scene? Roll an Intelligence."
    if roll_result <= 65:
        n "From your investigative training in the Academy, you can deduce that whoever was sitting on that chair stood up in a hurry, knocking it over in the process."
        jump study2
    else:
        n "You do not find out any extra information from the scene in the study."
        jump study2

    label study2:
        n "The table holds several books of maritime tales, a pipe and a pouch of tobacco, a sketchbook, watercolor paints, paintbrushes, and paper."
        n "More interestingly, what appears to be a recently finished watercolor also sits on the table beside a neat stack of other paintings. This piece appears to show a window and a dark shadow with wide eyes leering through the glass pane."
        n "You realize that the window can easily be identified as the same one next to the artist's desk. You suddenly feel extreme unease and the all too familiar feeling of being watched."
        n "Do you want to inspect the painting further, explore the study further, or explore the other rooms?"
    menu:
        "Inspect the painting further.":
            jump study3
        "Explore the study.":
            jump study4
        "Explore the other rooms.":
            jump returntohallway

    label study3:
        n "With a successful Zoology and/or Painting roll, you can find out more about the painting."
    if roll_result <= 38:
        n "Success! You can tell that the shadow's eyes look bulbous and appear to be placed almost to the side of its head, similar to the anatomy of a fish or a frog."
        jump choice_painting
    else:
        n "Failure! You do not receive new information."
        jump choice_painting
    if roll_result <= 21:
        n "Success! You realize that this piece was executed in a hurry, it lacks the care and finesse of the other paintings on the table."
        jump choice_painting
    else:
        n "Failure! You do not receive new information."
        jump choice_painting

    label choice_painting:
    menu:

        "Explore the study.":
            jump study4
        "Explore the other rooms.":
            jump returntohallway

    label study4:
        n "When flipping through the many neatly stacked watercolor paintings, one more image grabs your attention. It features the nearby thicket. In the darkness of the path leading into the thicket is the silhoutte of a man. Unlike the first painting, this one is dated: February 14th, 1926"
        n "There is a corresponding rough sketch with the previous day's date in the sketchbook. There is no matching sketch for the first painting."
        n "The roll-top writing desk on the other side of the room is closed but unlocked. Opening it reveals a half-empty, still warm mug of coffee and lots of stationary."
        n "A mess of invoices for coin appraisals from a variety of Rockport antique stores litter the rest of the desktop; the quotes range from two to five dollars, and are all dated late February 1926."
        n "Under a large coin catalog are several letters from further afield antique stores, librarians, and universities. Each letter begins with 'Dear Mr. Cassidy,' followed by an apology,explaining that the sender is unable to determine the origin of the coins."
        n "The writing desk also has two drawers. The left-hand one is open, but there is a key snapped off inside its lock -- the drawer holds an empty wooden box whose green velvet lining is shaped to hold a revolver. Six bullets lie loose in the same drawer. The right-hand drawer is locked."
        n "Do you want to attempt to forcibly open the locked drawer?"
    menu:
        "Yes.":
            jump choice_yes3
        "No.":
            jump returntohallway

    label choice_yes3:
    if roll_result <= 85:
        n "Success! You manage to force the drawer open. It contains a small journal belonging to George Cassidy. There is a rough sketch of an obelisk on the journal's cover."
        #n "As you read the journal,

    label returntohallway:
    menu:
        "1 (door closest to you on the left)":
            jump choice_study
        "2 (door closest to you on the right)":
            jump choice_bunkroom
        "3 (door farther on the left)":
            jump choice_kitchen
        "4 (door farther on the right)":
            jump choice_larder

















    # This ends the game.

    return
