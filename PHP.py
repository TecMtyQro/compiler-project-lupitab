# -----------------------------------------------------------------------------
# PHP.py
#
# V.1.0.0
# PHP Interpreter
# -----------------------------------------------------------------------------

import sys
#import files
sys.path.insert(0, "../..")

if sys.version_info[0] >= 3:
    raw_input = input



reserved = {
   'if' : 'IF',
   'else' : 'ELSE',
   'for' : 'FOR',
   'define' : 'DEFINE',
   'echo' : 'ECHO',
   'array' : 'ARRAY',
   'or' : 'OR',
   'and' : 'AND',
   'not' : 'NOT',
   'xor' : 'XOR',
   '$_POST' : 'POST'
}
tokens = ['EQ', 'EQA',
          'RUNPHP','ENDPHP',
          'LT', 'LE', 'GT', 'GE', 'EQEQ', 'IDENTICAL', 'DIFERENT', 'NE',
          'PLUS', 'MINUS', 'MULT', 'DIVIDE','EXPO',
          'QUOTESS','QUOTESD',
          'OPARENT', 'CPARENT', 'OKEY', 'CKEY','OSBRACKET', 'CSBRACKET', 'COMA','SEMICOLON',
          'INT', 'FLOAT','BOOL','STRING','CHAR',
          'NAME',
          'ID',
          'WORDSR',
          'COMMENT','COMMENTML', 'COMMENTC'] +  list (reserved.values())


#literals = ['=', '+', '-', '*', '/',':','{','}' ]
#literals = ['/*']
#  () {} ;
#Operadores Aritmeticos --> + - * /  ++  -- %  **
# **  -> exponente
#  =   =>
#Asignacion en arrays -> => EQA
#operadores de comparacion --> == === != <> <  >  <= >=
#Operadres Logicos  --> and &&    or ||      not !     xor

# Tokens
#'EQ', 'EQA',
#          'AND', 'OR', 'NOT', 'XOR',

#          'LT', 'LE', 'GT', 'GE', 'EQEQ', 'IDENTICAL', 'DIFERENT', 'NE',
#          'PLUS', 'MINUS', 'MULT', 'DIVIDE',
#          'OPARENT', 'CPARENT', 'OKEY', 'CKEY', 'SEMICOLON'
t_RUNPHP = r'\<(\?)php'
t_ENDPHP =  r'\?>'
t_EQ = r'\='
t_EQA = r'\=>'
t_AND = r'\&&'
t_OR = '\|\|'
t_NOT = r'\!'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULT = r'\*'
t_EXPO = r'\*\*'
t_DIVIDE = r'\/'
t_STRING = r'\'(.|\n|\t)*\''
#def t_OR(t):
#    r'\|+'
#    if t.value == "||" :
#        return t
#    else :
#        print("Illegal character '%s'" % t.value[0])
#        t.lexer.skip(1)

#t_NOT = r'\!'

t_EQEQ = r'\=='
t_IDENTICAL = r'\==='
t_LT = r'\<'
t_LE = r'\<='
t_GT = r'\>'
t_GE = r'\>='
t_DIFERENT = r'\<>'
t_QUOTESS = r'\''
t_QUOTESD = r'\"'
t_OPARENT = r'\('
t_CPARENT = r'\)'
t_OKEY = r'\{'
t_CKEY = r'\}'
t_OSBRACKET = r'\['
t_CSBRACKET = r'\]'
t_SEMICOLON = r'\;'
t_COMA = r'\,'
#t_ID  = r'\$[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*'

def  t_ID(t):
     r'\$[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*'
     if t.value in reserved:
        t.type = reserved[ t.value ]

     return t

def t_COMMENT(t):
    r'\//.*'
    #pass
    return t
def t_COMMENTC(t):
    r'\#.*'
    #pass
    return t

def t_COMMENTML(t):
#    r'\open.*close'
    #pass
    r'\/\*(.|\n|\t)*'
    return t


def t_FLOAT(t):
    r'-?\+?\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'-?\+?\d+'
    t.value = int(t.value)
    return t

def t_BOOL(t):
    r'TRUE|FALSE'
    t.value = bool(t.value)
    return t

#def t_STRING(t):
    #r'\".*"'
    #t.value = str(t.value)
    #return t

def  t_WORDSR(t):
     r'[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*'
     if t.value in reserved:
        t.type = reserved[ t.value ]
        return t




t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
     #raise LexerError("Illegal character '%s'" % t.value)
     print ("Test Error : carácter ilegal '% s'"% t.value [0])
     t.lexer.skip(1)

# Build the lexer
class Lexer:
    def __init__(self, script):
       self.script = script;
       #print("Iniciar Lexical Analyser")

    def runLexA(self):
        import ply.lex as lex
        lex.lex()
        #f = open ('imput&output_Case.txt','r')
        #mensaje = f.read()
        #print(self.script)
        lex.input(self.script)
        #f.close()

        while True:
            tok = lex.token()
            if not tok:
                break
            print(tok)
