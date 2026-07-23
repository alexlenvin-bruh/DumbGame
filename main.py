import pygame
import random
import os
import sys

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

WIDTH = 800
HEIGHT = 800
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SkyBlue = (135, 206, 250)
Yellow = (255, 206, 0)
TextBlue = (0, 92, 255)
NumberCol = (58, 1, 255)  # (92, 46, 255)


# ----------------------------Окно, создание игры, папка с картинками----------------------------
pygame.init()  # запускаем pygame
# pygame.mixer.init()  #звука пока нема
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The worst game ever")
clock = pygame.time.Clock()  # для того, чтобы убедиться, что игра работает с заданным фпс

# game_folder = os.path.dirname(__file__)  # папка с картинками
# img_folder = os.path.join(game_folder, 'img')
# font_folder = os.path.join(game_folder, 'fonts')

img_folder = resource_path('img')
font_folder = resource_path('fonts')

#background = pygame.image.load(os.path.join(img_folder, 'BackGround1.png')).convert()
background = pygame.image.load(resource_path(os.path.join('img', 'BackGround1.png'))).convert()
background_rect = background.get_rect()
# print(type(background_rect))

clouds = pygame.image.load(os.path.join(img_folder, 'clouds1.png')).convert_alpha()  # облачка
clouds_rect = clouds.get_rect()

player_img_1 = pygame.image.load(os.path.join(img_folder, 'kot 11.png')).convert_alpha()  # подрубаем кота влево
player_img_1 = pygame.transform.scale(player_img_1, (100, 100))

player_img_2 = pygame.image.load(os.path.join(img_folder, 'kot 22.png')).convert_alpha()  # подрубаем кота вправо
player_img_2 = pygame.transform.scale(player_img_2, (100, 100))

fish_reg_img = pygame.image.load(os.path.join(img_folder, 'regularfish.png')).convert_alpha()  # подрубаем обычную рыбу
fish_reg_img = pygame.transform.scale(fish_reg_img, (40, 40))

fish_gold_img = pygame.image.load(os.path.join(img_folder, 'goldfish.png')).convert_alpha()  # подрубаем золотую рыбу
fish_gold_img = pygame.transform.scale(fish_gold_img, (40, 40))

coco_img = pygame.image.load(os.path.join(img_folder, 'coconut.png')).convert_alpha()  # подрубаем кокос
coco_img = pygame.transform.scale(coco_img, (40, 40))


# --------------------------------------------Кот-----------------------------------------
class Player(pygame.sprite.Sprite):  # котяра
    def __init__(self, allgroup):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img_1
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 50)  # спавн
        self.add(allgroup)
        self.speed_x = 0
        self.hp = 15
        self.beginHP = 15
        self.score = 0

    def update(self):
        self.speed_x = 0
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT] or key_state[pygame.K_a]:
            self.speed_x = -8
            self.image = player_img_2

        if key_state[pygame.K_RIGHT] or key_state[pygame.K_d]:
            self.speed_x = 8
            self.image = player_img_1

        self.rect.x += self.speed_x

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.rect.left < 0:
            self.rect.left = 0

    def change(self, points, hp):  # меняем значение хп и набранныех очков
        self.score += points
        self.hp += hp
        if self.hp > self.beginHP:
            self.hp = self.beginHP
        if self.score < 0:
            self.score = 0

    def get_hp(self):
        return self.hp

    def get_score(self):
        return self.score


# --------------------------------------------Рыбы-----------------------------------------

class Fish(pygame.sprite.Sprite):
    def __init__(self, group, allgroup):
        pygame.sprite.Sprite.__init__(self)
        self.image = fish_reg_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(30, WIDTH - 30)
        self.add(group)
        self.add(allgroup)
        self.rect.y = random.randrange(-400, 0)
        self.speed_y = 5

    def update(self):
        if self.rect.y < HEIGHT:
            self.rect.y += self.speed_y
        else:
            self.kill()


class GoldenFish(Fish):
    def __init__(self, group, allgroup):
        Fish.__init__(self, group, allgroup)
        self.speed_y = 7
        self.image = fish_gold_img


class Coconut(Fish):
    def __init__(self, group, allgroup):
        super().__init__(group, allgroup)
        self.speed_y = 6
        self.image = coco_img


# -----------------------------------------общие штуки и группы----------------------------
fish = pygame.sprite.Group()  # кучка рыбов
goldfish = pygame.sprite.Group()  # кучка золотых рыбов
coconut = pygame.sprite.Group()  # кучка кокосов
all_sprites = pygame.sprite.Group()  # ВСЕ спрайты !!!!!!!

kot = Player(all_sprites)  # создаем игрока
Fish(fish, all_sprites)  # создаем рыбу

pygame.time.set_timer(pygame.USEREVENT, 1600)  # чтобы новая рыба появлялась каждые 1.6 секунды


