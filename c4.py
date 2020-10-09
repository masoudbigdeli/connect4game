class connect4:
  def __init__(self):
    self.B = [[0 for i in range(7)] for j in range(6)]
    
    self.player = 1
  def get_open_spots(self):
      return [[r,c] for r in range(6) for c in range(7)
              if self.B[r][c] == 0]
  def is_valid_move(self,r,c):
    self.row = r
    self.col = c
    for c in range(7):
        for r in range(6):
            if self.B[r][c] == 0:
              self.max_row = r      
        if self.row == self.max_row and c == self.col and 0<=c<=6 :
            self.u = True
            break
        else:
            self.u = False
    return self.u

  def make_move(self,r,c):
      if self.is_valid_move(r,c):
        self.B[r][c] = self.player
        self.player = (self.player+2)%2 + 1
      else: 
        print('not valid move')

  def check_for_winner(self):
    for m in range(3):
      self.Rows = m + 3
      for n in range(4):
        self.Cols = n + 3
        for j in range(self.Rows-3,self.Rows+1):
          for i in range(self.Cols-3,self.Cols+1):
            self.Sqr =[[self.B[v][w] for v in range(self.Rows-3,self.Rows+1)] for w in range(self.Cols-3,self.Cols+1)]

        for h in range(4):
          if self.Sqr[0][h]==self.Sqr[1][h]==self.Sqr[2][h]==self.Sqr[3][h]!=0:
            return self.Sqr[0][h]
        for f in range(4):
          if self.Sqr[f][0]==self.Sqr[f][1]==self.Sqr[f][2]==self.Sqr[f][3]!=0:
            return self.Sqr[f][0]
        if self.Sqr[0][0]==self.Sqr[1][1]==self.Sqr[2][2]==self.Sqr[3][3]!=0:
          return self.Sqr[0][0]
        if self.Sqr[3][0]==self.Sqr[2][1]==self.Sqr[1][2]==self.Sqr[0][3]!=0:
          return self.Sqr[3][0]
        if self.get_open_spots()==[]:
          return 0
    return -1
def print_board():
  chars = ['-', 'X', 'O']
  for r in range(6):
    for c in range(7):
      print(chars[game.B[r][c]], end=' ')
    print()
game = connect4()
while game.check_for_winner()==-1:
  print_board()
  r,c = eval(input('Enter spot, player ' + str(game.player) + ': '))
  game.make_move(r,c)

print_board()
x = game.check_for_winner()
if x == 0:
  print("It's a draw.")
else:
  print('Player', x, 'wins!')
