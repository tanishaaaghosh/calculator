### Problem Statement 

Mathematical expression evaluation is a fundamental component of programming languages,
compilers, interpreters, and scientific computing applications. While modern programming environments 
provide built-in mechanisms for evaluating expressions, understanding the underlying process requires
knowledge of data structures, parsing techniques, and expression evaluation algorithms. The objective of 
this project is to design and develop a scientific expression calculator in Python capable of evaluating 
user-defined arithmetic expressions without the use of built-in evaluation functions such as eval(). 
The system shall accept expressions in conventional infix notation, process them through
lexical analysis (tokenization), convert them into postfix notation using a
stack-based parsing algorithm, and evaluate the resulting postfix expression
to produce the final result. The calculator must correctly handle operator precedence,
associativity, and nested parentheses while providing meaningful error handling for 
invalid inputs. The project aims to expose students to the foundational concepts of
expression parsing and computational language processing through the implementation
of a practical and extensible software system.


### Scope of work 

The proposed calculator shall:

Accept arithmetic expressions from the user in infix notation.
Support fundamental arithmetic operators such as addition (+), subtraction (-), multiplication (*), division (/), and exponentiation (^).
Correctly process nested parentheses and operator precedence.
Generate postfix (Reverse Polish Notation) representations of expressions.
Evaluate postfix expressions and display the computed result.
Detect and report syntactic and computational errors, including malformed expressions and division by zero.
Provide a modular architecture that allows future enhancements such as support for mathematical functions, variables, and user-defined operations.
