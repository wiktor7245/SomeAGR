def Euler(matrix, sv):
        out = []
        stack = [sv]
        while stack:
            v = stack[-1]
            is_edge = 0
            for i in range(len(matrix)):
                if matrix[v][i] == 1:
                    matrix[v][i] = -1
                    matrix[i][v] = -1
                    stack.append(i)
                    is_edge = 1
                    break
            if is_edge == 1:
                continue
            stack.pop()
            out.append(v)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j]*=-1
        return out

'''MATRIX = [
[0,1,1,0,0,0],
[1,0,1,1,1,0],
[1,1,0,1,1,0],
[0,1,1,0,1,1],
[0,1,1,1,0,1],
[0,0,0,1,1,0],
]
print ("EULER")
print(Euler(MATRIX,0))'''

