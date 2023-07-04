serial_number = ""
num_batteries = 0

def config():
    #This function updates the global variables for serial number and number of batteries. Since these parameters are fairly common questions, I have created the option to preconfigure them.
    global serial_number 
    serial_number = input("SERIAL NUMBER: ").lower()
    global num_batteries 
    num_batteries = int(input("NUMBER OF BATTERIES: "))
    print(f"\nSERIAL NUMBER UPDATED TO: {serial_number}")
    print(f"NUMBER OF BATTERIES UPDATED TO: {num_batteries}")

def password_cracker():
    #User input statements, it is required for the user to put spaces between characters. e.g. 'abcdef' invalid. 'a b c d e f' valid.
    third_column = input("Enter all letters from the third column: ").lower()
    third_column = third_column.split()

    #The split statements splits the user-input string into a list using blankspaces as the discriminator.
    fifth_column = input("Enter all letters from the fifth column: ").lower()
    fifth_column = fifth_column.split()

    #Outermost for loop iterates through the third column list, checking for specific letters.
    for i in range(len(third_column)):
        
        if third_column[i] == "a":

            #If certain letters are found in the third column, a similar loop then iterates through the fifth column list.
            for j in range(len(fifth_column)):

                #If a certain letter is then found in the fifth column, print the potential solution.
                if fifth_column[j] == "e":
                    print("place")
                elif fifth_column[j] == "l":
                    print("small")
                elif fifth_column[j] == "n":
                    print("again or learn")
                elif fifth_column[j] == "t":
                    print("plant")

        elif third_column[i] == "e":

            for j in range(len(fifth_column)):

                if fifth_column[j] == "e":
                    print("there, these, or where")
                elif fifth_column[j] == "l":
                    print("spell")
                elif fifth_column[j] == "r":
                    print("their")
                elif fifth_column[j] == "t":
                    print("great")
                elif fifth_column[j] == "y":
                    print("every")

        elif third_column[i] == "g":

            for j in range(len(fifth_column)):

                if fifth_column[j] == "t":
                    print("right")

        elif third_column[i] == "h":

            for j in range(len(fifth_column)):

                if fifth_column[j] == "r":
                    print("other")
    
        elif third_column[i] == "i":

            for j in range(len(fifth_column)):

                if fifth_column[j] == "e":
                    print("write")
                elif fifth_column[j] == "g":
                    print("thing")
                elif fifth_column[j] == "h":
                    print("which")
                elif fifth_column[j] == "k":
                    print("think")
                elif fifth_column[j] == "l":
                    print("still")
                elif fifth_column[j] == "t":
                    print("point")

        elif third_column[i] == "l":

            for j in range(len(fifth_column)):

                if fifth_column[j] == "w":
                    print("below")

        elif third_column[i] == "o":

            for j in range(len(fifth_column)):

                if fifth_column[j] == "t":
                    print("about")
        
        elif third_column[i] == "r":

            for j in range(len(fifth_column)):

                if fifth_column[j] == "d":
                    print("world")
                elif fifth_column[j] == "e":
                    print("large, or three")
                elif fifth_column[j] == "t":
                    print("first")

        elif third_column[i] == "t":

            for j in range(len(fifth_column)):

                if fifth_column[j] == "r":
                    print("after, or water")

        elif third_column[i] == "u":

            for j in range(len(fifth_column)):

                if fifth_column[j] == "d":
                    print("could, found, sound, or would")
                elif fifth_column[j] == "e":
                    print("house")
                elif fifth_column[j] == "y":
                    print("study")

        elif third_column[i] == "v":

            for j in range(len(fifth_column)):

                if fifth_column[j] == "r":
                    print("never")

        #This approach only narrows down the potential solutions. The defuser will have to look at the other columns to further narrow down the actual answer.

