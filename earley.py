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
    def complete(cls, d: List[Set[Situation]], situations: Set[Situation],
                 updated_situations: Set[Situation], pos: int):
        for situation in situations:
            if situation.dot_position != len(situation.rule.next):
                continue
            for new_situation in d[situation.index]:
                try:
                    if situation.rule.start == new_situation.rule.next[new_situation.dot_position]:
                        current_situation = Situation(new_situation.rule,
                                                      new_situation.dot_position + 1,
                                                      new_situation.index)
                        if current_situation not in d[pos]:
                            updated_situations.add(current_situation)
                except Exception as e:
                    pass

    @classmethod
    def predict(cls, g: List[Rule], d: List[Set[Situation]], situations: Set[Situation],
                updated_situations: Set[Situation], pos: int):
        for situation in situations:
            if situation.dot_position >= len(situation.rule.next):
                continue
            for rule in g:
                try:
                    if rule.start == situation.rule.next[situation.dot_position]:
                        current_situation = Situation(rule, 0, pos)
                        if current_situation not in d[pos]:
                            updated_situations.add(current_situation)
                except Exception as e:
                    pass

    @classmethod
    def run(cls, g: List[Rule], w: str):
        d = [set() for i in range(len(w) + 1)]
        d[0].add(Situation(Rule('S', 'X'), 0, 0))
        for i in range(len(w) + 1):
            cls.scan(d, w, i - 1)
            new_situations: Set[Situation] = set()
            old_situations: Set[Situation] = set()
            cls.complete(d, d[i], new_situations, i)
            cls.predict(g, d, d[i], new_situations, i)
            while len(new_situations) > 0:
                for situation in new_situations:
                    d[i].add(situation)
                    old_situations.add(situation)
                new_situations = set()
                cls.complete(d, old_situations, new_situations, i)
                cls.predict(g, d, old_situations, new_situations, i)
                old_situations = new_situations
            for situation in old_situations:
                d[i].add(situation)
        if Situation(Rule('S', 'X'), 1, 0) in d[len(w)]:
            return True
        else:
            return False
