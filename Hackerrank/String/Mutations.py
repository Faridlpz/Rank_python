def mutate_string(string, position, character):
    lista = [ a for a in s] 
    lista[position] = character
    string = ''.join(lista)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

print("probando el curso GIT")
