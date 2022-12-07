from main_game import *
import main_game
import os

pygame.init()
configurations_state = False

#////////////////////////////////MENU PRINCIPAL/////////////////////////////////
#////////////////////////////////MENU PRINCIPAL/////////////////////////////////

def menu():           #ventana principal
    menu = pygame.display.set_mode((960, 540))
    pygame.display.set_caption("Battle: Menu")
    icon = pygame.image.load('Imagenes/archer.png')
    pygame.display.set_icon(icon)
    backgroundM = pygame.image.load('Imagenes/backgroundM.png') 
    menu.blit(backgroundM, (0,0))
    fuente = pygame.font.SysFont(None, 35)
    Tconfig = fuente.render('Settings',0,(0, 0, 0))    #Texto de los botones
    Thelps = fuente.render('Help',0,(0, 0, 0))
    TNewGame = fuente.render('New Game',0,(0, 0, 0))
    TCredits = fuente.render('Credits',0,(0, 0, 0))
    TLoadGame = fuente.render('Load Game',0,(0, 0, 0))
    TRanking = fuente.render('Ranking',0,(0, 0, 0))
    save_games = os.listdir('PartidaG')
    if user_name in save_games:
        load = True
    else:
        load = False
    running = True
    while running:
        pos = pygame.mouse.get_pos()                                                    #botones y funcion para ir a cada boton
        config = Button('Imagenes/buttom.png','Imagenes/buttom1.png')
        config.setCords(100,190), config.setrangeEnd(193,54), config.draw(menu, pos)
        menu.blit(Tconfig, (110,205))
        helps = Button('Imagenes/buttom.png','Imagenes/buttom1.png')
        helps.setCords(100,270), helps.setrangeEnd(193,54), helps.draw(menu, pos)
        menu.blit(Thelps, (110,285))
        newgame = Button('Imagenes/buttom.png','Imagenes/buttom1.png')
        newgame.setCords(100,110), newgame.setrangeEnd(193,54), newgame.draw(menu, pos)
        menu.blit(TNewGame, (110,125))
        creditss = Button('Imagenes/buttom.png','Imagenes/buttom1.png')
        creditss.setCords(100,430), creditss.setrangeEnd(193,54), creditss.draw(menu, pos)
        menu.blit(TCredits, (110,445))
        ranking = Button('Imagenes/buttom.png','Imagenes/buttom1.png')
        ranking.setCords(100,350), ranking.setrangeEnd(193,54), ranking.draw(menu, pos)
        menu.blit(TRanking, (110,365))
        if load == True:
            loadgame = Button('Imagenes/buttom.png','Imagenes/buttom1.png')
            loadgame.setCords(100,30), loadgame.setrangeEnd(193,54), loadgame.draw(menu, pos)
        menu.blit(TLoadGame, (110,45))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if config.pressed(pos):
                    running = False
                    return configurations()
                if helps.pressed(pos):
                    running = False
                    return helping()
                if creditss.pressed(pos):
                    running = False
                    return crediting()
                if load == True:
                    if loadgame.pressed(pos):
                        running = False
                        return loadgaming()
                if newgame.pressed(pos):
                    running = False
                    return newgaming()
                if ranking.pressed(pos):
                    running = False
                    return rankingg()
        pygame.display.update()
    pygame.quit()

#////////////////////////////////CONFIGURATIONS/////////////////////////////////
#////////////////////////////////CONFIGURATIONS/////////////////////////////////

