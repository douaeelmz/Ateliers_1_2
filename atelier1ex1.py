somme= 0
def fctr(n):
   if n == 1:  # si n est egale a 1 le factoriel est 1
    return 1
   else:
    return n * fctr(n - 1)
for n in range(1,6):
    somme = somme + (fctr(n)/n)

print("la somme des séries est",somme)



