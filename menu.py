# JOGNA1 – Entrega Jogo N2
# Grupo 6
# Douglas Augusto Lacerda - Roteiro
# Leonardo Taguchi Agata - Artista
# Pedro Henrique Lemes Saccucci - Programador
# Renan Borges de Araújo - Documentação

import pygame, random
from sys import exit

print('-- Inicio do Programa --')

#Variáveis

SCREENX = 1280
Tam_screenx = 1280
SCREENY = 720
GAME_SPEED = 2
Tam_delorean = 72
Tam_Button = 128
mini_del = 48
big_del = 128
Tamx_health = 128
Tamy_health = 128
tam_enemy = 64
vel_delorean = 6
vel_alienx = 4
vel_alieny = 0
vel_alien2y = 0
vel_col_x1 = 0
vel_heartx = 4
vel_hearty = 0
vel_missil_x = 0
vel_dinax = 0
vel_dinay = 0
lancou = False
gravidade = 0.5
vel_missil_y = 0
vel_missil_inimigo2 = 0
pos_player_x = 200
pos_player_y = 300
pontos = 0
vez = 0
nez = 0
ii = 0
bg_indice = 0
indice_vid = 0
i_v = 0
toca = 0
triggered = False
triggered_inimigo2 = False
colidiu = False
passou = False
estado = 'cutscene'
morreu = False
reinicia = False
aparece = False

rodando = True
relogio = pygame.time.Clock()
current_time = 0    # Para Cronometrar
timer1 = 5000          # para spawnar powerup1
timer2 = 5000
timer3 = 0
timer4 = 0
explodiu = False
cut_timer = 4000
p1 = False
p2 = False
teleguiado = False



pygame.init()

# músicas e sons

musica_menu = pygame.mixer.music.load('music/cyberpunk/13.mp3')  # pygame.mixer.mixer() Só aceita MP3 
pygame.mixer.music.set_volume(0.3) #valores entre 0 e 1 para o som da música
# pygame.mixer.music.play(-1) # -1 começa a tocar denovo (em looping)

som_tiro = pygame.mixer.Sound('music/laser1.wav') # pygame.mixer.Sound() Só aceita WAV e ogg
som_tiro_inimigo2 = pygame.mixer.Sound('music/laserfire01.ogg') # pygame.mixer.Sound() Só aceita WAV e ogg
som_tiro.set_volume(1) #valores entre 0 e 1 para o som deste barulho
som_tiro_inimigo2.set_volume(1) #valores entre 0 e 1 para o som deste barulho

som_cutscene = pygame.mixer.Sound('music/mars.wav') # pygame.mixer.Sound() Só aceita WAV e ogg
som_cutscene.set_volume(1) #valores entre 0 e 1 para o som deste barulho
# pygame.mixer.music.play() começar (aqui vai o número de repetições, -1 é infinito) // pygame.mixer.music.stop() parar  // TEM PARA O SOUND
# pygame.mixer.music.pause() pausar // pygame.mixer.music.unpause() retomar de onde parou
# pygame.mixer.music.rewind() reiniciar musica // pygame.mixer.music.set_volume() define o volume de 0 a 1 // SÓ O SET_VOLUME PARA O SOUND

screen = pygame.display.set_mode((SCREENX,SCREENY))
pygame.display.set_caption('Jogo Nave')

font = pygame.font.SysFont('arial', 20, True, True) #1- qual font, tamanho, negrito, itálico

fundo_menu = pygame.image.load('Assets/main/menu_final.png').convert_alpha()
instrucao = pygame.image.load('Assets/main/como_jogar.png').convert_alpha()
post_it = pygame.image.load('Assets/main/how_2_play.png').convert_alpha()
post_it2 = post_it
post_it2 = pygame.transform.scale(post_it2, (72,72))


# Fundo

class Fundo(pygame.sprite.Sprite):         # Cria a classe fundo

    def __init__(self, xpos, indice):       # define parametros da Classe fundo
        super().__init__()
        
        self.sprites = []
        self.sprites.append(pygame.image.load('Assets/fundo_separado/1.png').convert_alpha())
        self.sprites.append(pygame.image.load('Assets/fundo_separado/2.png').convert_alpha())
        self.sprites.append(pygame.image.load('Assets/fundo_separado/3.png').convert_alpha())
        self.sprites.append(pygame.image.load('Assets/fundo_separado/4.png').convert_alpha())
        self.sprites.append(pygame.image.load('Assets/fundo_separado/5.png').convert_alpha())
        
        self.image = self.sprites[indice]       #Escolhendo o Sprite que será mostrado
        self.image = pygame.transform.scale(self.image, (SCREENX,SCREENY))

        self.rect = self.image.get_rect()                   # pega o retangulo da imagem (0,0,fundox,fundoy)
        self.rect[0] = xpos                                 # muda o primeiro parametro por xpos (esse,0,fundox,fundoy)
        self.rect[1] = 0        # muda o segundo parametro (0,esse,fundox,fundoy)
    
    def update(self):       #atualizar coisas 'nesse caso para o fundo'
        self.rect[0] -= GAME_SPEED
        
fundo_group = pygame.sprite.Group()    # Cria um Grupo
for i in range(5):          # Cria no máximo 2 i onde i é o número de vezes, na primeira interação i vale 0, na segunda i vale 1, ...
    fundo = Fundo(SCREENX * i, i)   # xpos = (SCREENX * i) isso é o x do primeiro fundo, o segundo vai estar lá na frente, depois de toda a largura do fundo
    fundo_group.add(fundo)    # adiciona no grupo

# VÍDEO CUTSCENE

video_ = []
video_.append(pygame.image.load('Assets/vid_png/1.png').convert_alpha())
video_.append(pygame.image.load('Assets/vid_png/2.png').convert_alpha())
video_.append(pygame.image.load('Assets/vid_png/3.png').convert_alpha())
video_.append(pygame.image.load('Assets/vid_png/4.png').convert_alpha())
video_.append(pygame.image.load('Assets/vid_png/5.png').convert_alpha())
video_.append(pygame.image.load('Assets/vid_png/6.png').convert_alpha())
video_.append(pygame.image.load('Assets/vid_png/7.png').convert_alpha())
video_.append(pygame.image.load('Assets/vid_png/8.png').convert_alpha())
video_.append(pygame.image.load('Assets/vid_png/9.png').convert_alpha())
video_.append(pygame.image.load('Assets/vid_png/10.png').convert_alpha())
video_.append(pygame.image.load('Assets/vid_png/11.png').convert_alpha())
video_.append(pygame.image.load('Assets/vid_png/12.png').convert_alpha())
video_.append(pygame.image.load('Assets/vid_png/13.png').convert_alpha())
video_.append(pygame.image.load('Assets/vid_png/14.png').convert_alpha())
video_.append(pygame.image.load('Assets/vid_png/15.png').convert_alpha())
video_.append(pygame.image.load('Assets/vid_png/16.png').convert_alpha())
video_.append(pygame.image.load('Assets/vid_inicio.png').convert_alpha())
video_.append(pygame.image.load('Assets/vid_inicio.png').convert_alpha())
video_.append(pygame.image.load('Assets/vid_inicio.png').convert_alpha())
video_.append(pygame.image.load('Assets/vid_inicio.png').convert_alpha())

