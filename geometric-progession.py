def geometricProgression(a, r, n):
    return a * ( ( 1 - (r**n)) // ( 1 - r ))

print(geometricProgression(2, 3, 4))