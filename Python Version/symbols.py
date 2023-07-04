import pygame
import os

pygame.init()
pygame.display.set_caption("Symbols Solver")
screen = pygame.display.set_mode((1152,512))
clock = pygame.time.Clock()
running = True

regfont = pygame.font.SysFont('consolas',20)
bigfont = pygame.font.SysFont('consolas',70)

def draw_text(text,x,y):
    textobj = regfont.render(text,1,(0,0,0))
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    screen.blit(textobj,textrect)

def draw_big_text(text,x,y,color,font):
    textobj = font.render(text,1,color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    screen.blit(textobj,textrect)

memory = []
flagged = []
solutions = [[24,11,25,10,6,8,20],[14,24,20,22,2,8,17],[0,7,22,4,13,25,2],[9,18,26,6,4,17,3],[21,3,26,19,18,16,1],[9,14,23,12,21,15,5]]

def symbol_init():
    global memory
    screen.fill("gray")

    index = 0
    symbols = os.listdir('symbols')
    while index < len(symbols):
        filename = symbols[index]
        if filename.endswith('.png'):
            with open(os.path.join('symbols', filename)) as f:
                image = pygame.image.load(f)
                image = pygame.transform.scale(image, (128,128))
                memory.append(image)
                flagged.append(False)
                if index < 9:
                    xpos = 128*index
                    screen.blit(image, (xpos,0))
                elif index < 18:
                    xpos = 128*(index-9)
                    screen.blit(image, (xpos,128))
                else:
                    xpos = 128*(index-18)
                    screen.blit(image, (xpos,256))
        index += 1

    pygame.draw.rect(screen,(0,0,180), pygame.Rect(64,400,512,80))
    draw_big_text("SOLVE",218,410,"white",bigfont)

def symbol_logic():
    symbols = []
    working_mem = []
    working_symbols = []
    ordered_solution = []
    if num_flagged == 4:
        for i in range(len(flagged)):
            if flagged[i] == True:
                symbols.append(i)
                working_symbols.append(i)
    
        for j in range(len(solutions)):
            if symbols[0] in solutions[j]:
                working_mem.append(solutions[j])
        symbols.pop(0)

        for k in range(3):
            for l in range(len(working_mem)):
                try:
                    if symbols[0] not in working_mem[l]:
                        working_mem.pop(l)
                except IndexError:
                    continue
            symbols.pop(0)
        
        for z in range(len(working_mem[0])):
            if working_mem[0][z] in working_symbols:
                ordered_solution.append(working_mem[0][z])

        pygame.draw.rect(screen,(190,190,190), pygame.Rect(640,384,512,128))

        draw_text("1",640,400)
        draw_text("2",768,400)
        draw_text("3",896,400)
        draw_text("4",1024,400)

        sym0 = pygame.transform.scale(memory[ordered_solution[0]], (128,128))
        sym1 = pygame.transform.scale(memory[ordered_solution[1]], (128,128))
        sym2 = pygame.transform.scale(memory[ordered_solution[2]], (128,128))
        sym3 = pygame.transform.scale(memory[ordered_solution[3]], (128,128))

        screen.blit(sym0, (640,384))
        screen.blit(sym1, (768,384))
        screen.blit(sym2, (896,384))
        screen.blit(sym3, (1024,384))

        working_mem.clear()
        working_symbols.clear()
        ordered_solution.clear()

def button_flip(x,y,index):
    sym = pygame.transform.scale(memory[index], (128,128))
    if flagged[index] == False and num_flagged < 4:
        pygame.draw.rect(screen,(150,150,150), pygame.Rect(x,y,128,128))
        screen.blit(sym, (x,y))
        flagged[index] = True
    else:
        pygame.draw.rect(screen,(190,190,190), pygame.Rect(x,y,128,128))
        screen.blit(sym, (x,y))
        flagged[index] = False

symbol_init()

while running:

    num_flagged = flagged.count(True)
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            #ROW 1
            if 0 < mouse[0] < 128 and 0 < mouse[1] < 128:
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

            if 64 < mouse[0] < 576 and 400 < mouse[1] < 480:
                symbol_logic()

    pygame.display.flip()

pygame.quit()