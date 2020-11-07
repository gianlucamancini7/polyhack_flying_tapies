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


class Statement():
    def evaluate(self, state):
        raise NotImplementedError

    def validate_statement(self, valid_ids):
        raise NotImplementedError


class RandomAtom():
    def __init__(self, prob=0.5):
        self.prob = 0.5

    def evaluate(self):
        import random
        return random.random() < self.prob


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


class EvaluateAtom(Statement):
    def __init__(self, id):
        self.id = id

    def evaluate(self, state):
        return bool(state.data(self.id))

    def validate_statement(self, valid_ids):
        return self.id in valid_ids


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


class And(Statement):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, state):
        return self.left.evaluate(state) and self.right.evaluate(state)

    def validate_statement(self, valid_ids):
        return self.left.validate_statement(valid_ids) and self.right.validate_statement(valid_ids)


class Or(Statement):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, state):
        return self.left.evaluate(state) or self.right.evaluate(state)

    def validate_statement(self, valid_ids):
        return self.left.validate_statement(valid_ids) and self.right.validate_statement(valid_ids)


class Not(Statement):
    def __init__(self, statement):
        self.statement = statement

    def evaluate(self, state):
        return not self.statement.evaluate(state)

    def validate_statement(self, valid_ids):
        return self.statement.validate_statement(valid_ids)


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

        Rule(
            FuzzyAtom(devices[0]['id'], 30, 1000),

            [devices[5]['id']]
        ),

    ]

    dump_rules(rules, 'data/rules_easy.data')
