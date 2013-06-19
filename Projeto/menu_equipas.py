# -*- coding: utf-8 -*-

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
    print " *** Menu Equipas **** "
    print
    print "1. Inserir nova equipa"
    print "2. Listar todas as equipas"
    print "3. Pesquisar equipa"
    print "4. Alterar dados de uma equipa"
    print "5. Eliminar equipa"
    print 
    print "0. Menu Anterior"

    op = raw_input("Opção: ")
    return op



if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"

