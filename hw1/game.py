import sys
import random
import pwd
import os

def main():
    N=9
    map = create_map(N=9)
    not_win = True
    health = 100
    oxygen = 100
    healthy = oxy = True
    bleeding = True
    current_position = [N//2+1,N//2+1]
    print '''
    You woke up in barely recognizable place. Your head aches like hell.
    You can't even see normally. Everything is like in a mist.
    1. Try to look around
    '''
    a1 = int(raw_input('Your action: '))
    if a1!= 1:
        mistake_option()
    else:
        print '''
        You trun your head  to look around. There is a little around you.
        A trash can is in the corner near your bed, for example.
        And you see a few empty bottles of booze near it.
        - Ah, so this is just a hangover. At least I know why my head is splitting apart, - you thought.
        There is also a wardrobe in the room. And that's it.
        The room is empty. The walls are stone and metal. Cold.
        1. Try to get out of bed
        '''
    a1 = int(raw_input('Your action: '))
    if a1 != 1:
        mistake_option()
    else:
        print '''
        You are trying to get out of bed and...
        OH FUCK! Sharp pain just hits you in the area just below your stomach.
        HOLY SHIT! WHAT THE HELL IS THIS???
        Remember earlier you wasn't able to even open your eyes? They are widely open now.
        You can see a knife in you, just to your right above your belt. Wound is not fresh, but does it really matter?
        The growing pain just knocks you and you fall without any conscious on the floor
        ...
        ...
        ...
        - Easy, easy, just easy, - remind you to yourself.
        There are few questions you want to know. Where the fuck are you and what the fuck happened here - are just few of them
        Under the bed you see a medical kit and a small note.
        1. Take a medkit.
        2. Read a note.
        '''
    a1 = int(raw_input('Your action: '))
    if a1 == 1:
        print '''
        Medkit is empty.
        Almost. There are two pills there. Red and blue. Should you take one of them?
        1. Take a blue one
        2. Take a red one
        3. Read the note'''
        a1 = int(raw_input('Your action: '))
        if a1 == 1:
            print '''
            Oh, you feel so strong. You are just able to walk without pain. To run.
            You feel invincible. Immortal. Wanna see? Just pull out a knife from your stomach.
            Great! You feel anything? That's what I'm talking about!
            Now cut your throat. Yes, yes, cut it. Just slice
            Feel the salty taste in your mouth? It is a taste of immortality.
            Or rather a taste of blood. And death a little.
            Just before you fall dead - a thought comes through your mind. What was in the note?
            '''
            sys.exit()
        elif a1 == 2:
            print '''
            You take two pills in your hands. You feel like Morpheus from the Matrix. And you pick red
            Just like Neo. Dark consumes you. You start breathing heavily. You are suffocating. You are drowning.
             You feel every inch of your body, every cell of it. Yor hands start to shake, the blue pill falls on the floor
             And you accidentally step on it. But that doesn't matter. Because you feel aging for 50 years.
             You fall on your knees but several minutes later you are able to get up.
             You feel your life's being slowly sucked out from you. You are alive but pain isn't going away.
              You wonder, what it would be like, taking blue pill instead? Was your pick worthy?
            '''
        elif a1==3:
            print '''
            What would you choose? Suffering or pleasure? Feel no pain or feel all of it?
            Use your gift to see through fire and the fire will consume you. You'll live in agonizing pain.
            It will drive you mad. It will make you question yourself why. It will slowly eat you from the inside.
            Or would you rather dive into the blue ocean and feel free? From all of your pain. Forever and ever.
            Fire or water? Suffering life or immortality? Choose carefully but remember, that everything has it's price to pay.
            Choose wisely ##########
                          ##########'''
            print '                    ', get_username()
            print '''
            1. Take a blue one
            2. Take a red one
             '''
            a2 = int(raw_input('Your action: '))
            if a2 == 1:
                print '''
                Oh, you feel so strong. You are just able to walk without pain. To run.
                You feel invincible. Immortal. Wanna see? Just pull out a knife from your stomach.
                Great! You feel anything? That's what I'm talking about!
                Now cut your throat. Yes, yes, cut it. Just slice
                Feel the salty taste in your mouth? It is a taste of immortality.
                Or rather a taste of blood. And death a little.
                Just before you fall dead - a thought comes through your mind. What about red pill?
                    '''
                sys.exit()
            elif a2 == 2:
                print '''
                You take two pills in your hands. You feel like Morpheus from the Matrix. And you pick red.
                Just like Neo did. You feel strange right? There was something dark born inside you. Dark and cruelly hot.
                The dark consumes you. You start breathing heavily. You are suffocating. You are drowning.
                You feel every inch of your body, every cell of it aching. Yor hands start to shake, the blue pill falls on the floor
                And you accidentally step on it and crash. But that doesn't matter. Because you feel aging for 50 years.
                You fall on your knees but several minutes later you are able to get up.
                You feel your life's being slowly sucked out from you. You are alive but pain isn't going away.
                You wonder, what it would be like, taking blue pill instead? Was your pick worthy?
                '''
            else:
                mistake_option()
        else:
            mistake_option()
    elif a1==2:
        print '''
        What would you choose? Suffering or pleasure? Feel no pain or feel all of it?
        Use your gift to see through fire and the fire will consume you. You'll live in agonizing pain.
        It will drive you mad. It will make you question yourself why. It will slowly eat you from the inside.
        Or would you rather dive into the blue ocean and feel free? From all of your pain. Forever and ever.
        Fire or water? Suffering life or immortality? Choose carefully but remember, that everything has it's price to pay.
        Choose wisely ##########
                      ##########'''
        print '                    ', get_username()
        print '''
        1. Take a blue one
        2. Take a red one
             '''
        a2 = int(raw_input('Your action: '))
        if a2 == 1:
            print '''
            Oh, you feel so strong. You are just able to walk without pain. To run.
            You feel invincible. Immortal. Wanna see? Just pull out a knife from your stomach.
            Great! You feel anything? That's what I'm talking about!
            Now cut your throat. Yes, yes, cut it. Just slice
            Feel the salty taste in your mouth? It is a taste of immortality.
            Or rather a taste of blood. And death a little.
            Just before you fall dead - a thought comes through your mind. What about red pill?
                    '''
            sys.exit()
        elif a2 == 2:
            print '''
            You take two pills in your hands. You feel like Morpheus from the Matrix. And you pick red.
            Just like Neo did. You feel strange right? There was something dark born inside you. Dark and cruelly hot.
            The dark consumes you. You start breathing heavily. You are suffocating. You are drowning.
            You feel every inch of your body, every cell of it aching. Yor hands start to shake, the blue pill falls on the floor
            And you accidentally step on it and crash. But that doesn't matter. Because you feel aging for 50 years.
            You fall on your knees but several minutes later you are able to get up.
            You feel your life's being slowly sucked out from you. You are alive but pain isn't going away.
            You wonder, what it would be like, taking blue pill instead? Was your pick worthy?
                '''
        else:
            mistake_option()
    else:
        mistake_option()
    print '''
    You are finally able to gather your thoughts together. You are standing still (at least for now)
    The note? Was it for you? If yes, is this who you are? ''' + get_username() + '?'
    a1 = int(raw_input(''' And what that crossed lines above your name were?
    1. Look around
    Your action: '''))
    if a1 != 1:
        mistake_option()
    else:
        print '''
        As earlier, you may see a trash can and a wardrobe.
        But now you see alos a little window in your room (or rather cell?).
        And a massive door just behind a wardrobe. Is it your way out?
        You feel like every step around a room is laying another heavy burden on you.
        Your ankles are week, your knees are trembling.
        Your wound opened and you'll be bleeding in a few minutes
        '''
    print '''
        In a wardrobe you find a space suit. You put it on and open the door
        Reality awaits you. A desert on the forgotten planet. How do you know it?
        You don't know, but suddenly you feel certain about something since your waking up
        And while your are going bleed to death there is a hope.
        Or rather Hope. A small spaceship should be nearby. Some kind of little shuttle.
        On the front door you see a crudely drawn map and coordinates [2, 7].
        It doesn't tell you anything but at least it's something.
        Suddenly your space suit beeps and you see [5,5] on your hand
        Are these your coordinates?
        You should run. But with every your step the knife goes deeper into your tissues. You'll die soon.
        Hurry up!
        '''
    while healthy and oxy and not_win:
        print 'Your current position ', current_position
        print 'Your health: ', health, 'Your oxygen: ', oxygen
        current_position, health, oxygen = move(current_position, health, oxygen)
        healthy = False if health<=0 else True
        oxy = False if oxygen<=0 else True
        if health<=0 or oxygen<=0:
            healthy=False
            print '''
            You've died to soon, before being able to reach Hope.
            There is no hope for you either. You'll rot in this wasteland.
            And no one will ever know about what happened to you'''
            sys.exit()

        if current_position == [2,7]:
            not_win = False
            print '''
            You've reached the location on the map but nothing is here.
            Except the wall of sand, you can hardly see through.
            But just at the time you wanted to leave, you hear a roar in the sky.
            A little shuttle is landing near you.
            '''
    kill_him = '''
    You rush towards the figure with a fury and kick him.
    You are trying to break his helmet with you bare hands, but you are tow weak.
    In other second you hear the sound of a shot. It's you. You are falling to the ground trying to grasp a final portion of oxygen
    The last thing you see is endless mist. And a person who shot you comes jsut above you.
    - Are you FUCKING mad? Are you out of your fucking mind?
    I was told, that you guys are freaks, but I was here just to bring you food and alcohol.
    Son of a bitch.
    ...
    ...
    Son of a bitch. Your last thing to hear. Close your eyes. Just die.'''
    print '''
    -Hi. - said the voice from the mist. -How are you? As agreed, I'm here to drop you some booze.
    You barely see a person in front of you.
    -What's your name?

    1. Answer your name, you've seen on the note
    2. Answer, you don't know
    3. Kill him
    '''
    a1 = int(raw_input('Your action: '))
    if a1 == 1 or a1==2:
        print '''
        You are trying to said something but it's just you are numb. No sound goes through you throat.
        - You must be kidding. - you hear a figure laughing., - It is said 'Steve Sussmann' on your suit.
        - Are you cool? My name is Ivo Bobul. I am here on regular cruise to bring supplies with me.
        You feel no harm from the person beside you. It is just you can't uderstand him.
        Just drop off some booze means he is leaving you here?'''
    elif a1==3:
        print kill_him
        sys.exit()
    else:
        mistake_option()

    print '''
    - You can eat inside the shuttle. Come on, lad.
    You have enough strength to go into the ship, but then you just fall on your knees.
    Ivo trying to put your suit off and sees a knife.
     - That's bad, - he says. - You know I can't take you with me, a colony needs a watcher.
     I just patch you up and let go.
    '''
    raw_input('What you are thinking about?: ')
    print'''
    That's great. Puzzle is not clicking, right?
    You feel better, the wound is patched. Knife is laying near you.
    Ivo is preparing some food. You see him putting his laser pistol on the table.
    A thought crosses your mind, that you ain't going to be left here.
    '''
    raw_input('You are trying to say something to Ivo: ')
    print'''
    But you can't say anything. You are numb somehow.
    Ivo is coming close to you.
     - You know what, I don't know how that happen, but I'll call for help on the next station.
     And with my small medkit. I've used it almost all on your wound.
     The only things that left are those pills. Suicide pills they call them, you know.
     The yellow one is greatest analgesic pill of our time. No pain for day or so. After that pain returns though
     But it is also called amnesia pill. You'll never recall anything happened in your life.
     It is suicidal because somehow our mind can't bear this uncertainty and drives us mad to death.
     The blue one makes you feel immortal. Downside of that - people often want to try it out and kill themselves
     The red one is making your body ache, but it makes it tireless, so you can walk long distances.
     Clearly a poor guy dies of exhaustion unless treated in clinic. And they sometimes become even numb for unknown reasons.
     ...
     - Numb..., he says thoughtfully. Now by the change on his face, you know that he knows.
     Ivo starts looking towards his pistol and you know it's time to act.
    '''
    act = raw_input('1. Stab him with a knife: ')
    if act != "1":
        print '''You wasn't able to do anything, so Ivo just throws you out of the shuttle and flies away
        The red pill is going to kill you in
        5
        4
        3
        2
        1
        total darkness
        .'''
        sys.exit()
    else:
        print '''
        You take a knife and shoves it into the Ivo's belly. You feel pity for him.
        But that feel quickly goes away.
        You've already have a plan.
        Who the fuck cares about who you are? May be you are even Steve Sussman, but now you can be Ivo Bobul
        You put a yellow pill into the mouth of moaning Ivo. It is great that it will free Ivo out of pain, you thought.
        But it's more amnesia side effect you need to make sure nobody finds out.
        You put your space suit (or rather Steve's) on Ivo and take him unconscious to the your cell.
        And safely fly away.'''

    print 'Welcome to your new life, Ivo. Just don\'t forget to visit a doctor in a nearby station'

    raw_input('The end')

    print '''
    A guy wakes up in an agonizing pain in a cell made of stone and steel with a knife in his stomach.
    There is a note near him ending with:
    Choose wisely ##########
                  ##########
                  ##########
                  Ivo Bobul
    '''

def mistake_option():
    print '''
    Well now you know why it was so hard for you to recall anything. Because you are stupid.
    You can't even choose from available options. It was a pleasure to meet you.
    Just kidding, it was not. You slowly die without knowing who are you and where are you dying at
    '''
    sys.exit()


def create_map(N):
    #create poi()
    pass

def perform_step(health, oxygen, direction):
    pass

def create_poi():
    pass

def create_action_list(map, current_position, known):
    pass

def print_action_list(action_list):
    pass

def move(current_position, health, oxygen, bleeding = True):
    print ('''What direction you want to move?
        1. North
        2. South
        3. East
        4. West
        5. Stay still
        ''')
    #direction = random.randint(5)
    direction = int(raw_input('Your direction: '))
    # direction = 1
    current_position = update_position(current_position, direction)
    #health, oxygen, current_position = perform_step(health, oxygen, current_position, direction)
    oxygen = oxygen - 15
    if bleeding:
        health = health - 12

    return current_position, health, oxygen

def get_username():
    return pwd.getpwuid( os.getuid() )[ 0 ]

def update_position(pos, direction):
    #print ("Your pos ", pos)

    if direction == 1:
        pos[1]+=1
    elif direction == 2:
        pos[1]-=1
    elif direction == 3:
        pos[0]+=1
    elif direction == 4:
        pos[0]-=1
    return [pos[0], pos[1]]

if __name__ == "__main__":
    main()