def maze_solver():

    #This open statement opens my txt file to display ASCII art mazes. It opens the file, then creates a list using commas as a discriminator.
    with open('mazeart.txt') as art_file:
        maze_list = art_file.read().split(",")

    #Display the blank maze to familiarize a user with the coordinate system. Then, display basic info.
    print(maze_list[0])
    print("FOR COORDINATES, DO NOT USE PARENTHESIS. JUST LIST NUMBERS. I.E. (1,5), (6,4) SHOULD BE '1564'. ORDER OF COORDINATES DO NOT MATTER.")
    ident = input("COORDINATES OF IDENTIFYING CIRCLES: ")
    
    #Armed with the player input, match the coordinates to the maze.
    match ident:
        case "1564" | "6415":
            print(maze_list[1])
        case "2364" | "6423":
            print(maze_list[2])
        case "4363" | "6343":
            print(maze_list[3])
        case "1316" | "1613":
            print(maze_list[4])
        case "4154" | "5441":
            print(maze_list[5])
        case "3256" | "5632":
            print(maze_list[6])
        case "2126" | "2621":
            print(maze_list[7])
        case "3346" | "4633":
            print(maze_list[8])
        case "1235" | "3512":
            print(maze_list[9])
        case _:
            print("Invalid coordinates, try again.")

    #It is up to the expert to guide the defuser through the maze. It'd take an AI to do the rest.

