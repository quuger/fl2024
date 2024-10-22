import sys
from antlr4 import *
from dist.GrammarLexer import GrammarLexer
from dist.GrammarParser import GrammarParser
from dist.GrammarVisitor import GrammarVisitor


class Instruction:
    def __init__(self, command, args=None):
        self.command = command
        self.args = args


class CalcVisitor(GrammarVisitor):
    line = 0

    def visitRegex(self, ctx):
        result = self.visit(ctx.unionExp())
        self.line += 1
        return result + [Instruction("match")]

    def helper(self, ctx, child_id):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        if child_id == ctx.getChildCount() - 1:
            return self.visit(ctx.getChild(child_id))

        current_begin = self.line + 1
        self.line += 1
        current = self.visit(ctx.getChild(child_id))

        next_begin = current_begin + len(current) + 1
        self.line += 1
        next = self.helper(ctx, child_id + 2)

        result = [Instruction("split", (current_begin, next_begin))]
        result.extend(current)
        result.append(Instruction("jmp", next_begin + len(next)))
        result.extend(next)

        return result

    def visitOrExpr(self, ctx):
        return self.helper(ctx, 0)

    def visitConcatExpr(self, ctx):
        result = []
        for child_id in range(ctx.getChildCount()):
            result += self.visit(ctx.getChild(child_id))
        return result

    def visitRepeatExpr(self, ctx):
        if ctx.op is None:
            return self.visitAtomExpr(ctx)
        op = ctx.op.text
        if op == '+':
            return self.visitPlusExpr(ctx)
        if op == '*':
            return self.visitStarExpr(ctx)
        if op == '?':
            return self.visitQuesExpr(ctx)
        return self.visitErrorNode(ctx)

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
    tree = parser.regex()

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
    instructions = calc()

    # print_instructions(instructions)

    print(check(instructions, 0, input()))


# 0 split 1 5
# 1 split 2 4
# 2 char a
# 3 jmp 1
# 4 jmp 7
# 5 char b
# 6 split 5 7
# 7 match