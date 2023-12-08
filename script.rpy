# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define gordon = Character("Gordon Hobbs")
define n = Character("Voice")
define sailor = Character("Captain of the SS Essex County")
define monster = Character("Unknown Creature")
define cassidy = Character("George Cassidy")
define turner = Character("Michael Turner")
define coastguard = Character("Coastguard")

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
$ luck = 27

# The game starts here.

label start:

    scene stormy sea
    show gordon reg

    gordon "I am a Special Agent for the Bureau of Investigation. My current assignment in this godforsaken hell hole is keeping an eye out for any illegal activity conducted along the popular east coast shipping routes."
    gordon "So far, there's not been much to report, with the exception of one unmarked vessel spotted passing Rockport during a storm in early February, which seems to have vanished without a trace."
    gordon "A fellow undercover agent and friend, Michael Turner, has been stationed up on Beacon Island. What better place to keep an eye on passing ships than from a lighthouse?"
    gordon "He got a message to me that he'd uncovered some sort of evidence of smuggling, but he didn't go into any details. He also asked to meet me in Rockport tomorrow morning, so here I am, on a late boat heading for our rendesvous."
    gordon "I really hope he's found something that would signal an end to my time here. This whole region gives me the creeps. Maybe it's just my imagination; maybe I've just been involved intoo many weird cases in the past."
    gordon "Ah, it's probably nothing. But if it is, why do I always get the feeling I'm being watched whenever I'm on the water?"

    hide gordon reg

    n "April 12th, 1926, 8:15pm. The Beacon Island lighthouse off the shore of Folly Point, Massachusetts, ceased to cast its light over the region’s dangerous rocky waters about 15 minutes ago."
    n "As a result, the SS Essex County, a mixed passenger and cargo vessel on which you are traveling to Rockport, has foundered on the rocks and incurred considerable damage to its hull. The ship is sinking, and the crew hurries you toward one of the many small rowboats acting as the ship’s lifeboats."

    show sailor

    sailor "Your best bet is to aim for Beacon Island."
    sailor "I doubt you'll make the mainland as a storm is brewing. You should have just enough time to reach the island before it hits."

    hide sailor

    n "Then, without another word, they shove you off into the dark, churning waters. All you hve to guide you is the small light shining at the base of the lighthouse's towering silhoutte."

    n "As you brave the roaring waters, your rowboat hits something hard in the dark waters. Twisted metal has become lodged on a nearby sandbank, while yet more lurks just below the surface."
    n "Can you find out any information about this? Please roll for Spot Hidden."

    # Dice roll results

    $ roll_result = renpy.random.randint(1,100)
    $ damage_result = renpy.random.randint(1,3)
    $ roll_result4 = renpy.random.randint(1,4)
    $ roll_result6 = renpy.random.randint(1,6)

    # Scene start

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
    if roll_result6 >= 5:
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
        n "Success! You are able to fix the generator!"
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
    else:
        n "Failure! You do not see anything else of interest in the hallway."
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
        n "Failure! You do not receive new information about the shadow in the painting."
        jump choice_painting
    if roll_result <= 21:
        n "Success! You realize that this piece was executed in a hurry, it lacks the care and finesse of the other paintings on the table."
        jump choice_painting
    else:
        n "Failure! You do not receive new information about the painting itself."
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
        n "Do you want to read the journal?"
    menu:
        "Yes.":
            jump choice_journal
        "No.":
            jump returntohallway

    label choice_journal:
    # show cassidy
        cassidy "February 13th, 1926. I found something on one of my walks. A coin! I kept walking and found another then another! I know it’s gold. Found some mechanical parts as well. Looks like it might be from a ship. Must have gone down recently, but I don’t recall hearing anything about no wreck of late."
        cassidy "I better keep this quiet. Don’t want the other two here to get a slice of the action. I will keep this journal as a means of documenting my findings. This has to be worth a mint!"
        cassidy "February 16th, 1926. That coin catalog I bought in Folly Point is useless. One thing I know is that the coins are old. Real old. I've asked if I can stay on for as long as I can until I'm sure there's nothing left here for me to line my pockets. And I have to find a good lead on these coins and go where the money takes me."
        cassidy "Maybe I should write to some of my old 'colleagues' to see if they can help. Should probably try some of those fancy antique stores in Rockport, while I'm at it."
        cassidy "March 10th, 1926. The coins are getting hard to find. The two new crew members aren't helping matters. Makes it difficult to search without being noticed. Hope they don't cause me any trouble. Even so. I've filled a small purse which I keep on me at all times."
        cassidy "April 3rd, 1926. I've got a good lead now. I'll be sending one more letter to Innsmouth then I'm confident I can get off this stinking island for good. I think Michael is watching me. I've bought a gun just in case."
        cassidy "April 11th, 1926. Smith said he will leave the lighthouse tomorrow morning. He says he doesn't care if it voids his contract--he's had enough of this island and everything on it. Least that's one less pair of eyes wacthing me. Still stuck with that sneak, Michael, though."
        cassidy "Smith says the radio busted again halfway through talking to the bosses. Said he'd fix it before he leaves. Counted my coins just to be sure he didn't lift any off me in my sleep. I've seen Michael peering out the window, spying my daily walks. I'll have to be a bit more careful."
        cassidy "April 12th, 1926. Smith left without a word. Me and Michael didn't even see him go. Didn't take his paintings with him, which is a bit odd. Lousy rat didn't even repair the radio before he left. I'll get to it later tonight. Michael has gone to check something outside. Seems paranoid."
        cassidy "Think there's more than just tobacco in that pipe of his. At least I get more time to write. No word from -"
    # hide cassidy
        n "The last entry cuts off abruptly, as if Cassidy was interrupted while writing it."
    show gordon
    gordon "What is going on in this island? Michael? Paranoid? Where is everybody?"
    jump returntohallway
    hide gordon


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
            "5 Go up the winding stairs to the lighthouse service room.":
                jump serviceroom

    label choice_bunkroom:
        n "You open the door. This room looks like a bunkroom. It contains three neatly-made beds. A large pile of books is stacked tidily in one corner of the room. There are also three large cupboards, each holding soap towels, fresh bedding, and extra blankets."
        n "Those belonging to Turner and Cassidy contain warious articles of clothing along with a few small personal effects; the one belonging to Smith contains only the linen and towels."
        n "Do you see anything in the room? Roll for Spot Hidden."
    if roll_result <= 75:
        jump bunkroom1
    else:
        jump bunkroom2

    label bunkroom1:
        n "Success! Your investigative skills as a Bureau Agent has helped you find one gold coin, six loose bullets, and a pocket-sized notebook stuffed in Turner's mattress."
        n "Open the notebook?"
    menu:
        "Yes.":
            jump notebook
        "No.":
            jump returntohallway

    label bunkroom2:
        n "Failure! You cannot find more information from the bunkroom."
        jump returntohallway

    label notebook:
        #show turner
        turner "George Cassidy previous criminal record. Involved in smuggling?"
        turner "Lights on water. Small rowboat?"
        turner "Found ship parts on north shore."
        turner "Found gold coin on north shore."
        turner "Bigger than just bootleg moonshine. What is going on?"
        turner "Smith said saw someone in trees and peering through window."
        turner "Men on island at night?"
        turner "Croaking noise?"
        turner "Frogs?"
        #hide turner
        show gordon
        gordon "Michael..."
        hide gordon
        jump returntohallway

    label choice_kitchen:
        n "The door to the kitchen is slightly open. You see the pool of blood leading from the kitchen to the hallway. You push open the door."
        n "The kitchen has some dirty plates and a saucepot in the sink, a table with three chairs, and three doors: one leading outside, one to the hallway, and one to the study. A small wood-fired stove is located in the far corner; a still warm kettle sits on the hearth next to it."
        n "One of the chairs lie broken on the floor; there is a small pool of blood on the floor beside it."
        n "To learn more about the scene, roll for Intelligence."
    if roll_result <= 65:
        jump kitchen1
    else:
        jump kitchen2

    label kitchen1:
        n "Success! From the way the chair looks, you can infer that it may have been used as a weapon."
        jump kitchen3

    label kitchen2:
        n "Failure! You cannot find more information in the room."
        jump kitchen3

    label kitchen3:
        n "Is there anything unusual about the blood? Can you find out more information? Roll for Medicine."
    if roll_result <= 35:
        n "The pool of blood is recent and formed within the last hour. There is something not quite right about the blood, like it may not be human in origin."
        jump returntohallway
    else:
        n "You fail to recover more information."
        jump returntohallway

    label choice_larder:
        n "You open the door. You sneeze as the dust hits your nose. You open your eyes to a room filled with shelves of food, all neatly stacked with all manner of dried, canned, and preserved foods -- enough to see three people through if cut off from the mainland for several months."
        jump returntohallway

    label serviceroom:
        n "As you climb the stairs, you eventually reach the lighthouse's service room, located immediately below the lantern room. The mechanism used to turn the lamp can be seen mounted in the ceiling, and from the noise, it appears to still be working."
        n "A separate set of steps leads up through a trapdoor into the lantern room above. There are several boxes stored here; each contains a replacement bulb for the lighthouse's beacon."
        n "There is also a small workbench and a tool bag. On the workbench is a log of the various service checks performed on the lighthouse."
        n "Opposite the workbench is a table with a radio set in a semi-state of disrepair."
        n "what is your next course of action?"
        jump serviceroomchoices

    label serviceroomchoices:
    menu:
        "Read the lighthouse's service logs.":
            jump servicelogs
        "Try to fix the radio.":
            jump fixradio
        "Go up the lantern room.":
            jump lanternroom

    label servicelogs:
        n "Majority of the checks are purely routine; however, one entry stands out. On February 12th, 1926, wiring problems caused the lighthouse's lamp bulb to prematurely burn out."
        n "The log records how the electrical short cauesd by the bulb's failure, coupled with the severe storm, hampered the repairs, meaning the lighthouse was in darkness for several hours."
        jump serviceroomchoices

    label fixradio:
        n "A successful Electric Repair roll fixes the radio with ease. Roll for Electric Repair."
    if roll_result <= 50:
        jump fixedradio
    else:
        "Failure! You failed to fix the radio."
        jump serviceroomchoices

    label fixedradio:
        n "You fixed the radio. You may call for help to the local coastguard."
    n "Ring..."
    show gordon reg
    gordon "Hello? My name is Gordon Hobbs, I work for the Bureau of Investigation. You need to send rescue to Beacon Island immediately! There are - "
    hide gordon reg
    show coastguard
    coastguard "Hello?"
    hide coastguard
    show gordon reg
    gordon "Hello? Can you hear me?"
    gordon "Hello? Please come to Beacon Island!"
    n "The line disconnects."
    hide gordon reg
    show gordon mad
    gordon "Agh!"
    gordon "I've got to get upstairs."
    jump lanternroom

    label lanternroom:
        n "You reach the lantern room to be greeted by a wet, bloody scene. Two panes of glass in the lantern room's windows have been broken somehow; their shattered remains crunch underfoot."
        n "The rain blows in through the gaps, making the metal decking slippery underfoot. Adding to the slipperiness is blood from the corpses of two men, along with that from two bizarre fish-creatures which lie inside the room's narrow confines."
        n "One of the dead fish-things is latched onto on of the men's necks by its teeth, even in death."
        n "You lose [roll_result6] sanity."
    if roll_result6 <= 5:
        jump lanternroom1
    else:
        jump lanternroom2

    label lanternroom1:
        n "Despite the gruesome scene before you, you manage to calm your nerves. You are a Bureau Agent after all."
        n "You start searching the various corpses around you. The body near the stairs is very strange-looking. The man, garbed in a heavy, hooded raincoat, appears to have a narrow head and pronounced flaps of skin around his neck and jowls."
        n "He also seems to be suffering from some sort of skin condition, going by his gray, rough complexion."
        n "His bulging, watery eyes stare sightlessly in the direction of Cassidy's corpse."
        n "To find more information from the body, roll for Zoology."
    if roll_result <= 38:
        jump fishbody1
    else:
        n "Failure! You do not find more information about the corpse."
        jump flr1

    label fishbody1:
        n "Success! You find out that the creature has been shot twice, and that these bullet wounds led to his death."
        n "A dead fish-creature lies beside the strange man. Both it and the one attached to Cassidy's corpse have been shot as well -- one through the eye, and one through its belly."
        n "Beyond the creatures' obvious fishlike appearance and amphibious nature, this species of fish is not recorded anywhere in any book known to you."
        n "The bizzare piscine-things look like they would be extremely mobile on land due to their muscular legs, and perfectly at home in the water due to their fins and gills."
        jump lanternroom3

    label flr1:
        n "A dead fish-creature lies beside the strange man. Both it and the one attached to Cassidy's corpse have been shot as well -- on through the eye, and one through its belly."
        n "Beyond the creatures' obvious fishlike appearance and amphibious nature, this species of fish is not recorded anywhere in any book known to you."
        n "The bizzare piscine-things look like they would be extremely mobile on land due to their muscular legs, and perfectly at home in the water due to their fins and gills."
        jump lanternroom3

    label lanternroom3:
        n "Can you find information about these bodies? Roll for Zoology again."
    if roll_result <= 38:
        n "Success! You see that the bullets which entered both creatures only killed them because they went into the softest, fleshiest, most vulnerable parts of their bodies."
        n "The rest of their scaly exteriors, although penetrable, are coarse and tough, no doubt providing the creatures with a form of natural armor. Evidently, Cassidy was a 'lucky' shot, for all the good it did him."
        jump lanterncassidy
    else:
        n "Failure! You fail to find out more information."
        jump lanterncassidy

    label lanterncassidy:
        n "The final corpse is that belonging to Cassidy. Hidden under the late lighthouse keeper's shirt is a heavy purse full of the strange gold coins, tied around his neck on a thick leather cord. A six-shooter, a Colt M1877, is held firmly in his still-warm hands."
        n "All of the bullets in the chamber have been spent. The revolver appears to match the size and shape of the one missing from the desk drawer downstairs. Taking into account the two bullets in the strange man, and the two in the fish-creatures, two bullets are still unaccounted for."
        n "Can you find the other bullets? Roll for Spot Hidden."
    if roll_result >= 65:
        n "Success! You identify a bullet hole in the lamp's lens; the bullet which caused it appears to have shattered the bulb inside before carrying on through to smash one of the lantern room's missing panes of glass."
        n "This, at least, explains why the lighthouse beacon stopped working at 8 pm this evening. It can easily be surmised that the second broken pane was destroyed by the other bullet."
        jump startofattack
    else:
        n "Failure! You fail to find the missing two bullets."
        jump startofattack

    label startofattack:
    show gordon reg
    gordon "Damn it. I've got to call for help! What the fuck is going on here?"
    n "Wait. Did you lock the door to the cottage? Roll for Luck."
    if roll_result <= 27:
        n "Lucky! You remember that you did lock the door after entering the cottage."
        jump lockeddoor
    else:
        n "Uh oh."
        jump unlockeddoor

    label lockeddoor:
        n "You hear banging from the front door downstairs. What is your course of action?"
    menu:
        "Barricade yourself and hope rescue gets to you first before whatever this thing is.":
            jump barricade
        "Go downstairs and position yourself for a surprise attack.":
            jump fight

    label barricade:































    # This ends the game.

    return
