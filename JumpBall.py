import pygame
import random

pygame.init()

pygame.display.set_caption('JumpBall')
schermo = pygame.display.set_mode((500, 500))
palla = pygame.image.load('palla.png')
gameover = pygame.image.load('gameover.png')
punteggio = pygame.font.SysFont("Arial", 60, bold=True)
jump_effect = pygame.mixer.Sound("jump_effect.mp3")
gameoversound = pygame.mixer.Sound("gameoversound.mp3")

#colori
nero = (0,0,0)
bianco = (255, 255, 255)

def inizializza():
    global x, y, spostamentoy, pavimento_x, velocita, salto, pos_x,pos_y, score
    x = 20
    y = 319
    spostamentoy = 10
    pavimento_x = 0
    velocita = 3
    salto = False
    pos_x = 500 #posizione x ostacolo
    pos_y = random.randint(200,330)
    score = 0

def haiPerso():
    schermo.blit(gameover, (100,100))
    pygame.display.update()
    gameoversound.play()
    durata = True
    while durata:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                inizializza()
                durata = False
            if event.type == pygame.QUIT:
                pygame.quit()
        
#inserisco oggetti 
def inserisci_oggetti(x,y):
    schermo.blit(palla,(x,y))
    punteggio1  = punteggio.render(str(score), 1 , nero)
    schermo.blit(punteggio1, (400,20))

def collisione(x,y,pos_x):
    #calcolo i lati della pallina e dell'ostacolo
    palladx = x + palla.get_width()
    pallasx = x
    pallasu = y
    pallagiu = y + palla.get_height()
    ostacolodx = pos_x + 20
    ostacolosx = pos_x
    ostacolosu = 250
    #ostacologiu = 350 #ordinata pavimento
    if palladx > ostacolosx and pallasx < ostacolodx and pallasu > ostacolosu:
        haiPerso()
        

inizializza()

#main
duratagioco = True
while duratagioco:
    pavimento_x -=velocita
    if pavimento_x < -30:
        pavimento_x = 0
    schermo.fill(bianco)
    pavimento = pygame.draw.rect(schermo,(0,0,0),(pavimento_x,350,530,230),0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            duratagioco = False

    #salto
    if salto is False and pygame.key.get_pressed()[pygame.K_SPACE]:
        salto = True
        jump_effect.play()
    if salto is True:
        y -= spostamentoy*3
        spostamentoy -= 1
        if spostamentoy < -10:
            salto = False
            spostamentoy = 10
    ostacolo = pygame.draw.rect(schermo,nero,(pos_x,pos_y,20,300),0)  #ostacolo
    pos_x -= 8 #scorrimento ostacolo
    if pos_x < 0:
        pos_x = 500
        pos_y = random.randint(200,330)
    #collisione
    collisione(x,y,pos_x)

    if x > pos_x and pos_x >7 :
        score += int((350 - pos_y)/10)
  
    inserisci_oggetti(x,y)
    pygame.time.delay(30)
    pygame.display.update()
pygame.quit()
quit #chiusura gioco
