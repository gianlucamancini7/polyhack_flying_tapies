import pickle


def parse_rules(filename):
    return pickle.load(open(filename, 'rb'))


def dump_rules(rule, filename):
    pickle.dump(rule, open(filename, 'wb'))


class Statement():
    def evaluate(self, state):
        raise NotImplementedError


class AtomicStatement(Statement):
    def __init__(self, id, threshold):
        self.id = id
        self.threshold = threshold

    def evaluate(self, state):
        return state.data(self.id) < self.threshold


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
