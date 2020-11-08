import pickle
import json
import time


def parse_rules(filename):
    return pickle.load(open(filename, 'rb'))


def dump_rules(rule, filename):
    pickle.dump(rule, open(filename, 'wb'))


class Rule:
    def __init__(self, statement, activators):
        self.statement = statement
        self.activators = activators

    def to_str(self):
        return f"If ({self.statement.to_str()}) then ({self.activators})"


class Statement():
    def evaluate(self, state):
        raise NotImplementedError

    def validate_statement(self, valid_ids):
        raise NotImplementedError

    def to_str(self):
        raise NotImplementedError


class RandomAtom():
    def __init__(self, prob=0.5):
        self.prob = prob

    def evaluate(self, state):
        import random
        return random.random() < self.prob

    def validate_statement(self, valid_ids):
        return 0 <= self.prob <= 1

    def to_str(self):
        return f"random({self.prob})"


class TemporalAtom():
    def __init__(self, id, elapsed_time):
        self.id = id
        self.elapsed_time = elapsed_time

    def evaluate(self, state):
        start = state.last_msg(self.id)
        if start is None:
            return False

        end = time.time()
        return (end - start) < self.elapsed_time

    def validate_statement(self, valid_ids):
        return self.id in valid_ids

    def to_str(self):
        return f"last {self.id[:5]} msg less than {self.elapsed_time}"


class EvaluateAtom(Statement):
    def __init__(self, id):
        self.id = id

    def evaluate(self, state):
        return bool(state.data(self.id))

    def validate_statement(self, valid_ids):
        return self.id in valid_ids

    def to_str(self):
        return f"bool({self.id[:5]})"


class FuzzyAtom(Statement):
    def __init__(self, id, threshold, delta):
        self.id = id
        self.threshold = threshold
        self.delta = delta

    # Compute whether we are in a certain range of the value with tolerance
    def evaluate(self, state):
        data = state.data(self.id)
        if data is None:
            return False
        return abs(data - self.threshold) < self.delta

    def validate_statement(self, valid_ids):
        return self.id in valid_ids

    def to_str(self):
        return f"{self.id[:5]} < {self.threshold} (± {self.delta})"


class And(Statement):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, state):
        return self.left.evaluate(state) and self.right.evaluate(state)

    def validate_statement(self, valid_ids):
        return self.left.validate_statement(valid_ids) and self.right.validate_statement(valid_ids)

    def to_str(self):
        return f"({self.left.to_str()}) AND ({self.right.to_str()})"


class Or(Statement):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, state):
        return self.left.evaluate(state) or self.right.evaluate(state)

    def validate_statement(self, valid_ids):
        return self.left.validate_statement(valid_ids) and self.right.validate_statement(valid_ids)

    def to_str(self):
        return f"({self.left.to_str()}) OR ({self.right.to_str()})"


class Not(Statement):
    def __init__(self, statement):
        self.statement = statement

    def evaluate(self, state):
        return not self.statement.evaluate(state)

    def validate_statement(self, valid_ids):
        return self.statement.validate_statement(valid_ids)

    def to_str(self):
        return f"NOT({self.statement.to_str()})"


if __name__ == '__main__':

    devices = json.load(open('data/sensors.json', 'rb'))

    rules = [
        Rule(
            FuzzyAtom(devices[2]['id'], 0.5, 0.05),

            [devices[5]['id']]
        ),

        Rule(
            EvaluateAtom(devices[0]['id']),

            [devices[5]['id']]

        ),
        Rule(
            And(
                EvaluateAtom(devices[0]['id']),
                EvaluateAtom(devices[1]['id'])
            ),

            [devices[5]['id']]

        ),

        Rule(
            EvaluateAtom(devices[0]['id']),
            [devices[5]['id'], devices[6]['id']]
        ),
    ]

    dump_rules(rules, 'data/rules_comp.data')
