print("Entrez la taille de votre tableau ")              #demande la taille du tableau a l'utilisateur
taille=int(input(""))
L=[]
for i in range(0,taille):
    elem=float(input("Entrez une valeur "))                  #demande les valeur des elements du tableeau suivant la taille saisi par l'utilisateur
    L.append(elem)
print("votre tableau est")                      #Affiche le tableau avant le tri
print(L)

def rechercheMin(L,i) :
	""" retourne l'indice d'un élément minimal
	parmi les éléments L[i], L[i+1], L[i+2] ..."""
	indiceDuMini, mini = i, L[i]

	for k in range( i+1, len(L) ) :
		if L[k]<mini :
			indiceDuMini, mini = k, L[k]
	return indiceDuMini


def triselection(L) :
	for i in range( len(L) -1 ) :
		indiceDuMini=rechercheMin(L,i)
		L[i], L[indiceDuMini] = L[indiceDuMini], L[i]


triselection(L)
print('L après tri :\n ', L)
