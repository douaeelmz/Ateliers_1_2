def frequency(char, sentence):
    count = 0
    for k in list(sentence):
        if k == char:
            count+=1
    return count
char= str(input("le caractere cherché "))
sentence= str(input("Saisi la chaine "))
print("le fréquence est ",frequency(char, sentence))
