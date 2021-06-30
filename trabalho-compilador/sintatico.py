import sys

from tag import Tag

class Sintatico:
    def __init__(self, analisador):
        self.lexer = analisador
        self.token = analisador.proxToken()  # Leitura inicial obrigatoria do primeiro simbolo

        if self.token is None:  # erro no Lexer
            sys.exit(0)

    def sinalizaErroSemantico(self, message):
        print("[Erro Semantico] na linha " + str(self.token.getLinha()) + " e coluna " + str(
            self.token.getColuna()) + ": ")
        print(message, "\n")

    def sinalizaErroSintatico(self, message):
        print("[Erro Sintatico] na linha " + str(self.token.getLinha()) + " e coluna " + str(
            self.token.getColuna()) + ": ")
        print(message, "\n")

    def advance(self):
        print("[DEBUG] token: ", self.token.toString())
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

        