def configurations():
    white = (255,255,255)
    red = (255,0,0)
    configurations = pygame.display.set_mode((600, 500))
    pygame.display.set_caption("Battle: Configurations")
    icon = pygame.image.load('Imagenes/archer.png')
    pygame.display.set_icon(icon)
    flechador = pygame.image.load('Imagenes/flechador.png') #Cargar imagenes para avatars
    escudero = pygame.image.load('Imagenes/escudero.png')
    canibal = pygame.image.load('Imagenes/canibal.png')
    lenador = pygame.image.load('Imagenes/lenador.png')
    rocks = pygame.image.load('Imagenes/firerook.png')
    fuenteT = pygame.font.SysFont("Arial", 25)     #fuente para texto
    Tavatars = fuenteT.render('Avatars',0,(0,0,0))         #Todos los textos necesarios
    Trocks = fuenteT.render('Rocks',0,(0,0,0))
    Tindica = fuenteT.render('Todos los parametros deben de ser configurados entre 1 y 9',0,red)
    Tavance = fuenteT.render('Avance (s): ', 0, white)
    Tataque = fuenteT.render('Ataque (s): ', 0, white)
    Trock = fuenteT.render('Frecuencia de ataque (s)', 0, white)
    avance_flechador = InputBox(230, 120, 40, 30)#
    ataque_flechador = InputBox(234, 155, 40, 30)
    avance_escudero = InputBox(230, 240, 40, 30)#
    ataque_escudero = InputBox(230, 275, 40, 30)
    avance_canibal = InputBox(510, 120, 40, 30)#
    ataque_canibal = InputBox(510, 155, 40, 30)
    avance_lenador = InputBox(510, 240, 40, 30)#
    ataque_lenador = InputBox(510, 275, 40, 30)
    velocidad_rocks = InputBox(190, 435, 40, 30)#
    input_box = [avance_flechador,ataque_flechador,
                 avance_escudero,ataque_escudero,
                 avance_canibal,ataque_canibal,
                 avance_lenador,ataque_lenador,
                 velocidad_rocks]
    running = True
    while running:
        configurations.fill((50,57,49))
        configurations.blit(Tindica, (20,10))
        configurations.blit(Tavatars, (20, 50))
        configurations.blit(flechador,(20, 100))#
        configurations.blit(Tavance, (125, 115))
        configurations.blit(Tataque, (125, 150))
        configurations.blit(escudero, (20, 220))#
        configurations.blit(Tavance, (125, 235))
        configurations.blit(Tataque, (125, 270))
        configurations.blit(canibal, (300, 100))#
        configurations.blit(Tavance, (405, 115))
        configurations.blit(Tataque, (405, 150))
        configurations.blit(lenador, (300, 220))#
        configurations.blit(Tavance, (405, 235))
        configurations.blit(Tataque, (405, 270))
        configurations.blit(Trocks, (20, 330))
        configurations.blit(rocks, (20, 380))
        configurations.blit(Trock, (125, 395))
        pos = pygame.mouse.get_pos()
        save = Button('Imagenes/save.png','Imagenes/save1.png')
        save.setCords(500,55), save.setrangeEnd(50,50), save.draw(configurations, pos)
        back = Button('Imagenes/back.png','Imagenes/back1.png')
        back.setCords(530,444), back.setrangeEnd(70,56), back.draw(configurations, pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if save.pressed(pos):
                    global configuraciones
                    configuraciones = []
                    for box in input_box:
                        configuraciones += [int(box.get_text())]
                    running = False
                    return save_configurations()
                if back.pressed(pos):
                    running = False
                    return menu()
            for box in input_box:
                box.handle_event(event)
        for box in input_box:
            box.update()
        for box in input_box:
            box.draw(configurations)
        pygame.display.update()
    pygame.quit()

def save_configurations():
    global configurations_state
    for config in configuraciones:
        if config not in range(1, 10):
            configurations_state = False
            break
        else:
            configurations_state = True
    return menu()
            

#//////////////////////////////////HELP CENTER//////////////////////////////////
#//////////////////////////////////HELP CENTER//////////////////////////////////

def helping():
    helps = pygame.display.set_mode((960, 540))
    pygame.display.set_caption("Battle: Help")
    icon = pygame.image.load('Imagenes/archer.png')
    pygame.display.set_icon(icon)
    helps.fill((70,77,69))
    backgroundH = pygame.image.load('Imagenes/backgroundH.png')
    helps.blit(backgroundH, (0,0))
    running = True
    while running:
        pos = pygame.mouse.get_pos()
        back = Button('Imagenes/back.png','Imagenes/back1.png')
        back.setCords(890,484), back.setrangeEnd(70,56), back.draw(helps, pos)
        go = Button('Imagenes/go.png','Imagenes/go1.png')
        go.setCords(545,495), go.setrangeEnd(40,41), go.draw(helps, pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.pressed(pos):
                    running = False
                    return menu()
                if go.pressed(pos):
                    running = False
                    return defensa_ataque()
        pygame.display.update()
    pygame.quit()

def defensa_ataque():
    denfata = pygame.display.set_mode((960, 540))
    pygame.display.set_caption("Battle: Help")
    icon = pygame.image.load('Imagenes/archer.png')
    pygame.display.set_icon(icon)
    denfata.fill((70,77,69))
    backgroundHAD = pygame.image.load('Imagenes/backgroundHAD.png')
    denfata.blit(backgroundHAD, (0,0))
    running = True
    while running:
        pos = pygame.mouse.get_pos()
        back = Button('Imagenes/back.png','Imagenes/back1.png')
        back.setCords(890,484), back.setrangeEnd(70,56), back.draw(denfata, pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.pressed(pos):
                    running = False
                    return helping()
        pygame.display.update()
    pygame.quit()

#////////////////////////////////////CREDITS////////////////////////////////////
#////////////////////////////////////CREDITS////////////////////////////////////

def crediting():
    credit = pygame.display.set_mode((960, 540))
    pygame.display.set_caption("Battle: Credits")
    icon = pygame.image.load('Imagenes/archer.png')
    pygame.display.set_icon(icon)
    credit.fill((70,77,69))
    backgroundCR = pygame.image.load('Imagenes/backgroundCR.png')
    credit.blit(backgroundCR,(0,0))
    running = True
    while running:
        pos = pygame.mouse.get_pos()
        back = Button('Imagenes/back.png','Imagenes/back1.png')
        back.setCords(890,484), back.setrangeEnd(70,56), back.draw(credit, pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.pressed(pos):
                    running = False
                    return menu()
        pygame.display.update()
    pygame.quit()
    
#///////////////////////////////////LOAD GAME///////////////////////////////////
#///////////////////////////////////LOAD GAME///////////////////////////////////

def loadgaming():
    main_game.load_game = True
    
    datos = []
    with open('PartidaG/'+user_name, 'r') as f:
        lineas = f.readlines()
        for row in lineas:
            datos += [row[:-1]]

    lista = datos[3] + ']'
    configura = []
    for i in range(0,9):
        dato = lista[1+3*i]
        configura += [int(dato)]

    matriz = []
    with open('PartidaG/'+user_name+'Matrix.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                matriz += [row]
            print(matriz)
            print('separador')
            

    kills = int(datos[1])
    coins.total_coins = int(datos[2])
    main_game.load_time = int(datos[0])
    main_game.matriz = matriz

    play(user_name, configura, kills)
    
    
#///////////////////////////////////NEW GAME////////////////////////////////////
#///////////////////////////////////NEW GAME////////////////////////////////////

def newgaming():
    if configurations_state == False:
        return configurations()
    else:
        play(user_name, configuraciones, 0)

#////////////////////////////////////RANKING////////////////////////////////////
#////////////////////////////////////RANKING////////////////////////////////////

def rankingg():
    ranki = pygame.display.set_mode((750, 422))
    pygame.display.set_caption("Battle: Ranking")
    icon = pygame.image.load('Imagenes/archer.png')
    pygame.display.set_icon(icon)
    backgroundR = pygame.image.load('Imagenes/backgroundR.png')
    ranki.blit(backgroundR, (0,0))
    datos = []
    nombre = []
    tiempo = []
    with open('ranking.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            datos += [(row)]
            nombre += [(row['Name'])]
            tiempo += [(row['Time'])]
    first = 100000
    firstP = 0
    minim = 0
    while minim < len(tiempo): #saca la posicion numero 1 del ranking con la pos
        if float(tiempo[minim]) <= first:
            first = float(tiempo[minim])
            firstP = minim
            minim += 1
        else:
            minim += 1
    second = 100000
    secondP = 0
    mini = 0
    while mini < len(tiempo): #saca la posicion numero 2 del ranking con la pos
        if float(tiempo[mini]) <= second and float(tiempo[mini]) > first:
            second = float(tiempo[mini])
            secondP = mini
            mini += 1
        else:
            mini += 1
    third = 100000
    thirdP = 0
    minimo = 0 
    while minimo < len(tiempo): #saca la posicion numero 3 del ranking con la pos
        if float(tiempo[minimo]) <= third and float(tiempo[minimo]) > second:
            third = float(tiempo[minimo])
            thirdP = minimo
            minimo += 1
        else:
            minimo += 1
    fuente = pygame.font.SysFont('Arial Black', 20)
    white = (255, 255, 255)
    black = (0, 0, 0)
    Tfirst = fuente.render(nombre[firstP],0,black)
    TfirstT = fuente.render(tiempo[firstP]+'s',0,black)
    Tsecond = fuente.render(nombre[secondP],0,black)
    TsecondT = fuente.render(tiempo[secondP]+'s',0,black)
    Tthird = fuente.render(nombre[thirdP],0,black)
    TthirdT = fuente.render(tiempo[thirdP]+'s',0,black)
    ranki.blit(Tfirst, (170,15))
    ranki.blit(TfirstT, (170,35))
    ranki.blit(Tsecond, (70,75))
    ranki.blit(TsecondT, (70,95))
    ranki.blit(Tthird, (310,90))
    ranki.blit(TthirdT, (310,110))
    Ttodos = fuente.render('Todos los jugadores',0,white)
    ranki.blit(Ttodos, (500, 40))
    i = 0
    while i < len(nombre):
        Tprint = fuente.render(nombre[i]+': '+tiempo[i]+'s',0, white)
        ranki.blit(Tprint, (530, 70+25*i))
        i += 1 
    running = True
    while running:
        pos = pygame.mouse.get_pos()
        back = Button('Imagenes/back.png','Imagenes/back1.png')
        back.setCords(685,0), back.setrangeEnd(70,56), back.draw(ranki, pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.pressed(pos):
                    running = False
                    return menu()
        pygame.display.update()
    pygame.quit()

##///////////////////////////////////LOGIN//////////////////////////////////////
##///////////////////////////////////LOGIN//////////////////////////////////////

def login():
    login = pygame.display.set_mode((320, 180))
    pygame.display.set_caption("Login")
    icon = pygame.image.load('Imagenes/archer.png')
    pygame.display.set_icon(icon)
    backgroundL = pygame.image.load('Imagenes/login.png')
    fuenteL = pygame.font.SysFont("Arial", 30)
    Tusuario = fuenteL.render('Write your USER',0,(0,0,0))
    Tenter = fuenteL.render('Press ENTER',0,(0,0,0))
    input_box = InputBox(60, 75, 200, 32)
    done = False
    while not done:
        login.blit(backgroundL, (0,0))
        login.blit(Tusuario, (70,10))
        login.blit(Tenter, (90, 140))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            elif event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)
                key_name = key_name.upper()
                if key_name == 'RETURN':
                    done = True
                    global user_name
                    user_name = input_box.get_text()
                    return menu()
            input_box.handle_event(event)
        input_box.update()
        input_box.draw(login)
            
        pygame.display.flip()
    pygame.quit()

##//////////////////////////////////////////////////////////////////////////////
##//////////////////////////////////////////////////////////////////////////////

if __name__ == '__main__':
    login()
    pygame.quit()
