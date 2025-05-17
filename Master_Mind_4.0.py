# Welcome to Master Mind made by Josa #

import pygame
import os
import random


# Initial Variables #
# Colors #
white=(255,255,255)
black=(0,0,0)
grey=(128,128,128)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
orange=(255,128,0)
pink=(255,0,191)
yellow=(255,255,0)
cyan=(0,255,255)

# Loading image backgrounds and preparing some variables #
running=True
location='setup'
setup=pygame.image.load("setup.png")
start_menu=pygame.image.load("start.png")
gg=pygame.image.load('GG.png')
boo=pygame.image.load('BOO.png')
playing=True

# Setup portion of the program to choose a resolution #
screen=pygame.display.set_mode((500,200))
pygame.display.set_caption('Master Mind Setup')
resolution1=(390,765)
resolution1_x=(25,50)
resolution1_y=(125,150)
resolution=''

# Setup window #
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            playing = False
        key=pygame.key.get_pressed()
        mouse_pos=pygame.mouse.get_pos()
        screen.blit(setup,(0,0))
        if resolution1_x[0]<mouse_pos[0]<resolution1_x[1] and resolution1_y[0]<mouse_pos[1]<resolution1_y[1] and event.type==pygame.MOUSEBUTTONDOWN:
            resolution=resolution1
        if resolution==resolution1:
            pygame.draw.circle(screen,black,((resolution1_x[0]+resolution1_x[1])/2,(resolution1_y[0]+resolution1_y[1])/2),10)
        if key[pygame.K_RSHIFT] and resolution !='':
            running=False
        if key[pygame.K_ESCAPE]:
            running= False
            playing=False
    pygame.display.flip()
pygame.QUIT

# Starting the actual game #

