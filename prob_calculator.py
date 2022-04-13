import copy
import random
# Consider using the modules imported above.

def list_to_dict(drawn):
    result = dict()
    for item in drawn:
        if(item in result):
            result[item]+=1
        else:
            result[item]=1
    return result

def bingo(drawn, expected):
    drawn_dict = list_to_dict(drawn)
    for k,v in expected.items():
        if(k in drawn_dict):
            if(drawn_dict[k] < v):
                return 0
        else:
            return 0
    return 1

class Hat:
    def __init__(self, **kwargs):
        self.contents = list()
        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, todraw):
        result = list()
        if (todraw > len(self.contents)):
            return self.contents
        for i in range(todraw):
            drawn = random.choice(self.contents)
            self.contents.remove(drawn)
            result.append(drawn)
        return result


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        m += bingo(hat_copy.draw(num_balls_drawn), expected_balls)
    return m / num_experiments
