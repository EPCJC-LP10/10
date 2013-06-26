# -*- coding: utf-8 -*-

from collections import namedtuple

import menu


jogadorReg = namedtuple("jogadorReg", "cod, cod_equipa, nome, golosm, goloss, cartõesa, cartõesv")
listaJogadores = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listaJogadores)):
        if listaJogadores[i].id == codigo:
            pos = i
            break
                            
    return pos


def inserir_jogador():
    cod = input("Qual o codigo do jogador? ")

    pos = encontrar_posicao(cod)

    if pos >= 0:
        print "Código já existe"
        return

    #ler dados
    nome = raw_input("Qual o nome? ")
    codequipa = input("Qual o codigo do jogador? ")
    
    registo = jogadorReg(cod, codequipa, nome, 0, 0, 0, 0)
    listaJogadores.append(registo)


def pesquisar_jogador():
    cod = input("Qual o codigo do jogador a pesquisar? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe jogador com esse código"
        return

    print "Código: ", listaJogadores[pos].id
    print "Nome: ", listaJogadores[pos].nome
    


def listar_jogadores():
    for i in range (len(listaJogadores)):
        print "Código: ", listaJogadores[i].id
        print "Nome: ", listaJogadores[i].nome
        
  

def eliminar_jogador():
    cod = input ("Código do jogador a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe jogador com esse código"
        return

    # TODO: Confirmar eliminação
    listaJogadores.pop(pos)


    
def alterar_jogador():
    cod = input ("Código do jogador a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe jogador com esse código"
        return

    # só altera o nome
    novojogador = raw_input("Qual o nome? ")
    listaJogadores[pos] = listaJogadores[pos]._replace(nome=novojogador)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.jogadores()

        if op == '1':
            inserir_jogador()
        elif op =='2':
            listar_jogadores()
        elif op == '3':
            pesquisar_jogador()
        elif op == '4':
            alterar_jogador()
        elif op == '5':
            eliminar_jogador()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"










