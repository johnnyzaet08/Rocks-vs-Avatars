# Objeto Button
# argumentos: image, image1, cord, rangeX, rangeY
# metodos:
# setCords(x,y) setea las coordenadas donde va a aparecer el button
# setrangeEnd(rangeEndX, rangeEndY) setea los margenes de la imagen para saber hsata donde llega
# draw(window, pos) dibuja en la ventana indicada la imagen segun la posicion del raton
# pressed(pos) obtiene si el button fue presionado

import pygame
pygame.init()

pygame.mixer.init()
buttom_sound = pygame.mixer.Sound('Sonidos/buttom.wav')
    
class Button():

    def __init__(self, image, image1):
        self.image = pygame.image.load(image)
        self.image1 = pygame.image.load(image1)

    #set coords
    def setCords(self,x,y):
        self.cord = (x,y)

    #set dimentions
    def setrangeEnd(self, rangeEndX, rangeEndY):
        self.rangeX, self.rangeY = rangeEndX, rangeEndY

    #set image
    def setimage(self, image, image1):
        self.image = pygame.image.load(image)
        self.image = pygame.image.load(image1)

    #draw de bottom in the window
    def draw(self, window, pos):
        if pos[0] in range(self.cord[0], self.cord[0] + self.rangeX) and pos[1] in range(self.cord[1], self.cord[1] + self.rangeY):
            window.blit(self.image1, self.cord)
        else:
            window.blit(self.image, self.cord)

    #get if button presed 
    def pressed(self, pos):
        if pos[0] in range(self.cord[0], self.cord[0] + self.rangeX) and pos[1] in range(self.cord[1], self.cord[1] + self.rangeY):
            buttom_sound.play()
            return True
        else:
            return False

# Objeto InputBox
# argumentos: rect, width, color, text, txt_surface, active
# metodos:
# handle_event(event) obtiene si el evento fue dentro del rango del inputbox y cambia de color el rec
# update() si el texto se pasa del rango del inputbox actualiza el inputbox a mas grande
# draw(screen) dibuja el inputbox en la ventana indicada


COLOR_INACTIVE = pygame.Color('black')
COLOR_ACTIVE = pygame.Color('white')
FONT = pygame.font.SysFont('Arial', 30) 
class InputBox:
    def __init__(self, x, y, w, h, text=''): 
        self.rect = pygame.Rect(x, y, w, h)
        self.width = w
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
    def update(self):
        # Resize the box if the text is too long.
        width = max(self.width, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

    def get_text(self):
        return self.text
