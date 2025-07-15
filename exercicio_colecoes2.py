# Tuplas - Gabriel Perencine

tupla = ('Gabriel', 19, 'Santo André')
a, b, c = tupla

print(a)
print(b)
print(c,'\n')

# NÃO é possivel alterar o primeiro elemento
# pois a tupla é IMUTÁVEL, não conseguimos alterar depois de criada

hobbies = ('videogame', 'basquete', 'academia')

tupla_concatenada = tupla + hobbies

print(tupla)
print(hobbies)
print(tupla_concatenada)