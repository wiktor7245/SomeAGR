f = open('Hamilton.txt', 'r')
hamilton_file = [[int(num) for num in line.split(' ')] for line in f]

def hamilton(matrix,v,V,out):
    temp = []
    #case where we have new cycle
    if len(V)==len(matrix) :
        out.append(V+[0])
        #trick in len to display only the last element of result array
        print("CYKL HAMILTONA: " + str(out[len(out)-1]))
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
            hamilton(matrix,w,V,out)
            V.pop()
        if temp != V and len(temp) != 0:
            print(V)
            temp.pop()
        temp = V.copy()

res= []
hamilton(hamilton_file,0,[],res)
