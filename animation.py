import time
import images


broken_archer = True
broken_shield = False
broken_axe = False
broken_cannibal = False
end = False

def display_broken_attacks(totaltick):
    global broken_shield, broken_axe, broken_cannibal, broken_archer, end
    if totaltick <= 2000:
        broken_shield = True
        broken_archer = False
        return images.BROKEN_ARCHER_IMG, 100

    elif totaltick <= 4000:
        broken_axe = True
        broken_shield = False
        return images.BROKEN_SHIELD_IMG, 350

    elif totaltick <= 6000:
        broken_cannibal = True
        broken_axe = False
        return images.BROKEN_AXE_IMG, 550

    elif totaltick <= 8000:
        broken_cannibal = False
        end = True
        return images.BROKEN_CANNIBAL_IMG, 750

    else:
        print(None)

def end_animation():
    global end
    if end:
        time.sleep(1)
        return True
