from enum import StrEnum
from dataclasses import dataclass

class TokenType(StrEnum):
    # Any number present in R
    NUMBER="NUMBER"

    # Operators
    PLUS = "+"
    MINUS = "-"
    MUL = "*"
    DIV = "/"
    CARET = "^"

    # brackets
    LPAREN = "("
    RPAREN = ")"

    # End of File.
    EOF = "EOF"

@dataclass
class Token:
    type: TokenType
    start: int
    end: int

    def lexeme(self, source : str):
        return source[self.start:self.end]