def whos_on_first():
    #local variable bank.
    located = False
    decrypted = False
    stage = 1

    #Self explanatory while loop. And no, I don't think a zero index is appropriate here.
    while stage <= 3:

        #This first loop will not let you go until you enter a word that works, or the exit command. If you fuck up and type 'yse', it'll default to case_.
        while located == False:
            locate = input("\nWORD ON DISPLAY: ")
            locate = locate.lower()                 #Sidenote, all input should be .lower() to ensure homogenity of input.

            match locate:

                #Upon inputting a correct word, the user is told what to read, and the variables are toggled to move to phase two.
                case "" | "leed" | "reed" | "they're":
                    print("BOTTOM LEFT.")
                    located = True
                    decrypted = False
                case "cee" | "display" | "hold on" | "lead" | "no" | "says" | "see" | "there" | "you are":
                    print("BOTTOM RIGHT.")
                    located = True
                    decrypted = False
                case "led" | "nothing" | "they are" | "yes":
                    print("MIDDLE LEFT.")
                    located = True
                    decrypted = False
                case "blank" | "read" | "red" | "their" | "you" | "you're" | "your":
                    print("MIDDLE RIGHT.")
                    located = True
                    decrypted = False
                case "ur":
                    print("UPPER LEFT.")
                    located = True
                    decrypted = False
                case "c" | "okay" | "first":
                    print("UPPER RIGHT.")
                    located = True
                    decrypted = False

                #Default case to catch user input error
                case _:
                    print("ERROR: CHECK SPELLING. ENTER [X] TO QUIT. ENTER ANYTHING ELSE TO CONTINUE.")
                    cont = input()
                    cont = cont.lower()

                    if cont == "x":
                        located = True
                        decrypted = True
                        stage = 4

        #Phase two starts here.
        #This second loop is similar to the first, it won't let you go until you enter something valid or the exit command. 
        while decrypted == False:

            decrypt = input("WORD: ")
            decrypt = decrypt.lower()

            #Similar structure as phase one as well.
            match decrypt:
                case "blank":
                    print("WAIT, RIGHT, OKAY, MIDDLE, BLANK")
                    decrypted = True
                    stage += 1 
                    located = False
                case "done":
                    print("SURE, UH HUH, NEXT, WHAT? YOUR, UR, YOU'RE, HOLD, LIKE, YOU, U, YOU ARE, UH UH, DONE")
                    decrypted = True
                    stage += 1 
                    located = False
                case "first":
                    print("LEFT, OKAY, YES, MIDDLE, NO, RIGHT, NOTHING, UHHH, WAIT, READY, BLANK, WHAT, PRESS, FIRST")
                    decrypted = True
                    stage += 1 
                    located = False
                case "hold":
                    print("YOU ARE, U, DONE, UH UH, YOU, UR, SURE, WHAT?, YOU'RE, NEXT, HOLD")
                    decrypted = True
                    stage += 1
                    located = False
                case "left":
                    print("RIGHT, LEFT")
                    decrypted = True
                    stage += 1
                    located = False
                case "like":
                    print("YOU'RE, NEXT, U, UR, HOLD, DONE, UH UH, WHAT?, UH HUH, YOU, LIKE")
                    decrypted = True
                    stage += 1
                    located = False
                case "middle":
                    print("BLANK, READY, OKAY, WHAT, NOTHING, PRESS, NO, WAIT, LEFT, MIDDLE")
                    decrypted = True
                    stage += 1
                    located = False
                case "next":
                    print("WHAT?, UH HUH, UH UH, YOUR, HOLD, SURE, NEXT")
                    decrypted = True
                    stage += 1
                    located = False
                case "no":
                    print("BLANK, UHHH, WAIT, FIRST, WHAT, READY, RIGHT, YES, NOTHING, LEFT, PRESS, OKAY, NO")
                    decrypted = True
                    stage += 1
                    located = False
                case "nothing":
                    print("UHHH, RIGHT, OKAY, MIDDLE, YES, BLANK, NO, PRESS, LEFT, WHAT, WAIT, FIRST, NOTHING")
                    decrypted = True
                    stage += 1
                    located = False
                case "okay":
                    print("MIDDLE, NO, FIRST, YES, UHHH, NOTHING, WAIT, OKAY")
                    decrypted = True
                    stage += 1
                    located = False
                case "press":
                    print("RIGHT, MIDDLE, YES, READY, PRESS")
                    decrypted = True
                    stage += 1
                    located = False
                case "ready":
                    print("YES, OKAY, WHAT, MIDDLE, LEFT, PRESS, RIGHT, BLANK, READY")
                    decrypted = True
                    stage += 1
                    located = False
                case "right":
                    print("YES, NOTHING, READY, PRESS, NO, WAIT, WHAT, RIGHT")
                    decrypted = True
                    stage += 1
                    located = False
                case "sure":
                    print("YOU ARE, DONE, LIKE, YOU'RE, YOU, HOLD, UH HUH, UR, SURE")
                    decrypted = True
                    stage += 1
                    located = False
                case "u":
                    print("UH HUH, SURE, NEXT, WHAT?, YOU'RE, UR, UH UH, DONE, U")
                    decrypted = True
                    stage += 1
                    located = False
                case "uh huh":
                    print("UH HUH")
                    decrypted = True
                    stage += 1
                    located = False
                case "uh uh":
                    print("UR, U, YOU ARE, YOU'RE, NEXT, UH UH")
                    decrypted = True
                    stage += 1
                    located = False
                case "uhhh":
                    print("READY, NOTHING, LEFT, WHAT, OKAY, YES, RIGHT, NO, PRESS, BLANK, UHHH")
                    decrypted = True
                    stage += 1
                    located = False
                case "ur":
                    print("DONE, U, UR")
                    decrypted = True
                    stage += 1
                    located = False
                case "wait":
                    print("UHHH, NO, BLANK, OKAY, YES, LEFT, FIRST, PRESS, WHAT, WAIT")
                    decrypted = True
                    stage += 1
                    located = False
                case "what":
                    print("UHHH, WHAT")
                    decrypted = True
                    stage += 1
                    located = False
                case "what?":
                    print("YOU, HOLD, YOU'RE. YOUR, U, DONE, UH UH, LIKE, YOU ARE, UH HUH, UR, NEXT, WHAT?")
                    decrypted = True
                    stage += 1
                    located = False
                case "yes":
                    print("OKAY, RIGHT, UHHH, MIDDLE, FIRST, WHAT, PRESS, READY, NOTHING, YES")
                    decrypted = True
                    stage += 1
                    located = False
                case "you":
                    print("SURE, YOU ARE, YOUR, YOU'RE, NEXT, UH HUH, UR, HOLD, WHAT?, YOU")
                    decrypted = True
                    stage += 1
                    located = False
                case "you are":
                    print("YOUR, NEXT, LIKE, UH HUH, WHAT?, DONE, UH UH, HOLD, YOU, U, YOU'RE, SURE, UR, YOU ARE")
                    decrypted = True
                    stage += 1
                    located = False
                case "you're":
                    print("YOU, YOU'RE")
                    decrypted = True
                    stage += 1
                    located = False
                case "your":
                    print("UH UH, YOU ARE, UH HUH, YOUR")
                    decrypted = True
                    stage += 1
                    located = False
                case _:
                    print("ERROR: CHECK SPELLING. ENTER [X] TO QUIT. ENTER ANYTHING ELSE TO CONTINUE.")
                    cont = input()
                    cont = cont.lower()

                    if cont == "x":
                        decrypted = True
                        stage = 4

