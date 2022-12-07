import pygame
import images
import random
import level

# objeto Avatar
# argumentos: image, attack_frequency, tiempo_entre_avance, tiempo_para_avanzar, attack_power, defense_power, attack_image, tiempo_para_salir, time_for_attack, inflicted_attack_power, attack.
# métodos:
# move_avatar(column, row, tiempo_para_avanzar): verifica si puede avanzar
# find_tiempo_para_avanzar(): retorna tiempo para avanzar
# can_place_avatar(tiempo_para_salir): verifica si puede dibujarse un avatar
# can_attack(): verifica si puede atacar


def set_values_avatars(configuraciones):
    a = configuraciones[0]
    b = configuraciones[1]
    c = configuraciones[2]
    d = configuraciones[3]
    e = configuraciones[4]
    f = configuraciones[5]
    g = configuraciones[6]
    h = configuraciones[7]
    global ARCHER_VALUES,SHIELD_VALUES,AXE_VALUES,CANNIBAL_VALUES,lista_avatars
    # imagen, tiempo entre ataque, tiempo entre avance, ataque, defensa, imagen de ataque
    ARCHER_VALUES = (images.ARCHER_AVATAR_IMG, b, a, 2, 5, images.ARCHER_ATTACK_IMG)
    SHIELD_VALUES = (images.SHIELD_AVATAR_IMG, d, c, 3, 10, images.SHIELD_ATTACK_IMG)
    AXE_VALUES = (images.AXE_AVATAR_IMG, f, e, 9, 20, images.AXE_ATTACK_IMG)
    CANNIBAL_VALUES = (images.CANNIBAL_AVATAR_IMG, h, g, 12, 25, images.CANNIBAL_ATTACK_IMG)
    
    lista_avatars = [ARCHER_VALUES, ARCHER_VALUES, ARCHER_VALUES, SHIELD_VALUES, SHIELD_VALUES, AXE_VALUES, CANNIBAL_VALUES]


class Avatar:
    def __init__(self, values):
        self.tiempo_entre_avance_ataque = values[1] * 60
        self.image = values[0]
        self.attack_frequency = values[1]
        self.tiempo_entre_avance = values[2] * 60
        self.tiempo_para_avanzar = values[2] * 60
        self.attack_power = values[3]
        self.defense_power = values[4]
        self.attack_image = values[5]
        self.tiempo_para_salir = 2 * 60
        self.time_for_attack = 0
        self.inflicted_attack_power = None
        self.attack = None

    def move_avatar(self, column, row, tiempo_para_avanzar):
        if tiempo_para_avanzar <= 0:
            self.tiempo_para_avanzar = self.tiempo_entre_avance
            return True
        else:
            self.tiempo_para_avanzar -= 1

    def find_tiempo_para_avanzar(self):
        return self.tiempo_para_avanzar

    def can_place_avatar(self, tiempo_para_salir):
        if tiempo_para_salir <= 0:
            return True
        else:
            tiempo_para_salir -= 1

    def can_attack(self):
        if self.time_for_attack <= 0:
            self.time_for_attack = self.attack_frequency
            return True
        else:
            self.time_for_attack -= 1

# funcion que crea un avatar de tipo aleatorio

def create_avatar(lista):
    avatar = Avatar(lista[random.randint(0, 6)])
    return avatar










