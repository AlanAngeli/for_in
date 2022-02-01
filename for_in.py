print("For in")

texto = "Python"

for letra in texto:
    print(letra)

print()
print()

# Com While ficaria desta forma:

#texto = "Python"
#c = 0
#while c < len(texto):
#    print(texto[c])
#    c += 1

##################################
print("enumerate")

for n, letra in enumerate(texto): # Deixar numerado o texto
    print(n, letra)

print()
print()

##################################
"""

Função range: (start-=0, stop, step=1)

"""
print("range")

for numero in range(10):
    print(numero)

#exemplo usando step:
print()
print()

for n in range (0, 10, 2): #step é o 2, significa que vai contar de 2 em 2
    print(n)

#outro exemplo:

print()
print()

for a in range (20, 0, -2):
    print(a)

# usando %

print()
print()

for b in range (100):
    if b % 8 == 0:  # % mostra o resto da divisão entre um número e outro
        print(b) # o resultado será múltiplos de 8