def memory_game():
    """
    So, an array is created to memorize everything. Every round, the program first asks what the screen displays.
    Upon being told what is on the screen, the program will tell you what button to press.
    On the same line, it will ask you what the label/position is, as that info is relevant to later rounds.
    The user needs to be careful not to accidently hit enter, as there are no failsafes here.

    Once the user inputs the label/position, the program stores the data as a tuple in the 'memory' list.
    Tuple structure is (label, position).

    e.g. The screen initially displays a 1.
        PRESS BUTTON IN POSITION 2. LABELED: 4  --> memory at this point is [(4,2)]
        The screen displays a 3.
        PRESS BUTTON IN POSITION 1. LABELED: 2 --> memory at this point is [(4,2),(2,1)]

    Let us rewind. Instead of the screen displaying a 3 on round two, what if:
        The screen displays a 2.
        "PRESS BUTTON IN POSITION {memory[0][1]}. LABELED: ?
        This f string reads what this ^ is, and auto formats it into a string. Pretty cool stuff.

        Remember, memory looks like [(4,2)] at this point.
        memory[0] = (4,2)

        Now we need to pick the part of the tuple that corresponds to the position, NOT label. Therefore,
        memory[0][1] = 2.

        f string auto formats, so what the user actually sees (in this case):
        PRESS BUTTON IN POSITION 2. LABELED:

        Simple.
    """

    #Another local variable bank.
    memory = []
    stage = 1

    #Another outer loop that isn't zero indexed.
    while stage <= 5:

        query = input("\nDISPLAYED NUMBER: ")

        if stage == 1:
            match query:
                case "1" | "2":
                    memory.append((input("PRESS BUTTON IN POSITION 2. LABELED: "),2))
                case "3":
                    memory.append((input("PRESS BUTTON IN POSITION 3. LABELED: "),3))
                case "4":
                    memory.append((input("PRESS BUTTON IN POSITION 4. LABELED: "),4))
    
        if stage == 2:
            match query:
                case "1":
                    memory.append((4,input("PRESS BUTTON LABELED 4. POSITION: ")))
                case "2" | "4":
                    memory.append((input(f"PRESS BUTTON IN POSITION {memory[0][1]}. LABELED: "),memory[0][1]))
                case "3":
                    memory.append((input("PRESS BUTTON IN POSITION 1. LABELED: "),1))
                     

        if stage == 3:
            match query:
                case "1":
                    memory.append((memory[1][0],input(f"PRESS BUTTON LABELED {memory[1][0]}. POSITION: ")))
                case "2":
                    memory.append((memory[0][0],input(f"PRESS BUTTON LABELED {memory[0][0]}. POSITION: ")))
                case "3":
                    memory.append((input("PRESS BUTTON IN POSITION 3. LABELED: "),3))
                case "4":
                    memory.append((4,input("PRESS BUTTON LABELED 4. POSITION: ")))
                     
        
        if stage == 4:
            match query:
                case "1":
                    memory.append((input(f"PRESS BUTTON IN POSITION {memory[0][1]}. LABELED: "),memory[0][1]))
                case "2":
                    memory.append((input("PRESS BUTTON IN POSITION 1. LABELED: "),1))
                case "3" | "4":
                    memory.append((input(f"PRESS BUTTON IN POSITION {memory[1][1]}. LABELED: "),memory[1][1]))
                     

        if stage == 5:
            match query:
                case "1":
                    print(f"PRESS BUTTON LABELED {memory[0][0]}.")
                case "2":
                    print(f"PRESS BUTTON LABELED {memory[1][0]}.")
                case "3":
                    print(f"PRESS BUTTON LABELED {memory[3][0]}.")
                case "4":
                    print(f"PRESS BUTTON LABELED {memory[2][0]}.")

        stage += 1

