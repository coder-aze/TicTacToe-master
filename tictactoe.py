class Tic:
  table=[[1,2,3],[4,5,6],[7,8,9]]
  def __init__(self,p1,p2):
    self.p1=p1
    self.p2=p2
  def player1(self):
    index,index_1=0,0
    for i in Tic.table:
      print(i)
    x=int(input("X: "))
    for j in Tic.table:
      if x in j:
        index_1=j.index(x)
        Tic.table[index][index_1]=self.p1
      index+=1
  def player2(self):
    index,index_1=0,0
    for i in Tic.table:
      print(i)
    y=int(input("Y: "))
    for j in Tic.table:
      if y in j:
        index_1=j.index(y)
        Tic.table[index][index_1]=self.p2
      index+=1
  def control(self):
    if Tic.table[0][0] == Tic.table[0][1] == Tic.table[0][2]==self.p1:
      print(f"{self.p1} WINNN","\n",20*"-")
      Tic.table=[[1,2,3],[4,5,6],[7,8,9]]
    elif Tic.table[0][0] == Tic.table[0][1] == Tic.table[0][2]==self.p2:
      print(f"{self.p2} WINNN","\n",20*"-")
      Tic.table=[[1,2,3],[4,5,6],[7,8,9]]
    elif Tic.table[1][0] == Tic.table[1][1] == Tic.table[1][2]==self.p1:
      print(f"{self.p1} WINNN","\n",20*"-")  
      Tic.table=[[1,2,3],[4,5,6],[7,8,9]] 
    elif Tic.table[1][0] == Tic.table[1][1] == Tic.table[1][2]==self.p2:
      print(f"{self.p2} WINNN","\n",20*"-")
      Tic.table=[[1,2,3],[4,5,6],[7,8,9]]
    elif Tic.table[2][0] == Tic.table[2][1] == Tic.table[2][2]==self.p1:
      print(f"{self.p1} WINNN","\n",20*"-")
      Tic.table=[[1,2,3],[4,5,6],[7,8,9]]
    elif Tic.table[2][0] == Tic.table[2][1] == Tic.table[2][2]==self.p2:
      print(f"{self.p2} WINNN","\n",20*"-")
      Tic.table=[[1,2,3],[4,5,6],[7,8,9]]
    elif Tic.table[0][0] == Tic.table[1][0] == Tic.table[2][0]==self.p1:
      print(f"{self.p1} WINNN","\n",20*"-")
      Tic.table=[[1,2,3],[4,5,6],[7,8,9]]
    elif Tic.table[0][0] == Tic.table[1][0] == Tic.table[2][0]==self.p2:
      print(f"{self.p2} WINNN","\n",20*"-")
      Tic.table=[[1,2,3],[4,5,6],[7,8,9]]
    elif Tic.table[0][1] == Tic.table[1][1] == Tic.table[2][1]==self.p1:
      print(f"{self.p1} WINNN","\n",20*"-")
      Tic.table=[[1,2,3],[4,5,6],[7,8,9]]
    elif Tic.table[0][1] == Tic.table[1][1] == Tic.table[2][1]==self.p2:
      print(f"{self.p2} WINNN","\n",20*"-")
      Tic.table=[[1,2,3],[4,5,6],[7,8,9]]
    elif Tic.table[0][2] == Tic.table[1][2] == Tic.table[2][2]==self.p1:
      print(f"{self.p1} WINNN","\n",20*"-")
      Tic.table=[[1,2,3],[4,5,6],[7,8,9]]
    elif Tic.table[0][2] == Tic.table[1][2] == Tic.table[2][2]==self.p2:
      print(f"{self.p2} WINNN","\n",20*"-")
      Tic.table=[[1,2,3],[4,5,6],[7,8,9]]
    elif Tic.table[0][0] == Tic.table[1][1] == Tic.table[2][2]==self.p1:
      print(f"{self.p1} WINNN","\n",20*"-")
      Tic.table=[[1,2,3],[4,5,6],[7,8,9]]
    elif Tic.table[0][0] == Tic.table[1][1] == Tic.table[2][2]==self.p2:
      print(f"{self.p2} WINNN","\n",20*"-")
      Tic.table=[[1,2,3],[4,5,6],[7,8,9]]
    elif Tic.table[1][0] == Tic.table[1][1] == Tic.table[1][2]==self.p1:
      print(f"{self.p1} WINNN","\n",20*"-")
      Tic.table=[[1,2,3],[4,5,6],[7,8,9]]
    elif Tic.table[0][2] == Tic.table[1][1] == Tic.table[2][0]==self.p2:
      print(f"{self.p2} WINNN","\n",20*"-")
      Tic.table=[[1,2,3],[4,5,6],[7,8,9]]
    depo=[]
    depo1=[]
    for x in Tic.table:
      for y in x:
        depo.append(y)
    for i in depo:
      if isinstance(i,int):
        continue
      else:
        depo1.append(i)
      if len(depo1)==9:
        print("TRY AGAIN")
        Tic.table=[[1,2,3],[4,5,6],[7,8,9]]
        break
test=Tic("X","Y")
while (True):
  test.player1()
  test.control()
  test.player2()
  test.control()
