from earley import EarleyAlgorithm
from models import Rule


def read_grammar():
    grammar = []
    n = int(input())
    for i in range(n):
        x = input().split()
        if len(x) == 1:
            x.append('')
        grammar.append(Rule(x[0], x[1]))
    return grammar


if __name__ == '__main__':
    g = read_grammar()
    w = input()
    print(EarleyAlgorithm.run(g, w))
