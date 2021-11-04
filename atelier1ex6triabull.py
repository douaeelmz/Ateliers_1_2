print("Entrez la taille de votre tableau ")              #demande la taille du tableau a l'utilisateur
taille=int(input(""))
arr=[]
for i in range(0,taille):
    elem=float(input("Entrez une valeur "))                  #demande les valeur des elements du tableeau suivant la taille saisi par l'utilisateur
    arr.append(elem)
print("votre tableau est")                      #Affiche le tableau avant le tri
print(arr)

def triabull(arr):
    for i in range(0,len(arr)-1):
        for j in range(len(arr)-1):                      #vérifie si l'element précedant est supérieur à l'element suivant
            if (arr[j]>arr[j+1]):                             #si vrai on stocke l'element le plus grand dans un var temporaire
                temp=arr[j]                           #puis on affecte la valeur de l'element suivant  à l'element précedent
                arr[j]=arr[j+1]                           #et on affecte la valeur de l'element le plus grand à l'element suivant
                arr[j+1]=temp
    return arr
print("Le tableau devient :",triabull(arr))







