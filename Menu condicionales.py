
while True:
    print ("Pedir un número y determinar si es positivo, negativo o cero(1)")
    print ("Solicitar la calificación semestral de un alumno y determinar si está aprobado o no.(2)")
    print ("Solicitar las calificaciones parciales de un alumno y determinar si está aprobado(3)")
    print ("Solicitar el año de nacimiento de una persona y determinar si es mayor de edad.(4)")
    print ("Pedir dos números y determinar cuál es mayor. (5)")
    print ("Verificar si un número ingresado es mayor de 100 (6)")
    print ("Determinar si un día ingresado es laboral o no (días laborales L-V) (7)")
    print ("Verificar si una letra ingresada es vocal (8)")
    print ("Pedir tres números y determinar cuál de ellos es el mayor (9)")
    print ("Determinar si un año es bisiesto (10)")
    print ("Determinar si un número ingresado es divisible entre 3 y 5 (11)")
    
    nose=int(input("ingrese un numero para empezar! (el ciclo terminara con 0)"))



    #////// 1:
    if (nose==1):
        num=int(input("hola, pasa un numero :]"))
        if (num>0):
            print ("tu numero es positivo")
        elif (num<0):
            print ("tu numero es negativo")
        else:
            print ("tu numero es 0")
        #//////////
    elif (nose==2):
        num = float(input("pasame un numero >:["))
        if num>0:
            print("tu numero es mayor a 0")
        elif num==0:
            print("tu numero es igual a cero")
        else:
            print("es menor q cero")
        #///////////
    elif (nose==3):
        cal = float(input("pasame tu calificacion semestral"))
        if cal>=7:
            print("pasaste wuuuuu")
        else:
            print("mi loco dele pa fuera")
        #///////////////
    elif (nose==4):    
        edad= int(input("Ingresa tu edad: "))
        
        if edad >= 18:
         print("Eres mayor de edad! ya tienes edad para que te metan al bot-")
        else:
          print("Aún eres menor de edad, wawita")
        
        #5 //////////
    elif (nose==5):
        val1= int(input("escribe un numero: ")) 
        val2= int(input("escribe otro numero: ")) 
        
        if (val1>val2):
            print (val1, "es mayor que", val2)
        elif (val1==val2):
            print (val1, "es igual que", val2)
        else:
            print (val1, "es menor que", val2)
        
        #6 ///////
    elif (nose==6):
        ecie1= int(input("escribe un numero: ")) 
        
        if (ecie1>100):
            print (ecie1, "es mayor que 100")
        else:
            print (ecie1, "no es mayor que 100")
        
        #7////////////
    elif (nose==7):
        laborales=["lunes","martes","miercoles","jueves","viernes"]
        descanso=["sabado","domingo"]
        
        dia =(input("escriba su dia de la semana: "))
        
        if (dia in laborales):
            print ("tu dia de la semana es laboral")
        elif (dia in descanso):
            print ("tu dia es de descanso (quien pudiera-)")
        else:
            print ("orale chistoso, ese no es dia de la semana >:(")
        
        #8 ///////////
    elif (nose==8):
        vocales = ["a","e","i","o","u"]
        letra = input("ingrese una letra: ")
        if letra.isalpha():
            if (letra in vocales):
                print ("tu letra es una vocal :D")
            else:
                print ("tu letra no es una vocal :P")
        else:
            print ("vamos poniendo una LETRA loco, eso no es una letra >:P")
        
        #9 //////////////
    elif (nose==9):
        mayor1 = int(input("escribe tu primer numero: "))
        mayor2 = int(input("escribe tu segundo numero: "))
        mayor3 = int(input("escribe tu tercer numero: "))
        
        if (mayor1>=mayor2 and mayor1>=mayor3):
            print (mayor1, "es el mayor")
        elif (mayor2>=mayor1 and mayor2>=mayor3):    
            print (mayor2, "es el mayor")
        else:
             print (mayor3, "es el mayor")
        
        #10 ///////
    elif (nose==10):
        bisiesto = int(input("ingrese un año: "))
        
        if (bisiesto%4==0):
            print ("tu año es bisiesto")
        else:
            print ("tu año no es bisiesto")
        
        #11 ///////////////////
    elif (nose==11):
        divisible = int(input("ingrese un numero: "))
        
        if (divisible%3==0 or divisible%5==0):
            print ("tu numero es divisible entre 3 o 5")
        else:
            print ("tu numero no es divisible entre 3 o 5")
        
    elif (nose==0):
        print ("Hasta pronto! gracias!")
        break
    else:
         print ("dato no valido, intente de nuevo :[")
         print ("cambio muy necesario para probar")
