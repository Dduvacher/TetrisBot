from Bot.Strategies.OurStrategy import OurStrategy
from Bot.Game.Field import Field
from Bot.Game import Piece

# field = map(lambda r: map(lambda x: int(x), r.split(",")), field.split(";"))
# for line in field:
#     print(line)

field = """
0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,0,0,0,0,0"""

initialField = map(lambda r: map(lambda x: int(x), r.split(",")), field.split(";"))
piece = Piece.create("L")
print(piece.positions())

fieldObj = Field()
fieldObj.updateField(initialField)

bestScore = -float("inf")
offset = 0
rotation = 0

for i in range(0, len(piece._rotations)):
    print("")
    for x in range(0, fieldObj.width):
        fieldObj.updateField(initialField)
        field = fieldObj.projectPieceDown(piece, [x, 0])
        if not field is None:
            # for line in field:
            #     print(line)
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

fieldObj.updateField(initialField)
piece = Piece.create("L")
piece.turnRight(rotation)
field = fieldObj.projectPieceDown(piece, [offset, 0])
for line in field:
    print(line)

#print(fieldObj.heights())
#print(OurStrategy.aggregateHeight(fieldObj))


# field = """
# 0,0,0,0,1,1,0,0,0,0;
# 0,0,0,0,0,0,0,0,0,0;
# 0,0,0,0,0,0,0,0,0,0;
# 0,0,0,0,0,0,0,0,0,0;
# 0,0,0,0,0,0,0,0,0,0;
# 0,0,0,0,0,0,0,0,0,0;
# 0,0,0,0,0,0,0,0,0,0;
# 0,0,0,0,0,0,0,0,0,0;
# 0,0,0,0,0,0,0,0,0,0;
# 0,0,0,0,0,0,0,0,0,0;
# 0,0,0,0,0,0,0,0,0,0;
# 0,0,0,0,0,0,0,0,0,0;
# 0,0,0,0,0,0,0,0,0,0;
# 0,0,0,0,0,0,0,0,0,0;
# 0,0,0,0,0,0,0,0,0,0;
# 0,0,0,0,1,1,0,0,0,0;
# 0,0,0,0,1,1,0,0,0,1;
# 0,0,1,0,1,1,0,1,0,1;
# 0,1,1,1,1,1,0,1,0,1;
# 1,1,1,1,1,1,1,1,0,1"""
