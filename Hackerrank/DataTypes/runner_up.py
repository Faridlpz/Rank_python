n = 5
arr = list(map(int, input().split()))
mayor = max(arr)
lista_aux = arr[:]
for i in lista_aux:
    if i == mayor:
        arr.remove(mayor)
        segundo = max(arr)
        
print(segundo)
        
