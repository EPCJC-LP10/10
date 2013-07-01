# -*- coding: utf-8 -*-
"""
Created on Mon Jul 01 11:41:36 2013

@author: i12106
"""

from collections import namedtuple

import menu


torneioReg = namedtuple("torneioReg", "cod, nome, equipas, classificacao, resultados, melhor_marcador, melhor_gr, cartoes")
listaTorneios = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listaTorneios)):
        if listaTorneios[i].id == codigo:
            pos = i
            break
                            
    return pos


def inserir_torneio():
    cod = input("Qual o codigo? ")

    pos = encontrar_posicao(cod)

    if pos >= 0:
        print "Código já existe"
        return

    #ler dados
    nome = raw_input("Qual o nome do torneio? ")
    
    registo = torneioReg(cod, nome, equipas, 0, 0, 0, 0, 0)
    listaTorneios.append(registo)


def pesquisar_torneio():
    cod = input("Qual o codigo do torneio a pesquisar? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe equipa com esse torneio"
        return

    print "Código: ", listaTorneios[pos].id
    print "Nome: ", listaTorneios[pos].nome
    print "Equipa:", listaTorneios[pos].equipas


def listar_torneios():
    for i in range (len(listaTorneios)):
        print "Código: ", listaTorneios[i].id
        print "Nome: ", listaTorneios[i].nome
        
  

def eliminar_torneio():
    cod = input ("Código do torneio a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe equipa com esse código"
        return

    # TODO: Confirmar eliminação
    listaTorneios.pop(pos)


    
def alterar_torneio():
    cod = input ("Código do torneio a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe equipa com esse código"
        return

    # só altera o nome
    novaequipa = raw_input("Qual o nome? ")
    listaTorneios[pos] = listaTorneios[pos]._replace(nome=novaequipa)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.torneios()

        if op == '1':
            inserir_torneio()
        elif op =='2':
            listar_torneios()
        elif op == '3':
            pesquisar_torneio()
        elif op == '4':
            alterar_torneio()
        elif op == '5':
            eliminar_torneio()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"