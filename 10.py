class MealyError(Exception):
    def __init__(self, method_name):
        self.method_name = method_name


class Mealy:
    def __init__(self):
        self.state = 'A'

    def skid(self):
        transitions = {'A': ('B', 0), 'B': ('C', 2),
                       'C': ('C', 5), 'D': ('E', 6),
                       'E': ('F', 7), 'G': ('D', 10)}
        try:
            transition = transitions[self.state]
            self.state = transition[0]
            return transition[1]
        except KeyError:
            raise MealyError("skid")

    def trash(self):
        transitions = {'A': ('F', 1), 'B': ('D', 3),
                       'C': ('D', 4), 'H': ('C', 11),
                       'F': ('G', 8), 'G': ('H', 9)}

        try:
            transition = transitions[self.state]
            self.state = transition[0]
            return transition[1]
        except KeyError:
            raise MealyError("trash")


def main():
    return Mealy()


def test():
    o = main()
    o.skid()  # 0
    o.skid()  # 2
    o.skid()  # 5
    o.trash()  # 4
    o.skid()  # 6
    o.skid()  # 7
    o.trash()  # 8
    o.skid()  # 10
    o.skid()  # 6
    try:
        o.trash()  # MealyError
    except MealyError:
        pass
    o.skid()  # 7
    try:
        o.skid()  # MealyError
    except MealyError:
        pass
    o.trash()  # 8
    o.trash()  # 9
    o.trash()  # 11
    o.trash()  # 4
    try:
        o.trash()  # MealyError
    except MealyError:
        pass
    o.skid()  # 6


test()
