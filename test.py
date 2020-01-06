from earley import EarleyAlgorithm
from models import Rule


class Test:

    def test_1(self):
        rules = [
            Rule('X', 'C'),
            Rule('D', 'aDb'),
            Rule('X', 'XC'),
            Rule('C', 'cD'),
            Rule('D', '')
        ]
        w = 'ccaabbccccccccaaaabbbb'
        assert EarleyAlgorithm.run(rules, w)

    def test_2(self):
        rules = [
            Rule('X', 'C'),
            Rule('D', 'aDb'),
            Rule('X', 'XC'),
            Rule('C', 'cD'),
            Rule('D', '')
        ]
        w = 'ccaacbbccccccccaaaabbbb'
        assert not EarleyAlgorithm.run(rules, w)

    def test_3(self):
        rules = [
            Rule('X', 'Xa'),
            Rule('X', 'XXb'),
            Rule('X', 'C'),
            Rule('C', 'Dd'),
            Rule('D', 'cD'),
            Rule('D', '')
        ]
        w = 'ccccdcdbaa'
        assert EarleyAlgorithm.run(rules, w)

    def test_4(self):
        rules = [
            Rule('X', 'Xa'),
            Rule('X', 'XXb'),
            Rule('X', 'C'),
            Rule('C', 'Dd'),
            Rule('D', 'cD'),
            Rule('D', '')
        ]
        w = 'ccccdcdddbaa'
        assert not EarleyAlgorithm.run(rules, w)

    def test_5(self):
        rules = [
            Rule('X', ''),
            Rule('X', 'a'),
            Rule('X', 'b'),
            Rule('X', 'c'),
            Rule('X', 'aXa'),
            Rule('X', 'bXb'),
            Rule('X', 'cXc')
        ]
        w = 'cabcaacbac'
        assert EarleyAlgorithm.run(rules, w)

    def test_6(self):
        rules = [
            Rule('X', ''),
            Rule('X', 'a'),
            Rule('X', 'b'),
            Rule('X', 'c'),
            Rule('X', 'aXa'),
            Rule('X', 'bXb'),
            Rule('X', 'cXc')
        ]
        w = 'cabccacbac'
        assert not EarleyAlgorithm.run(rules, w)

    def test_7(self):
        rules = [
            Rule('X', ''),
            Rule('X', 'XX'),
            Rule('X', '(X)')
        ]
        w = '(())()()((()))'
        assert EarleyAlgorithm.run(rules, w)

    def test_8(self):
        rules = [
            Rule('X', ''),
            Rule('X', 'XX'),
            Rule('X', '(X)')
        ]
        w = '(())()()((())))'
        assert not EarleyAlgorithm.run(rules, w)

    def test_9(self):
        rules = [
            Rule('P', 'x'),
            Rule('X', '(P+P)'),
            Rule('X', '(P-P)'),
            Rule('X', '(P*P)'),
            Rule('X', '(P/P)'),
            Rule('X', '(X+X)'),
            Rule('X', '(X-X)'),
            Rule('X', '(X*X)'),
            Rule('X', '(X/X)'),
            Rule('X', '(X+P)'),
            Rule('X', '(X-P)'),
            Rule('X', '(X*P)'),
            Rule('X', '(X/P)'),
            Rule('X', '(P+X)'),
            Rule('X', '(P-X)'),
            Rule('X', '(P*X)'),
            Rule('X', '(P/X)'),
        ]
        w = '((x-(x/x))/(x+(x*x)))'
        assert EarleyAlgorithm.run(rules, w)

    def test_10(self):
        rules = [
            Rule('P', 'x'),
            Rule('X', '(P+P)'),
            Rule('X', '(P-P)'),
            Rule('X', '(P*P)'),
            Rule('X', '(P/P)'),
            Rule('X', '(X+X)'),
            Rule('X', '(X-X)'),
            Rule('X', '(X*X)'),
            Rule('X', '(X/X)'),
            Rule('X', '(X+P)'),
            Rule('X', '(X-P)'),
            Rule('X', '(X*P)'),
            Rule('X', '(X/P)'),
            Rule('X', '(P+X)'),
            Rule('X', '(P-X)'),
            Rule('X', '(P*X)'),
            Rule('X', '(P/X)'),
        ]
        w = '((x-(x/x))/(x+(x*x+x)))'
        assert not EarleyAlgorithm.run(rules, w)
