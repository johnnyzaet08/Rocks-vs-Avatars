import images

# objeto Level
# argumentos: totalavatars, level, background, timeforavatar, finished.
# métodos:
#check_level(totalkills): verifica el nivel en el que está
#get_level()

AVATARS_NIVEL1 = 1 # 5
AVATARS_NIVEL2 = 7 # 7
AVATARS_NIVEL3 = 10 # 10

TIMEFORAVATAR_NIVEL1 = 4 * 60
TIMEFORAVATAR_NIVEL2 = 3 * 60 # es 2.8 pero se redondeo
TIMEFORAVATAR_NIVEL3 = 2 * 60 # es 2.1 pero se redondeo


class Level:
    def __init__(self, level, totalavatars, background, timeforavatar):
        self.totalavatars = totalavatars
        self.level = level
        self.background = background
        self.timeforavatar = timeforavatar
        self.finished = False

    def check_level(self, totalkills):
        if self.level < 2 and totalkills >= AVATARS_NIVEL1:
            self.level = 2
            self.background = images.BACKGROUND2_IMG
            self.timeforavatar = TIMEFORAVATAR_NIVEL2
            return True

        if self.level < 3 and totalkills >= AVATARS_NIVEL1 + AVATARS_NIVEL2:
            self.level = 3
            self.background = images.BACKGROUND3_IMG
            self.timeforavatar = TIMEFORAVATAR_NIVEL3
            return True

        if totalkills >= AVATARS_NIVEL1 + AVATARS_NIVEL2 + AVATARS_NIVEL3:
            self.finished = True
            return False

    def get_level(self):
        return self.level
