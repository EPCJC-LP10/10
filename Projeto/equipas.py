# -*- coding: utf-8 -*-

from collections import namedtuple

import menu


equipaReg = namedtuple("equipaReg", "cod, nome, jogos, vitorias, empates, derrotas, auto_golos_adversario, pontos")
listaEquipas = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listaEquipas)):
        if listaEquipas[i].id == codigo:
            pos = i
            break
                            
    return pos


def inserir_equipa():
    cod = input("Qual o codigo? ")

    pos = encontrar_posicao(cod)

    if pos >= 0:
        print "Código já existe"
        return

    #ler dados
    nome = raw_input("Qual o nome da equipa? ")
    
    registo = equipaReg(cod, nome, 0, 0, 0, 0, 0, 0)
    listaEquipas.append(registo)


def pesquisar_equipa():
    cod = input("Qual o codigo da equipa a pesquisar? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe equipa com esse código"
        return

    print "Código: ", listaEquipas[pos].id
    print "Nome: ", listaEquipas[pos].nome
    


def listar_equipas():
    for i in range (len(listaEquipas)):
        print "Código: ", listaEquipas[i].id
        print "Nome: ", listaEquipas[i].nome
        
  

def eliminar_equipa():
    cod = input ("Código da equipa a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe equipa com esse código"
        return

    # TODO: Confirmar eliminação
    listaEquipas.pop(pos)


    
def alterar_equipa():
    cod = input ("Código da equipa a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe equipa com esse código"
        return

    # só altera o nome
    novaequipa = raw_input("Qual o nome? ")
    listaEquipas[pos] = listaEquipas[pos]._replace(nome=novaequipa)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.equipas()

        if op == '1':
            inserir_equipa()
        elif op =='2':
            listar_equipas()
        elif op == '3':
            pesquisar_equipa()
        elif op == '4':
            alterar_equipa()
        elif op == '5':
            eliminar_equipa()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"










