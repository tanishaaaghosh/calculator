from Lexer import Lexer
def main():
    print(*Lexer("1-23 / 2.").tokenize(), sep="\n")


if __name__ == "__main__":
    main()