def simple_wires():
    import swire

def complicated_wires():
    done = False
    print("CONFIGURATION NEEDED:")
    parallel = input("IS THE BOMB EQUIPPED WITH A PARALLEL PORT? (Y/N) ").lower()
    global serial_number
    if serial_number == "":
        serial = input("IS THE LAST DIGIT OF THE SERIAL NUMBER EVEN? (Y/N) ").lower()
    else:
        num = int(serial_number[-1])
        if num % 2 == 0:
            serial = "y"
        else:
            serial = "n"
    global num_batteries
    if num_batteries == 0:
        num_batteries = int(input("HOW MANY BATTERIES ARE ON THE BOMB? "))

    print("BOMB CONFIGURED. ENTER [X] TO EXIT MODULE. ENTER [H] FOR HELP. DESCRIBE WIRE OTHERWISE.")
    while done == False:
        wire = input("\nWIRE: ").lower()

        if (wire == "br" or wire == "rb" or wire == "lbr" or wire == "lrb" or wire == "blr" or wire == "brl" or wire == "rlb" or wire == "rbl" or wire == "b" or wire == "r"):
            if(serial == "y"):
                print("CUT")
            else:
                print("DO NOT CUT")

        elif (wire == "brs" or wire == "bsr" or wire == "rbs" or wire == "rsb" or wire == "sbr" or wire == "srb" or wire == "lb" or wire == "bl" or wire == "lbs" or wire == "lsb" or wire == "bsl" or wire == "bls" or wire == "sbl" or wire == "slb"):
            if(parallel == "y"):
                print("CUT")
            else:
                print("DO NOT CUT")

        elif (wire == "lbrs" or wire == "lbsr" or wire == "lrbs" or wire == "lrsb" or wire == "lsbr" or wire == "lsrb" or wire == "blsr" or wire == "blrs" or wire == "brsl" or wire == "brls" or wire == "bsrl" or wire == "bslr" or wire == "rlbs" or wire == "rlsb" or wire == "rbls" or wire == "rbsl" or wire == "rslb" or wire == "rsbl" or wire == "slrb" or wire == "slbr" or wire == "sbrl" or wire == "sblr" or wire == "srbl" or wire == "srlb" or wire == "bs" or wire == "sb" or wire == "lw" or wire == "wl"):
            print("DO NOT CUT")

        elif (wire == "ls" or wire == "sl" or wire == "lr" or wire == "rl" or wire == "lrs" or wire == "lsr" or wire == "rls" or wire == "rsl" or wire == "srl" or wire == "slr" or wire == "lws" or wire == "lsw" or wire == "wsl" or wire == "wls" or wire == "swl" or wire == "slw"):
            if(num_batteries >= 2):
                print("CUT")
            else:
                print("DO NOT CUT")

        elif (wire == "w" or wire == "ws" or wire == "sw" or wire == "rs" or wire == "sr"):
            print("CUT")

        elif wire == "x":
            done = True

        elif wire == "h":
            print("SYNTAX IS AS FOLLOWS:\nUSE THE FIRST LETTER OF AN ADJECTIVE TO DESCRIBE WIRE. ORDER DOESN'T MATTER. REMEMBER, ONLY SPECIFY A WIRE IS WHITE IF IT IS COMPLETELY WHITE. CANDY CANE WIRES ARE ONLY RED, OR BLUE.\nEXAMPLES:\nA RED WIRE WITH AN LED == rl\nA BLUE WIRE WITH LED AND STAR == bls")

        else:
            print("ERROR: SYNTAX NOT RECOGNIZED.")