def draw_text(sur, text, size, x, y, col):
    t = pygame.font.Font(os.path.join(font_folder, 'chococooky.ttf'), size).render(text, True, col)  # текст, сглаживание, цвет текcта, цвет фона
    sur.blit(t, (x, y))


running = True
fail = False
lvl = 1

# ----------------------------------Штуки для геймоверного окна-------------------------------

text_surface = pygame.font.Font(os.path.join(font_folder, 'impact.ttf'), 50).render("ПОТРАЧЕНО", True, TextBlue)
text_rect = text_surface.get_rect()
text_rect.midtop = (WIDTH / 2, HEIGHT / 2 - 50)

# ------------------------------------------Цикл игры----------------------------------------

while running:
    clock.tick(FPS)
    if not fail:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if kot.get_hp() <= 0:
                fail = True
            if event.type == pygame.USEREVENT:
                for i in range(0, lvl):
                    rand = random.randint(0, 100)
                    if rand < 10:
                        GoldenFish(goldfish, all_sprites)
                    else:
                        if rand < 50:
                            Coconut(coconut, all_sprites)
                        else:
                            Fish(fish, all_sprites)

                if kot.get_score() >= lvl * 10:
                    lvl += 1

        all_sprites.update()

        if pygame.sprite.spritecollide(kot, fish, True):
            kot.change(1, 0)  # очки хп

        if pygame.sprite.spritecollide(kot, goldfish, True):
            kot.change(5, 5)

        if pygame.sprite.spritecollide(kot, coconut, True):
            kot.change(-2, -2)

        screen.fill(SkyBlue)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        screen.blit(clouds, clouds_rect)  # если заменить clouds_rect на координаты в скобках, то облака подвинутся

        draw_text(screen, "Уровень: ", 24, 250, 10, TextBlue)
        draw_text(screen, str(lvl), 24, 380, 10, NumberCol)
        draw_text(screen, "Очки: ", 24, 430, 10, TextBlue)
        draw_text(screen, str(kot.get_score()), 24, 520, 10, NumberCol)
        draw_text(screen, "Здоровье: ", 24, WIDTH / 2 - 80, 50, TextBlue)
        draw_text(screen, str(kot.get_hp()), 24, WIDTH / 2 + 50, 50, NumberCol)
    else:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is clicked on the button the game is terminated
                if WIDTH / 2 - 70 <= mouse[0] <= WIDTH / 2 + 70 and HEIGHT / 2 + 20 <= mouse[1] <= HEIGHT / 2 + 60:
                    running = False

        screen.fill(SkyBlue)
        screen.blit(background, background_rect)
        screen.blit(clouds, clouds_rect)

        screen.blit(text_surface, text_rect)

        if WIDTH / 2 - 70 <= mouse[0] <= WIDTH / 2 + 70 and HEIGHT / 2 + 20 <= mouse[1] <= HEIGHT / 2 + 60:
            pygame.draw.rect(screen, SkyBlue, [WIDTH / 2 - 70, HEIGHT / 2 + 20, 140, 40])
        else:
            pygame.draw.rect(screen, TextBlue, [WIDTH / 2 - 70, HEIGHT / 2 + 20, 140, 40])

        draw_text(screen, 'Press to press F', 19, WIDTH / 2 - 70, HEIGHT / 2 + 25, WHITE)

        screen.blit(coco_img, (WIDTH / 4 - 20, HEIGHT / 4))
        draw_text(screen, 'Очки: -2', 19, WIDTH / 4 - 20, HEIGHT / 4 + 50, TextBlue)
        draw_text(screen, 'Здоровье: -2', 19, WIDTH / 4 - 20, HEIGHT / 4 + 70, TextBlue)

        screen.blit(fish_reg_img, (WIDTH / 2 - 20, HEIGHT / 4))
        draw_text(screen, 'Очки: +1', 19, WIDTH / 2 - 20, HEIGHT / 4 + 50, TextBlue)
        draw_text(screen, 'Здоровье: 0', 19, WIDTH / 2 - 20, HEIGHT / 4 + 70, TextBlue)

        screen.blit(fish_gold_img, (3 * WIDTH / 4 - 20, HEIGHT / 4))
        draw_text(screen, 'Очки: +5', 19, 3 * WIDTH / 4 - 20, HEIGHT / 4 + 50, TextBlue)
        draw_text(screen, 'Здоровье: +5', 19, 3 * WIDTH / 4 - 20, HEIGHT / 4 + 70, TextBlue)

        draw_text(screen, 'Уровень: ', 19, WIDTH / 3 + 10, HEIGHT / 2 + 100, TextBlue)
        draw_text(screen, str(lvl), 19, WIDTH / 3 + 110, HEIGHT / 2 + 100, TextBlue)

        draw_text(screen, 'Очки: ', 19, WIDTH / 3 + 160, HEIGHT / 2 + 100, TextBlue)
        draw_text(screen, str(kot.get_score()), 19, WIDTH / 3 + 240, HEIGHT / 2 + 100, TextBlue)

    pygame.display.update()

pygame.quit()
