import pygame
from pygame.locals import *
from sys import exit
from random import randint
from datetime import time


pygame.init()

tempo = int(60)
largura = 640
altura = 480
X = 0
x1 = 0
Y = 0
y1 = 0
a = randint(40, 600)
b = randint(50, 430)

fundo = pygame.image.load('th.png')
pikachu = pygame.image.load('pikachu-removebg-preview.png')
pokebola = pygame.image.load('pokeball_PNG10 (1).png')

pontos = 0
font = pygame.font.SysFont('areal', 40, True, True)
font = pygame.font.SysFont('areal', 40, True, True)

pygame.mixer.music.set_volume(0.5)
musica = pygame.mixer.music.load('Pokemon_Abertura_em_Portugues_-_Temos_que_Pegar__PT_BR__[_YouConvert.net_].mp3')
pygame.mixer.music.play(-1)

barulho = pygame.mixer.Sound('select2.wav')
barulho.set_volume(0.2)

tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)
pygame.display.set_caption("izuna jogo")
relogio = pygame.time.Clock()

jogando = True

aberto = True
while aberto:
    if jogando == True:

        mensagem = f'pontos:{pontos}'
        mensagem1 = f'tempo:{' {:.0f}'.format(tempo)}'
        texto_formatad0 = font.render(mensagem, True, (0, 0, 0))
        tempo_formatad0 = font.render(mensagem1, True, (0, 0, 0))
        relogio.tick(30)
        tela.fill([255, 255, 255])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
        if pygame.key.get_pressed()[K_a]:
            X =X-20

        if pygame.key.get_pressed()[K_d]:
            X =X+20

        if pygame.key.get_pressed()[K_w]:
            Y =Y-20

        if pygame.key.get_pressed()[K_s]:
            Y =Y+20
        if tempo <= 0:
            jogando = False

        pikachu_rect =pygame.draw.rect(tela, (0, 255, 0), (X, Y, 20, 60))
        pokebola_circle =pygame.draw.circle(tela, (255, 0, 0), (a, b,), 40)
        
        if pikachu_rect.colliderect(pokebola_circle):
            a = randint(40, 600)
            b = randint(50, 430)
            pontos = pontos+1
            barulho.play()

        if Y <= 20:
            Y = 20
        if Y >= 425:
            Y = 425
        if X <= 20:
            X = 20
        if X >= 580:
            X = 580
        
        fundo1 = pygame.transform.smoothscale(fundo, (640, 480))
        pikachu1= pygame.transform.smoothscale(pikachu, (100, 100))
        pokebola1 = pygame.transform.smoothscale(pokebola, (100, 100))
        tela.blit(fundo1, (0, 0))
        tela.blit(pikachu1, (X-30, Y-20))
        tela.blit(pokebola1, (a-50, b-50))

        tela.blit(texto_formatad0, (420, 40))
        tempo = tempo-0.05
        tela.blit(tempo_formatad0, (10, 10))
        
    else:
        tela.fill((0,0,0))
        testo_fim = font.render('o tempo acabou', True, (255,255,255))
        testo_fim1 = font.render('vc fez {} pontos'.format(pontos), True, (255,0,0))
        testo_fim2 = font.render('aperte ESPASSO para jogar novamente'.format(pontos), True, (255,255,255))
        tela.blit(testo_fim, [40, 200])
        tela.blit(testo_fim1, [40, 230])
        tela.blit(testo_fim2, [40, 260])

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                jogando = True
                tempo = int(60)     
                pontos = 0
    pygame.display.update()