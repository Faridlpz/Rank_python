lista = []
for _ in range(int(input())):
        lista.append([input(),float(input())])

second = sorted(list(set(cal for name,cal in lista)))[1]
print("\n".join(sorted(list(set(name for name,cal in lista if cal == second)))))