# TECLAS ANIMADAS

teclas_animadas = []
teclas_animadas.append(pygame.image.load('Assets/main/w.png').convert_alpha())
teclas_animadas.append(pygame.image.load('Assets/main/w_.png').convert_alpha())
teclas_animadas.append(pygame.image.load('Assets/main/a.png').convert_alpha())
teclas_animadas.append(pygame.image.load('Assets/main/a_.png').convert_alpha())
teclas_animadas.append(pygame.image.load('Assets/main/s.png').convert_alpha())
teclas_animadas.append(pygame.image.load('Assets/main/s_.png').convert_alpha())
teclas_animadas.append(pygame.image.load('Assets/main/d.png').convert_alpha())
teclas_animadas.append(pygame.image.load('Assets/main/d_.png').convert_alpha())
teclas_animadas.append(pygame.image.load('Assets/main/e.png').convert_alpha())
teclas_animadas.append(pygame.image.load('Assets/main/e_.png').convert_alpha())
teclas_animadas.append(pygame.image.load('Assets/main/ctrl.png').convert_alpha())
teclas_animadas.append(pygame.image.load('Assets/main/ctrl_.png').convert_alpha())
teclas_animadas.append(pygame.image.load('Assets/main/space.png').convert_alpha())
teclas_animadas.append(pygame.image.load('Assets/main/space_.png').convert_alpha())
teclas_animadas.append(pygame.image.load('Assets/main/h.png').convert_alpha())
teclas_animadas.append(pygame.image.load('Assets/main/h_.png').convert_alpha())
teclas_animadas[14] = pygame.transform.scale(teclas_animadas[14], (Tam_Button,Tam_Button))
teclas_animadas[15] = pygame.transform.scale(teclas_animadas[15], (Tam_Button,Tam_Button))
teclas_animadas[14] = pygame.transform.rotate(teclas_animadas[14], -10)
teclas_animadas[15] = pygame.transform.rotate(teclas_animadas[15], -10)



w = 0
a = 2
s = 4
d = 6
e = 8
ctrl = 10
space = 12
h = 14

# MAIN

# Start Button

c1 = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW)  #normal
c2 = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND)   #maozinha
c3 = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_WAIT)   #Carregando
        
cursors = [c1,c2, c3]
cursor_index = 0

pygame.mouse.set_cursor(cursors[cursor_index])

class Start_button(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('Assets/main/start_menu_1.png').convert_alpha())
        self.sprites.append(pygame.image.load('Assets/main/start_menu_2.png').convert_alpha())
        self.sprites[0] = pygame.transform.rotate(self.sprites[0], 10)
        self.sprites[1] = pygame.transform.rotate(self.sprites[1], 10)
        
        
        self.atual = 0
        self.image = self.sprites[self.atual]
        
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (Tam_Button,Tam_Button))
        
        self.rect.topleft = (xpos, ypos)
        
        self.clicked = False

    def update(self):
        self.atual += 0.05
        if self.atual >= 2:
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        
    def draw(self, surface):
        action = False
		# Pega a posição do mouse
        pos = pygame.mouse.get_pos()
        
        #Verifica se o mouse foi clicado e se o cliked == False
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

		#Desenha o Botão na tela
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action


start_button = Start_button((Tam_screenx//2 - 380), (SCREENY//2))

# EXIT Button

class Exit_button(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('Assets/main/exit_menu_1.png').convert_alpha())
        self.sprites.append(pygame.image.load('Assets/main/exit_menu_2.png').convert_alpha())
        self.sprites[0] = pygame.transform.rotate(self.sprites[0], 10)
        self.sprites[1] = pygame.transform.rotate(self.sprites[1], 10)
        
        
        self.atual = 0
        self.image = self.sprites[self.atual]
        
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (Tam_Button,Tam_Button))
        self.rect.topleft = (xpos, ypos)
        
        self.clicked = False

    def update(self):
        self.atual += 0.05
        if self.atual >= 2:
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        
    def draw(self, surface):
        action = False
		# Pega a posição do mouse
        pos = pygame.mouse.get_pos()

        #Verifica se o mouse foi clicado e se o cliked == False
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

		# Desenha o Botão na tela
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action


exit_button = Exit_button((Tam_screenx//2 - 280), (SCREENY//2 + 40))

#Classes
class Delorean(pygame.sprite.Sprite):       # Criando a classe Delorean, que herda a classe Sprite
    def __init__(self, xpos, ypos):                     # Método construtor
        # pygame.sprite.Sprite.__init__(self) # Para inicializar a classe
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('Assets/delorean_novo1.png').convert_alpha())   #[0]medio1 #Adicionando os Sprites
        self.sprites.append(pygame.image.load('Assets/delorean_novo2.png').convert_alpha())   #[1]medio2
        self.sprites.append(pygame.image.load('Assets/delorean_novo4.png').convert_alpha())   #[2]grande
        self.sprites.append(pygame.image.load('Assets/delorean_novo3.png').convert_alpha())   #[3]pequeno
        
        self.atual = 0                              #escolhendo qual Sprite
        self.image = self.sprites[self.atual]       #Escolhendo o Sprite que será mostrado, usando o atributo self.image que é da classe Sprite
        self.image = pygame.transform.scale(self.image, (Tam_delorean,Tam_delorean))      #Para definir a Escala da Imagem, o Tamanho
        
        self.mini = False
        
        self.rect = self.image.get_rect()           #Usa o metodo rect, da classe Sprite, e o get_rect também desta classe, para pegar as 'coordenadas'
        self.rect.topleft = (xpos, ypos)              #  Pego o canto superior esquerdo, e coloco na posição (x,y)

        self.animar = False             # Vou usar para definir se quero animar ou Não
        
    def mover_vertical(self):
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_w] or tecla[pygame.K_s] or tecla[pygame.K_UP] or tecla[pygame.K_DOWN]:
            if (tecla[pygame.K_w] or tecla[pygame.K_UP]) and self.rect.y > 1:
                self.animar = False
                self.direcao = 'cima'
            #mover
                if self.rect.y > 1:    # verifica se ta dentro da tela
                    self.rect.y -= vel_delorean
            if (tecla[pygame.K_s] or tecla[pygame.K_DOWN]) and self.rect.y < 665:
                self.animar = False
                self.direcao = 'baixo'
                #mover
                if self.rect.y < 665:  # verifica se ta dentro da tela
                    self.rect.y += vel_delorean   
        else:                       #se não apertar nada
            self.animar = True      # executa a função para quando ele estiver parado
    
    def mover_horizontal(self):
        tecla = pygame.key.get_pressed()
        if (tecla[pygame.K_a] or tecla[pygame.K_LEFT]) and self.rect.x > 1:
            self.rect.x += -vel_delorean
        if (tecla[pygame.K_d] or tecla[pygame.K_RIGHT]) and self.rect.x < 1000:
            self.rect.x += vel_delorean
    
    def animar_del(self):
        if self.animar == True:
            self.atual = self.atual + 0.05             # Muda o valor do self.atual, utilizo este número quebrado para mudar devagar
            #if self.atual >= len(self.sprites):     #se o self.atual foi maior que o numero de sprites
            if self.atual >= 2:                     # se for maior ou igual a 2
                self.atual = 0                      # Muda self.atual para 0
                self.animar = False                 # Para parar de animar
            self.image = self.sprites[int(self.atual)]   # Atualiza para o próximo sprite, eu utilizo o int para não ter problemas 
            self.image = pygame.transform.scale(self.image, (Tam_delorean,Tam_delorean))      #Tenho que colocar denovo para aplicar em todos os sprites, Para definir a Escala da Imagem, o Tamanho
        else:
            if self.direcao == 'cima':   # se para cima
                #subir
                self.atual = 2      # define o sprite [2]
                self.image = self.sprites[int(self.atual)]
                self.image = pygame.transform.scale(self.image, (Tam_delorean,Tam_delorean))

            else:                   #se para baixo
                #descer
                self.atual = 3      # define o sprite [3]
                self.image = self.sprites[int(self.atual)]
                self.image = pygame.transform.scale(self.image, (Tam_delorean,Tam_delorean))
    def pequeno(self):
        global vel_delorean
        if tecla[pygame.K_LCTRL]: # se apertar o left control
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (mini_del,mini_del))
            vel_delorean = 9
            self.mini = True
        else:
            vel_delorean = 6
            self.mini = False
    
    def update(self):   #para atualizar
        self.mover_vertical()
        self.mover_horizontal()
        self.animar_del()
        self.pequeno()
        
    
        

