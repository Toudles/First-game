import pygame
from pygame.locals import *
import random

size = width, height = (800, 800)
# width of the road
road_w = int(width/1.6)
roadmark_w = int(width/80)
# right side and left side of the lane(s)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4

#speed of enemy
speed = 1


pygame.init()
running = True
# set the window size
# using the above on line 4, this allows our window to stay relatively same
# based on the changes the user makes to the window. (if they make it 200,800 it would still look nice and playable)
screen = pygame.display.set_mode((size))
# set title
pygame.display.set_caption("Andrew's first game")
# set the background color
screen.fill((60, 220,0))

# we moved all this inside the while loop so that the images don't duplicate
# when we move our character around
""" # draw graphics (in this case, a rectangle)
pygame.draw.rect(
    screen,
    # (50, 50, 50) gives us a gray color for the road
    (50, 50, 50),
    # coordinates of our rectanlge (main road to play on)
    # (x-value horizontal coordinates, y-value vertical coordinates, 
    # total width of the shape (road_w), height of the shape (height))
    # We did width/2-road_w/2 to center our road on the screen. 
    (width/2-road_w/2, 0, road_w, height))
# this is to create the middle yellow strips on a road known as center mark (same process as above)
pygame.draw.rect(
    screen,
    (255, 240, 60),
    (width/2 - roadmark_w/2, 0, roadmark_w, height))

# left side white strip
pygame.draw.rect(
    screen,
    (255, 255, 255),
    (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))

# right side white strip
pygame.draw.rect(
    screen,
    (255, 255, 255),
    (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height)) """


# apply changes
pygame.display.update()

# load player's vehicle
motorcycle = pygame.image.load("motorcycle.png")
# first have to fetch the location of our image (motorcycle location)
motorcycle_loc = motorcycle.get_rect()
# now we can specify the location of our motorcycle (center of the image)
motorcycle_loc.center = (right_lane, height * 0.8)

# load enemy's vehicle
car2 = pygame.image.load("otherCar.png")
# first have to fetch the location of our image (motorcycle location)
car2_loc = car2.get_rect()
# now we can specify the location of our motorcycle (center of the image)
car2_loc.center = (left_lane, height * 0.2)


counter = 0
# game loop
while running:
    counter += 1
    # amount of iterations before we level up (one whole lap)
    if counter == 1024:
        speed += 2
        counter = 0
        print("Level up", speed)
    # animate the enemy vehicle
    # only tackle y coordinate because we want it to off the screen if we can pass it
    # while our character tackels x because we want it to only move left or right
    # we use an index of 1 in our list because using 0 would return our x coordinate but we only
    # want to use our y coordinates
    car2_loc[1] += speed
    # make sure the car comes back
    # so if the y value of our enemy car is higher than our map, we change the index to -200 so that it'll come back
    # to the screen 
    if car2_loc[1] > height:
        # don't need this line anymore because we specify it below.
        #car2_loc[1] = -200

        # we pick between 2 numbers 0 and 1 and make our enemy car go on the left/right lane depending.
        if random.randint(0,1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200
    
    # end game 
    # if our x coordinates are the same and the enemy's y coordinate is greater than ours - 250 (so the fronts collide)
    # our game ends
    if motorcycle_loc[0] == car2_loc[0] and car2_loc[1] > motorcycle_loc[1] - 250:
        print("GAME OVER! YOU LOST")
        break

    # start the event/allows us to set a quit option 
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        # keyboard inputs
        if event.type == KEYDOWN:
            # use a list to say that if we press either A or left arrow, our car moves left.
            # we use "and" so that the car doesn't leave the border. Makes it centered in the lanes
            if event.key in [K_a, K_LEFT] and motorcycle_loc.center[0] != (left_lane):
                # use a list to move our car with x, y coordinates
                # reduce half of the road width for the x coordinate when moving left/right
                motorcycle_loc = motorcycle_loc.move([-int(road_w/2), 0])

            if event.key in [K_d, K_RIGHT] and motorcycle_loc.center[0] != (right_lane):
                motorcycle_loc = motorcycle_loc.move([int(road_w/2), 0])

    # draw graphics (in this case, a rectangle)
    pygame.draw.rect(
        screen,
        # (50, 50, 50) gives us a gray color for the road
        (50, 50, 50),
        # coordinates of our rectanlge (main road to play on)
        # (x-value horizontal coordinates, y-value vertical coordinates, 
        # total width of the shape (road_w), height of the shape (height))
        # We did width/2-road_w/2 to center our road on the screen. 
        (width/2-road_w/2, 0, road_w, height))
    # this is to create the middle yellow strips on a road known as center mark (same process as above)
    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width/2 - roadmark_w/2, 0, roadmark_w, height))

    # left side white strip
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))

    # right side white strip
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height))

    # we loaded the image but haven't placed it so this allows us to have the image on our screen.
    # and have to update our display
    screen.blit(motorcycle, motorcycle_loc)
    screen.blit(car2, car2_loc)
    pygame.display.update()


pygame.quit()