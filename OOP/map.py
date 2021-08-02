# map function
li = [1,2,3,4,5,6,7,8,9]

def func(x):
    return x**x

print(list(map(func,li)))

print([ func(x) for x in li])