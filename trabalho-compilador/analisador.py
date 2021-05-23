import sys
from ts import TS
from tag import Tag
from token import Token

class Analisador():
    def __init__(self, input_file):
        try:
            self.input_file = open(input_file, 'rb')
            self.lookahead = 0
            self.n_linha = 1
            self.n_coluna = 0
            self.ts = TS()
        except IOError:
            print('Erro de abertura do arquivo. Encerrando.')
            sys.exit(0)

    def closeFile(self):
        try:
            self.input_file.close()
        except IOError:
            print('Erro ao fechar arquivo. Encerrando.')
            sys.exit(0)

    def sinalizaErroLexico(self, message):
        print("[Erro Lexico]: ", message, "\n");

    def retornaPonteiro(self):
        if (self.lookahead.decode('ascii') != ''):
            self.input_file.seek(self.input_file.tell() - 1)

    def printTS(self):
        self.ts.printTS()

    def proxToken(self):
        # Implementa um AFD.

        estado = 1
        lexema = ""
        c = '\u0000'

        while (True):
            self.lookahead = self.input_file.read(1)
            c = self.lookahead.decode('ascii')

            if (estado == 1):
                if (c == ''):
                    return Token(Tag.EOF, "EOF", self.n_linha, self.n_coluna)
                elif (c == ' ' or c == " "):
                    self.n_coluna = self.n_coluna + 1
                    estado = 1
                elif (c == '\t'):
                    self.n_coluna = self.n_coluna + 3
                    estado = 1
                elif (c == '\n'):
                    self.n_coluna = 0
                    self.n_linha = self.n_linha + 1
                    estado = 1
                elif (c == '/'):
                    estado = 2
                elif (c == '>'):
                    estado = 6
                elif (c == '<'):
                    estado = 7
                elif (c == '='):
                    estado = 8
                elif (c == '!'):
                    estado = 9
                elif (c == '+'):
                    self.n_coluna = self.n_coluna + 1
                    return Token(Tag.OP_AD, '+', self.n_linha, self.n_coluna)
                elif (c == '*'):
                    self.n_coluna = self.n_coluna + 1
                    return Token(Tag.OP_MUL, '*', self.n_linha, self.n_coluna)
                elif (c == '-'):
                    self.n_coluna = self.n_coluna + 1
                    return Token(Tag.OP_MIN, '-', self.n_linha, self.n_coluna)
                else:
                    self.sinalizaErroLexico("Caractere invalido [" + c + "] na linha " +
                                            str(self.n_linha) + " e coluna " + str(self.n_coluna))
                    return None
            elif (estado == 2):
                if (c == '*'):
                    estado = 3
                elif (c == '/'):
                    estado = 5
                else:
                    estado = 1
                    self.n_coluna = self.n_coluna + 1
                    self.retornaPonteiro()
                    return Token(Tag.OP_DIV, '/', self.n_linha, self.n_coluna)

            elif (estado == 3):
                if (c == '*'):
                    estado = 4
                if (c == '\n'):
                    self.n_linha = self.n_linha + 1

            elif (estado == 4):
                if (c == '/'):
                    estado = 1
                else:
                    estado = 3

            elif (estado == 5):
                if (c == '\n'):
                    self.n_coluna = 0
                    self.n_linha = self.n_linha + 1
                    estado = 1
            elif (estado == 6):
                if (c == '='):
                    self.n_coluna = self.n_coluna + 1
                    return Token(Tag.OP_GE, '>=', self.n_linha, self.n_coluna)
                self.retornaPonteiro()
                self.n_coluna = self.n_coluna + 1
                return Token(Tag.OP_GT, '>', self.n_linha, self.n_coluna)
            elif (estado == 7):
                if (c == '='):
                    self.n_coluna = self.n_coluna + 1
                    return Token(Tag.OP_LE, '<=', self.n_linha, self.n_coluna)
                self.retornaPonteiro()
                self.n_coluna = self.n_coluna + 1
                return Token(Tag.OP_LT, '<', self.n_linha, self.n_coluna)
            elif (estado == 8):
                if (c == '='):
                    self.n_coluna = self.n_coluna + 1
                    return Token(Tag.OP_EQ, '==', self.n_linha, self.n_coluna)
                self.retornaPonteiro()
                self.n_coluna = self.n_coluna + 1
                return Token(Tag.OP_ATRIB, '=', self.n_linha, self.n_coluna)
            elif (estado == 9):
                if (c == '='):
                    self.n_coluna = self.n_coluna + 1
                    return Token(Tag.OP_EQ, '!=', self.n_linha, self.n_coluna)
                self.sinalizaErroLexico("Caractere invalido [" + c + "] na linha " +
                                        str(self.n_linha) + " e coluna " + str(self.n_coluna))
                return None