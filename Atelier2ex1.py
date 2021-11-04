l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3 = []
for ind in range(0,len(l1)):            #la boucle for va parcourir la liste 1
    if ind%2==1:                            #on vérifie si l'index est impaire
        l3.append(l1[ind])              #on ajoute l'élement de l'index impaire
for ind in range(0,len(l2)):                #la boucle for va parcourir la liste 2
    if ind%2==0:                            #on vérifie si l'index est paire
        l3.append(l2[ind])                 #on ajoute l'élement de l'index paire
print(l3)

