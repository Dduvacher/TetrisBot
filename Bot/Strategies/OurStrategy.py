from random import randint
from Bot.Game.Field import Field
from Bot.Game import Piece

from AbstractStrategy import AbstractStrategy


class OurStrategy(AbstractStrategy):
    def __init__(self, game):
        AbstractStrategy.__init__(self, game)
        self._actions = ['left', 'right', 'turnleft', 'turnright', 'down', 'drop']

    def choose(self):
        piece = self._game.piece
        xOffset = self._game.piecePosition[0]
        bestScore = -float("inf")
        offset = 0
        rotation = 0

        fieldObj = Field()
        initialField = self._game.me.field.field

        for i in range(0, len(piece._rotations)):
            print("")
            for x in range(0, fieldObj.width):
                fieldObj.updateField(initialField)
                field = fieldObj.projectPieceDown(piece, [x, 0])
                if not field is None:
                    fieldObj.updateField(field)
                    a = -0.510066
                    b = 0.760666
                    c = -0.35663
                    d = -0.184483
                    result = a * (fieldObj.aggregateHeight()) + b * (fieldObj.completLine()) + c * (fieldObj.numberOfHole()) + d * (fieldObj.bumpiness())
                    if result > bestScore:
                        bestScore = result
                        offset = x
                        rotation = i
            piece.turnRight()

        moves = []
        offset = offset - xOffset
        for _ in range(0, rotation):
            moves.append("turnright")
        for _ in range(0, abs(offset)):
            if offset > 0:
                moves.append("right")
            else:
                moves.append("left")
        moves.append('drop')
        return moves