def wire_sequence():
    print("ENTER [X] TO QUIT.")
    solved = False
    red_count = 0
    red_seq = ["C","B","A","A OR C","B","A OR C","YES","A or B","B"]
    blue_count = 0
    blue_seq = ["B","A OR C","B","A","B","B OR C","C","A OR C","A"]
    black_count = 0
    black_seq = ["YES","A OR C","B","A OR C","B","B OR C","A OR B","C","C"]
    while solved == False:
        wire = input("WIRE: ").lower()
        match wire:
            case "red" | "r":
                print(f"CUT: {red_seq[red_count]}")
                red_count += 1

            case "blue" | "b":
                print(f"CUT: {blue_seq[blue_count]}")
                blue_count += 1
            
            case "black" | "k":
                print(f"CUT: {black_seq[black_count]}")
                black_count += 1

            case "x":
                solved = True

            case _:
                print("ERROR: SYNTAX NOT RECOGNIZED.")

def button():
    print("CONFIGURATION NEEDED:")
    color = input("COLOR: ").lower()
    label = input("LABEL: ").lower()
    global num_batteries
    if num_batteries == 0:
        num_batteries = int(input("NUMBER OF BATTERIES: "))

    if label == "abort" and color == "blue":
        print("HOLD. RELEASE ON [YELLOW | 5] [BLUE | 4] [OTHER | 1]")

    elif label == "detonate" and num_batteries > 1:
        print("PRESS AND IMMEDIATELY RELEASE.")

    elif color == "white":
        car_indicator = input("CAR INDICATOR LIT? (Y/N) ").lower()
        if car_indicator == "y":
            print("HOLD. RELEASE ON [YELLOW | 5] [BLUE | 4] [OTHER | 1]")
        else:
            if num_batteries > 2:
                frk_indicator = input("FRK INDICATOR LIT? (Y/N) ").lower()
                if frk_indicator == "y":
                    print("PRESS AND IMMEDIATELY RELEASE.")
                else:
                    if label == "hold" and color == "red":
                        print("PRESS AND IMMEDIATELY RELEASE.")
                    else:
                        print("HOLD. RELEASE ON [YELLOW | 5] [BLUE | 4] [OTHER | 1]")

    elif num_batteries > 2:
        frk_indicator = input("FRK INDICATOR LIT? (Y/N) ").lower()
        if frk_indicator == "y":
            print("PRESS AND IMMEDIATELY RELEASE.")
        else:
            if label == "hold" and color == "red":
                print("PRESS AND IMMEDIATELY RELEASE.")
            else:
                print("HOLD. RELEASE ON [YELLOW | 5] [BLUE | 4] [OTHER | 1]")

    elif label == "hold" and color == "red":
        print("PRESS AND IMMEDIATELY RELEASE.")
    else:
        print("HOLD. RELEASE ON [YELLOW | 5] [BLUE | 4] [OTHER | 1]")

