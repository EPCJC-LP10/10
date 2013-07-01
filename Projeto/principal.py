# -*- coding: utf-8 -*-

import menu
import jogadores
import equipas
import util


# nome dos ficheiros
fxequipas = "equipas.dat"
fxjogadores = "jogadores.dat"
fxtorneios = "torneios.dat"

def ler_ficheiros():
    # adicionar todos ficheiros a ler
    jogadores.listaJogadores = util.ler_ficheiro(fxjogadores)
    equipas.listaEquipas = util.ler_ficheiro(fxequipas)
    

def escrever_ficheiros():
	# adicionar todos ficheiros a guardar
     util.escrever_ficheiro(fxjogadores, jogadores.listaJogadores)
     util.escrever_ficheiro(fxequipas, equipas.listaEquipas)


# Bloco Principal

ler_ficheiros()

terminar = False
while not terminar:
    op = menu.principal()
    
    if op == '1':
        jogadores.gerir()
    elif op == '2':
        pass    #por fazer
    elif op == '0':
        terminar = True


escrever_ficheiros()


