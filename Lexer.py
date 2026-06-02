from Cursor import Cursor
from Token import Token, TokenType

class Lexer(Cursor):

    OPERATORS = {
        "+": TokenType.PLUS,
        "-": TokenType.MINUS,
        "*": TokenType.MUL,
        "/": TokenType.DIV,
        "^": TokenType.CARET,
        "(": TokenType.LPAREN,
        ")": TokenType.RPAREN,
    }

    def __init__(self, text: str):
        super().__init__(text)

    def number(self):
        start = self.pos
        seen_decimal = False

        while self.current() is not None and (self.current().isdigit() or self.current() == "."):

            if self.current() == ".":
                if seen_decimal:
                    raise SyntaxError(
                        f"Invalid number at position {self.pos}"
                    )
                seen_decimal = True

            self.next()

        return Token(TokenType.NUMBER,start,self.pos)


    def tokenize(self):
        while self.current() is not None:

            ch = self.current()
            start = self.pos

            if ch.isdigit() or ch == ".":
                yield self.number()

            elif ch.isspace():
                self.next()

            elif ch in self.OPERATORS:
                yield Token(self.OPERATORS[ch], start, self.pos +1)

                self.next()

            else:
                raise SyntaxError(
                    f"Invalid Token Found at {self.pos, self.current()}"
                )

        yield Token(TokenType.EOF, self.pos, self.pos)