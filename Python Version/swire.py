import pygame

pygame.init()
pygame.display.set_caption("Simple Wire Solver")
pygame.display.set_icon(pygame.image.load("plier.png"))
screen = pygame.display.set_mode((860,720))
clock = pygame.time.Clock()
running = True

width = screen.get_width()
height = screen.get_height()

bigfont = pygame.font.SysFont('consolas',70)
regfont = pygame.font.SysFont('consolas',20)
specialfont = pygame.font.SysFont('consolas',58)

wire1count = 0
wire2count = 0
wire3count = 0
wire4count = 0
wire5count = 0
wire6count = 0
switch_state = "n"

def draw_big_text(text,x,y,color,font):
    textobj = font.render(text,1,color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    screen.blit(textobj,textrect)

def draw_text(text,x,y):
    textobj = regfont.render(text,1,(255,255,255))
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    screen.blit(textobj,textrect)

def draw_switch(state):
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
    pygame.draw.rect(screen,(0,0,0), pygame.Rect(30,580,800,100))
    draw_big_text(text,x,y,(255,255,255),font)

def wire_init():
    screen.fill("gray")
    pygame.draw.rect(screen,(50,50,50), pygame.Rect(30,30,25,500))
    pygame.draw.rect(screen,(50,50,50), pygame.Rect(500,30,25,500))

    pygame.draw.rect(screen,colors[0], wire1)
    pygame.draw.rect(screen,colors[0], wire2)
    pygame.draw.rect(screen,colors[0], wire3)
    pygame.draw.rect(screen,colors[0], wire4)
    pygame.draw.rect(screen,colors[0], wire5)
    pygame.draw.rect(screen,colors[0], wire6)

    pygame.draw.rect(screen,(50,50,50), pygame.Rect(20,570,820,120))
    pygame.draw.rect(screen,(0,0,0), pygame.Rect(30,580,800,100))

    pygame.draw.rect(screen,(145,115,65), pygame.Rect(545,72,300,25))
    draw_text("LAST DIGIT OF SERIAL ODD?",560,75)
    draw_switch(switch_state)
    
    pygame.draw.rect(screen,(50,50,50),pygame.Rect(545,200,300,300))
    pygame.draw.circle(screen,(0,0,180),(695,350),130)
    draw_big_text("SOLVE",600,320,(255,255,255),bigfont)

def wire_del(wire):
    pygame.draw.rect(screen,(50,50,50), pygame.Rect(30,30,25,500))
    pygame.draw.rect(screen,(50,50,50), pygame.Rect(500,30,25,500))

    pygame.draw.rect(screen,colors[wire1count], wire1)
    pygame.draw.rect(screen,colors[wire2count], wire2)
    pygame.draw.rect(screen,colors[wire3count], wire3)

    if wire == 4:
        pygame.draw.rect(screen,"gray",(55,300,445,25))
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
    global switch_state
    count_to_color = {-1:"g",0:"r",1:"b",2:"y",3:"k",4:"w"}
    lineup = []
    wires = [wire1count,wire2count,wire3count,wire4count,wire5count,wire6count]
    for i in range(len(wires)):
        lineup.append(count_to_color[wires[i]])

    final_list = [x for x in lineup if x != 'g']
    num_wires = len(final_list)

    match num_wires:
        case 3:
            if not "r" in final_list:
                flash_screen("CUT THE SECOND WIRE.",55,600,bigfont)
            elif final_list[-1] == "w":
                flash_screen("CUT THE FINAL WIRE.",75,600,bigfont)
            elif final_list.count("b") > 1:
                flash_screen("CUT THE FINAL BLUE WIRE.",53,600,specialfont)
            else:
                flash_screen("CUT THE FINAL WIRE.",75,600,bigfont)

        case 4:
            if final_list.count("r") > 1 and switch_state == "y":
                flash_screen("CUT THE FINAL RED WIRE.",65,600,specialfont)
            elif final_list[-1] == "y" and "r" not in final_list:
                flash_screen("CUT THE FIRST WIRE.",75,600,bigfont)
            elif final_list.count("b") == 1:
                flash_screen("CUT THE FIRST WIRE.",75,600,bigfont)
            elif final_list.count("y") > 1:
                flash_screen("CUT THE FINAL WIRE.",75,600,bigfont)
            else:
                flash_screen("CUT THE SECOND WIRE.",55,600,bigfont)

        case 5:
            if final_list[-1] == "k" and switch_state == "y":
                flash_screen("CUT THE FOURTH WIRE.",55,600,bigfont)
            elif final_list.count("r") == 1 and final_list.count("y") > 1:
                flash_screen("CUT THE FIRST WIRE.",75,600,bigfont)
            elif not "k" in final_list == 0:
                flash_screen("CUT THE SECOND WIRE.",55,600,bigfont)
            else:
                flash_screen("CUT THE FIRST WIRE.",75,600,bigfont)

        case 6:
            if not "y" in final_list and switch_state == "y":
                flash_screen("CUT THE THIRD WIRE.",75,600,bigfont)
            elif final_list.count("y") == 1 and final_list.count("w") > 1:
                flash_screen("CUT THE FOURTH WIRE.",55,600,bigfont)
            elif not "r" in final_list:
                flash_screen("CUT THE FINAL WIRE.",75,600,bigfont)
            else:
                flash_screen("CUT THE FOURTH WIRE.",55,600,bigfont)

wire1 = pygame.Rect(45,75,465,25)
wire2 = pygame.Rect(45,150,465,25)
wire3 = pygame.Rect(45,225,465,25)
wire4 = pygame.Rect(45,300,465,25)
wire5 = pygame.Rect(45,375,465,25)
wire6 = pygame.Rect(45,450,465,25)

colors = [(255,0,0),(0,0,255),(255,255,0),(0,0,0),(255,255,255),(0,255,0)]

wire_init()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        mouse = pygame.mouse.get_pos()
        dist = pygame.math.Vector2((mouse[0],mouse[1])).distance_to((700,350))

        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if dist <= 130:
                wire_logic()
            
            if 545 < mouse[0] < 845 and 105 < mouse[1] < 180:
                if switch_state == "n":
                    switch_state = "y"
                    draw_switch(switch_state)
                elif switch_state == "y":
                    switch_state = "n"
                    draw_switch(switch_state)

            if 45 <= mouse[0] <= 510 and 75 <= mouse[1] <= 100:
                if wire1count < 4:
                    wire1count +=1
                else:
                    wire1count = 0
                pygame.draw.rect(screen,colors[wire1count],wire1)
                
            if 45 <= mouse[0] <= 510 and 150 <= mouse[1] <= 175:
                if wire2count < 4:
                    wire2count +=1
                else:
                    wire2count = 0
                pygame.draw.rect(screen,colors[wire2count],wire2)

            if 45 <= mouse[0] <= 510 and 225 <= mouse[1] <= 250:
                if wire3count < 4:
                    wire3count +=1
                else:
                    wire3count = 0
                pygame.draw.rect(screen,colors[wire3count],wire3)

            if 45 <= mouse[0] <= 510 and 300 <= mouse[1] <= 325:
                if wire4count < 4:
                    wire4count += 1
                    pygame.draw.rect(screen,colors[wire4count],wire4)
                else:
                    wire4count = -1
                    wire_del(4)

                
            if 45 <= mouse[0] <= 510 and 375 <= mouse[1] <= 400:
                if wire5count < 4:
                    wire5count += 1
                    pygame.draw.rect(screen,colors[wire5count],wire5)
                else:
                    wire5count = -1
                    wire_del(5)


            if 45 <= mouse[0] <= 510 and 450 <= mouse[1] <= 475:
                if wire6count < 4:
                    wire6count += 1
                    pygame.draw.rect(screen,colors[wire6count],wire6)
                else:
                    wire6count = -1
                    wire_del(6)

    pygame.display.flip()

pygame.quit()