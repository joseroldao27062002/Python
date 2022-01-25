numberOfPieces = int(input())
sizeOfBoard = int(input())
board = []
piecesOnBoard = 0
startGame = False

for i in range(sizeOfBoard):
    board.append([0] * sizeOfBoard)

for j in range(numberOfPieces):
    positionX, positionY = input().split()
    positionX = int(positionX)
    positionY = int(positionY)

    if board[positionX][positionY] != 0:
        pass
    else:
        board[positionX][positionY] = 1
        piecesOnBoard += 1

if piecesOnBoard == numberOfPieces:
    startGame = True
    print('{}\n0'.format(startGame))
else:
    print('{}\n{}'.format(startGame, (numberOfPieces - piecesOnBoard)))

