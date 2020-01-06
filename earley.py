from typing import List, Set

from models import Situation, Rule


class EarleyAlgorithm:

    @classmethod
    def scan(cls, d: List[Set[Situation]], w: str, pos: int):
        if pos < 0:
            return
        for situation in d[pos]:
            try:
                if situation.rule.next[situation.dot_position] == w[pos]:
                    d[pos + 1].add(Situation(situation.rule, situation.dot_position + 1, situation.index))
            except Exception as e:
                pass

    @classmethod
    def complete(cls, d: List[Set[Situation]], pos: int):
        updated_situations: List[Situation] = []
        for situation in d[pos]:
            if situation.dot_position != len(situation.rule.next):
                continue
            for new_situation in d[situation.index]:
                try:
                    if situation.rule.start == new_situation.rule.next[new_situation.dot_position]:
                        updated_situations.append(Situation(new_situation.rule,
                                                            new_situation.dot_position + 1,
                                                            new_situation.index))
                except Exception as e:
                    pass
        for situation in updated_situations:
            d[pos].add(situation)

    @classmethod
    def predict(cls, g: List[Rule], d: List[Set[Situation]], pos: int):
        updated_situations: List[Situation] = []
        for situation in d[pos]:
            for rule in g:
                try:
                    if rule.start == situation.rule.next[situation.dot_position]:
                        updated_situations.append(Situation(rule, 0, pos))
                except Exception as e:
                    pass
        for situation in updated_situations:
            d[pos].add(situation)

    @classmethod
    def run(cls, g: List[Rule], w: str):
        d = [set() for i in range(len(w) + 1)]
        d[0].add(Situation(Rule('S', 'X'), 0, 0))
        for i in range(len(w) + 1):
            cls.scan(d, w, i - 1)
            while True:
                check = len(d[i])
                cls.complete(d, i)
                cls.predict(g, d, i)
                if check == len(d[i]):
                    break
        if Situation(Rule('S', 'X'), 1, 0) in d[len(w)]:
            return True
        else:
            return False
