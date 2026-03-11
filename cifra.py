# Iniciando projeto Cifra de Cesar
import os

alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","n","m","o","p","q","r","s","u","v","x","z"]

# Chave 1 e 2
def cifra(texto, numero):
    os.system("clear")
    print("==========================")
    cont = (len(texto) - 1)
    n = numero
    pos = 0
    load = ""
    list_pos = []
    
    for letra in texto:
        for palavra in alfabeto:
            if letra.lower() == palavra.lower():
                list_pos.append(alfabeto.index(palavra))
                if numero > 0:
                    numero -= 1
                elif numero <= 0:
                    load += letra
    

    j = list_pos[-1]

    while n > 0:
        load += alfabeto[(j+1)]
        list_pos.append(int(list_pos[cont]))
        j += 1
        n -= 1
    return load
                               

print(cifra("MarioBros",3))
print("==========================")