delorean_group = pygame.sprite.Group()  #Para criar o grupo de Sprites        
delorean = Delorean(pos_player_x,pos_player_y)       #Crio meu objeto Delorean, com os atributos e métodos da classe Delorean      
delorean_group.add(delorean)    #adicionando o  objeto delorean no Grupo

# Health

class Health(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos):
        # pygame.sprite.Sprite.__init__(self)
        super().__init__()
        
        
        self.sprites = []
        self.sprites.append(pygame.image.load('Assets/health/1.png').convert_alpha())   #[0] 5 corações
        self.sprites.append(pygame.image.load('Assets/health/2.png').convert_alpha())   #[1] 4 corações
        self.sprites.append(pygame.image.load('Assets/health/3.png').convert_alpha())   #[2] 3 corações
        self.sprites.append(pygame.image.load('Assets/health/4.png').convert_alpha())   #[3] 2 corações
        self.sprites.append(pygame.image.load('Assets/health/5.png').convert_alpha())   #[4] 1 corações
        self.sprites.append(pygame.image.load('Assets/health/6.png').convert_alpha())   #[5] 0 corações
        
        self.atual = 0                              #escolhendo qual Sprite
        self.image = self.sprites[self.atual]       #Escolhendo o Sprite que será mostrado, usando o atributo self.image que é da classe Sprite
        self.image = pygame.transform.scale(self.image, (Tamx_health,Tamy_health))
        
        self.rect = self.image.get_rect()           #Usa o metodo rect, da classe Sprite, e o get_rect também desta classe, para pegar as 'coordenadas'
        self.rect.topleft = (xpos, ypos)
        
    def update(self):
        self.image = self.sprites[int(self.atual)]   # Atualiza para o próximo sprite, eu utilizo o int para não ter problemas 
        self.image = pygame.transform.scale(self.image, (Tamx_health,Tamy_health))
    def perdeu_vida(self):
        if self.atual < 5:
            self.atual += 1
    def ganhou_vida(self):
        if self.atual > 0:
            self.atual -= 1
    def morreu(self):
        global reinicia
        if self.atual == 5:
            reinicia = True
        #     exit()
        #     rodando = False
        #     # estado = 'menu'
        # else:
        #     rodando = True
        #     # estado = 'game'
        return reinicia
        # return estado
    
health_group = pygame.sprite.Group()  #Para criar o grupo de Sprites        
health = Health(20,20)       #Crio meu objeto Delorean, com os atributos e métodos da classe Delorean      
health_group.add(health)    #adicionando o  objeto delorean no Grupo

# Classe Missil Delorean

class Missil(pygame.sprite.Sprite):
    
    def __init__(self, xpos, ypos):
        # pygame.sprite.Sprite.__init__(self)
        super().__init__()
        
        
        self.sprites = []
        self.sprites.append(pygame.image.load('Assets/missil1.png').convert_alpha())
        self.sprites.append(pygame.image.load('Assets/missil5.png').convert_alpha())
        self.sprites.append(pygame.image.load('Assets/nada.png').convert_alpha())
        self.sprites.append(pygame.image.load('Assets/missil_azul1.png').convert_alpha())
        self.sprites.append(pygame.image.load('Assets/missil_azul2.png').convert_alpha())
        self.sprites[0] = pygame.transform.scale(self.sprites[0], (32,32))                              # Conversão do Tamanho
        self.sprites[1] = pygame.transform.scale(self.sprites[1], (32,32))                              # Conversão do Tamanho
        self.sprites[3] = pygame.transform.scale(self.sprites[3], (32,32))                              # Conversão do Tamanho
        self.sprites[4] = pygame.transform.scale(self.sprites[4], (32,32))
        # self.sprites[0] = pygame.transform.rotate(self.sprites[0], -45)
        
        self.atual = 0
        self.image = self.sprites[self.atual]
        
        self.rect = self.image.get_rect()           #Usa o metodo rect, da classe Sprite, e o get_rect também desta classe, para pegar as 'coordenadas'
        self.rect.topleft = (xpos, ypos)
        
        
    def pequeno(self):
        if tecla[pygame.K_LCTRL]: # se apertar o left control
            self.atual = 2
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (mini_del,mini_del))
            
    def movimentacao(self):
        global vel_missil_x, triggered
        if triggered == False:
            self.rect.y = delorean.rect.y
            self.rect.x = delorean.rect.x
        if self.rect.x >= 1300:
            vel_missil_x = 0
            triggered = False
            self.rect.x = delorean.rect.x
            self.rect.y = delorean.rect.y
    
    def teleguiado(self):
        global vel_missil_y, teleguiado, triggered
        if teleguiado == True and triggered == True:
            if self.rect.y < ((inimigo1_group.sprites()[0]).rect.y):
                vel_missil_y = 2
            elif self.rect.y > ((inimigo1_group.sprites()[0]).rect.y):
                vel_missil_y = -2
            else:
                vel_missil_y = 0
        else:
            vel_missil_y = 0
        
        if teleguiado == True:
            self.atual += 0.05
            if self.atual >= 5:
                self.atual = 3
            self.image = self.sprites[int(self.atual)]
        else:
            self.atual += 0.05
            if self.atual >= 2:
                self.atual = 0
            self.image = self.sprites[int(self.atual)]
            
    
    def update(self):
            
        self.movimentacao()
        self.pequeno()
        self.teleguiado()
        
        self.rect.x += vel_missil_x
        self.rect.y += vel_missil_y
    
    def respawn_missil_(self):
        triggered = False
        vel_missil_x = 0
        self.rect.x = delorean.rect.x
        self.rect.y = delorean.rect.y
        print(self.rect.y)
        return triggered, vel_missil_x
    
