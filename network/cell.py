import random

from random import randint

class InputCell:
    x=1
class OutputCell:
    y=1
class HiddenCell:
    z=1
class Preceptron:
    def __init__(self, n):
        self.weights = [0]*n
        for i in range(0,len(self.weights)):
            x = randint(1,2)
            if x == 1:
                self.weights[i] = -1
            else:
                self.weights[i] = 1

    def feedForward(self,inputs):
        sum = 0
        for i in range(0,len(self.weights)):
            sum+=inputs[i]*self.weights[i]
        return self.activate(sum)

    def activate(self, sum):
        if sum > 0:
            return 1
        else:
            return -1
    def train(self, inputs, desired):
        self.c = 0.01
        guess = self.feedForward(inputs)
        error = desired - guess
        for i in range(0,len(self.weights)):
            self.weights[i] += c * error * inputs[i]
