# Questão 2, importações
import pygame
from pygame.locals import *
import mecanica
import visual


#  Questão 3, inicializações
janela = visual.inicializar_jogo()

música = visual.inicializar_musica()

carro = visual.inicializar_carro('jogador')
carro2 = visual.inicializar_carro('oponente')

carro_loc = carro_loc = visual.posicionar_carro(carro, visual.FAIXA_DIREITA, 0.8 * visual.JANELA_ALTURA)
carro2_loc = visual.posicionar_carro(carro2, visual.FAIXA_ESQUERDA, 0.2 * visual.JANELA_ALTURA)

contador = 0
velocidade = 1

esta_executando = True

# loop de jogo
while esta_executando:

  # Questão 5, item 2
    carro2_loc = mecanica.mover_adversario_aleatoriamente(carro2_loc, velocidade, visual.JANELA_ALTURA, mecanica.VEICULO_ALTURA, mecanica.FAIXA_ESQUERDA, mecanica.FAIXA_DIREITA)

    # esse trecho verifica se houve eventos de entrada (mouse, teclado)
    for event in pygame.event.get():
        if event.type == QUIT:
            esta_executando = False

        # Questão 6
        if event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                mecanica.alternar_faixa(carro_loc, visual.FAIXA_ESQUERDA)
            elif event.key == K_d or event.key == K_RIGHT:
                mecanica.alternar_faixa(carro_loc, visual.FAIXA_DIREITA)

    # redesenha elementos na janela
    visual.desenhar_estrada(janela)
    # Questão 4
    visual.desenhar_carros(janela, [[carro, carro_loc], [carro2, carro2_loc]])
    visual.atualizar_tela()


    # Questão 7, item 2
    bateu = mecanica.houve_colisao(carro_loc, carro2_loc)
    if bateu == True:
        print("GAME OVER!")
        break

        # Questão 8, itens 2 e 3

    if contador == 5000:
        velocidade = mecanica.subir_nivel(velocidade)
        print(f"Subiu de nível - Velocidade: {velocidade}")
        contador = 0
    contador += 1


# Questão 9
visual.encerrar_jogo()


