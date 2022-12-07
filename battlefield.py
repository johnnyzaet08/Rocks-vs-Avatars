import pygame
import images
import avatar
import avatarattack
import rook
import rookattack
import random
import coins

# objeto BattleField
# argumentos: lost, pos, tiempo_para_avanzar, tiempo_para_salir, tiempo_para_moneda, tiempo_para_remover_moneda, total_avatars, total_kills, matrix.
# métodos:
# clear_level(): cambia todos los elementos de la matriz por una imagen transparente
# draw_matrix(x, y, screen): dibuja la matriz
# place(column, row, element): dibuja elemento en la matriz
# remove(column, row): elimina elemento de la matriz
# get(column, row): retorna element de la matriz
# mouse_pos_to_matrix(pos) : cambia posición del mouse a filas y columnas
# matrix_to_mouse_pos(column, row): cambia filas y columnas a posición del mouse
# place_avatar(time_for_avatar): pone un avatar
# place_coin(): pone una moneda
# remove_coin(): elimina una moneda
# find_avatar(column, row): busca avatars en la matriz
# find_rook(column, row): busca rooks en la matriz
# find_avatar_and_move(): mueve un avatar ya existente
# launch_rook_attack(screen): lanza ataque de rook
# launch_avatar_attack(screen): lanza ataque de avatar

# add hit avatar sound
pygame.mixer.init()
avatar_hit = pygame.mixer.Sound('Sonidos/punch.wav')

# matrix size settings
MATRIX_COLUMNS = 9
MATRIX_ROWS = 5
CELL_SIZE = 110
MATRIX_STARTX = 200
MATRIX_STARTY = 100

ROOK_IS_SELECTED = False


