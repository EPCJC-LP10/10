# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:33:25 2013

@author: i12106
"""

def principal():
    print
    print " **** MENU ****** "
    print
    print "   1. Gestão de Torneios"
    print "   2. Gestão de Equipas"
    print "   3. Gestão de Jogadores"
    print 
    print "   0. Sair"
    print 

    op = raw_input("Opção: ")
    return op


def jogador():
    print
    print " *** Menu Jogadores **** "
    print
    print "1. Inserir novo Jogador"
    print "2. Listar todos os jogadores"
    print "3. Pesquisar jogador"
    print "4. Alterar dados de um jogador"
    print "5. Eliminar jogador"
    print 
    print "0. Menu Anterior"

    op = raw_input("Opção: ")
    return op



if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"

