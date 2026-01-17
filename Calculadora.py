#Esta es una calculadora simple que hacer operaciones entre dos operandos

#Aqui le indicamos al usuario las opciones disponibles y solicitamos elegir la que desea realizar
print ("------CALCULADORA------")
print ("Operaciones disponibles:")
print ("1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.Modulo\n6.Exponencial")
op = input("Selecciona la operacion:")
print (op)

#utilizando un valor booleano para poder interrumpir la interaccion si eligen una opcion incorrecta o que no existe en el menu
error = True

#En esta parte se confirma al usuario la opcion que eligio
if op == "1":
    print ("Has seleccionado la operacion Suma") 
elif op == "2":
    print ("Has seleccionado la operacion Resta")
elif op == "3":
    print ("Has seleccionado la opcion multiplicacion")
elif op == "4":
    print ("Has seleccionado la operacion Division")
elif op == "5":
    print ('Has seleccionado la operacion Resto de divison')
elif op == "6":
    print ('Has seleccionado la operacion exponencial')
else:
    print ("Seleccion no valida")

#Aqui es donde si elige una opcion no valida la calculadora finaliza su operacion y pide comenzar nuevamente
    error = False
    
    print ("Por favor vuelva a ejecutar la calculadora")

#En esta parte se realiza todo el codigo de operacion de la calculadora    
if error:
    
    #solicitando los operandos
    print ("Ahora ingresa los numeros que deseas calcular")
    a = float(input("Primer operando: "))
    b = float(input("Segundo operando: "))

    #esta es la parte de la ejecucion de las operaciones
    if op == "1":
        print (f"El resultado es {a+b}")
    
    elif op == "2":
        print (f"El resultado es {a-b}")
    
    elif op == "3":
        print (f"El resultado es {a*b}")
    
    elif op == "4":
        if b != "0":
            d = round(a/b , 2)
            print (f"El resultado es {d}")
        
        else:
            print ("Error: No se puede dividir entre 0")
    
    elif op == "5":
        print (f"El resultado es {a%b}")
    elif op == "6":
        print (f"El resultado es {a**b}")

else:
    print ("Hemos finalizado")
