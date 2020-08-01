
#var1==0
tiktoe=[1,2,3,4,5,6,7,8,9]
#user choice
def board():
  print(str(tiktoe[0])+"|"+str(tiktoe[1])+"|"+str(tiktoe[2])+"|")
  print("_________________")
  print(str(tiktoe[3])+"|"+str(tiktoe[4])+"|"+str(tiktoe[5])+"|")
  print("__________________")
  print( str(tiktoe[6])+"|"+str(tiktoe[7])+"|"+str(tiktoe[8])+"|")
  print("")
  print("")

def userchoice1 ():
  Xuser = (input()) 
  daboy=0         
  Xuser=int(Xuser)
  Xguess=Xuser-1
  while tiktoe[Xguess]== "X" or tiktoe[Xguess] == "O":
    Xuser=int(input("already claimed pick another square"))
    Xguess=Xuser-1
  if tiktoe[Xguess]!= "X" or tiktoe[Xguess] != "O":
    tiktoe[Xguess]="X"      
  board()


def userchoice2 (): 
  Xuser = (input()) 
  daboy=0  
  Xuser=int(Xuser)     
  Xguess=Xuser-1
  while tiktoe[Xguess]== "X" or tiktoe[Xguess] == "O":
    Xuser=int(input("already claimed pick another square"))
    Xguess=Xuser-1
  if tiktoe[Xguess]!= "X" or tiktoe[Xguess] != "O":
    tiktoe[Xguess]="O"      
  board()
  

winner=3
def get_win(tiktoe): 
  tiktoecheck=tiktoe.copy()
  

  for i in range (0, len(tiktoecheck)):
    if tiktoecheck[i] != "O" and tiktoecheck[i]!="X":
      tiktoecheck[i]=" "
  count = 0

  #print(tiktoecheck)
  #print(tiktoe)
#user1 
  if tiktoe[0]=="X" and tiktoe[1]=="X" and tiktoe[2]=="X":
    return(1)
  if tiktoe[3]=="X" and tiktoe[4]=="X" and tiktoe[5]=="X":
    return(1)
  if tiktoe[6]=="X" and tiktoe[7]=="X" and tiktoe[8]=="X":
    return(1)
  if tiktoe[0]=="X" and tiktoe[3]=="X" and tiktoe[6]=="X":
    return(1)
  if tiktoe[1]=="X" and tiktoe[4]=="X" and tiktoe[7]=="X":
    return(1)
  if tiktoe[2]=="X" and tiktoe[5]=="X" and tiktoe[8]=="X":
    return(1)
  if tiktoe[1]=="X" and tiktoe[4]=="X" and tiktoe[7]=="X":
    return(1)
  if tiktoe[2]=="X" and tiktoe[5]=="X" and tiktoe[8]=="X":
    return(1)
  if tiktoe[0]=="X" and tiktoe[4]=="X" and tiktoe[8]=="X":
    return(1)
  if tiktoe[2]=="X" and tiktoe[4]=="X" and tiktoe[6]=="X":
    return(1)
  if tiktoe[0]=="X" and tiktoe[1]=="X" and tiktoe[2]=="X":
    return(1)

  #user 2:
  if tiktoe[3]=="O" and tiktoe[4]=="O" and tiktoe[5]=="O":
    return(2)
  if tiktoe[6]=="O" and tiktoe[7]=="O" and tiktoe[8]=="O":
    return(2)
  if tiktoe[0]=="O" and tiktoe[3]=="O" and tiktoe[6]=="O":
    return(2)
  if tiktoe[1]=="O" and tiktoe[4]=="O" and tiktoe[7]=="O":
    return(2)
  if tiktoe[2]=="O" and tiktoe[5]=="O" and tiktoe[8]=="O":
    return(2)
  if tiktoe[1]=="O" and tiktoe[4]=="O" and tiktoe[7]=="O":
    return(2)
  if tiktoe[2]=="O" and tiktoe[5]=="O" and tiktoe[8]=="O":
    return(2)
  if tiktoe[0]=="O" and tiktoe[4]=="O" and tiktoe[8]=="O":
    return(2)
  if tiktoe[2]=="O" and tiktoe[4]=="O" and tiktoe[6]=="O":
    return(2)
  if not " " in tiktoecheck:
    return(3)

  else:
    return (0)

def main():
  ans = 0 

  if ans == 1:
    print("user 1 wins")
  elif ans==2:
    print("user 2 wins")
  elif ans==3:
    print("tie")

  while  ans==0: 
    userchoice1()
    ans=get_win(tiktoe)
    if ans == 1:
      print("user 1 wins")
    userchoice2()
    ans=get_win(tiktoe)
    if ans==2:
      print("user 2 wins")
    ans=get_win()
    if ans == 3: 
      print ("tie")
  
if __name__ == "__main__": main()