missil_group = pygame.sprite.Group()  #Para criar o grupo de Sprites        
missil = Missil(delorean.rect.x, delorean.rect.y)       #Crio meu objeto Missil, com os atributos e métodos da classe Missil      
missil_group.add(missil)    #adicionando o  objeto delorean no Grupo


# Classe DYNAMITE

class Dynamite(pygame.sprite.Sprite):
    
    def __init__(self, xpos, ypos):
        # pygame.sprite.Sprite.__init__(self)
        super().__init__()
        
        
        self.sprites = []
        self.sprites.append(pygame.image.load('Assets/dynamite/dina_32.png').convert_alpha())
        self.sprites.append(pygame.image.load('Assets/dynamite/explosion.png').convert_alpha())
        self.sprites.append(pygame.image.load('Assets/nada.png').convert_alpha())
        self.sprites[0] = pygame.transform.scale(self.sprites[0], (32,32))                              # Conversão do Tamanho 
        self.sprites[1] = pygame.transform.scale(self.sprites[1], (32,32))                              # Conversão do Tamanho 
        # self.sprites[0] = pygame.transform.rotate(self.sprites[0], -45)
        
        self.atual = 2
        self.image = self.sprites[self.atual]
        
        self.rect = self.image.get_rect()           #Usa o metodo rect, da classe Sprite, e o get_rect também desta classe, para pegar as 'coordenadas'
        self.rect.topleft = (xpos, ypos)
        
        
    def pequeno(self):
        if tecla[pygame.K_LCTRL]: # se apertar o left control
            self.atual = 2
            self.image = self.sprites[int(self.atual)]
            # self.image = pygame.transform.scale(self.image, (mini_del,mini_del))
            
    def movimentacao(self):
        global vel_dinax, vel_dinay, lancou
        if lancou == False:
            self.rect.y = delorean.rect.y
            self.rect.x = delorean.rect.x
        if self.rect.x >= 1300 or self.rect.y >= 750:
            vel_dinax = 0
            vel_dinay = 0
            lancou = False
            self.rect.x = delorean.rect.x
            self.rect.y = delorean.rect.y
            self.atual = 2
            
    def gravity(self):
        global vel_dinay, vel_dinax, lancou
        if (self.rect.y <= (delorean.rect.y - 50) or lancou == True) and explodiu == False:
            vel_dinay += gravidade
            vel_dinax = 4
            # lancou = Truee
    
    def update(self):
        
        self.image = self.sprites[int(self.atual)]
            
        self.movimentacao()
        self.pequeno()
        self.gravity()
        

        
        self.rect.x += vel_dinax
        self.rect.y += vel_dinay
    
dina_group = pygame.sprite.Group()  #Para criar o grupo de Sprites        
dina = Dynamite(delorean.rect.x, delorean.rect.y)       #Crio meu objeto Dynamite, com os atributos e métodos da classe Dynamite      
dina_group.add(dina)    #adicionando o  objeto Dynamite no Grupo

# Classe Inimigo1

class Inimigo1(pygame.sprite.Sprite):
    
    def __init__(self, xpos, ypos):
        # pygame.sprite.Sprite.__init__(self)
        super().__init__()
        
        
        self.sprites = []
        self.sprites.append(pygame.image.load('Assets/inimigo_1_invisible.png').convert_alpha())
        self.sprites.append(pygame.image.load('Assets/inimigo_1_v_c_.png').convert_alpha())
        self.sprites.append(pygame.image.load('Assets/inimigo_1_a_s_.png').convert_alpha())
        self.sprites.append(pygame.image.load('Assets/inimigo_1_a_c_.png').convert_alpha())
        # self.sprites[0] = pygame.transform.flip(self.sprites[0], True, False)
        
        # self.sprites[0] = pygame.transform.scale(self.sprites[0], (50,50))                              # Conversão do Tamanho 
        
        self.atual = 3
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image, (tam_enemy,tam_enemy))
        
        self.rect = self.image.get_rect()           #Usa o metodo rect, da classe Sprite, e o get_rect também desta classe, para pegar as 'coordenadas'
        self.rect.topleft = (xpos, ypos)
        
    def update(self):
        global pontos, vel_alienx, vez, vel_alieny, vel_col_x1
        #passou = 0
        if pontos <= 10:
            vel_alienx = 4
        elif pontos <= 15:
            vel_alienx = 6
        elif pontos <= 20:
            if vez <= 20:
                if self.rect.top > 0:
                    vel_alieny = -4
                else:
                    vel_alieny = 0
                    vez = 20
                if vez == 20:
                    vez += 20
                else:
                    vez += 1
                    #print(vez)
            else:
                if self.rect.top < 650:
                    vel_alieny = 4
                else:
                    vel_alieny = 0
                    vez = 21
                if vez == 21:
                    vez -= 20
                else:
                    vez -= 1
        else:
            if self.rect.y < delorean.rect.y:
                vel_alieny = 2
            elif self.rect.y > delorean.rect.y:
                vel_alieny = -2
            else:
                vel_alieny = 0
        self.rect.x -= (vel_alienx + vel_col_x1)
        self.rect.y += vel_alieny
                
def get_random_y_inimigo1(xpos):  #inimigos2
    posy_inimigo1 = random.randint(1,650)
    inimigo1 = Inimigo1(xpos, posy_inimigo1)
    return inimigo1

def get_delorean_y_inimigo1(xpos):
    posy_inimigo1 = delorean.rect.y
    inimigo1 = Inimigo1(xpos, posy_inimigo1)
    return inimigo1
        
inimigo1_group = pygame.sprite.Group()  #Para criar o grupo de Sprites
inimigo1 = get_random_y_inimigo1(Tam_screenx + 70)      
inimigo1_group.add(inimigo1)    #adicionando o  objeto inimigo1 no Grupo


# Classe Inimigo2

