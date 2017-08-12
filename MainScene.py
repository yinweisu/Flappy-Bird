import random
from Bird import *
from Pipe import *
from Ground import *
from pygame.locals import *
from sys import exit

SCREEN_RESOLUTION = (640, 480)
Bird_image = 'birds.png'
Pipe_image = 'pipe1.png'
Ground_image = 'land.png'
Background_image = 'sky.png'


# init
pygame.init()
screen = pygame.display.set_mode(SCREEN_RESOLUTION, 0, 32)
pygame.display.set_caption('Flappy Bird')
bird_imgs = pygame.image.load(Bird_image)
pipe_img = pygame.image.load(Pipe_image)
ground_img = pygame.image.load(Ground_image).convert()
background = pygame.image.load(Background_image).convert()

x = 90
y = int(screen.get_height() / 2)
center = [x, y]

# config bird

bird_img1_rect = pygame.Rect(8, 11, 34, 24)
bird_img1 = bird_imgs.subsurface(bird_img1_rect).convert_alpha()
bird_img2_rect = pygame.Rect(60, 11, 34, 24)
bird_img2 = bird_imgs.subsurface(bird_img2_rect).convert_alpha()
bird_img3_rect = pygame.Rect(112, 11, 34, 24)
bird_img3 = bird_imgs.subsurface(bird_img3_rect).convert_alpha()
bird_images = [bird_img1, bird_img2, bird_img3]
bird_pos = center
bird_counter = 0
bird = Bird(bird_images[bird_counter], bird_pos)


# config pipe
def config_pipe(x):
    pipe_x_down = x
    pipe_height_down = random.randrange(130, 350 , 1)

    pipe_x_up = pipe_x_down
    pipe_height_up = 380 - pipe_height_down

    pipe_down = Pipe(pipe_img, pipe_x_down, pipe_height_down, False)
    pipe_up = Pipe(pipe_img, pipe_x_up, pipe_height_up, True)

    return pipe_down, pipe_up


pipe_down, pipe_up = config_pipe(640)
pipe_down2, pipe_up2 = config_pipe(960)

# config ground
ground1 = Ground(ground_img, 0)
ground2 = Ground(ground_img, 336)
ground3 = Ground(ground_img, 672)
ground4 = Ground(ground_img, 1008)

# config timer
frame_passed = 0

running = True


while running:

    collision = (pygame.sprite.collide_rect(bird, pipe_down) or pygame.sprite.collide_rect(bird, pipe_up)) or (pygame.sprite.collide_rect(bird, pipe_down2) or pygame.sprite.collide_rect(bird, pipe_up2)) or bird.y > 360

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            exit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            bird.jump()
            # reset
            if collision:
                bird = Bird(bird_images[bird_counter], bird_pos)
                pipe_down, pipe_up = config_pipe(640)
                pipe_down2, pipe_up2 = config_pipe(960)
                ground1 = Ground(ground_img, 0)
                ground2 = Ground(ground_img, 336)
                ground3 = Ground(ground_img, 672)
                ground4 = Ground(ground_img, 1008)
                frame_passed = 0
                collision = False
                continue

    # count the frame
    if frame_passed < 5:
        frame_passed += 1
    else:
        frame_passed = 0
    # update the picture
    if bird_counter < 2 and frame_passed >= 5:
        bird_counter += 1
    elif bird_counter == 2 and frame_passed >= 5:
        bird_counter -= 2
    if not collision:
        bird.update()
        bird.update_image(bird_images[bird_counter])
        pipe_down.move()
        pipe_down2.move()
        pipe_up.move()
        pipe_up2.move()
        ground1.move()
        ground2.move()
        ground3.move()
        ground4.move()
    if pipe_down.x < -48:
        pipe_down, pipe_up = config_pipe(640)
    if pipe_down2.x < -48:
        pipe_down2, pipe_up2 = config_pipe(640)

    # update screen
    screen.blit(background, (0, 0))
    screen.blit(bird.image, bird.rect)
    screen.blit(pipe_down.image, pipe_down.rect)
    screen.blit(pipe_up.image, pipe_up.rect)
    screen.blit(pipe_down2.image, pipe_down2.rect)
    screen.blit(pipe_up2.image, pipe_up2.rect)
    screen.blit(ground1.image, ground1.rect)
    screen.blit(ground2.image, ground2.rect)
    screen.blit(ground3.image, ground3.rect)
    screen.blit(ground4.image, ground4.rect)
    pygame.display.update()

