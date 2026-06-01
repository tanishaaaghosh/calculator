from enum import Enum, auto
from dataclasses import dataclass


class TokenType(Enum):
    NUMBER=auto()  # Any number present in Z-

    DECIMAL= auto()

    PLUS = auto()  # +
    MINUS = auto()  # -
    MUL = auto()  # *
    DIV = auto()  # /
    CARET = auto()  # ^

    LPAREN = auto()
    RPAREN = auto()

    EOF = auto()

@dataclass
class Token:
    type: TokenType
    start: int
    end: int


class Lexer:

    def __init__(self, text: str):
        self.text = text
        self.pos = 0

    def current(self):

        if self.pos >= len(self.text):
            return None
        return self.text[self.pos]

    def next(self):
        self.pos += 1

    def peek(self):
        if self.current() is None or self.pos + 1 == len(self.text):
            return None
        return self.text[self.pos + 1]

    def number(self, sign="+"):
        start = self.pos
        isdecimal = False

        while self.current() is not None and (self.current().isdigit() or self.current() == "."):
            if self.current() == ".":
                isdecimal = True
            self.next()

        if isdecimal:
            return Token(TokenType.DECIMAL,start,self.pos)
        else:
            return Token(TokenType.NUMBER,start,self.pos)


    def tokenize(self):

        tokens = []

        while self.current() is not None:

            ch = self.current()
            start = self.pos

            if ch.isdigit():
                tokens.append(self.number())

            elif ch.isspace():
                self.next()

            elif ch == "+":
                tokens.append(Token(TokenType.PLUS, start, start))
                self.next()

            elif ch == "*":
                tokens.append(Token(TokenType.MUL, start, start))

                self.next()

            elif ch == "-":
                tokens.append(Token(TokenType.MINUS, start, start))
                self.next()

            elif ch == "/":
                tokens.append(Token(TokenType.DIV, start, start))

                self.next()

            # where does (
            elif ch == "(":
                tokens.append(Token(TokenType.LPAREN, start, start))

                self.next()

            elif ch == ")":
                tokens.append(Token(TokenType.RPAREN, start, start))

                self.next()

            elif ch == "^":
                tokens.append(Token(TokenType.CARET, start, start))

                self.next()

            else:

                raise SyntaxError(
                    f"Invalid Token Found at {self.pos, self.current()}"
                )

        tokens.append(Token(TokenType.EOF, self.pos, self.pos))

        return tokens



def main():
    lex = Lexer("1* -23 / 2.4")

    print(lex.tokenize())


if __name__ == "__main__":
    main()