def simon_says():
    memory = []
    print("CONFIGURATION NEEDED:")
    strikes = int(input("CURRENT NUMBER OF STRIKES: "))
    global serial_number
    if serial_number == "":
        vowel = input("SERIAL NUMBER CONTAINS A VOWEL? (Y/N) ").lower()
    else:
        if "a" in serial_number or "e" in serial_number or "i" in serial_number or "o" in serial_number or "u" in serial_number:
            vowel = "y"
    print("BOMB CONFIGURED. ENTER [X] TO QUIT. ENTER [S] TO INCREMENT STRIKE COUNTER. ENTER [S-] TO DECREMENT STRIKE COUNTER. OTHERWISE ENTER COLOR.")
    while True:
        color = input("COLOR: ").lower()
        if color == "x":
            break
        elif color == "s":
            strikes += 1
            print(f"STRIKE COUNTER INCREMENTED TO {strikes}")
            memory.clear()
        elif color == "s-":
            strikes -= 1
            print(f"STRIKE COUNTER DECREASED TO {strikes}")
            memory.clear()
        else:
            if strikes == 0:
                if vowel == "y":
                    match color:
                        case "red" | "r":
                            memory.append("BLUE")
                        case "blue" | "b":
                            memory.append("RED")
                        case "green" | "g":
                            memory.append("YELLOW")
                        case "yellow" | "y":
                            memory.append("GREEN")

                else:
                    match color:
                        case "red" | "r":
                            memory.append("BLUE")
                        case "blue" | "b":
                            memory.append("YELLOW")
                        case "yellow" | "y":
                            memory.append("RED")
                        case "green" | "g":
                            memory.append("GREEN")

            elif strikes == 1:
                if vowel == "y":
                    match color:
                        case "red" | "r":
                            memory.append("YELLOW")
                        case "blue" | "b":
                            memory.append("GREEN")
                        case "yellow" | "y":
                            memory.append("RED")
                        case "green" | "g":
                            memory.append("BLUE")
                
                else:
                    match color:
                        case "red" | "r":
                            memory.append("RED")
                        case "blue" | "b":
                            memory.append("BLUE")
                        case "yellow" | "y":
                            memory.append("GREEN")
                        case "green" | "g":
                            memory.append("YELLOW")

            elif strikes == 2:
                if vowel == "y":
                    match color:
                        case "red" | "r":
                            memory.append("GREEN")
                        case "blue" | "b":
                            memory.append("RED")
                        case "yellow" | "y":
                            memory.append("BLUE")
                        case "green" | "g":
                            memory.append("YELLOW")

                else:
                    match color:
                        case "red" | "r":
                            memory.append("YELLOW")
                        case "blue" | "b":
                            memory.append("GREEN")
                        case "yellow" | "y":
                            memory.append("RED")
                        case "green" | "g":
                            memory.append("BLUE")

        print(memory)

def morse():
    print("ENTER ONE LETTER AT A TIME, NO SPACES. ENTER [X] TO QUIT. ENTER [L] TO LOOKUP WORDS & FREQUENCIES. ENTER [C] TO CLEAR MEMORY.")
    morse_to_letter = {
        '.-':"A",
        '-...':"B",
        '-.-.':"C",
        '-..':"D",
        '.':"E",
        '..-.':"F",
        '--.':"G",
        '....':"H",
        '..':"I",
        '-.-':"K",
        '.-..':"L",
        '--':"M",
        '-.':"N",
        '---':"O",
        '.-.':"R",
        '...':"S",
        '-':"T",
        '...-':"V",
        '-..-':"X"
    }
    word_to_freq = {
        "shell":"3.505",
        "halls":"3.515",
        "slick":"3.522",
        "trick":"3.532",
        "boxes":"3.535",
        "leaks":"3.542",
        "strobe":"3.545",
        "bistro":"3.552",
        "flick":"3.555",
        "bombs":"3.565",
        "break":"3.572",
        "brick":"3.575",
        "steak":"3.582",
        "sting":"3.592",
        "vector":"3.595",
        "beats":"3.600"
    }
    bank = []
    while True:
        guess = input("LETTER IN MORSE: ").lower()
        if guess == "x":
            break

        elif guess == "l":
            print(word_to_freq)

        elif guess == "c":
            bank.clear()

        else:
            try:
                bank.append(morse_to_letter[guess])
            except KeyError:
                print("ERROR: INVALID LETTER.")
            print(bank)

def symbols():
    import symbols
    
def vent():
    print("REPLY NO TO DETONATE, YES TO VENT GAS.")

def knob():
    print("DO NOT ZERO INDEX. FIND THE INDEX OF THE FIRST OCCURENCE OF A DOUBLE LIT COLUMN. IF NO DOUBLE LIT COLUMN, ENTER [0].")
    pos = input("COLUMN: ")

    match pos:
        case "0" | "2":
            print("DOWN.")
        case "1":
            print("RIGHT.")
        case "3":
            print("UP.")
        case "4":
            print("LEFT.")
        case _:
            print("INVALID COLUMN INDEX.")

