n = int(input())
pr = 0
for i in range(n):
    s = input()
    if s == "Tetrahedron":
        pr += 4
    elif s == "Cube":
        pr += 6
    elif s == 'Octahedron':
        pr += 8
    elif s == 'Dodecahedron':
        pr += 12
    elif s == "Icosahedron":
        pr += 20
print(pr)