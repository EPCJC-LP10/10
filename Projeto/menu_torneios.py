# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:46:08 2013

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


def equipa():
    print
    print " *** Menu Torneios **** "
    print
    print "1. Inserir novo Torneio"
    print "2. Listar todos os Torneios"
    print "3. Pesquisar Torneio"
    print "4. Alterar dados de um Torneio"
    print "5. Eliminar Torneio"
    print 
    print "0. Menu Anterior"

    op = raw_input("Opção: ")
    return op



if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"