def help():
    print("TO PRECONFIGURE SOME COMMON BOMB ATTRIBUTES, ENTER [CONFIG]")
    print("TO CRACK A PASSWORD, ENTER [PASSWORD]")
    print("TO PRINT A MAZE, ENTER [MAZE]")
    print("TO PLAY WHO'S ON FIRST, ENTER [FIRST]")
    print("TO PLAY MEMORY, ENTER [MEMORY]")
    print("TO CUT SIMPLE WIRES, ENTER [SWIRE]")
    print("TO CUT COMPLICATED WIRES, ENTER [CWIRE]")
    print("TO CUT A WIRE SEQUENCE, ENTER [SEQUENCE]")
    print("TO PRESS A BUTTON, ENTER [BUTTON]")
    print("TO PLAY SIMON SAYS, ENTER [SIMON]")
    print("TO DECRYPT MORSE CODE, ENTER [MORSE]")
    print("TO SEE A LIST OF SYMBOLS, ENTER [SYMBOLS]")
    print("TO ANSWER A YES OR NO QUESTION, ENTER [VENT]")
    print("TO CONFIGURE A KNOB, ENTER [KNOB]")
    print("TO DISCHARGE A CAPACITOR, TRY THINKING ABOUT IT. IF THAT FAILS, PRESS THE LEVER.")

debug = False
print("BEFORE YOU CAN START DEFUSING, PLEASE READ THE TERMS AND CONDITIONS:")
print("\n-----------TERMS AND CONDITIONS-----------")
print("THE UNAUTHORIZED REPRODUCTION OR DISTRIBUTION OF A COPYRIGHTED WORK IS ILLEGAL.\nCRIMINAL COPYRIGHT INFRINGEMENT, INCLUDING INFRINGEMENT WITHOUT MONETARY GAIN, IS INVESTIGATED BY THE FBI \nAND IS PUNISHABLE BY UP TO 5 YEARS IN FEDERAL PRISON AND A FINE OF $250,000.")
print("BY USING THIS DEFUSER, THE 'EXPERT' RECOGNIZES THAT PRISM IS NOT RESPONSIBLE FOR ANY BOMBS THAT FAIL TO BE DEFUSED.")
print("THIS DEFUSER IS ONLY CERTIFIED TO DEFUSE NON MODDED BOMBS AS PER DEFUSAL MANUAL VERSION 241.")
tc = input("\nDO YOU AGREE TO THE TERMS AND CONDITIONS? (Y/N) ").lower()
if tc == "y":
    debug = True
    print("\nWELCOME TO THE DEFUSER. ENTER [HELP] FOR HELP. ENTER [CONFIG] TO PRECONFIGURE THE BOMB. ENTER [QUIT] TO QUIT. HAPPY DEFUSING.")

while debug == True:
    
    query = input("\n").lower()

    match query:

        case "help":
            help()

        case "config":
            config()

        case "password":
            password_cracker()

        case "maze":
            maze_solver()

        case "first":
            whos_on_first()

        case "memory":
            print("FOLLOW ALL PROMPTS. BE CAREFUL TO NOT ACCIDENTLY ADVANCE PROMPTS.")
            memory_game()

        case "swire":
            simple_wires()

        case "cwire":
            print("PLEASE NOTE: ONLY SPECIFY THAT THE WIRE IS WHITE IF IT IS ONLY WHITE. CONSIDER 'CANDY CANE' WIRES TO BE JUST RED, OR BLUE.\n")
            complicated_wires()

        case "sequence":
            wire_sequence()

        case "button":
            button()

        case "simon":
            simon_says()

        case "morse":
            morse()

        case "symbols":
            symbols()

        case "vent" | "detonate":
            vent()

        case "knob":
            knob()

        case "quit":
            print("THANK YOU FOR USING THE DEFUSER.")
            debug = False