class Inimigo2(pygame.sprite.Sprite):
    
    def __init__(self, xpos, ypos):
        # pygame.sprite.Sprite.__init__(self)
        super().__init__()
        
        
        self.sprites = []
        
        self.sprites.append(pygame.image.load('Assets/jetpack_novo2.png').convert_alpha())
        self.sprites.append(pygame.image.load('Assets/jetpack_novo3.png').convert_alpha())
        self.sprites.append(pygame.image.load('Assets/jetpack_novo4.png').convert_alpha())

        self.image = self.sprites[1]
        self.image = pygame.transform.scale(self.image, (tam_enemy,tam_enemy))
        
        self.rect = self.image.get_rect()           #Usa o metodo rect, da classe Sprite, e o get_rect também desta classe, para pegar as 'coordenadas'
        self.rect.topleft = (xpos, ypos)
        
    def update(self):
        global pontos, vel_alienx, ii, vel_alien2y
        if self.rect.x > 1200:
            self.rect.x -= vel_alienx
        if pontos > 10 and pontos <= 20:
            if ii <= 40:
                if self.rect.top > 0:
                    vel_alien2y = -2
                else:
                    vel_alien2y = 0
                    ii = 40
                if ii == 40:
                    ii += 40
                else:
                    ii += 1
                    #print(ii)
            else:
                if self.rect.top < 650:
                    vel_alien2y = 2
                else:
                    vel_alien2y = 0
                    ii = 41
                if ii == 41:
                    ii -= 40
                else:
                    ii -= 1
        elif pontos > 20:
            if self.rect.y < delorean.rect.y:
                vel_alien2y = 2
            elif self.rect.y > delorean.rect.y:
                vel_alien2y = -2
            else:
                vel_alien2y = 0
            # self.rect.y = delorean.rect.y
            # vel_alien2y = 0
        if vel_alien2y == 0:
            self.atual = 1
        elif vel_alien2y > 0:
            self.atual = 0
        else:
            self.atual = 2
        self.image = self.sprites[self.atual]
        self.rect.y += vel_alien2y
    
def voltar():
    inimigo2.rect.x = 1350
    inimigo2.rect.y = random.randint(1,640)
        
def get_random_y_inimigo2(xpos):  #inimigos2
    posy_inimigo2 = random.randint(1,640)
    inimigo2 = Inimigo2(xpos, posy_inimigo2)
    return inimigo2
        
inimigo2_group = pygame.sprite.Group()  #Para criar o grupo de Sprites
inimigo2 = get_random_y_inimigo2(Tam_screenx + 70)      
inimigo2_group.add(inimigo2)    #adicionando o  objeto inimigo2 no Grupo

class Projetil_inimigo2(pygame.sprite.Sprite):
    
    def __init__(self, xpos, ypos):
        # pygame.sprite.Sprite.__init__(self)
        super().__init__()
        
        
        self.sprites = []
        self.sprites.append(pygame.image.load('Assets/fire.png').convert_alpha())
        self.sprites.append(pygame.image.load('Assets/nada.png').convert_alpha())
        self.sprites[0] = pygame.transform.scale(self.sprites[0], (50,50))                              # Conversão do Tamanho 
        self.sprites[0] = pygame.transform.rotate(self.sprites[0], -90)
        
        self.atual = 1 
        self.image = self.sprites[self.atual]
        
        self.rect = self.image.get_rect()           #Usa o metodo rect, da classe Sprite, e o get_rect também desta classe, para pegar as 'coordenadas'
        self.rect.topleft = ((xpos), ypos)
        
    def aparecer_tiro(self):
        global triggered_inimigo2, aparece
        if triggered_inimigo2 == True and aparece == True:
            self.atual = 0
        else:
            self.atual = 1
    
    def update(self):
        global vel_missil_inimigo2, triggered_inimigo2, aparece
        
        self.aparecer_tiro()
        self.image = self.sprites[int(self.atual)]
        
        self.rect.x -= vel_missil_inimigo2
        if triggered_inimigo2 == False:
            self.rect.y =(inimigo2_group.sprites()[0]).rect.y
            self.rect.x =((inimigo2_group.sprites()[0]).rect.x - 20)
            #print('entrou1')
        if self.rect.x <= -50:
            vel_missil_inimigo2 = 0
            triggered_inimigo2 = False
            self.rect.x = ((inimigo2_group.sprites()[0]).rect.x - 20)
            self.rect.y = (inimigo2_group.sprites()[0]).rect.y
        if self.rect.x <= 0:
            aparece = False
        if self.rect.x >= Tam_screenx:
            vel_missil_inimigo2 = 0
            triggered_inimigo2 = False
            self.rect.x = ((inimigo2_group.sprites()[0]).rect.x - 20)
            self.rect.y = (inimigo2_group.sprites()[0]).rect.y
            #print('entrou2')
        #print(self.rect.x, self.rect.y)
    
    def respawn_missil_inimigo2(self):
        triggered_inimigo2 = False
        vel_missil_inimigo2 = 0
        self.rect.x = ((inimigo2_group.sprites()[0]).rect.x - 20)
        self.rect.y = (inimigo2_group.sprites()[0]).rect.y
        return triggered_inimigo2, vel_missil_inimigo2
    
projetil_inimigo2_group = pygame.sprite.Group()  #Para criar o grupo de Sprites        
projetil_ini_2 = Projetil_inimigo2(((inimigo2_group.sprites()[0]).rect.x - 20), (inimigo2_group.sprites()[0]).rect.y)       #Crio meu objeto projetil_ini_2, com os atributos e métodos da classe projetil_ini_2      
projetil_inimigo2_group.add(projetil_ini_2)    #adicionando o  objeto projetil_ini_2 no Grupo

class PowerUp1(pygame.sprite.Sprite):
    
    def __init__(self, xpos, ypos):
        # pygame.sprite.Sprite.__init__(self)
        super().__init__()
        
        
        self.sprites = []
        self.sprites.append(pygame.image.load('Assets/health/heart_1.png').convert_alpha())
        self.sprites.append(pygame.image.load('Assets/health/heart_2.png').convert_alpha())
        self.sprites[0] = pygame.transform.scale(self.sprites[0], (64,64))                              # Conversão do Tamanho 
        
        self.atual = 0
        self.image = self.sprites[self.atual]
        
        self.rect = self.image.get_rect()           #Usa o metodo rect, da classe Sprite, e o get_rect também desta classe, para pegar as 'coordenadas'
        self.rect.topleft = (xpos, ypos)
        
    def update(self):
        global pontos, vel_heartx, nez, vel_hearty
        #passou = 0
        if pontos <= 10:
            vel_heartx = 4
        elif pontos <= 25:
            vel_heartx = 6
        else:
            if nez <= 40:
                if self.rect.top > 0:
                    vel_hearty = -4
                else:
                    vel_hearty = 0
                    nez = 40
                if nez == 40:
                    nez += 40
                else:
                    nez += 1
                    #print(vez)
            else:
                if self.rect.top < 650:
                    vel_hearty = 4
                else:
                    vel_hearty = 0
                    nez = 41
                if nez == 41:
                    nez -= 40
                else:
                    nez -= 1
        self.rect.x -= vel_heartx
        self.rect.y += vel_hearty
                
