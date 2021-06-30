from enum import Enum


class Tag(Enum):

    # Fim de arquivo
    EOF = -1

    # Palavras-chave
    KW_PROGRAM = 1
    KW_IF = 2
    KW_ELSE = 3
    KW_WHILE = 4
    KW_WRITE = 5
    KW_READ = 6
    KW_NUM = 7
    KW_CHAR = 8
    KW_NOT = 9
    KW_OR = 10
    KW_AND = 11

    # Operadores
    OP_EQ = 12
    OP_NE = 13
    OP_GT = 14
    OP_LT = 15
    OP_GE = 16
    OP_LE = 17
    OP_AD = 18
    OP_MIN = 19
    OP_MUL = 20
    OP_DIV = 21
    OP_ATRIB = 22

    # Simbolos
    SMB_OBC = 23
    SMB_CBC = 24
    SMB_OPA = 25
    SMB_CPA = 26
    SMB_COM = 27
    SMB_SEM = 28

    # Identificador
    ID = 29

    # Constantes
    NUM_CONST = 30
    CHAR_CONST = 31