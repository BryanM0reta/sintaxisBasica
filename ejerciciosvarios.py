#ingresar un numero y me refleje si es par o es impar

# while True:
#     numero=int(input('ingrese un número: \n'))
#     if numero%2==0:
#         print("su numero es par")
#     else:
#         print("su numero es impar")

#-----------------------------------------------------------------------------------------------
#sistema de login donde una se llamara usuario y otra password

# userDefault="admin"
# passwordDefaut="admin"

# user=input('ingrese su usuario: \n')
# password=input('ingrese su contraseña: \n')

# if user==userDefault and password==passwordDefaut:
#     print("Bienvenido administrador")
# else:
#     print("Quien eres?")

#-----------------------------------------------------------------------------------------------
#crear una lista de 10 numero y que sume los 10 numeros

# lista=[]
# sumatoria=0
# for i in range (10):
#     numero=int(input('ingrese un numero: \n'))
#     sumatoria=sumatoria+numero
#     lista.append(numero)

# print("la sumatoria es: ", sumatoria)
# print("la lista es: ", lista)

#-----------------------------------------------------------------------------------------------
#menu que permita depositar, sacar dinero o ver el saldo

# choice = input('1>deposito\n2>retiro\n3>check_balance\n4>salir\n')
# choice=int(choice)
# balance=50
# while True:
#     if choice==1:
#         ingreso=int(input('ingrese cantidad a depositar: \n'))
#         balance=balance+ingreso
#         print("su balance actual es: ", balance)
#     if choice==2:
#         retiro=int(input('ingrese cantidad a depositar: \n'))
#         if balance < retiro:
#             print("usted no puede retirar\n")
#         else:
#             balance= balance-retiro
#             print("retirando, espere...............")
#             print("su balance actual es: ", balance)
#     if choice==3:
#         print("su balance actual es: ", balance)
#     if choice==4:
#         break
#     if choice!= 1 and 2 and 3 and 4:
#         print("su opcion no esta en la lista")
#     choice = input('1>deposito\n2>retiro\n3>check_balance\n4>salir\n')
#     choice=int(choice)

#-----------------------------------------------------------------------------------------------

# class Estudiante:
#     def __init__(self,name,curso="AI"):
#         print("el estudiante ha sido registrado")
#         self.name=name
#         self.curso=curso
#     def dataStudent(self):
#         print(f"Nombre: {self.name} y su curso: {self.curso} ")
#         return

# student1=Estudiante("Bryan")
# student2=Estudiante("Freddy","Ingles")

# student1.dataStudent()
# student2.dataStudent()

#-----------------------------------------------------------------------------------------------

# class Estudiante:
#     def __init__(self,name,curso="AI"):
#         print("el estudiante ha sido registrado")
#         self.name=name
#         self.curso=curso
#     def dataStudent(self,status="No activo"):
#         print(f"Nombre: {self.name} su curso: {self.curso} y su estado: {self.status}")
#         return

# student1=Estudiante("Bryan")
# student2=Estudiante("Freddy","Ingles")

# student1.dataStudent("activo")
# student2.dataStudent("activo")

#-----------------------------------------------------------------------------------------------