def get_random_y_powerup1(xpos):  #inimigos2
    posy_powerup1 = random.randint(1,650)
    powerup1 = PowerUp1(xpos, posy_powerup1)
    return powerup1

powerup1_group = pygame.sprite.Group()  #Para criar o grupo de Sprites

class PowerUp2(pygame.sprite.Sprite):
    
    def __init__(self, xpos, ypos):
        # pygame.sprite.Sprite.__init__(self)
        super().__init__()
        
        
        self.sprites = []
        self.sprites.append(pygame.image.load('Assets/mira_.png').convert_alpha())
        self.sprites[0] = pygame.transform.scale(self.sprites[0], (64,64))                              # Conversão do Tamanho 
        
        self.atual = 0
        self.image = self.sprites[self.atual]
        
        self.rect = self.image.get_rect()           #Usa o metodo rect, da classe Sprite, e o get_rect também desta classe, para pegar as 'coordenadas'
        self.rect.topleft = (xpos, ypos)
        
    def update(self):
        global pontos, vel_pwup2x
        #passou = 0
        if pontos <= 20:
            vel_pwup2x = 4
        else:
            vel_pwup2x = 6
        self.rect.x -= vel_pwup2x
                
def get_random_y_powerup2(xpos):  #inimigos2
    posy_powerup2 = random.randint(1,650)
    powerup2 = PowerUp2(xpos, posy_powerup2)
    return powerup2

powerup1_group = pygame.sprite.Group()  #Para criar o grupo de Sprites
powerup2_group = pygame.sprite.Group()  #Para criar o grupo de Sprites

# Funções

def play_music():
    pygame.mixer.music.play(-1) # -1 começa a tocar denovo (em looping)
    
def stop_music():
    pygame.mixer.music.stop() # parar a musica

def atirou():
    global triggered
    if triggered == False:
        som_tiro.play()
    vel_missil_x = 12
    triggered = True
    return vel_missil_x, triggered
def atirou2():
    som_tiro_inimigo2.play()
    vel_missil_inimigo2 = 12
    triggered_inimigo2 = True
    aparece = True
    return vel_missil_inimigo2, triggered_inimigo2, aparece

def lancar():
    global lancou, vel_dinax, vel_dinay
    if lancou == False:
        som_tiro.play()
        vel_dinax = 4
        vel_dinay = -10
        lancou = True
        dina.atual = 0
    return vel_dinax, vel_dinay, lancou, dina.atual

def spawn_proj_inimigo2():
    projetil_ini_2 = Projetil_inimigo2(((inimigo2_group.sprites()[0]).rect.x - 20), (inimigo2_group.sprites()[0]).rect.y)
    return projetil_ini_2 

def is_off_screen(sprite):  # define se o sprite está fora da tela
    return sprite.rect[0] < -(sprite.rect[2])

def is_off_screeny(sprite):  # define se o sprite está fora da tela
    return sprite.rect[1] < -(sprite.rect[3])


def colisions():
    global pontos, vel_missil_inimigo2, colidiu, triggered_inimigo2, p1, vel_col_x1, p2, teleguiado, vel_dinax, vel_dinay, timer4, explodiu, lancou
    if (pygame.sprite.groupcollide(delorean_group, inimigo1_group, False, False,  pygame.sprite.collide_mask)) :     # colisao delorean/inimigo1 ou inimigo1/sair da tela
        inimigo1_group.remove(inimigo1_group.sprites()[0])
        if pontos <= 20:
            inimigo1 = get_random_y_inimigo1(Tam_screenx + 70)   
        else:
            inimigo1 = get_delorean_y_inimigo1(Tam_screenx + 70)   
            
        inimigo1_group.add(inimigo1)    #adicionando o  objeto inimigo1 no Grupo
        health.perdeu_vida()
        #pontos -= 1
        colidiu = True
    elif (pygame.sprite.groupcollide(delorean_group, inimigo2_group, False, False,  pygame.sprite.collide_mask)) or (is_off_screen(inimigo2_group.sprites()[0])):     # colisao delorean/inimigo1 ou inimigo1/sair da tela
        inimigo2_group.remove(inimigo2_group.sprites()[0])
        inimigo2 = get_random_y_inimigo1(Tam_screenx + 70)    
        inimigo2_group.add(inimigo2)    #adicionando o  objeto inimigo2 no Grupo
        #voltar()
        #pontos -= 1
        health.perdeu_vida()
        colidiu =  True
    elif (pygame.sprite.groupcollide(delorean_group, projetil_inimigo2_group, False, False,  pygame.sprite.collide_mask)):     # colisao delorean/Projetil_Inimigo2 ou Projetil_Inimigo2/sair da tela
        projetil_inimigo2_group.remove(projetil_inimigo2_group.sprites()[0])
        vel_missil_inimigo2 = 0
        triggered_inimigo2 = False
        projetil_ini_2 = spawn_proj_inimigo2()   
        projetil_inimigo2_group.add(projetil_ini_2)    #adicionando o  objeto inimigo2 no Grupo
        #triggered_inimigo2, vel_missil_inimigo2 = projetil_ini_2.respawn_missil_inimigo2()
        #pontos -= 1
        health.perdeu_vida()
        colidiu =  True
    elif (pygame.sprite.groupcollide(missil_group, inimigo1_group, False, False,  pygame.sprite.collide_mask)):      # colisao missil/inimigo1
        inimigo1_group.remove(inimigo1_group.sprites()[0])
        
        if pontos <= 20:
            inimigo1 = get_random_y_inimigo1(Tam_screenx + 70)   
        else:
            inimigo1 = get_delorean_y_inimigo1(Tam_screenx + 70)   

        inimigo1_group.add(inimigo1)    #adicionando o  objeto inimigo1 no Grupo
        pontos += 1
        colidiu = True
    elif (pygame.sprite.groupcollide(missil_group, inimigo2_group, False, False,  pygame.sprite.collide_mask)):      # colisao missil/inimigo2
        pontos += 3
        inimigo2_group.remove(inimigo2_group.sprites()[0])
        inimigo2 = get_random_y_inimigo2(Tam_screenx + 70)    
        inimigo2_group.add(inimigo2)    #adicionando o  objeto inimigo2 no Grupo
    elif (pygame.sprite.groupcollide(delorean_group, powerup1_group, False, True,  pygame.sprite.collide_mask)):      # colisao missil/inimigo2
        # powerup1_group.remove(powerup1_group.sprites()[0])
        if health.atual > 0:
            health.atual -= 1
        p1 = False
    elif (pygame.sprite.groupcollide(delorean_group, powerup2_group, False, True,  pygame.sprite.collide_mask)):      # colisao missil/inimigo2
        teleguiado = True
        p2 = False
    elif (pygame.sprite.groupcollide(dina_group, inimigo1_group, False, False,  pygame.sprite.collide_mask)):      # colisao missil/inimigo2
        dina.atual = 1
        dina.image = dina.sprites[int(dina.atual)]
        vel_dinax = 0
        vel_dinay = 0
        explodiu = True
        # lancou = False
        timer4 = (pygame.time.get_ticks() + 0)
        inimigo1_group.remove(inimigo1_group.sprites()[0])
        
        if pontos <= 20:
            inimigo1 = get_random_y_inimigo1(Tam_screenx + 70)   
        else:
            inimigo1 = get_delorean_y_inimigo1(Tam_screenx + 70)   

        inimigo1_group.add(inimigo1)    #adicionando o  objeto inimigo1 no Grupo
        pontos += 2
        colidiu = True
    elif (pygame.sprite.groupcollide(dina_group, inimigo2_group, False, False,  pygame.sprite.collide_mask)):      # colisao missil/inimigo2
        dina.atual = 1
        dina.image = dina.sprites[int(dina.atual)]
        vel_dinax = 0
        vel_dinay = 0
        explodiu = True
        # lancou = False
        timer4 = (pygame.time.get_ticks() + 0)
        
        pontos += 6
        inimigo2_group.remove(inimigo2_group.sprites()[0])
        inimigo2 = get_random_y_inimigo2(Tam_screenx + 70)    
        inimigo2_group.add(inimigo2)    #adicionando o  objeto inimigo2 no Grupo
    elif (is_off_screen(inimigo1_group.sprites()[0])):
        if vel_col_x1 <= 10:
            vel_col_x1 += 0.5
        inimigo1_group.remove(inimigo1_group.sprites()[0])
        # (inimigo1_group.sprites()[0]).rect.x = Tam_screenx + 70
        if pontos <= 20:
            inimigo1 = get_random_y_inimigo1(Tam_screenx + 70)   
        else:
            inimigo1 = get_delorean_y_inimigo1(Tam_screenx + 70) 

        inimigo1_group.add(inimigo1)    #adicionando o  objeto inimigo1 no Grupo
    elif p1 == True and (is_off_screen(powerup1_group.sprites()[0])):     # colisao delorean/Projetil_Inimigo2 ou Projetil_Inimigo2/sair da tela
        powerup1_group.remove(powerup1_group.sprites()[0])
        p1 = False
    elif p2 == True and (is_off_screen(powerup2_group.sprites()[0])):     # colisao delorean/Projetil_Inimigo2 ou Projetil_Inimigo2/sair da tela
        powerup2_group.remove(powerup2_group.sprites()[0])
        p2 = False
    else:
        colidiu = False
    return colidiu, vel_missil_inimigo2, triggered_inimigo2, p1, p2, vel_col_x1, teleguiado

