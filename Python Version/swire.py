import pygame

# Boilerplate code to draw the window, and name it "Simple Wire Solver" with the special little icon.
pygame.init()
pygame.display.set_caption("Simple Wire Solver")
pygame.display.set_icon(pygame.image.load("plier.png"))
screen = pygame.display.set_mode((860,720))
clock = pygame.time.Clock()
running = True

width = screen.get_width()
height = screen.get_height()

#Setting the fonts to be used for drawing text on screen later. 
bigfont = pygame.font.SysFont('consolas',70)
regfont = pygame.font.SysFont('consolas',20)
specialfont = pygame.font.SysFont('consolas',58)

#Variables used to keep track of progression through the wire color cycle. I feel there is a better solution out there that isnt as ugly, but I've yet to think of it.
wire1count = 0
wire2count = 0
wire3count = 0
wire4count = 0
wire5count = 0
wire6count = 0
switch_state = "n"

def draw_big_text(text,x,y,color,font):
    #Function that makes a giant block of text for the YES/NO switch.
    textobj = font.render(text,1,color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    screen.blit(textobj,textrect)

def draw_text(text,x,y):
    #Function that creates a regular block of text for everything else. 
    textobj = regfont.render(text,1,(255,255,255))
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    screen.blit(textobj,textrect)

def draw_switch(state):
    #Function that draws the YES/NO switch
    #If statement determines whether the switch displays the YES or NO state.
    if state == "y":
        pygame.draw.rect(screen,(50,50,50), pygame.Rect(545,105,300,75))
        pygame.draw.rect(screen,(0,185,0), pygame.Rect(550,110,265,65))
        pygame.draw.rect(screen,(100,100,100), pygame.Rect(815,110,25,65))
        draw_big_text("YES",640,112,(0,100,0),bigfont)
    elif state == "n":
        pygame.draw.rect(screen,(50,50,50), pygame.Rect(545,105,300,75))
        pygame.draw.rect(screen,(185,0,0), pygame.Rect(575,110,265,65))
        pygame.draw.rect(screen,(100,100,100), pygame.Rect(550,110,25,65))
        draw_big_text("NO",660,112,(100,0,0),bigfont)

def flash_screen(text,x,y,font):
    #Function to redraw certain background elements so the display screen doesn't turn to jibberish after two rounds, as well as communicate to the user what the solution is.
    pygame.draw.rect(screen,(0,0,0), pygame.Rect(30,580,800,100))
    draw_big_text(text,x,y,(255,255,255),font)

def wire_init():
    #This function is the very first function called, draws all of the pretty art.
    #This block makes the background grey, and draws the two dark grey wire-connecting thingies.
    screen.fill("gray")
    pygame.draw.rect(screen,(50,50,50), pygame.Rect(30,30,25,500))
    pygame.draw.rect(screen,(50,50,50), pygame.Rect(500,30,25,500))

    #This block draws the wires themselves.
    pygame.draw.rect(screen,colors[0], wire1)
    pygame.draw.rect(screen,colors[0], wire2)
    pygame.draw.rect(screen,colors[0], wire3)
    pygame.draw.rect(screen,colors[0], wire4)
    pygame.draw.rect(screen,colors[0], wire5)
    pygame.draw.rect(screen,colors[0], wire6)

    #This block draws the screen that reveals the solution to the player.
    pygame.draw.rect(screen,(50,50,50), pygame.Rect(20,570,820,120))
    pygame.draw.rect(screen,(0,0,0), pygame.Rect(30,580,800,100))

    #This draws a plate that asks the user a question, and insists the user flip the YES/NO switch to the corresponding state.
    pygame.draw.rect(screen,(145,115,65), pygame.Rect(545,72,300,25))
    draw_text("LAST DIGIT OF SERIAL ODD?",560,75)
    draw_switch(switch_state)
    
    #This draws the SOLVE button
    pygame.draw.rect(screen,(50,50,50),pygame.Rect(545,200,300,300))
    pygame.draw.circle(screen,(0,0,180),(695,350),130)
    draw_big_text("SOLVE",600,320,(255,255,255),bigfont)

def wire_del(wire):
    #This function redraws the exposed background when a wire is deleted.
    #This block redraws the two dark grey wire-connecting thingies.
    pygame.draw.rect(screen,(50,50,50), pygame.Rect(30,30,25,500))
    pygame.draw.rect(screen,(50,50,50), pygame.Rect(500,30,25,500))

    #Since we redrew the wire-connecting thingies, they are now on top of the remaining wire elements, so first we redraw the wires that can't be removed.
    pygame.draw.rect(screen,colors[wire1count], wire1)
    pygame.draw.rect(screen,colors[wire2count], wire2)
    pygame.draw.rect(screen,colors[wire3count], wire3)

    #If statement that determines which wire we want painted out.
    
    
    if wire == 4:
        #Once we've determined the wire we want, draw a rectangle that is the same color as the background to cover up the previous wire.
        pygame.draw.rect(screen,"gray",(55,300,445,25))

        #But! What if the other wires that could be painted out aren't supposed to be? We need to redraw those too!
        #Unless of course, it also needs to stay invisible, so cover it up again just to be safe.
        if wire5count == -1:
            pygame.draw.rect(screen,"gray",(55,375,445,25))
        else:
            pygame.draw.rect(screen,colors[wire5count], wire5)
        if wire6count == -1:
            pygame.draw.rect(screen,"gray",(55,450,445,25))
        else:
            pygame.draw.rect(screen,colors[wire6count], wire6)

    if wire == 5:
        if wire4count == -1:
            pygame.draw.rect(screen,"gray",(55,300,445,25))
        else:
            pygame.draw.rect(screen,colors[wire4count], wire4)
        pygame.draw.rect(screen,"gray",(55,375,445,25))
        if wire6count == -1:
            pygame.draw.rect(screen,"gray",(55,450,445,25))
        else:
            pygame.draw.rect(screen,colors[wire6count], wire6)

    if wire == 6:
        if wire4count == -1:
            pygame.draw.rect(screen,"gray",(55,300,445,25))
        else:
            pygame.draw.rect(screen,colors[wire4count], wire4)
        if wire5count == -1:
            pygame.draw.rect(screen,"gray",(55,375,445,25))
        else:
            pygame.draw.rect(screen,colors[wire5count], wire5)
        pygame.draw.rect(screen,"gray",(55,450,445,25))

def wire_logic():
    #This function does all of the thinking to tell the user what wire to cut given the input wires.

    global switch_state                                                          #Reference the state of the YES/NO switch, as it determines logic.
    count_to_color = {-1:"g",0:"r",1:"b",2:"y",3:"k",4:"w"}                      #Dictionary that maps color of the wire to a specific number.
    lineup = []                                                                  #Create a blank list to soon populate
    wires = [wire1count,wire2count,wire3count,wire4count,wire5count,wire6count]  #Create a list that contains the numeric data that represents the submitted colors of wires.
    
    for i in range(len(wires)):                                                  #For every number in the list, append a letter to a new list using the aforementioned dictionary to correlate. 
        lineup.append(count_to_color[wires[i]])                                  #Upon review, perhaps this is a useless extra step. I'll revisit this later.

    final_list = [x for x in lineup if x != 'g']                                 #Now armed with a list of colors, remove the wires colored "green" because thats code for a removed wire.
    num_wires = len(final_list)                                                  #With the removed wires, well, removed; count the remaining wires.


    #Case-match the number of wires, and work down the logic tree. 
    match num_wires:
        case 3:
            if not "r" in final_list:                                       #If no red wires
                flash_screen("CUT THE SECOND WIRE.",55,600,bigfont)
            elif final_list[-1] == "w":                                     #Else, if the final wire is white
                flash_screen("CUT THE FINAL WIRE.",75,600,bigfont)
            elif final_list.count("b") > 1:                                 #Else, if there is more than one blue wire
                flash_screen("CUT THE FINAL BLUE WIRE.",53,600,specialfont)
            else:                                                           #Ok, it must be:
                flash_screen("CUT THE FINAL WIRE.",75,600,bigfont)

        case 4:
            if final_list.count("r") > 1 and switch_state == "y":           #If there is more than one red wire, and the switch state is YES
                flash_screen("CUT THE FINAL RED WIRE.",65,600,specialfont)
            elif final_list[-1] == "y" and "r" not in final_list:           #Else, if the final wire is yellow and there are no red wires
                flash_screen("CUT THE FIRST WIRE.",75,600,bigfont)
            elif final_list.count("b") == 1:                                #Else, if there is exactly one blue wire
                flash_screen("CUT THE FIRST WIRE.",75,600,bigfont)
            elif final_list.count("y") > 1:                                 #Else, if there is more than one yellow wire
                flash_screen("CUT THE FINAL WIRE.",75,600,bigfont)
            else:                                                           #Ok, it must be:
                flash_screen("CUT THE SECOND WIRE.",55,600,bigfont)

        case 5:
            if final_list[-1] == "k" and switch_state == "y":               #If the final wire is black, and the switch state is YES
                flash_screen("CUT THE FOURTH WIRE.",55,600,bigfont)
            elif final_list.count("r") == 1 and final_list.count("y") > 1:  #Else, if there is exactly one red wire, and there is more than 1 yellow wire
                flash_screen("CUT THE FIRST WIRE.",75,600,bigfont)
            elif not "k" in final_list:                                     #Else, if there are no black wires
                flash_screen("CUT THE SECOND WIRE.",55,600,bigfont)
            else:                                                           #Ok, it must be:
                flash_screen("CUT THE FIRST WIRE.",75,600,bigfont)

        case 6:
            if not "y" in final_list and switch_state == "y":               #If there are no yellow wires, and the switch state is YES
                flash_screen("CUT THE THIRD WIRE.",75,600,bigfont)
            elif final_list.count("y") == 1 and final_list.count("w") > 1:  #Else, if there is exactly one yellow wire, and there is more than one white wire
                flash_screen("CUT THE FOURTH WIRE.",55,600,bigfont)
            elif not "r" in final_list:                                     #Else, if there are no red wires
                flash_screen("CUT THE FINAL WIRE.",75,600,bigfont)
            else:                                                           #Ok, it must be:
                flash_screen("CUT THE FOURTH WIRE.",55,600,bigfont)

#Variables that set the dimensions of the rectangles that constitute the wires.
wire1 = pygame.Rect(45,75,465,25)
wire2 = pygame.Rect(45,150,465,25)
wire3 = pygame.Rect(45,225,465,25)
wire4 = pygame.Rect(45,300,465,25)
wire5 = pygame.Rect(45,375,465,25)
wire6 = pygame.Rect(45,450,465,25)

#List of colors to paint the wires, in the order to cycle through them.
colors = [(255,0,0),(0,0,255),(255,255,0),(0,0,0),(255,255,255),(0,255,0)]

wire_init()  #Begin the game.

while running:                                  #This overarching while loop is used so the user can do as many "rounds" as they'd like.
    for event in pygame.event.get():              
        if event.type == pygame.QUIT:           #If the user clicks the exit button, break the loop
            running = False

        mouse = pygame.mouse.get_pos()                                              #Get the current position of the mouse
        dist = pygame.math.Vector2((mouse[0],mouse[1])).distance_to((700,350))      #Mathematically determines if the mouse is hovered over the SOLVE button or not.

        if event.type == pygame.MOUSEBUTTONDOWN:                    #If the user clicks the left mouse button...
            
            if dist <= 130:                                                 #.... and if the user's mouse is over the SOLVE button, figure out the solution
                wire_logic()
            
            if 545 < mouse[0] < 845 and 105 < mouse[1] < 180:               #.... and "if the users mouse is hovered over the YES/NO switch", determine the switch's current state, flip it, and redraw it.
                if switch_state == "n":                                             
                    switch_state = "y"
                    draw_switch(switch_state)
                elif switch_state == "y":
                    switch_state = "n"
                    draw_switch(switch_state)

            if 45 <= mouse[0] <= 510 and 75 <= mouse[1] <= 100:             #.... and "if the users mouse is hovered over the first wire", determine where the wire is in the color cycle, progress through the cycle, and redraw with the new color.
                if wire1count < 4:
                    wire1count +=1
                else:
                    wire1count = 0
                pygame.draw.rect(screen,colors[wire1count],wire1)
                
            if 45 <= mouse[0] <= 510 and 150 <= mouse[1] <= 175:            #Same as above, but for wire 2
                if wire2count < 4:
                    wire2count +=1
                else:
                    wire2count = 0
                pygame.draw.rect(screen,colors[wire2count],wire2)

            if 45 <= mouse[0] <= 510 and 225 <= mouse[1] <= 250:            #Same as above, but for wire 3
                if wire3count < 4:
                    wire3count +=1
                else:
                    wire3count = 0
                pygame.draw.rect(screen,colors[wire3count],wire3)

            if 45 <= mouse[0] <= 510 and 300 <= mouse[1] <= 325:            #.... and "if the users mouse is hovered over the fourth wire", determine where the wire is in the color cycle, progress through the cycle, and redraw with the new color.
                if wire4count < 4:
                    wire4count += 1
                    pygame.draw.rect(screen,colors[wire4count],wire4)
                else:                                                       #Except, this wire is eligible for removal, so instead of cycling back to red, it needs to turn "green" and be painted out.
                    wire4count = -1
                    wire_del(4)

                
            if 45 <= mouse[0] <= 510 and 375 <= mouse[1] <= 400:            #Same as above, but for wire 5
                if wire5count < 4:
                    wire5count += 1
                    pygame.draw.rect(screen,colors[wire5count],wire5)
                else:
                    wire5count = -1
                    wire_del(5)


            if 45 <= mouse[0] <= 510 and 450 <= mouse[1] <= 475:            #Same as above, but for wire 6
                if wire6count < 4:
                    wire6count += 1
                    pygame.draw.rect(screen,colors[wire6count],wire6)
                else:
                    wire6count = -1
                    wire_del(6)

    pygame.display.flip()            #This updates the screen.

pygame.quit()                        #Since the user has broken the loop, terminate the program.