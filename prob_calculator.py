import random
import copy

class Hat:
    def __init__(self,**kwargs):
        self.contents=list()
        for k,v in kwargs.items():
            for j in range(v):
                self.contents.append(k)
        print(self.contents)
    def draw(self,n):
        if n>=len(self.contents):
            return self.contents
        else:
            a=list()
            for i in range(n):
                x=random.sample(self.contents,1)
                a+=x
                for j in x:
                    if j in self.contents:
                        self.contents.remove(j)
        print(a)
        print(self.contents)
        return a

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    event=0
    for exe in range(num_experiments):
        expected_list=list()
        for c,n in expected_balls.items():
            for j in range(n):
                expected_list.append(c)
        new_hat=copy.deepcopy(hat)
        sample_list=new_hat.draw(num_balls_drawn)
        print(sample_list)
        for color in sample_list:
            if color in expected_list:
                expected_list.remove(color)
        if len(expected_list)==0:
            event+=1
    prob=event/num_experiments
    print(prob)
    return prob





hat=Hat(blue=4, red=2, green=6)
hat.draw(2)
experiment(hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)