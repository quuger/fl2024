import sys
from antlr4 import *
from first.GrammarLexer import GrammarLexer
from first.GrammarParser import GrammarParser
from first.GrammarVisitor import GrammarVisitor


class Instruction:
    def __init__(self, command, args=None):
        self.command = command
        self.args = args


class CalcVisitor(GrammarVisitor):
    line = 0
    def visitStart(self, ctx):
        result =  self.visit(ctx.expr())
        self.line += 1
        return result + [Instruction("match")]

    def visitOrExpr(self, ctx):
        first_begin = self.line + 1
        self.line += 1
        first = self.visit(ctx.left)

        second_begin = self.line + 1
        self.line += 1
        second = self.visit(ctx.right)

        result = [Instruction("split", (first_begin, second_begin))]
        result.extend(first)
        result.append(Instruction("jmp", second_begin + len(second) + 1))
        result.extend(second)

        return result

    def visitConcExpr(self, ctx):
        first = self.visit(ctx.getChild(0))
        second = self.visit(ctx.getChild(1))
        return first + second

    def visitQuesExpr(self, ctx):
        old_line = self.line + 1
        self.line += 1
        first = self.visit(ctx.getChild(0))

        result = [Instruction("split", (old_line, old_line + len(first)))]
        result.extend(first)

        return result

    def visitStarExpr(self, ctx):
        old_line = self.line
        self.line += 1
        fisrt = self.visit(ctx.getChild(0))
        result = [Instruction("split", (old_line + 1, self.line + 1))]
        result.extend(fisrt)
        result.append(Instruction("jmp", old_line))
        self.line += 1
        return result

    def visitPlusExpr(self, ctx):
        old_line = self.line
        result = self.visit(ctx.getChild(0))
        result.append(Instruction("split", (old_line, self.line + 1)))
        self.line += 1
        return result

    def visitAtomExpr(self, ctx):
        return self.visit(ctx.atom())

    def visitCharExpr(self, ctx):
        self.line += 1
        return [Instruction("char", ctx.getText())]

    def visitParExpr(self, ctx):
        return self.visit(ctx.expr())


def calc() -> float:
    stream = InputStream(regular)

    lexer = GrammarLexer(stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.start()

    visitor = CalcVisitor()
    return visitor.visit(tree)


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

def print_instructions(result):
    line = 0
    for instruction in result:
        if instruction.command == "split":
            print(line, "split", instruction.args[0], instruction.args[1])
        else:
            print(line, instruction.command,
                  instruction.args if instruction.args is not None else "")
        line += 1


if __name__ == '__main__':
    regular = input()
    result = calc()
    
    print_instructions(result)
    print(check(result, 0, input()))
