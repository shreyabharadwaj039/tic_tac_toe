def ConstBoard(board):
  print("Current state of baord: \n\n")
  for i in range(9):
    if((i>0)and (i%3==0)):
      print("\n")
    if (board[i]==0):
      print("_", end=" ")
    if(board[i]==-1):
      print("X", end=" ")
    if(board[i]==1):
      print("O", end=" ")
  print("\n\n")

def User1Turn(board):
  pos=int(input("Enter X's position [1-9]"))
  if (board[pos-1]!=0):
    print("Wrong Move")
    exit(0)
  board[pos-1]=-1

def User2Turn(board):
  pos=int(input("Enter O's position [1-9]"))
  if (board[pos-1]!=0):
    print("Wrong Move")
    exit(0)
  board[pos-1]=1

def minmax(board,player):
  x= analyseboard(board)
  if (x!=0):
    return(x*player)
  pos=-1;
  value=-2
  for i in range (0,9):
    if (board[i]==0):
      board[i]=1
      score=-minmax(board,player*-1)
      board[i]=0
      if(score>value):
        value=score
        pos=i
  if (pos==-1):
    return 0
  return value

def CompTurn(board):
  pos=-1;
  value=-2
  for i in range (0,9):
    if (board[i]==0):
      board[i]=1
      score=-minmax(board,-1)
      board[i]=0
      if(score>value):
        value=score
        pos=i
  board[pos]=1

def analyseboard(board):
  cb=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

  for i in range(0,8):
    if (board[cb[i][0]]!=0 and
        board[cb[i][0]]==board[cb[i][1]]and
        board[cb[i][0]]==board[cb[i][2]]):
      return board[cb[i][0]];
  return 0;

def main():
  choice= int(input("Enter 1 for Single-Player or 2 for Multi-player Game: "))
  board=[0,0,0,0,0,0,0,0,0]
  if (choice==1):
    print("Comp: O vs You: X")
    player= int(input("Enter to play 1st or 2nd: "))
    for i in range (0,9):
      if (analyseboard(board)!=0):
        break
      if((i+player)%2==0):
        CompTurn(board);
      if (i%2==0):
        ConstBoard(board)
        User1Turn(board)
  else:
    for i in range(0,9):
      if (analyseboard(board)!=0):
        break
      if(i%2==0):
        ConstBoard(board)
        User1Turn(board)
      else:
        ConstBoard(board)
        User2Turn(board)


  x= analyseboard(board)
 
  if (x==0):
    ConstBoard(board)
    print("Draw!")
  if(x==-1):
    ConstBoard(board)
    print("Player 1 Wins!")
  if(x==1):
    ConstBoard(board)
    print("Player 2 Wins!")

main()
