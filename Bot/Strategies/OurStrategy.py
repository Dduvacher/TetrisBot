from random import randint

from AbstractStrategy import AbstractStrategy


class OurStrategy(AbstractStrategy):
    def __init__(self, game):
        AbstractStrategy.__init__(self, game)
        self._actions = ['left', 'right', 'turnleft', 'turnright', 'down', 'drop']

    def choose(self):
        ind = [randint(0, 4) for _ in range(1, 10)]
        moves = map(lambda x: self._actions[x], ind)
        moves.append('drop')

        return moves


    @staticmethod
    def aggregateHeight(field):
        result = 0
        width,height = field.size()
        for i in reversed(range(0, height)) :
            for j in range(0,width) :
                if( field.field[height-i][j] == 0):
                    result += height-i-1
        return result

    @staticmethod
    def completLine(field):
        result = 0
        sumTemp = 0
        width,height = field.size()
        for i in range (0,height) :
            sumTemp = 0
            for j in range(0,width) :
                if field.field[i][j] == 1:
                    sumTemp+=1
            if sumTemp == width:
                result+=1
        return result

    @staticmethod
    def bumpiness(field):
        result = 0
        heights = field.heights()
        for i in range(0, len(heights)-1):
            result += abs(heights[i]-heights[i+1])
        return result
