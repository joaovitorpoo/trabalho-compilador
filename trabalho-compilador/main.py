from tag import Tag
from token import Token
from analisador import Analisador
from sintatico import Sintatico

if __name__ == "__main__":

    analisador = Analisador('fonte.txt')
    sintatico = Sintatico(analisador)

    sintatico.prog()

    print("\n=>Tabela de simbolos:")
    analisador.printTS()
    analisador.closeFile()

    print('\n=> Fim da compilacao')
