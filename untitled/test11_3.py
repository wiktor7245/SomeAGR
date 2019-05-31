def make_connection(matrix, x, y):
    matrix[x][y] = 1
    matrix[y][x] = 1

def del_connection(matrix, x, y):
    matrix[x][y] = 0
    matrix[y][x] = 0

#*******************************************
#ROBI OK, ALE USUWA MACIERZ
def Hamilton(matrix,v,V,result):
    V.append(v)
    for w in range(len(matrix[v])):
        if matrix[v][w] == 1 and w not in V:
            del_connection(matrix, v, w)
            result = Hamilton(matrix, w, V, result)
            if result:
                return result
    if len(V) == len(matrix) and matrix[v][0] == 1:
        return V+[0]
    else:
        V.pop()
        if len(V) > 1:
            last = V[-1]
            make_connection(matrix, v, last)
#print (Hamilton(matrix,0,[],[]))

RESULT=[]
def multiHamilton(matrix,v,V,RESULT):
    #case where we have new cycle
    if len(V)==len(matrix) and matrix[v][0]:
        RESULT.append(V+[0])
        print(RESULT)
    #starting looking for new cycle
    if not len(V):
        V.append(0)
    #any other case
    for w in range(len(matrix[v])):
        if matrix[v][w] and w not in V:
            V.append(w)
            print(V)
            multiHamilton(matrix,w,V,RESULT)
            print(V)
            V.pop()

res2= []
mtx2= \
[[0,1,0,0,0,0],
 [0,0,1,0,1,0],
 [1,0,0,1,0,0],
[0,0,1,0,0,1],
[0,0,1,1,0,0],
[1,1,1,0,0,0]]
print("sdasd")
multiHamilton(mtx2,0,[],res2)
print(res2)
print("sadasd")
