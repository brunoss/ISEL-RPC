#a)
print('--------a--------')
print("Hello World!")
#print 'teste' Não funciona!

#b)
print()
print('--------b--------')
lista_de_numeros = [1, 2, 3, 4]
lista_de_palavras = ["ola", "hoje", "existe algo", "diferente"]
lista_misturada = [3, "ola", 44, "aqui chive", 'a', [3, "ola"], [[], 777]]

print(lista_de_numeros[0])
print(lista_misturada[len(lista_misturada) - 1])
print(lista_misturada[len(lista_misturada) - 1][0])
lista_misturada[len(lista_misturada) - 1][0].append(lista_de_numeros)
print(lista_misturada)
print(lista_misturada.pop(3))
print(lista_misturada)

#c)
print()
print('--------c--------')

idade = { 
    "Miguel": 24,
    "Ana": 28,
    "Adriana": 31
}

idade["Tu"] = 10
idade["Eu"] = "10"
print(idade)

del idade["Eu"]
print(idade)
print(idade.items())
print(idade.keys())

#d)
print()
print('--------d--------')

zoo = ('lobo', 'elefante', 'pinguim', 'ovelha', 777)
print(zoo)
try:
    zoo.append("erva")
except:
    print('cannot add element to tuple')

try:    
    result = zoo[0] + "&" + zoo[3] + zoo[len(zoo) - 1] + 223 
    print(result)
except BaseException as error:
    print(error)
    result = zoo[0] + "&" + zoo[3] + str(zoo[len(zoo) - 1] + 223)
    print(result)
    
outroZoo = ("macaco", "girafa", zoo)
print(outroZoo)
print(outroZoo[2][3])

print(zoo + zoo)
print(zoo * 3)

#e)
print()
print('--------e--------')
tmp = list(result)
tmp.sort()
print(tmp)

print(tuple(tmp))

t = (1, 2, 3, 4, 5)
l = [x + 20 for x in t]
print(l)

#f)
print()
print('--------f--------')

input = open('e_Config.py', 'r')
print(input.read())