class BattleField:
    def __init__(self):
        self.lost = False
        self.pos = [0, 0]
        self.tiempo_para_avanzar = None
        self.tiempo_para_salir = 0 * 60
        self.tiempo_para_moneda = 0
        self.tiempo_para_remover_moneda = self.tiempo_para_moneda + 1 * 60
        self.total_avatars = None
        self.total_kills = 0
        self.clear_level()

    def set_total_kills(self, kills):
        self.total_kills = kills
    
    def clear_level(self):
        self.matrix = []
        for column in range(0, MATRIX_COLUMNS + 1):
            self.matrix.append([])
            for row in range(0, MATRIX_ROWS):
                self.matrix[column].append(images.BLANK_IMG)

    def draw_matrix(self, x, y, screen):
        for column in range(0, MATRIX_COLUMNS):
            for row in range(0, MATRIX_ROWS):
                element = self.matrix[column][row]
                if element:
                    if isinstance(element, (rook.Rook, avatar.Avatar, coins.Coin)):
                        screen.blit(element.image, (x + CELL_SIZE * column, y + CELL_SIZE * row))

    def place(self, column, row, element):
        self.matrix[column][row] = element
        # print("PLACED", element)

    def remove(self, column, row):
        self.matrix[column][row] = None

    def get(self, column, row):
        return self.matrix[column][row]

    def mouse_pos_to_matrix(self, pos):
        column = (pos[0] - MATRIX_STARTX) // CELL_SIZE
        row = (pos[1] - MATRIX_STARTY) // CELL_SIZE
        if not column in range(0, MATRIX_COLUMNS) or not row in range(0, MATRIX_ROWS):
            return None
        else:
            #print(column, row)
            return column, row

    def matrix_to_mouse_pos(self, column, row):
        self.pos[0] = (column + 2) * CELL_SIZE
        self.pos[1] = (row + 1) * CELL_SIZE
        return self.pos[0], self.pos[1]

    def place_avatar(self, time_for_avatar):
        if self.total_kills == self.total_avatars:
            pass
        if self.tiempo_para_salir == 0:
            element = avatar.Avatar(avatar.lista_avatars[random.randint(0, 6)])
            self.place(9, random.randint(0, 4), element)
            self.tiempo_para_salir = time_for_avatar
        else:
            self.tiempo_para_salir -= 1

    def place_coin(self):
        if self.tiempo_para_moneda == 0:
            column = random.randint(0, MATRIX_COLUMNS - 1)
            row = random.randint(0, MATRIX_ROWS - 1)
            element = self.matrix[column][row]
            if not isinstance(element, (avatar.Avatar, rook.Rook)):
                element = coins.Coin(coins.coin_list[random.randint(0, 7)])
                self.place(column, row, element)
                self.tiempo_para_moneda = 5 * 60
                self.tiempo_para_remover_moneda = 4 * 60
        else:
            self.tiempo_para_moneda -= 1
            self.tiempo_para_remover_moneda -= 1

    def remove_coin(self):
        for column in range(0, MATRIX_COLUMNS + 1):
            for row in range(0, MATRIX_ROWS):
                element = self.matrix[column][row]
                if isinstance(element, coins.Coin):
                    if self.tiempo_para_remover_moneda == 0:
                        self.remove(column, row)

    def find_avatar(self, column, row):
        for column in range(0, MATRIX_COLUMNS):
            element = self.matrix[column][row]
            if isinstance(element, avatar.Avatar):
                return True

    def find_rook(self, column, row):
        for column in range(0, MATRIX_COLUMNS):
            element = self.matrix[column][row]
            if isinstance(element, rook.Rook):
                return True

    def find_avatar_and_move(self):
        for column in range(0, MATRIX_COLUMNS + 1):
            for row in range(0, MATRIX_ROWS):
                element = self.matrix[column][row]
                # print("FOUND", element, "AT", column, row)
                if isinstance(element, avatar.Avatar):
                    self.tiempo_para_avanzar = avatar.Avatar.find_tiempo_para_avanzar(element)
                    # print(self.tiempo_para_avanzar)
                    if avatar.Avatar.move_avatar(element, column, row, self.tiempo_para_avanzar):
                        if column == 0:
                            self.remove(column, row)
                            self.lost = True
                        else:
                            element_anterior = self.matrix[column - 1][row]
                            if isinstance(element_anterior, avatar.Avatar):
                                self.remove(column, row)
                                self.place(column - 2, row, element)
                            if isinstance(element_anterior, rook.Rook):
                                pass
                            else:
                                self.remove(column, row)
                                self.place(column - 1, row, element)

    # busca un rook y si lo encuentra, lanza un ataque
    def launch_rook_attack(self, screen):
        for column in range(0, MATRIX_COLUMNS):
            for row in range(0, MATRIX_ROWS):
                element = self.matrix[column][row]

                if isinstance(element, rook.Rook):
                    if element.attack:
                        element.attack.avanzar()
                        pos = self.mouse_pos_to_matrix((element.attack.x, element.attack.y))
                        if pos:
                            cell = self.matrix[pos[0]][pos[1]]

                            if isinstance(cell, avatar.Avatar):
                                cell.defense_power -= element.attack_power
                                if cell.defense_power <= 0:
                                    self.remove(pos[0], pos[1])
                                    self.total_kills += 1
                                    coins.total_coins += 100
                                avatar_hit.play()
                                element.attack = None
                                element.time_for_attack = element.attack_frequency
                        else:
                            element.attack = None
                            element.time_for_attack = element.attack_frequency
                    else:
                        if self.find_avatar(column, row):
                            if element.can_attack():
                                x = self.matrix_to_mouse_pos(column, row)[0]
                                y = self.matrix_to_mouse_pos(column, row)[1]
                                element.attack = rookattack.RookAttack(element.attack_image, x, y, screen)

    def launch_avatar_attack(self, screen):
        for column in range(0, MATRIX_COLUMNS):
            for row in range(0, MATRIX_ROWS):
                element = self.matrix[column][row]

                if isinstance(element, avatar.Avatar):
                    if element.attack:
                        element.attack.avanzar()
                        pos = self.mouse_pos_to_matrix((element.attack.x, element.attack.y))
                        if pos:
                            cell = self.matrix[pos[0]][pos[1]]

                            if isinstance(cell, rook.Rook):
                                cell.defense_power -= element.attack_power
                                if cell.defense_power <= 0:
                                    self.remove(pos[0], pos[1])
                                element.attack = None
                                element.time_for_attack = element.attack_frequency
                        else:
                            element.attack = None
                            element.time_for_attack = element.attack_frequency
                    else:
                        if self.find_rook (column, row):
                            if element.can_attack():
                                x = self.matrix_to_mouse_pos(column, row)[0]
                                y = self.matrix_to_mouse_pos(column, row)[1]
                                element.attack = avatarattack.AvatarAttack(element.attack_image, x, y, screen, element.tiempo_entre_avance_ataque)

    def get_matrix(self):
        return self.matrix

    def get_kills(self):
        return self.total_kills

    def set_matrix(self, matrix):
        self.matrix = matrix
        print('dentro del battlefield')
        print(self.matrix)