def reiniciar():
    global p1, p2
    estado = 'menu'
    stop_music()
    dina.atual = 2
    health.atual = 0
    pontos = 0
    vel_alieny = 0
    vel_alien2y = 0
    vel_alienx = 4
    vel_col_x1 = 0
    vel_hearty = 0
    vel_heartx = 4
    vel_missil_inimigo2 = 0
    vel_missil_x = 0
    vel_missil_y = 0
    vel_dinax = 0
    vel_dinay = 0
    lancou = False
    triggered = False
    teleguiado = False
    timer1 = (pygame.time.get_ticks() + 2000)
    timer2 = (pygame.time.get_ticks() + 2000)
    delorean_group.sprites()[0].rect.topleft = (pos_player_x, pos_player_y) 
    missil_group.remove(missil_group.sprites()[0])
    missil = Missil(delorean.rect.x, delorean.rect.y)      
    missil_group.add(missil)
    dina.rect.x = delorean.rect.x
    dina.rect.y = delorean.rect.y
    inimigo1_group.remove(inimigo1_group.sprites()[0])
    inimigo1 = get_random_y_inimigo1(Tam_screenx + 70)      
    inimigo1_group.add(inimigo1)
    inimigo2_group.remove(inimigo2_group.sprites()[0])
    inimigo2 = get_random_y_inimigo2(Tam_screenx + 70)      
    inimigo2_group.add(inimigo2)
    projetil_inimigo2_group.remove(projetil_inimigo2_group.sprites()[0])
    projetil_ini_2 = Projetil_inimigo2(((inimigo2_group.sprites()[0]).rect.x - 20), (inimigo2_group.sprites()[0]).rect.y)      
    projetil_inimigo2_group.add(projetil_ini_2)
    if p1 == True:
        if powerup1_group.sprites()[0].rect.x > 0: 
            powerup1_group.remove(powerup1_group.sprites()[0])
            p1 = False
    if p2 == True:
        if powerup2_group.sprites()[0].rect.x > 0: 
            powerup2_group.remove(powerup2_group.sprites()[0])
            p2 = False
    
    return estado, health.atual, pontos, vel_alieny, vel_alien2y, vel_alienx, vel_heartx, vel_hearty, timer1, timer2, p1, p2, vel_missil_inimigo2, vel_missil_x, vel_missil_y, triggered, teleguiado, vel_col_x1, vel_dinax, vel_dinay, lancou

