a = 2
b = 3

rname= "MORETA"

is_active = True

print(type(a))
print(type(b))
print(type(rname))

device = 'router'
id = 101


number1 = 4
number2 = 2



# result = number1 + number2
# print("la suma es: ", result)

print("El resultado es: ", number1+number2)  #suma
print("El resultado es: ", number1-number2)  #resta
print("El resultado es: ", number1*number2)  #multiplicacion
print("El resultado es: ", number1/number2)  #division
print("El resultado es: ", number1**number2)  #potencia


#STRINGS
print("string")

name = "bryan moreta"

print(name.upper())
print(name.capitalize())
print(name.lower())

lenguaje='PYTHON'
print(lenguaje[0])
print(lenguaje[-1])

print(len(lenguaje))

#LIST
print("#LIST")
devices=['router','switch',"cable",45, True, False]
print(len(devices))

print(devices[0])
print(devices[-1])

devices.append("Server")
print(devices)

names=list()
names.append('rey')
names.append('josias')
names.append('bryan')
names.append('mlevin')
print(names)
names[1]="sebastian"
print(names)


numbers=list(range(10))
print(numbers)
selectednumbers=numbers[2:4]
print(selectednumbers)


print(numbers[:-1])
print(numbers[:3])
numbers[2:3]=[100.100]
print(numbers)

#TUPLE
print("TUPLE")

contenedortuple=(10 , 20)
mi_lista=list(contenedortuple)
mi_lista.append(50)
mi_lista.append(80)
mi_lista.append(90)
print(mi_lista)

contenedortuple= tuple(mi_lista)
print(contenedortuple[0])


#DICCIONARIO
print("DICCIONARIO")
animales={"cat": "pretty","perro":"nice", "mono":"black"}
print(animales["cat"])

animales["perro"]="ugly"
print(animales)
print("tortuga" in animales)

del animales["perro"]
print(animales)

animales["pez"]="branqueas"
animales["rata"]="plaga"

# for item in animales:
#     feature= (animales[item])
#     print("%item tiene %feature"%(item,feature))

#NUEVO DICCIONARIO

my_diccionario = dict()
my_diccionario["humanos"]=2
my_diccionario["raton"]=4
my_diccionario["araña"]=8

for animales in my_diccionario:
    data=my_diccionario[animales]
    print(f'los %s tienen %d'%(animales,data))

#LOOPS

# counter=0
# while counter<10 :
#     print(counter)
#     counter=counter+1
#     #counter+=1
# name= input('ingrese su nombre: \n')
# print(f'hello, {name}')

#-------------------------------------------------------

# contador=0
# while contador<=100:
#     print(contador)
#     contador=contador+2

# lista_numeros=list()
# for i in range (12):
#     if i%2==0:
#         lista_numeros.append(i)
# lista_numeros=[i for i in range(12) if i%2==0]
# print(lista_numeros)

#-------------------------------------------------------

lista=[i*i for i in range(100)]
print(lista)

#-------------------------------------------------------

#lista con numeros aleatorios / 10 elementos y encontrar el numero maximo
numeros=[1,23,53,74,85,26,17,18,39,10]
numeros.sort()
print(numeros)
max = 0
for i in range(10):    
    numero_seleccionado = numeros[i]
    if max <= numero_seleccionado:
        max = numero_seleccionado
print(max)

#-------------------------------------------------------
#DEFINICION DE VARIABLES

def greetings ():
    return('hello world')

tmp=greetings()
print(tmp)

#-------------------------------------------------------

def greetings2(name='friend'):
    print(f'hello world, {name}')
    return
greetings2()

#-------------------------------------------------------

# counter=0
# while counter<10 :
#     print(counter)
#     counter=counter+1
#     #counter+=1
# name= input('ingrese su nombre: \n')
# print(f'hello, {name}')


#calculadora
operacion=input('ingrese la opreracion (suma, resta, multiplicacion, division): \n')
numero_1=int(input('ingrese el primer numero:  \n'))
numero_2=int(input('ingrese el segundo numero:  \n'))

if operacion == "suma":
    resultado = numero_1 + numero_2
    print(f'el resultado es: {resultado}')
    if operacion == "resta":
        resultado = numero_1 + numero_2
        print(f'el resultado es: {resultado}')
        if operacion == "multiplicacion":
            resultado = numero_1 * numero_2
            print(f'el resultado es: {resultado}')
            if operacion == "division":
                resultado = numero_1 / numero_2
                print(f'el resultado es: {resultado}')