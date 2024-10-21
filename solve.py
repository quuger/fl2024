import sys
from antlr4 import *
from dist.CalculantlrLexer import CalculantlrLexer
from dist.CalculantlrParser import CalculantlrParser
from dist.CalculantlrVisitor import CalculantlrVisitor


class CalcVisitor(CalculantlrVisitor):
    def visitAtomExpr(self, ctx:CalculantlrParser.AtomExprContext):
        return int(ctx.getText())

    def visitParenExpr(self, ctx:CalculantlrParser.ParenExprContext):
        return self.visit(ctx.expr())

    def visitOpExpr(self, ctx:CalculantlrParser.OpExprContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        op = ctx.op.text
        if op == '+':
            return l + r
        elif op == '-':
            return l - r
        elif op == '*':
            return l * r
        elif op == '/':
            if r == 0:
                print('divide by zero!')
                return 0
            return l / r



def calc(line) -> float:
    input_stream = InputStream(line)

    # lexing
    lexer = CalculantlrLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # parsing
    parser = CalculantlrParser(stream)
    tree = parser.expr()

    # use customized visitor to traverse AST
    visitor = CalcVisitor()
    return visitor.visit(tree)



if __name__ == '__main__':
    while True:
        print(">>> ", end='')
        line = input()
        print(calc(line))

class Instruction:
    def __init__(self, command, args=None):
        self.command = command
        self.args = args


def print_instructions(result):
    line = 0
    for instruction in result:
        if instruction.command == "split":
            print(line, "split", instruction.args[0], instruction.args[1])
        else:
            print(line, instruction.command,
                  instruction.args if instruction.args is not None else "")
        line += 1


def parse_simple(string, line):  # string without '|'
    result = []
    i = 0
    while i < len(string):
        if (i < len(string) - 1) and (string[i + 1] in {'?', '*', '+'}):
            if string[i + 1] == '?':
                result.append(Instruction("split", (line + 1, line + 2)))
                result.append(Instruction("char", string[i]))
                line += 2
            if string[i + 1] == '*':
                result.append(Instruction("split", (line + 1, line + 3)))
                result.append(Instruction("char", string[i]))
                result.append(Instruction("jmp", line))
                line += 3
            if string[i + 1] == '+':
                result.append(Instruction("char", string[i]))
                result.append(Instruction("split", (line, line + 2)))
                line += 2
            i += 2
            continue
        result.append(Instruction("char", string[i]))
        line += 1
        i += 1
    return result


def parse(string, line=0):
    if "|" not in string:
        return parse_simple(string, line)

    result = []
    delimiter = string.find('|')

    first_begin = line + 1
    first = parse(string[:delimiter], first_begin)

    second_begin = first_begin + len(first) + 1
    second = parse(string[delimiter + 1:], second_begin)

    result.append(Instruction("split", (first_begin, second_begin)))
    result.extend(first)
    result.append(Instruction("jmp", second_begin + len(second)))
    result.extend(second)
    return result


def check(instructions, line, word, index=0):
    command = instructions[line].command
    args = instructions[line].args

    if command == "char":
        return (index < len(word) and word[index] == args and
                check(instructions, line + 1, word, index + 1))
    if command == "match":
        return index == len(word)
    if command == "jmp":
        return check(instructions, args, word, index)
    if command == "split":
        return (check(instructions, args[0], word, index) or
                check(instructions, args[1], word, index))


def solve():
    instructions = parse(input())
    instructions.append(Instruction("match"))

    # print_instructions(instructions)

    return check(instructions, 0, input())


print(solve())