location='start'
while playing:
    # Start Menu #
    running=True
    if location=='start':
        start_x=(200,400)
        start_y=(150,200)        
        screen=pygame.display.set_mode((600,400))
        pygame.display.set_caption('Master Mind Start')
        while running :
            screen.blit(start_menu,(0,0))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    playing = False
                key=pygame.key.get_pressed()
                mouse_pos=pygame.mouse.get_pos()
                if key[pygame.K_ESCAPE]:
                    running= False
                    playing= False
                if start_x[0]<mouse_pos[0]<start_x[1] and start_y[0]<mouse_pos[1]<start_y[1] and event.type==pygame.MOUSEBUTTONDOWN:
                    location='game'
                    running= False
        pygame.QUIT
    if location=='game':
        screen=pygame.display.set_mode(resolution)
        pygame.display.set_caption('Master Mind Game')
        running=True
        answer='9999'
        A=''
        z=0
        while z <4:
            A=A+str(random.randint(1,8))
            z=z+1
        if resolution==resolution1:
            ball_radius=30
            coords_x=(3/2)*ball_radius
            coords_y=(3/2)*ball_radius
        while running :
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
                    playing = False
                key=pygame.key.get_pressed()
                mouse_pos=pygame.mouse.get_pos()
                if key[pygame.K_ESCAPE]:
                    running= False
                    location='start'
                    pygame.time.wait(500)

                # Drawing the colors #
                if key[pygame.K_1]:
                    pygame.draw.circle(screen,(red),(coords_x,coords_y),ball_radius)
                    answer=answer[:int(((coords_x-(3/2)*ball_radius))/((5/2)*ball_radius))]+'1'+answer[int((coords_x-((3/2)*ball_radius))/((5/2)*ball_radius))+1:]
                if key[pygame.K_2]:
                    pygame.draw.circle(screen,(green),(coords_x,coords_y),ball_radius)
                    answer=answer[:int(((coords_x-(3/2)*ball_radius))/((5/2)*ball_radius))]+'2'+answer[int((coords_x-((3/2)*ball_radius))/((5/2)*ball_radius))+1:]
                if key[pygame.K_3]:
                    pygame.draw.circle(screen,(blue),(coords_x,coords_y),ball_radius)
                    answer=answer[:int(((coords_x-(3/2)*ball_radius))/((5/2)*ball_radius))]+'3'+answer[int((coords_x-((3/2)*ball_radius))/((5/2)*ball_radius))+1:]
                if key[pygame.K_4]:
                    pygame.draw.circle(screen,(white),(coords_x,coords_y),ball_radius)
                    answer=answer[:int(((coords_x-(3/2)*ball_radius))/((5/2)*ball_radius))]+'4'+answer[int((coords_x-((3/2)*ball_radius))/((5/2)*ball_radius))+1:]
                if key[pygame.K_5]:
                    pygame.draw.circle(screen,(pink),(coords_x,coords_y),ball_radius)
                    answer=answer[:int(((coords_x-(3/2)*ball_radius))/((5/2)*ball_radius))]+'5'+answer[int((coords_x-((3/2)*ball_radius))/((5/2)*ball_radius))+1:]
                if key[pygame.K_6]:
                    pygame.draw.circle(screen,(orange),(coords_x,coords_y),ball_radius)
                    answer=answer[:int(((coords_x-(3/2)*ball_radius))/((5/2)*ball_radius))]+'6'+answer[int((coords_x-((3/2)*ball_radius))/((5/2)*ball_radius))+1:]
                if key[pygame.K_7]:
                    pygame.draw.circle(screen,(grey),(coords_x,coords_y),ball_radius)
                    answer=answer[:int(((coords_x-(3/2)*ball_radius))/((5/2)*ball_radius))]+'7'+answer[int((coords_x-((3/2)*ball_radius))/((5/2)*ball_radius))+1:]
                if key[pygame.K_8]:
                    pygame.draw.circle(screen,(cyan),(coords_x,coords_y),ball_radius)
                    answer=answer[:int(((coords_x-(3/2)*ball_radius))/((5/2)*ball_radius))]+'8'+answer[int((coords_x-((3/2)*ball_radius))/((5/2)*ball_radius))+1:]
                
                # Moving cursor #
                if key[pygame.K_RIGHT] and coords_x <(resolution[0]-(4*ball_radius)):
                    pygame.draw.circle(screen,black,(coords_x,coords_y),round(ball_radius+((1/8)*ball_radius)),round((1/8)*ball_radius))
                    coords_x=coords_x+((5/2)*ball_radius)
                else:
                    pygame.draw.circle(screen,yellow,(coords_x,coords_y),round(ball_radius+((1/8)*ball_radius)),round((1/8)*ball_radius))
                if key[pygame.K_LEFT] and coords_x >((3/2)*ball_radius):
                    pygame.draw.circle(screen,black,(coords_x,coords_y),round(ball_radius+((1/8)*ball_radius)),round((1/8)*ball_radius))
                    coords_x=coords_x-((5/2)*ball_radius)
                else:
                    pygame.draw.circle(screen,yellow,(coords_x,coords_y),round(ball_radius+((1/8)*ball_radius)),round((1/8)*ball_radius))
                
                # Submiting #    
                y=A
                num_point=0
                if key[pygame.K_RSHIFT] and '9' not in answer:
                    pygame.draw.circle(screen,black,(coords_x,coords_y),round(ball_radius+((1/8)*ball_radius)),round((1/8)*ball_radius))
                    o=0
                    w=0
                    r=0
                    for i in answer:
                        if i==y[o]:
                            r=r+1
                            answer=answer[:o]+'j'+answer[o+1:]
                            y=y[:o]+'k'+y[o+1:]
                        o=o+1
                    o=0
                    for i in answer:
                        if i in y:
                            w=w+1
                            y=y.replace(i,'k',1)
                        o=o+1
                    if r==4:
                        screen.fill((255,255,255))
                        screen.blit(gg,(0,resolution[1]/2))
                        pygame.display.flip()
                        pygame.time.delay(1000)
                        running=False
                    else:
                        score_x=resolution[0]-2*ball_radius
                        score_y=coords_y-((1/2)*ball_radius)
                        while r >0:
                            pygame.draw.circle(screen,red,(score_x,score_y),round((3/16)*ball_radius))
                            r=r-1
                            score_x=round(score_x+ball_radius)
                            num_point=num_point+1
                            if num_point==2:
                                score_x=resolution[0]-2*ball_radius
                                score_y=score_y+ball_radius
                        
                        while w > 0:
                            pygame.draw.circle(screen,white,(score_x,score_y),round((3/16)*ball_radius))
                            w=w-1
                            score_x=round(score_x+ball_radius)
                            num_point=num_point+1
                            if num_point==2:
                                score_x=resolution[0]-2*ball_radius
                                score_y=score_y+ball_radius
                        coords_y=coords_y+((5/2)*ball_radius)
                    answer='9999'
                    if coords_y<= (resolution[1]-((3/2)*ball_radius)):
                        pygame.draw.circle(screen,yellow,(coords_x,coords_y),round(ball_radius+((1/8)*ball_radius)),round((1/8)*ball_radius))
                    else :
                        screen.blit(boo,(0,(resolution[1]/2)))
                        pygame.display.flip()
                        pygame.time.delay(1000)
                        running=False
        pygame.QUIT