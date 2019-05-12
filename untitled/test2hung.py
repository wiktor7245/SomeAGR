import hungalg

mat =       [[1,1,1,0,0,0],
             [0,1,1,0,0,1],
             [0,0,1,0,1,0],
             [0,0,0,1,1,1],
             [0,1,0,0,0,1],
             [0,1,0,0,0,0]]

mat2 =      [[1,1,1,0,0,0],
             [0,1,1,0,0,1],
             [0,0,1,0,1,0],
             [0,0,0,1,1,1],
             [0,1,0,0,0,0],
             [0,1,0,0,0,0]]

mat3 = [[3,5,5,4,1],
        [2,2,0,2,2],
        [2,4,4,1,0],
        [0,1,2,0,0],
        [1,2,1,3,3]]

ans = hungalg.maximize(mat)
best = sum(mat[i][j] for i,j in ans)
print(ans)
print(best)
print(hungalg.maximize(mat2))

print(hungalg.maximize(mat3))
countline = 0
countcol = 0

for l in mat:
  if mat.index(l) == 0:
      countline = len(l)
      print("There are " + str(countline) + "columns")
  for k in l:
      if k is 3:
          print("dupa")
    #print(k)
  #print("sad")
  countcol +=1
print("There are " + str(countcol) + "lines")

