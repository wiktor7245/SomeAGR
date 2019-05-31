RESULT=[]
def multiHamilton(matrix,v,V,RESULT):
    temp = []
    #case where we have new cycle
    if len(V)==len(matrix) :
        RESULT.append(V+[0])
        #trick in len to display only the last element of result array
        print("CYKL HAMILTONA: " + str(RESULT[len(RESULT)-1]))
    #starting looking for new cycle
    if not len(V):
        V.append(0)
        print(V)
    #any other case
    for w in range(len(matrix[v])):
        if matrix[v][w] and w not in V:
            V.append(w)
            temp = V.copy()
            print(V)
            multiHamilton(matrix,w,V,RESULT)
            V.pop()
        if temp != V and len(temp) != 0:
            print(V)
            temp.pop()
        temp = V.copy()



res2= []
mtx2= \
[[0,1,0,0,0,0],
 [0,0,1,0,1,0],
 [1,0,0,1,0,0],
[0,0,1,0,0,1],
[0,0,1,1,0,0],
[1,1,1,0,0,0]]
multiHamilton(mtx2,0,[],res2)
