# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Laura = Character("Laura")
define Detective = Character("[povname]")
define Clara = Character("Clara")
define Clarence = Character("Clarence")
define David = Character("David")
define Rose = Character("Rose")
define Beth = Character("Beth")
define Anne = Character("Anne")


image bg kitchen: 
    "images/bg kitchen.jpg" 
    zoom 4
image bg placeholder:
    "images/placeholder.png"
    zoom 5
image bg field:
    "images/bg field.jpeg"
    zoom 3.5
image bg mansion:
    "images/bg mansion.jpg"
    zoom 4
image bg inside mansion:
    "images/bg inside mansion.jpg" 
    zoom 4
image bg dining:
    "images/bg dining.jpg"
    zoom 3
image bg parlor:
    "images/bg parlor.jpg"
    zoom 2
image bg porch:
    "images/bg porch.jpg"
    zoom 3
image bg room:
    "images/bg room.jpg"
    zoom 3
image bg carriage:
    "images/bg carriage.jpg"
    zoom 3

image laura:
    "images/laura default.jpg"
    zoom 0.5
image clara:
    "images/clara default.jpeg"
    zoom 3
image hand:
    "images/detective reach.jpg"
    zoom 2
image lantern:
    "images/detective lantern.jpg"
image rose:
    "images/rose default.jpeg"
    zoom 2

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    # FIRST DAY
    # scene bg start
    "The year was 1870 when Otis Smith died at his family estate down in the south. The family was filled with worry, scared that the killer might still be around."
    "They were right, the killer was very close-by. Closer than any of them could know. His wife Clara was horribly sad, despite their relationship souring in their later years." 
    "Her and Otis’ children and grandchildren all gathered around, mourning the loss of the father they all kind of disliked, as well as trying to sniff out who did it."
    "They called in someone special."
    "You."
    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Pat Smith"

    
    "You arrive the morning after Otis was found dead, killed right in front of the estate he had “kept running” for years even through the Civil War."
    "Good luck!"

    # short description of the land and how you arrive to the mansion
    scene bg mansion
    "It's been a long road trip and you've finally made it to Smith Mansion. Two maids await by the gate."
    "They help carry your belongings and bring you to Rose, the wife of family son David."

    scene bg inside mansion
    with fade
    
    show rose
    # simple conversation before Rose directs detective to the field

    Rose "You must be [povname]. I've read about you on the newspaper. Never thought I'd see someone famous like you one day."
    # show hand at right

    # More conversation

    Detective "May I speak to Clara?"
    "Rose looks over to the window"
    Rose "She's been spending most of her time sitting outside." 
    "You look out and there is a silhouette sitting on a chair in the middle by a large tree, facing an open field with a church in the far distance."

    scene bg field
    with fade

    "The sun is setting and it's getting dark."

    # Show small path with setting sun in background w/ walking noises over sticks/leaves
    "You finally made your way to Mrs. Smith, anxiety welling up in your chest. You take a deep breath and try to introduce yourself."
    show lantern at right
    Detective "Mrs. Smith, I'd like to offer you my deepest condolences. I know this is a tough time for you and your family. My name is [povname]. I've been sent here to help you."
    show clara
    Clara "...."
    Detective "Mrs. Smith? I'd like to obtain some more information regarding... your husband's death."
    "The lantern in your hand lightly flickers"
    Clara "Otis..."
    "Tears steam down her cheeks and her voice slowly crackles. It's obvious that she has been weeping for the past few days"
    

    # Clara and the detective goes back to the mansion
    "You and Clara head back." 
    scene bg inside mansion 
    "She invites you to have dinner with the family and you enjoy a luxurious feast with them."

    # After Dinner
    menu decision1:
        "Where should you go?"
        "My Room":
            jump room
        "Kitchen":
            jump kitchen_1
        "Parlor":
            jump parlor_1
    label room:
        "You feel tired and head back to your room to rest for the evening."

    label kitchen_1:
        scene bg kitchen
        "You head towards the kitchen, wanting a glass of water."
        "As you approach, you hear murmurs and the sounds of plates clattering. You stop by the door and hide just out of sight"
        Beth "Do you really think master tripped and fell to his death?"
        Anne "... I can't imagine that happenin to master"
        Beth "Same, what do you say to the chances of..."
        "She stops in the middle of her sentence,her face tense"
        Anne "What? of what?"
        "Beth looks around and makes sure no one else is around"
        "She whispers, but her voice still quite loud"
        Beth "of murder... Think about it, these couple past years aint the best for the master."
        "Anne gasps for a second, but calms afterwards"
        Anne "Well, you know what. That's ain't the craziest idea."

        # separate here for the choice to continue eavesdropping or join the conversation
        menu decision2:
            "Ask for a cup of water":
                jump join
            "Continue to eavesdrop":
                jump eavesdrop
        
        label join:
            Detective "Sorry to bother, may I get a glass of water?"
            "Both maids are startled."
            Beth "OHhh. Ofcourse."
            "She quickly prepares a cup of water."
            Detective "I didn't mean to pry, but I did overhear your conversation. Why's that you think Otis got murdered?"
            "Beth and Anne looks at each other horrified. They drop down to the floor and begs."
            Beth "Sorry, we really didn't mean anything just now, we just like to gossip here and there."
            Anne "Yeah, we don't mean it. Please don't tell anyone else, we don't want to get in no trouble."
            Detective "No need to be scared. I don't mean harm."
            # Continue the conversation            

        label eavesdrop:
            Beth "Did ya hear about it, that master got a will set up a couple years back."
            Anne "A will? Isn't that decide who gets what after somebody's die?"
            Beth "Yeah, I think somebody chose to murder master for their share of the will."
        
    label parlor_1:
        "You head towards the parlor."
        "You hear a conversation in the distance."
        David "That bastard Benjamin! He denied my proposal in front of all them company. He thinks that he has the most say just because granddad is gone."
        "Well, I'm gonna prove to them that Benjamin don't got the smarts to take over"
        Rose "Just take your time and don't make a fool of yourself. I reckon he'll make mistakes on his own then you'll be able to prove yerself."
        David "Ofcourse. I ain't stupid."
        # Detective heads back.

    # SECOND DAY

    "It's the second day. You head down for some breakfast."
    menu decision3:
        "Where should I go?"
        "Parlor":
            jump parlor_2
        "Dining Hall":
            jump dining

    label parlor_2:
        scene bg parlor
        "You head towards the parlor and see Clarence standing by the windows."
        Detective "So, I've heard that you've just recently returned back to America."
        Clarence "Yes, I had been away for quite some time in India."
        Detective "And what made you decide to come back at this time?"
        Clarence "... It felt like it was time to come back, that's all."
        Detective ""

    label dining:
        scene bg dining
        "You head into the dining room."
        "You see Benjamin sitting alone at the table with newspapers in hand. You gently knock on the door and Benjamin glances over.
        "He immediately puts down his papers and walks over."
        Benjamin "I have some urgent things I'd like to discuss with you. It's regarding father's death."
        Detective "Whh.. Yes? Did you wish to discuss them at this moment?"
        Benjamin "Yes, come to my room. I have something to show you."
        "Benjamin starts leading you out. As you start heading out, Clara and the others arrive at the door."
        "Clara gives a stern look to Benjamin."
        Clara "Guests at the Smith house should be treated properly. What is this nonsense sending our guest away before breakfast? Do you have no manners?"
        Benjamin "Sorry. Come, let us eat together."
        Detective "What about the.."
        Benjamin "That can wait."
        "Benjamin sits and gestures towards the chair next to him."
        # Continue the conversation 


    menu decision4: 
        "Breakfast was great, where should I go next?"
        # all three options can be explored
        "Front Porch":
            jump porch
        "Find Clara":
            jump clara_1
        "Parlor":
            jump parlor_3

    label porch:
        scene bg porch
        "You step out the front door to the porch and look down at the stairs that Otis fell and cracked his head.
        "The stairs are so clean and pristine. It's hard to imagine that someone had perished here."
        # Detective looks around for clues.
        "You walk down towards the bottom of the stairs and bend down to take a closer look."
        "The smell of the cleaning solution is strong, but still not sufficient to cover the smell of the blood completely."
        "From the reports you had looked over at the police station, Otis' dead body had remained undiscovered until the next morning."
        "Apparently it was quite normal for Otis to return late or even the next day due to his addiction to alcohol."
        "Cause of death had not been confirmed but the officers at the station had already closed the file as accidental death."
         # More??
        "That's enough for today." 
        "You head back to your room."
    
    label clara_1:
        "You walk upstairs looking for Clara. In the hallway, Anne is cleaning some vases and she tells you that Clara is her room."
        "Otis and Clara's Room"
        Detective "Mrs. Smith, may I bother you for a short while?"
        Clara "Yes, ofcourse. Come in"
        "Clara is sitting on a rocking chair staring at something in her hands. She looks up and gestures towards the sofa."
        Clara "Please, take a seat."
        Detective "Are those?..."
        Clara "Just some old photos of us, he was such a gentleman when we first met."
        # Clara talks about the time when Otis and her dated. Go to Memory Bubble

        Clara "Enough of me rambling."

    label parlor_3:
        scene bg parlor
        "Benjamin is waiting in the parlor, he looks tired."
        "Detective heads in and sits down"
        Detective "I hope I'm not bothering you, what was it that you needed to talk to me about?"
        Benjamin "Well... "
        Benjamin "It doesn't matter anymore, he's dead..."
        "Benjamin looks upset and gloomy"

    # SECOND DAY LUNCH
    "Everyone is at the table  except for Benjamin. He had requested to eat in his room and complained about a headache."
    
    
    # Parlor
    "In the afternoon, most of the family are gathered by the parlor."
    

    # Indra joins the story 
    "It's evening time - it's quite dark outside."
    "The women and the maids are cleaning up from dinner."
    "You stand in the dining room with the other men, listening to their heated discussion about how Otis died."
    Clarence "Dad's been drinking his whole life for all I could remember."
    David "I didn't say it was granddad's tolerance for alcohol."
    Benjamin "I reckon his tolerance is the highest out of all of us."
    "You sigh and look down to your empty notepad."
    
    "There is a knock at the side door. Clara tells Rose to answer the door; she complains that the servant should answer, but Clara gives her a look, so she goes anyway."
    "Rose opens the door, and standing there is a formidable and fiesty-looking girl. She speaks english with an accent."
    Indra "My name is Indra" 
    "She says and steps into the kitchen, barging past Rose. Indra looks arounnd."
    Clara "Young lady, it's proper to wait until one is invited..."
    "Indra boldy walks right up to her, which causes Clara to stop  talking"
    Indra "I am looking for Clarence Smith."
    # Clara tells maid to bring Clarence over

    "Clarence is at the parlor with the rest of the men."
    Beth "Master Clarence,  your mother has requested for you in the kitchen."
    "Clarence stops talking and looks puzzled"
    Clarence "Right this moment?"
    Beth "There is a young lady looking for you. She said her name was Indra."
    "A slight pause."
    "Clarence bolts up from his chair and dashes past the maid. Benjamin is surprised but he could tell something important is happening so he follows after Clarence."
    "Benjamin catches up to Clarence in the hallway"
    Benjamin "What's wrong? Why did you stop here?"
    Clarence,"Indra.. She is ..."
    Benjamin "You know this young lady Indra? I didn't expect you to..."
    Clarence "She's my daughter. I.. didn't think she would follow me to America."
    "Benjamin grabs his arm and pulls him into the garden.

    # Benjamin and Clarence argument

    "The argument gets heated."

    "Benjamin punches Clarence, a fight ensues."
    menu decision5:
        "What should I do?"
        "Stay in the garden":
        "Go to the kitchen":
        "Go to the living room":

    # THIRD DAY

    "Everyone has finished eating, now would be a good time to ask around."
    
    menu dinner:
        "Where should I go next?"
        "Kitchen":
            jump kitchen
        "Second floor":
            jump second
        "Parlor":
            jump parlor_4

    label kitchen:
        "You head towards the kitchen" 
        scene bg kitchen
        # scene bg placeholder
        with fade
        show laura
        "Laura is instructing the maids to clean up after dinner. She stands still, her gaze elsewhere. She seems to be lost in thought."
        "You clear your throat"
        # play sound "audio/clear_throat.mp3"
        show hand at right
        Detective "Pardon me, might I have a moment of your time?"
        "Laura looks over, a pause..."
        Laura "Yes, Ofcourse"
        "In the Hallway"
        # scene bg hallway
        # with fade
        Detective "Please accept my heartfelt sympathies for your loss and I understand this is a trying period for you all. I have a few questions I wish to make."
        "Laura nods."
        
        menu questions_laura:
            "When was the last time you saw Benjamin?":
                jump laura_1

            "When you saw him last, did he seem different than usual?":
                jump laura_2

            "What do you think about Benjamin?":
                jump laura_3    
        
        # need to rethink this part since detective is also at the dinner 

        label laura_1:
            Laura "The night before his death. We had dinner together with the family."
            Laura "He spoke about father's death."
            Detective "And what exactly did he talk about?"
            Laura "He said he'd work hard to support the family. He wanted to us to move past father's death."
            jump questions_laura

        label laura_2:
            Laura "He rarely spoke to the family, and was intensely focused on work."
            Detective "What about his demeanor?"
            Laura "He seemed more distant than usual. He doesn't involve himself in the daily house affairs so I rarely get the chance to speak with him but father's death... it really shut him off.
            "He spent way more time at the bars drinking away his grief."


        label laura_3:
            Laura "He has always been a great brother. I admire him greatly."

    label second:
        "You head upstairs to the second floor"
    
    label parlor_4:
        scene bg parlor
        "You head to the parlor"

    # This ends the game.

    return
