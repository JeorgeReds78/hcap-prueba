import numpy as np

#Función de la cosa esa
def convolucion(A, B):
    C = np.zeros((len(A)-2, len(A[0])-2))
    for i in range(0, len(A)-2):
        for j in range(0, len(A[0])-2):
            C[i][j] = A[i][j]*B[0][0] + A[i][j+1]*B[0][1] + A[i][j+2]*B[0][2] + A[i+1][j]*B[1][0] + A[i+1][j+1]*B[1][1] + A[i+1][j+2]*B[1][2] + A[i+2][j]*B[2][0] + A[i+2][j+1]*B[2][1] + A[i+2][j+2]*B[2][2]
    return C

Matriz1 = [[6,9,0,3],[8,4,9,1],[4,1,3,12],[3,2,1,100]]
Matriz2 = [[1,2,3,4,5,6],[7,8,9,10,11,12],[0,0,1,16,17,18],[0,1,0,7,23,24],[1,7,6,5,4,3]]
Filtro = [[1,0,2],[5,0,9],[6,2,1]]
Filtro2 = [[1,1,1],[0,0,0],[2,10,3]]

A = np.array(Matriz1)
A1 = np.array(Matriz2)
B = np.array(Filtro)
B1 = np.array(Filtro2)

print(convolucion(A, B))
print(convolucion(A1, B1))

