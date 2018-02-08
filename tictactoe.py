class Board():
    """A 3x3 Tic-tac-toe board where spaces are either ' ', 'X', or 'O' """
    WIN_INDICES = [ [1,2,3], [4,5,6], [7,8,9],  #horizontal wins
                    [1,4,7], [2,5,8], [3,6,9],  #vertical wins
                    [1,5,9], [3,5,7]]           #diagonal wins

    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]    #start with board of all spaces

    def __repr__(self):
        s = ''
        for i, row in enumerate(self.board):
            s += ' %s | %s | %s \n' % tuple(row)
            if i < 2 :
                s += '---|---|---\n'
        return s

    def move(self, player, position):
        """Place player string onto board at position if available
        Positions have this numbering:
         1 | 2 | 3
         --|---|--
         4 | 5 | 6
         --|---|--
         7 | 8 | 9
        """
        #ensure position is valid (on the board and not taken)
        if not self.posTaken(position):
            (row, col) = self.posToIndices(position)
            self.board[row][col] = player

    def posToIndices(self, position):
        if position in range(1, 10):   #ensure valid index
            row = (position - 1) // 3
            col = (position - 1) %  3
            return (row, col)
        raise RuntimeError('asking for index outside of tictactoe board! index=' + position)

    def posTaken(self, position):
        return self.getVal(position) != ' '

    def getVal(self, position):
        """Return value stored in board at index"""
        (row, col) = self.posToIndices(position)
        return self.board[row][col]

    def isGameOver(self):
        """Returns true if game is over, which results when:
        - A player has won.
        OR
        - The board is full.
        """
        return self.hasWon()[0] or self.isFull()

    def hasWon(self):
        for win_index in Board.WIN_INDICES:
            if all(self.getVal(pos) == 'X' for pos in win_index):
                return (True, 'X')
            elif all(self.getVal(pos) == 'O' for pos in win_index):
                return (True, 'O')
        return (False, None)

    def isFull(self):
        if any(self.getVal(pos) == ' ' for pos in range(1,10)):
            return False
        return True

    def isInvalid(self, move):
        return move not in list('0123456789') or self.posTaken(int(move))

    def play(self):
        player = 'X'
        while not self.isGameOver():
            #Ask first player for move
            currentMove = input("Player %s, Enter a number 1-9:" % player)
            while self.isInvalid(currentMove):
                currentMove = input("INVALID MOVE!\nPlayer %s,Enter a number 1-9:" % player)
            #move player
            self.move(player, int(currentMove))
            player = 'O' if player == 'X' else 'X'  #switch players
            #display board
            print(self)
        #change turns and repeat
        (won, winner) = self.hasWon()
        endString = '%s WINS!' % winner if won else 'TIE!'
        print(endString)



game = Board()
game.play()
