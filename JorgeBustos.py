import random
import csv
menu=-1
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
trab=[]
nombre={}
def asignar_sueldos():
    for i in trabajadores:
        nombre=i
        i=random.randint(300000,2500000)
        trab.append([f"nombre:{nombre}",f"sueldo: ", f"{int(i)}"])
    for t in trab:
        print(t)
    print("Se han generado los sueldos")

def clasificar_sueldos():
    try:
        print("Sueldos menores a $800.000")
        for i in trab:
            plata=int(i[2])
            if plata <800000:
                print(i)
        print("Sueldos entre $800.000 y $2.000.000")
        for i in trab:
            plata=int(i[2])
            if 800000<= plata <=2000000 :
                print(i)
        print("Sueldos mayores a $2.000.000")
        for i in trab:
            plata=int(i[2])
            if plata >2000000:
                print(i)
    except KeyError:
        print("No se han ingresado datos")
        
def reporte_de_sueldos():
    with open("trabajadores.csv",mode="w",newline="") as file:
        lista=csv.writer(file)
        lista.writerow(["Nombres", "Sueldo", "Descuento salud", "Descuento AFP", "Sueldo liquido"])
        for i in trab:
            plata=int(i[2])
            afp=plata*0.12
            salud=plata*0.7
            total=plata-salud-afp
            lista.writerow([i[0],i[1],plata,afp,salud,total])        

while menu!=0:
    print("1)Asignar sueldos aleatorios")
    print("2)Clasificar sueldos")
    print("3)Ver estadisticas")
    print("4)Reporte de sueldos")
    print("5)Salir del programa")
    try: 
        menu=int(input("---> "))

        ValueError
    except:
        print("Debe ingresar valores numericos...")
    else:
        if menu==1:
            asignar_sueldos()
        if menu==2:
            clasificar_sueldos()
        if menu==5:
            print("Finalizando programa...")
            print("Desarrollado por Jorge Bustos")
            print("RUT: 21.185.302-6")
            menu=0
        if menu==4:
            reporte_de_sueldos()