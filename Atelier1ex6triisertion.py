print("Entrez la taille de votre tableau ")              #demande la taille du tableau a l'utilisateur
taille=int(input(""))
L=[]
for i in range(0,taille):
    elem=float(input("Entrez une valeur "))                  #demande les valeur des elements du tableeau suivant la taille saisi par l'utilisateur
    L.append(elem)
print("votre tableau est")                      #Affiche le tableau avant le tri
print(L)


# Programme Python pour l'implémentation du tri par insertion
def tri_insertion(tab):
    # Parcour de 1 à la taille du tab
    for i in range(1, len(tab)):
        k = tab[i]
        j = i-1
        while j >= 0 and k < tab[j] :
                tab[j + 1] = tab[j]
                j -= 1
        tab[j + 1] = k
# Programme principale pour tester le code ci-dessus
tab = [98, 22, 15, 32, 2, 74, 63, 70]
tri_insertion(tab)
print ("Le tableau trié est:")
for i in range(len(tab)):
    print ("% d" % tab[i])
