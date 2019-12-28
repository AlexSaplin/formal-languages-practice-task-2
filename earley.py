from typing import List, Set

from models import Situation, Rule


class EarleyAlgorithm:

    @classmethod
    def scan(cls, d: List[Set[Situation]], w: str, pos: int):
        if pos < 0:
            return

        for situation in d[pos]:
            if situation.rule.next[situation.dot_position] == w[pos]:
                d[pos + 1].add(Situation(situation.rule, situation.dot_position + 1, situation.index))

    @classmethod
    def complete(cls, d: List[Set[Situation]], pos: int):
        updated_situations: List[Situation] = []
        for situation in d[pos]:
            if situation.dot_position != len(situation.rule.next):
                continue
            for new_situation in d[situation.index]:
                if situation.rule.start == new_situation.rule.next[new_situation.dot_position]:
                    updated_situations.append(Situation(new_situation.rule,
                                                        new_situation.dot_position + 1,
                                                        new_situation.index))
        for situation in updated_situations:
            d[pos].add(situation)

    @classmethod
    def predict(cls, g: List[Rule], d: List[Set[Situation]], pos: int):
        updated_situations: List[Situation] = []
        for situation in d[pos]:
            for rule in g:
                if rule.start == situation.rule.next[situation.dot_position]:
                    updated_situations.append(Situation(rule, 0, pos))
        for situation in updated_situations:
            d[pos].add(situation)

    @classmethod
    def main(cls, g: List[Rule], w: str):
        raise NotImplemented
