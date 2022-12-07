import pygame
import images
import battlefield

# objeto Rook
# argumentos: image, attack_power, defense_power, attack_image, attack_frequency, time_for_attack, inflicted_attack_power, attack.
# métodos:
# get_value() 
# can_attack(): verifica si puede atacar

# constant rook placement settings
ROOK_MARGIN = 100
ROOK_IMAGES_START = 30
SAND_ROOK_X = ROOK_IMAGES_START
SAND_ROOK_Y = 90
ROCK_ROOK_X = ROOK_IMAGES_START
ROCK_ROOK_Y = SAND_ROOK_Y + ROOK_MARGIN - 15
FIRE_ROOK_X = ROOK_IMAGES_START
FIRE_ROOK_Y = ROCK_ROOK_Y + ROOK_MARGIN
WATER_ROOK_X = ROOK_IMAGES_START
WATER_ROOK_Y = FIRE_ROOK_Y + ROOK_MARGIN



def draw_constants(screen, image, image_x, image_y):
    screen.blit(image, (image_x, image_y))


def draw_constant_rooks(screen):
    draw_constants(screen, images.SAND_ROOK_IMG, SAND_ROOK_X, SAND_ROOK_Y)
    draw_constants(screen, images.ROCK_ROOK_IMG, ROCK_ROOK_X, ROCK_ROOK_Y)
    draw_constants(screen, images.FIRE_ROOK_IMG, FIRE_ROOK_X, FIRE_ROOK_Y)
    draw_constants(screen, images.WATER_ROOK_IMG, WATER_ROOK_X, WATER_ROOK_Y)


# rook elements initial settings
SAND = False
ROCK = False
FIRE = False
WATER = False


# finds selected rook based on position of user click
def find_selected_rook(pos):
    global ROCK, FIRE, WATER, SAND
    if pos[0] in range(ROOK_IMAGES_START, ROOK_IMAGES_START + ROOK_MARGIN):
        #print(pos)
        if pos[1] in range(SAND_ROOK_Y, SAND_ROOK_Y + ROOK_MARGIN):
            SAND = True
            ROCK = False
            FIRE = False
            WATER = False
            #print("rook")
        elif pos[1] in range(ROCK_ROOK_Y, ROCK_ROOK_Y + ROOK_MARGIN):
            ROCK = True
            SAND = False
            FIRE = False
            WATER = False
            #print("rook")
        elif pos[1] in range(FIRE_ROOK_Y, FIRE_ROOK_Y + ROOK_MARGIN):
            FIRE = True
            SAND = False
            ROCK = False
            WATER = False
            #print("rook")
        elif pos[1] in range(WATER_ROOK_Y, WATER_ROOK_Y + ROOK_MARGIN):
            WATER = True
            SAND = False
            ROCK = False
            FIRE = False
            #print("rook")
        rook_element_list = [SAND, ROCK, FIRE, WATER]
        return rook_element_list


def assign_selected_rook(rook_element_list):
    global selected_rook_values
    if rook_element_list[0]:
        selected_rook_values = SAND_ROOK_VALUES
    elif rook_element_list[1]:
        selected_rook_values = ROCK_ROOK_VALUES
    elif rook_element_list[2]:
        selected_rook_values = FIRE_ROOK_VALUES
    elif rook_element_list[3]:
        selected_rook_values = WATER_ROOK_VALUES
    return selected_rook_values


SAND_ROOK_VALUES = (images.SAND_ROOK_IMG, 2, 7, images.SAND_ATTACK_IMG)
ROCK_ROOK_VALUES = (images.ROCK_ROOK_IMG, 4, 14, images.ROCK_ATTACK_IMG)
FIRE_ROOK_VALUES = (images.FIRE_ROOK_IMG, 8, 16, images.FIRE_ATTACK_IMG)
WATER_ROOK_VALUES = (images.WATER_ROOK_IMG, 8, 16, images.WATER_ATTACK_IMG)


def get_rook_cost(element):
    global cost
    if Rook.get_value(element) == images.SAND_ROOK_IMG:
        cost = 50
    if Rook.get_value(element) == images.ROCK_ROOK_IMG:
        cost = 100
    if Rook.get_value(element) == images.FIRE_ROOK_IMG:
        cost = 150
    if Rook.get_value(element) == images.WATER_ROOK_IMG:
        cost = 150
    return cost

rook_attack_frequency = 2

class Rook:
    def __init__(self, values):
        #print(values)
        self.image = values[0]
        self.attack_power = values[1]
        self.defense_power = values[2]
        self.attack_image = values[3]
        self.attack_frequency = rook_attack_frequency * 60
        self.time_for_attack = 0
        self.inflicted_attack_power = None
        self.attack = None

    def get_value(self):
        return self.image

    def can_attack(self):
        if self.time_for_attack <= 0:
            self.time_for_attack = self.attack_frequency
            return True
        else:
            self.time_for_attack -= 1


