# objeto AvatarAttack
# argumentos: screen, image, x, y, tiempo_entre_avance, tiempo_para_avanzar, attack_power, defense.
# métodos:
# draw_attack(): dibuja ataque
# avanzar(): mueve ataque

class AvatarAttack:
    def __init__(self, image, x, y, screen, tiempo_entre_avance_ataque):
        self.screen = screen
        self.image = image
        self.x = x
        self.y = y
        self.tiempo_entre_avance = 2
        self.tiempo_para_avanzar = 2
        self.attack_power = 2
        self.defense = 5
        # print(self.x, self.y)

    def draw_attack(self):
        self.screen.blit(self.image, (self.x, self.y))
        # print("rook attack drawn")

    def avanzar(self):
        if self.tiempo_para_avanzar == 0:
            self.x -= 15
            self.tiempo_para_avanzar = self.tiempo_entre_avance
            #print("avatar attack x: ", self.x)
        else:
            self.tiempo_para_avanzar -= 1
        self.draw_attack()
