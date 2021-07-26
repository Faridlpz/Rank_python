numero =[1,2,3,4,5]
def fun(numero):
        lista = [[numero[a],numero[a]**2] for a in range(len(numero)) ]
        return lista

print(fun(numero))

