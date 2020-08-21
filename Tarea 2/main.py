
import json
import csv
import xml.etree.ElementTree as ET 
import time


def leer_clientes():
    archivo1 = open (r"clientes.json","r")
    for linea in archivo1.readlines():
        print (linea)
        time.sleep(0.3)
    archivo1.close()

def leer_estudiantes():
    
    archivo2 = open (r"estudiantes.xml","r")
    for linea in archivo2.readlines():
        print (linea)
        time.sleep(0.3)
    archivo2.close()


def leer_paises():
    archivo3 = open (r"paises.csv","r")
    for linea in archivo3.readlines():
        print (linea)
        time.sleep(0.3)
    archivo3.close()




def  inicio():
    repetir = True
    while repetir:
        print("\x1b[1;32m"+"\t1 -Archivo JSON") 
        print("\x1b[1;33m"+"\t2 -Archivo XML") 
        print("\x1b[1;35m"+"\t3 -Archivo CSV") 
        print("\x1b[1;31m"+"\t4 -Salir") 


        opcion = input ("\x1b[3;37m"+"Ingrese opcion    ")
        if opcion == "1":
            leer_clientes()
            
        elif opcion == "2":
            leer_estudiantes()
        elif opcion == "3":
            leer_paises()
        elif opcion == "4":
            break
        else:
            print ("")
            input ("No ha pulsado ninguna opción correcta")

inicio()