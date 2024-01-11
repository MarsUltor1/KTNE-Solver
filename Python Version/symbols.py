import pygame
import os

#Boilerplate code to initiate the window
pygame.init()
pygame.display.set_caption("Symbols Solver")
screen = pygame.display.set_mode((1152,512))
clock = pygame.time.Clock()
running = True

#Determine and set the fonts to be used for drawing text.
regfont = pygame.font.SysFont('consolas',20)
bigfont = pygame.font.SysFont('consolas',70)

def draw_text(text,x,y):
    #Draws a regular sized textbox at the given coordinates with given text
    textobj = regfont.render(text,1,(0,0,0))
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    screen.blit(textobj,textrect)

def draw_big_text(text,x,y,color,font):
    #Draws a supersized textbox at the given coordinates with given text
    textobj = font.render(text,1,color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    screen.blit(textobj,textrect)

memory = []        #Memory allocated for how the program remembers the layout of the symbols on the board.
flagged = []       #A list that contains a boolean for each symbol in memory, FALSE by default and set to TRUE if flagged by the user.
solutions = [[24,11,25,10,6,8,20],[14,24,20,22,2,8,17],[0,7,22,4,13,25,2],[9,18,26,6,4,17,3],[21,3,26,19,18,16,1],[9,14,23,12,21,15,5]] #A 2D array that contains lists that will determine what order the flagged symbols must be pressed in order to not die.

def symbol_init():
    global memory                                   #Access the global memory
    screen.fill("gray")                             #Paint the background grey.

    index = 0                                       #Create a variable to iterate with
    symbols = os.listdir('symbols')                 #Open the folder containing the images for all the symbols.

    while index < len(symbols):                                     #While the index is less than the number of symbols in the folder (AKA until we've iterated through the whole folder)
        filename = symbols[index]                                   #Create a variable of a file

        if filename.endswith('.png'):                               #If this file is a PNG file:
            with open(os.path.join('symbols', filename)) as f:      

                image = pygame.image.load(f)                              #Load the file
                image = pygame.transform.scale(image, (128,128))          #Scale it to the proper size
                memory.append(image)                                      #Append the image to memory
                flagged.append(False)                                     #Since we're initializing the game, this symbol is NOT flagged by default thus mark it as FALSE.

                if index < 9:                                             #These if statements use the index and simple math to determine where to draw the symbol on the screen.
                    xpos = 128*index                                      #If the index is under 9, keep drawing symbols on the first row by shifting over 128*index pixels.
                    screen.blit(image, (xpos,0))

                elif index < 18:                                          #If the index is greater than nine, but under 18, then print on the second row. Index decremented by nine so the math works out.
                    xpos = 128*(index-9)
                    screen.blit(image, (xpos,128))

                else:                                                     #Finally, we have reached the third row, and the index must be decremented by 18 to ensure it prints in a grid.
                    xpos = 128*(index-18)
                    screen.blit(image, (xpos,256))

        index += 1                                                #Increment the index by one to move to the next file.

    #This code block draws a blue rectangle that says SOLVE for the user to click when they have flagged their symbols.
    pygame.draw.rect(screen,(0,0,180), pygame.Rect(64,400,512,80))
    draw_big_text("SOLVE",218,410,"white",bigfont)

def symbol_logic():
    symbols = []
    working_mem = []
    working_symbols = []
    ordered_solution = []

    if num_flagged == 4:                            #Only begin work if the user has flagged all four symbols.
        for i in range(len(flagged)):               #Iterate through the flagged list to search for what symbols the user flagged.
            if flagged[i] == True:                  #When a flagged symbol is identified:
                symbols.append(i)                       #Append it to the symbols list, which will be used for identifying the unique solution.
                working_symbols.append(i)               #Append it to the working_symbols list, which will be used for correctly ordering the symbols as determined by the unique solution.
    
        for j in range(len(solutions)):             #Iterate through the list of solutions
            if symbols[0] in solutions[j]:          #Check if this arbitrary symbol is present in the selected solution.
                working_mem.append(solutions[j])    #If so, append that solution to the working memory.
        symbols.pop(0)                              #Remove the symbol from the symbols list.

        for k in range(3):                                 #This outer loop iterates three times for the remaining three symbols, where we will determine the unique solution.
            for l in range(len(working_mem)):               #Nested loop iterates through our shortened solution list where we:
                try:                                            #Attempt the following check:
                    if symbols[0] not in working_mem[l]:           #Check if an arbitrary symbol isn't present in this solution, if it isn't: 
                        working_mem.pop(l)                         #Remove this solution from the list.
                except IndexError:                              #If an IndexError arises:
                    continue                                        #Do not crash, move on
            symbols.pop(0)                                  #Remove this symbol from the symbols list.
        
        for z in range(len(working_mem[0])):                    #Now that we have narrowed it down to a unique solution, iterate through it and:
            if working_mem[0][z] in working_symbols:            #If the symbol at solution[index] matches the symbol in the working_symbols list:
                ordered_solution.append(working_mem[0][z])      #Append it to the ordered solution list.

        pygame.draw.rect(screen,(190,190,190), pygame.Rect(640,384,512,128)) #This line draws a big rectangle to coverup and solutions from a previous round.

        #This block draws the earmarks to confirm the order in which the player should relay the info.
        draw_text("1",640,400)
        draw_text("2",768,400)
        draw_text("3",896,400)
        draw_text("4",1024,400)

        #These four statements draws the 4 symbols from memory, in the correct order, at the bottom right corner of the screen.
        sym0 = pygame.transform.scale(memory[ordered_solution[0]], (128,128))
        sym1 = pygame.transform.scale(memory[ordered_solution[1]], (128,128))
        sym2 = pygame.transform.scale(memory[ordered_solution[2]], (128,128))
        sym3 = pygame.transform.scale(memory[ordered_solution[3]], (128,128))

        #These four statements "blend" the symbol PNGs with the earmarks.
        screen.blit(sym0, (640,384))
        screen.blit(sym1, (768,384))
        screen.blit(sym2, (896,384))
        screen.blit(sym3, (1024,384))

        #Clear all the memory for the next round.
        working_mem.clear()
        working_symbols.clear()
        ordered_solution.clear()

def button_flip(x,y,index):
    #This code block makes the background turn a darker shade of grey to let the user know they have flagged that symbol.

    sym = pygame.transform.scale(memory[index], (128,128))                                    #Pull the symbol from memory.
    if flagged[index] == False and num_flagged < 4:                                           #Determine the state of the symbol, so we know whether to darken or lighten the background. Also, check if the user is trying to flag more than 4 symbols.
        pygame.draw.rect(screen,(150,150,150), pygame.Rect(x,y,128,128))                      #This one darkens the background, and flags the symbol
        screen.blit(sym, (x,y))
        flagged[index] = True
    else:
        pygame.draw.rect(screen,(190,190,190), pygame.Rect(x,y,128,128))                      #This one lightens the background, and unflags the symbol
        screen.blit(sym, (x,y))
        flagged[index] = False

symbol_init()  #Begin the game.

while running:                               #While loop to let user play as many rounds as they want.

    num_flagged = flagged.count(True)        #Determine number of flagged symbols
    mouse = pygame.mouse.get_pos()           #Get the coordinates of the mouse

    for event in pygame.event.get():
        if event.type == pygame.QUIT:        #Event that listens for users to quit out, and breaks the loop to safely exit the program.
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:                  #"If the left mouse button is clicked:"
            #ROW 1
            if 0 < mouse[0] < 128 and 0 < mouse[1] < 128:          #Essentially all of these check the mouse coordinates so the game knows what symbol was pressed based on mouse position.
                button_flip(0,0,0)

            if 128 < mouse[0] < 256 and 0 < mouse[1] < 128:
                button_flip(128,0,1)

            if 256 < mouse[0] < 384 and 0 < mouse[1] < 128:
                button_flip(256,0,2)

            if 384 < mouse[0] < 512 and 0 < mouse[1] < 128:
                button_flip(384,0,3)

            if 512 < mouse[0] < 640 and 0 < mouse[1] < 128:
                button_flip(512,0,4)

            if 640 < mouse[0] < 768 and 0 < mouse[1] < 128:
                button_flip(640,0,5)

            if 768 < mouse[0] < 896 and 0 < mouse[1] < 128:
                button_flip(768,0,6)

            if 896 < mouse[0] < 1024 and 0 < mouse[1] < 128:
                button_flip(896,0,7)

            if 1024 < mouse[0] < 1152 and 0 < mouse[1] < 128:
                button_flip(1024,0,8)

            #ROW 2
            if 0 < mouse[0] < 128 and 128 < mouse[1] < 256:
                button_flip(0,128,9)

            if 128 < mouse[0] < 256 and 128 < mouse[1] < 256:
                button_flip(128,128,10)

            if 256 < mouse[0] < 384 and 128 < mouse[1] < 256:
                button_flip(256,128,11)

            if 384 < mouse[0] < 512 and 128 < mouse[1] < 256:
                button_flip(384,128,12)

            if 512 < mouse[0] < 640 and 128 < mouse[1] < 256:
                button_flip(512,128,13)

            if 640 < mouse[0] < 768 and 128 < mouse[1] < 256:
                button_flip(640,128,14)

            if 768 < mouse[0] < 896 and 128 < mouse[1] < 256:
                button_flip(768,128,15)

            if 896 < mouse[0] < 1024 and 128 < mouse[1] < 256:
                button_flip(896,128,16)

            if 1024 < mouse[0] < 1152 and 128 < mouse[1] < 256:
                button_flip(1024,128,17)

            #ROW 3
            if 0 < mouse[0] < 128 and 256 < mouse[1] < 384:
                button_flip(0,256,18)

            if 128 < mouse[0] < 256 and 256 < mouse[1] < 384:
                button_flip(128,256,19)

            if 256 < mouse[0] < 384 and 256 < mouse[1] < 384:
                button_flip(256,256,20)

            if 384 < mouse[0] < 512 and 256 < mouse[1] < 384:
                button_flip(384,256,21)

            if 512 < mouse[0] < 640 and 256 < mouse[1] < 384:
                button_flip(512,256,22)

            if 640 < mouse[0] < 768 and 256 < mouse[1] < 384:
                button_flip(640,256,23)

            if 768 < mouse[0] < 896 and 256 < mouse[1] < 384:
                button_flip(768,256,24)

            if 896 < mouse[0] < 1024 and 256 < mouse[1] < 384:
                button_flip(896,256,25)

            if 1024 < mouse[0] < 1152 and 256 < mouse[1] < 384:
                button_flip(1024,256,26)

            if 64 < mouse[0] < 576 and 400 < mouse[1] < 480:            #This checks if the player clicked on the SOLVE button, in which the game will then solve your inputted symbols.
                symbol_logic()

    pygame.display.flip() #This statement causes the screen to update.

pygame.quit()