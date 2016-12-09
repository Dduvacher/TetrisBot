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
    %peut être mettre ces méthode dans la classe field
    def aggregateHeight(field):
        result = 0
        width,height = field.size()
        for j in range(0, width) :
            for i in range(0, height) :
                if( field.field[i][j] == 1):
                    result += height
        return result

    def completLine(field):
        result = 0
        sumTemp = 0
        for i in range (0,height) :
            sumTemp = 0
            for j in range(0,width) :
                if field.field[i][j] == 1 :
                    sumTemp++
            if sumTemp == width :
                result++
        return result


    def hasHole(field):
        tabLength=heights
        result=0
        hasAOne=false
        for j in range (0, width) :
            for i in range (0, height) :
                if field.field[i][j] == 0 && i<tabLength[j]
                    result+=1
        return result
