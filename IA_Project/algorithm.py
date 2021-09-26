arr = [[1,2,3],[4,5,6],[7,8,9]]
estados = []
estados.append(arr)
DIRECTIONS = {"U" : (-1, 0), "D": [1, 0], "L": [0, -1], "R": [0, 1]}
print(DIRECTIONS)

j = 0
k = 0

def swapT(arr, posI, posF):
    aux = arr[posI[0]][posI[1]]
    arr[posI[0]][posI[1]] = arr[posF[0]][posF[1]]
    arr[posF[0]][posF[1]] = aux


def sumT(t1, t2):
    return (t1[0]+t2[0], t1[1]+t2[1])

sol = sumT((j,k),(DIRECTIONS["R"]))
if sol[0] < 0 or sol[0] > 2 or sol[1] < 0 or sol[1] > 2:
    print("No jugada")
else :
    print(sol)
    arr = [row[:] for row in arr]
    swapT(arr, (j,k), sol)
    estados.append(arr)
    print(estados)

