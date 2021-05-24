from tag import Tag
from token import Token
from analisador import Analisador

if __name__ == "__main__":

    analisador = Analisador('fonte.txt')

    print("\n=>Lista de tokens:")
    token = analisador.proxToken()

    while (token is not None):
        print(token.toString(), "Linha: " + str(token.getLinha()) + " Coluna: " + str(token.getColuna()))
        if (token.getNome() == Tag.EOF):
            break
        else:
            token = analisador.proxToken()



    print("\n=>Tabela de simbolos:")
    analisador.printTS()
    analisador.closeFile()

    print('\n=> Fim da compilacao')