while rodando:      # ======================================================================================
    relogio.tick(60)        # define o número de frames por segundo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('-- Fim do Programa --')
            pygame.quit()
            #exit()
            # rodando = False
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
        
    if (x > start_button.rect.x) and (x < (start_button.rect.x + Tam_Button)) and (y > start_button.rect.y) and (y < (start_button.rect.y + Tam_Button) and estado == 'menu'):
        cursor_index = 1
        pygame.mouse.set_cursor(cursors[cursor_index])
    elif (x > exit_button.rect.x) and (x < (exit_button.rect.x + Tam_Button)) and (y > exit_button.rect.y) and (y < (exit_button.rect.y + Tam_Button) and estado == 'menu'):
        cursor_index = 1
        pygame.mouse.set_cursor(cursors[cursor_index])
    else:
        cursor_index = 0
        pygame.mouse.set_cursor(cursors[cursor_index])
    if estado == 'cutscene': # ===========================================
        cursor_index = 2
        pygame.mouse.set_cursor(cursors[cursor_index])
        
        current_time = pygame.time.get_ticks()  # pega os segundos
        screen.blit(video_[i_v], (0,0)) # Desenhar o BG
        if toca == 0:
            som_cutscene.play(-1)
            toca += 1
        if indice_vid < 16:
            indice_vid += 0.15
        i_v = int(indice_vid)
        if current_time > cut_timer:
            estado = 'menu'
        tecla1 = pygame.key.get_pressed()
        if tecla1[pygame.K_SPACE]:
            estado = 'how_to_play'
    elif estado == 'menu':  # =============================================
        screen.blit(fundo_menu, (0,0))
        screen.blit(post_it2, ((Tam_screenx//2 + 145), (SCREENY//2 + 10))) # 800,600
        h += 0.15
        if h >= 16:
            h = 14
        screen.blit(teclas_animadas[int(h)], ((Tam_screenx//2 + 200), (SCREENY//2 + 30)))
        start_button.update()
        exit_button.update()
        if toca == 0:
            som_cutscene.play(-1)
            toca += 1
        if start_button.draw(screen):
            estado = 'game'
            if toca == 1:
                som_cutscene.stop()
                toca -= 1
            play_music()
            # print(health.atual)
        if exit_button.draw(screen):
            print('-- Fim do Programa --')
            pygame.quit()
            #exit()
            # rodando = False
        tecla1 = pygame.key.get_pressed()
        if tecla1[pygame.K_h]:
            estado = 'how_to_play'
        if tecla1[pygame.K_c]:
            indice_vid = 0
            estado = 'cutscene'
            cut_timer = (pygame.time.get_ticks() + 4000)
        if tecla1[pygame.K_KP_ENTER]:
            estado = 'game'
            if toca == 1:
                som_cutscene.stop()
                toca -= 1
            play_music()
    elif estado == 'how_to_play': # ===============================================
        if is_off_screen(fundo_group.sprites()[0]): # Testa se o primeiro fundo do grupo [0] está fora da tela
            fundo_group.remove(fundo_group.sprites()[0]) # Se SIM apaga aquele fundo

            new_fundo = Fundo((SCREENX * 4) - 10, bg_indice)      #cria um new fundo onde a xpos é (SCREENX * 4) --- '-10' pq sobrava um espacinho
            if bg_indice < 4:
                bg_indice += 1
            else:
                bg_indice = 0
            fundo_group.add(new_fundo)
            
            
        fundo_group.draw(screen)
        screen.blit(instrucao, (240,60)) # 800,600
        screen.blit(post_it, (240,60)) # 800,600
        w += 0.15
        a += 0.15
        s += 0.15
        d += 0.15
        e += 0.15
        ctrl += 0.15
        space += 0.15
        
        if w >= 2:
            w = 0
        if a >= 4:
            a = 2
        if s >= 6:
            s = 4
        if d >= 8:
            d = 6
        if e >= 10:
            e = 8
        if ctrl >= 12:
            ctrl = 10
        if space >= 14:
            space = 12
        screen.blit(teclas_animadas[int(w)], (560,150))
        screen.blit(teclas_animadas[int(a)], (660,150))
        screen.blit(teclas_animadas[int(s)], (760,150))
        screen.blit(teclas_animadas[int(d)], (860,150))
        screen.blit(teclas_animadas[int(e)], (810,355)) #(810,255)
        screen.blit(teclas_animadas[int(ctrl)], (810,480))
        screen.blit(teclas_animadas[int(space)], (810,255))
        
        fundo_group.update()
        
            
        tecla1 = pygame.key.get_pressed()
        if tecla1[pygame.K_SPACE]:
            estado = 'menu'
    elif estado == 'game': # =======================================================
        current_time = pygame.time.get_ticks()  # pega os segundos
        
        if is_off_screen(fundo_group.sprites()[0]): # Testa se o primeiro fundo do grupo [0] está fora da tela
            fundo_group.remove(fundo_group.sprites()[0]) # Se SIM apaga aquele fundo

            new_fundo = Fundo((SCREENX * 4) - 10, bg_indice)      #cria um new fundo onde a xpos é ((SCREENX * 4) --- '-10' pq sobrava um espacinho
            if bg_indice < 4:
                bg_indice += 1
            else:
                bg_indice = 0
            fundo_group.add(new_fundo)

        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_SPACE] and delorean.mini == False:
            vel_missil_x, triggered = atirou()
            
        if tecla[pygame.K_e]:
            if dina.rect.y != delorean.rect.y:
                pass
            else:
                vel_dinax, vel_dinay, lancou, dina.atual = lancar()
            # timer1 = pygame.time.get_ticks()                
        if current_time - timer2 > 1800:
            vel_missil_inimigo2, triggered_inimigo2, aparece = atirou2()
            timer2 = pygame.time.get_ticks()
        
        if current_time - timer1 > 15000:        # Spawnar corações
            timer1 = pygame.time.get_ticks()    
            powerup1 = get_random_y_powerup1(Tam_screenx + 70)      
            powerup1_group.add(powerup1)    #
            p1 = True
            
        if current_time - timer3 > 30000:        # Spawnar Mira
            timer3 = pygame.time.get_ticks() 
            powerup2 = get_random_y_powerup2(Tam_screenx + 70)      
            powerup2_group.add(powerup2)    #
            p2 = True
            
        if current_time - timer3 > 15000:   # Tempo do missil Teleguiado
            teleguiado = False
            
        if current_time - timer4 > 300 and explodiu == True:    # Dynamite
            dina.movimentacao()
            explodiu = False
            lancou = False
            dina.atual = 2
        
        reinicia = health.morreu()
        if reinicia == True:
            estado, health.atual, pontos, vel_alieny, vel_alien2y, vel_alienx, vel_heartx, vel_hearty, timer1, timer2, p1, p2, vel_missil_inimigo2, vel_missil_x, vel_missil_y, triggered, teleguiado, vel_col_x1, vel_dinax, vel_dinay, lancou = reiniciar()
            reinicia = False
        # estado = health.morreu()
        
        if tecla[pygame.K_m]: # Voltar para o Menu
            estado, health.atual, pontos, vel_alieny, vel_alien2y, vel_alienx, vel_heartx, vel_hearty, timer1, timer2, p1, p2, vel_missil_inimigo2, vel_missil_x, vel_missil_y, triggered, teleguiado, vel_col_x1, vel_dinax, vel_dinay, lancou = reiniciar()
            
        colidiu, vel_missil_inimigo2, triggered_inimigo2, p1, p2, vel_col_x1, teleguiado = colisions()

        fundo_group.draw(screen)
        missil_group.draw(screen)
        delorean_group.draw(screen)
        health_group.draw(screen)
        inimigo1_group.draw(screen)
        inimigo2_group.draw(screen)
        projetil_inimigo2_group.draw(screen)
        powerup1_group.draw(screen)
        powerup2_group.draw(screen)
        dina_group.draw(screen)
        
        
        
        
        fundo_group.update()
        missil_group.update()
        delorean_group.update()
        health_group.update()
        inimigo1_group.update()
        inimigo2_group.update()
        projetil_inimigo2_group.update()
        powerup1_group.update()
        powerup2_group.update()
        dina_group.update()
        
    
        score = font.render(f' Pontos: {int(pontos)}', True, (0,0,0))
        screen.blit(score, (50,50)) 
    pygame.display.update()