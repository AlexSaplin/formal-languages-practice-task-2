class Rule:

    def __init__(self, start: str, go: str):
        self.start = start
        self.next = go

    def __eq__(self, other):
        return self.start == other.start and self.next == other.next


class Situation:

    def __init__(self, rule: Rule, dot_position: int, index: int):
        self.rule = rule
        self.dot_position = dot_position
        self.index = index

    def __hash__(self):
        return hash((self.rule.start, self.rule.next, self.dot_position, self.index))

    def __eq__(self, other):
        return self.rule == other.rule and self.dot_position == other.dot_position and self.index == other.index
