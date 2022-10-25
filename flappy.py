import pygame, time, random, sys
from pygame.locals import KEYDOWN, K_SPACE, QUIT

# INITIALIZE
pygame.init()
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy!")
white = (255, 255, 255)
green = (50, 168, 82)
black = (0, 0, 0)
red = (200, 0, 0)
grey = (105, 105, 105)
blue = (66, 185, 189)
FPS = 60
FONT = pygame.font.Font(None, 40)

# DRAW SCREEN


def draw_window(change_Y, y, bird_sprite, pillars, pillar_dict, og, counter, score):

    pillars += 1
    WIN.fill(blue)
    if pillars == 50:
        pillars = 0
        rand = random.randint(100, 400)
        pillar_dict[f"pillar{len(pillar_dict)}"] = ([770, 0], [60, rand])
        counter += 1
        pillar_dict[f"pillar{len(pillar_dict)}"] = (
            [770, random.randint(175, 200) + rand],
            [60, 800 - rand],
        )
        counter += 1
    # HITBOX
    g = pygame.draw.rect(WIN, blue, ((60, y), (67, 50)))
    for x in pillar_dict.values():
        if x[0][0] < 0:
            continue
        z = pygame.draw.rect(WIN, green, (x[0], x[1]))

        # COLLISION & DEATH ANIMATION
        if pygame.Rect.colliderect(z, g):

            while not y > 530:
                WIN.fill(blue)
                for x in pillar_dict.values():
                    if x[0][0] < 0:
                        continue
                    z = pygame.draw.rect(WIN, green, (x[0], x[1]))
                bird_sprite = pygame.transform.rotate(og, -80)
                WIN.blit(bird_sprite, (60, y))
                y += 4

                pygame.display.update()
                time.sleep(0.01)
            print(int(score))
            pygame.quit()

            quit()
        x[0][0] -= 10
        if x[0][0] < 0:
            score += 0.5

    y += change_Y
    WIN.blit(bird_sprite, (60, y))
    change_Y += 0.5
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        change_Y = -7

    pygame.display.update()
    return change_Y, y, bird_sprite, pillars, pillar_dict, score


# WAIT UNTIL KEYPRESS
def pause():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                return


# GAME LOOP
def play():
    counter, pillars, score = 0, 0, 0
    pillar_dict = {}
    bird_sprite = pygame.image.load(
        r"Path to flappy bird image"
    )
    og = bird_sprite = pygame.transform.scale(bird_sprite, (67, 50))
    bird_sprite = pygame.transform.rotate(og, 30)
    change_Y = 0
    clock = pygame.time.Clock()
    run = True
    y = 300
    draw_window(change_Y, y, bird_sprite, pillars, pillar_dict, og, counter, score)

    pause()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(score)
                run = False

        if change_Y > 0:
            bird_sprite = pygame.transform.rotate(og, -change_Y * 2)
        else:
            bird_sprite = pygame.transform.rotate(og, -change_Y * 2)

        change_Y, y, bird_sprite, pillars, pillar_dict, score = draw_window(
            change_Y, y, bird_sprite, pillars, pillar_dict, og, counter, score
        )
        if y > 530:
            run = False
    return score


if __name__ == "__main__":
    score = play()
    print(int(score))
