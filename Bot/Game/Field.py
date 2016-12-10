import copy

class Field:
    def __init__(self):
        self.width = 10
        self.height = 20
        self.field = [[0]*self.width]*self.height

    def size(self):
        return self.width, self.height

    def updateField(self, field):
        self.field = field

    def projectPieceDown(self, piece, offset):
        piecePositions = self.__offsetPiece(piece.positions(), offset)

        field = None
        for height in range(0, self.height-1):
            tmp = self.fitPiece(piecePositions, [0, height])

            if not tmp:
                break
            field = tmp

        return field

    def heightForColumn(self, column):
        width, height = self.size()
        for i in range(1, height):
            if(self.field[i][column] == 1):
                return height-i
        return 0

    def heights(self):
        result = []
        width, height = self.size()
        for i in range(0, width):
            result.append(self.heightForColumn(i))
        return result

    def aggregateHeight(self):
        return sum(self.heights())

    def completLine(self):
        result = 0
        width, height = self.size()
        for i in range (0, height) :
            if sum(self.field[i]) == width:
                result+=1
        return result

    def bumpiness(self):
        result = 0
        heights = self.heights()
        for i in range(0, len(heights)-1):
            result += abs(heights[i]-heights[i+1])
        return result

    def numberOfHole(self):
        width, height = self.size()
        heights = self.heights()
        result = 0
        for i in range (0, height) :
            for j in range(0, width) :
                if self.field[i][j] == 0 and height-i < heights[j]:
                    result+=1
        return result

    @staticmethod
    def __offsetPiece(piecePositions, offset):
        piece = copy.deepcopy(piecePositions)
        for pos in piece:
            pos[0] += offset[0]
            pos[1] += offset[1]

        return piece

    def __checkIfPieceFits(self, piecePositions):
        for x,y in piecePositions:
            if 0 <= x < self.width and 0 <= y < self.height:
                if self.field[y][x] >= 1:
                    return False
            else:
                return False
        return True

    def fitPiece(self, piecePositions, offset=None):
        if offset:
            piece = self.__offsetPiece(piecePositions, offset)
        else:
            piece = piecePositions

        field = copy.deepcopy(self.field)
        if self.__checkIfPieceFits(piece):
            for x,y in piece:
                field[y][x] = 1

            return field
        else:
            return None
