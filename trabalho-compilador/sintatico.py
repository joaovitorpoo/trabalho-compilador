import sys

from tag import Tag

class Sintatico:
    def __init__(self, analisador):
        self.lexer = analisador
        self.token = analisador.proxToken()

        if self.token is None:
            sys.exit(0)

    def sinalizaErroSintatico(self, message):
        print("[Erro Sintatico] na linha " + str(self.token.getLinha()) + " e coluna " + str(
            self.token.getColuna()) + ": ")
        print(message, "\n")
        sys.exit(0)

    def advance(self):
        print("[DEBUG] Token: ", self.token.toString(), "Linha: " + str(self.token.getLinha()) + " Coluna: " + str(self.token.getColuna()))
        self.token = self.lexer.proxToken()
        if self.token is None:  # erro no Lexer
            sys.exit(0)

    def skip(self, message):
        self.sinalizaErroSintatico(message)
        self.advance()

    # verifica token esperado t
    def eat(self, t):
        if (self.token.getNome() == t):
            self.advance()
            return True
        else:
            return False

    def prog(self):
        if (not self.eat(Tag.KW_PROGRAM)):
            self.sinalizaErroSintatico("Esperado \"program\", encontrado " + "\"" + self.token.getLexema() + "\"")

        if (not self.eat(Tag.ID)):
            self.sinalizaErroSintatico("Esperado \"ID\", encontrado " + "\"" + self.token.getLexema() + "\"")

        self.body()

    def body(self):
        self.declList()

        if (not self.eat(Tag.SMB_OBC)):
            self.sinalizaErroSintatico("Esperado \"{\", encontrado " + "\"" + self.token.getLexema() + "\"")

        self.stmtList()

        if (not self.eat(Tag.SMB_CBC)):
            self.sinalizaErroSintatico("Esperado \"}\", encontrado " + "\"" + self.token.getLexema() + "\"")

    def declList(self):
        if (self.token.getNome() != Tag.SMB_OBC):
            self.decl()

            if (not self.eat(Tag.SMB_SEM)):
                self.sinalizaErroSintatico("Esperado \";\", encontrado " + "\"" + self.token.getLexema() + "\"")

            self.declList()

            return True
        else:
            return False

    def stmtList(self):
        if (1 == 0):
            print("bbbbbbbb")

    def decl(self):
        self.type()
        self.idList()

    def type(self):
        if(self.token.getLexema() == 'num'):
            self.eat(Tag.KW_NUM)
        elif (self.token.getLexema() == 'char'):
            self.eat(Tag.KW_CHAR)
        else:
            self.sinalizaErroSintatico("Esperado \"num, char\", encontrado " + "\"" + self.token.getLexema() + "\"")

    def idList(self):
        if (not self.eat(Tag.ID)):
            self.sinalizaErroSintatico("Esperado \"ID\", encontrado " + "\"" + self.token.getLexema() + "\"")

        self.idListLinha()

    def idListLinha(self):
        if (self.token.getNome() != Tag.SMB_SEM):
            if (not self.eat(Tag.SMB_COM)):
                self.sinalizaErroSintatico("Esperado \", | ;\", encontrado " + "\"" + self.token.getLexema() + "\"")
            self.idList()
            return True
        else:
            return False