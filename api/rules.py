import pickle
import json


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


class EvaluateAtom(Statement):
    def __init__(self, id):
        self.id = id

    def evaluate(self, state):
        return bool(state.data(self.id))


class FuzzyAtom(Statement):
    def __init__(self, id, threshold, delta):
        self.id = id
        self.threshold = threshold
        self.delta = delta

    # Compute whether we are in a certain range of the value with tolerance
    def evaluate(self, state):
        return abs(state.data(self.id) - self.threshold) < self.delta


class And(Statement):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, state):
        return self.left.evaluate(state) and self.right.evaluate(state)


class Or(Statement):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, state):
        return self.left.evaluate(state) or self.right.evaluate(state)


class Not(Statement):
    def __init__(self, statement):
        self.statement = statement

    def evaluate(self, state):
        return not self.statement.evaluate(state)


if __name__ == '__main__':

    devices = json.load(open('data/sensors.json','rb'))



    rules = [
        Rule(
            FuzzyAtom(devices[2]['id'], 0.5, 0.05),

            [devices[5]['id']]
        ),

        Rule(
            EvaluateAtom(devices[2]['id']),

            [devices[5]['id']]

        ),
        Rule(
            And(
                EvaluateAtom(devices[2]['id']),
                EvaluateAtom(devices[1]) 
            ),

                [devices[5]['id']]
                
            ), 

        Rule(
            EvaluateAtom(devices[2]['id']),
            [devices[5]['id'], devices[6]['id']]
        )


    ]

    dump_rules(rules, 'rules_comp.data')
