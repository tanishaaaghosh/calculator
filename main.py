from enum import Enum, auto
from dataclasses import dataclass


class TokenType(Enum):
    NUMBER = auto() # Any number present in R

    PLUS = auto() # + 
    MINUS = auto() # -
    MUL = auto() # * 
    DIV = auto() # / 
    CARET = auto() # ^ 

    LPAREN = auto()
    RPAREN = auto()

    EOF = auto()

@dataclass
class Token:
    type: TokenType
    value: str | None = None #+,-,123, *, ^



class Lexer: 

    def __init__(self, text:str ): 
        self.text = text 
        self.pos =0


    def current(self): 

        if self.pos >= len(self.text): 
            return None 
        return self.text[self.pos] 

    def next(self): 
        self.pos +=1 




def main(): 
    lex = Lexer("1*2/3") 

    while lex.current() is not None: 
        print(lex.current()) 
        lex.next() 
        
if __name__ == "__main__" : 
    main()
