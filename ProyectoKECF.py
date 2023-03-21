#Bienvenida e introduccion acerca de la calculadora y sus usos.
print("Un saludo de paz y bien, bienvenidos\nLas opciones de calculo son las siguientes:\nSelecciones el numero de operación que desee.\n1)Conversor de longitud (1).\n2)Conversor de peso (2).\n3)Conversor de Bytes (3).\n4)Conversor de base numérica.(4)")
while True:
    opcion = input("Ingresa un número del 1 al 4: ")
    if opcion.isdigit() and int(opcion) in range(1, 5):
        opcion = int(opcion)
        break
    else:
        print("Opción no válida. Intenta de nuevo.")

    print(f"Seleccionaste la opción {opcion}.")
    

#Se crea el menu desplegable de las mediciones de longitud.
if opcion==1:
    print("Ingresa la operacion a realizar: \n(1)Centimetros a metros. \n(2)Centimetros a kilometros. \n(3)Metros a centímetros.\n(4)Metros a kilometros. \n(5)kilometros a centimetros. \n(6)kilometros a metros..")
    while True:
        medReal = input("Ingresa la operacion a realizar: ")
        if medReal.isdigit() and int(medReal) in range(1, 7):
            medReal = int(medReal)
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
#Se crean los diferentes submenus que se encontraran las mediciones o conversiones a realizar         
    if medReal==1:
        
#se crea un while true para no dejar que ingresen 0. al igual que con todas las demas.
#Tambien se piden que ingresen los datos. Este tipo de menu se va observar en las siguientes 3 menos como lo son: Longitu, Peso y bytes.        
        while True:
            cmam = input("Ingresa la longitud en centímetros (mayor que cero): ")
            try:
                cmam = float(cmam)
                
                if cmam > 0:
                    break
                
                else:
                    print("Longitud no válida. Intenta de nuevo.")
            except ValueError:
                print("Longitud no válida. Intenta de nuevo.")

        rmetros = cmam / 100.0
        print(f"{cmam} centímetros equivale a {rmetros} metros.")

    elif medReal==2:
        
        while True:
            cmak = input("Ingresa la longitud en centímetros (mayor que cero): ")
            try:
                cmak = float(cmak)
                
                if cmak > 0:
                    break
                
                else:
                    print("Longitud no válida. Intenta de nuevo.")
            except ValueError:
                print("Longitud no válida. Intenta de nuevo.")

        rkilometros = cmak / 100000.0
        print(f"{cmak} centímetros equivale a {rkilometros} kilometros.")

    if medReal==3:
        
        while True:
            macm = input("Ingresa la longitud en metros (mayor que cero): ")
            try:
                macm = float(macm)
                
                if macm > 0:
                    break
                
                else:
                    print("Longitud no válida. Intenta de nuevo.")
            except ValueError:
                print("Longitud no válida. Intenta de nuevo.")

        rcm = macm * 100.0
        print(f"{macm} metros equivale a {rcm}  centímetros.")

    elif medReal==4:
        
        while True:
            makm = input("Ingresa la longitud en metros (mayor que cero): ")
            try:
                makm = float(makm)
                
                if makm > 0:
                    break
                
                else:
                    print("Longitud no válida. Intenta de nuevo.")
            except ValueError:
                print("Longitud no válida. Intenta de nuevo.")

        rkm = makm / 1000.0
        print(f"{makm} metros equivale a {rkm} kilometros.")

    if medReal==5:
        
        while True:
            kacm = input("Ingresa la longitud en kilometros (mayor que cero): ")
            try:
                kacm = float(kacm)
                
                if kacm > 0:
                    break
                
                else:
                    print("Longitud no válida. Intenta de nuevo.")
            except ValueError:
                print("Longitud no válida. Intenta de nuevo.")

        rcen = kacm * 100000.0
        print(f"{kacm} kilometros equivale a {rcen}  centímetros.")

    elif medReal==6:
        
        while True:
            kmam = input("Ingresa la longitud en kilometros (mayor que cero): ")
            try:
                kmam = float(kmam)
                
                if kmam > 0:
                    break
                
                else:
                    print("Longitud no válida. Intenta de nuevo.")
            except ValueError:
                print("Longitud no válida. Intenta de nuevo.")

        rme = kmam * 1000.0
        print(f"{kmam} kilometros equivale a {rme} metros.")

    
if opcion==2:

    print("Ingresa la operacion a realizar: \n(1)onzas a libras. \n(2)onzas a kilogramos. \n(3)libras a onzas.\n(4)libras a kilogramos. \n(5)kilogramos a onzas. \n(6)kilogramos a libras..")
    while True:
        medpeso = input("Ingresa la operacion a realizar: ")
        if medpeso.isdigit() and int(medpeso) in range(1, 7):
            medpeso = int(medpeso)
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
#Peso        
    if medpeso==1:
        
        while True:
            ozaLi = input("Ingresa el peso en onzas (mayor que cero): ")
            try:
                ozaLi = float(ozaLi)
                
                if ozaLi > 0:
                    break
                
                else:
                    print("peso no válida. Intenta de nuevo.")
            except ValueError:
                print("peso no válida. Intenta de nuevo.")

        rlibras = ozaLi / 16.0
        print(f"{ozaLi} onzas equivale a {rlibras} libras.")

    elif medpeso==2:
        
        while True:
            cmak = input("Ingresa el peso en onzas (mayor que cero): ")
            try:
                cmak = float(cmak)
                
                if cmak > 0:
                    break
                
                else:
                    print("peso no válida. Intenta de nuevo.")
            except ValueError:
                print("peso no válida. Intenta de nuevo.")

        rkilogramos = cmak / 35.274
        print(f"{cmak} onzas equivale a {rkilogramos} kilogramos.")

    if medpeso==3:
        
        while True:
            lbaoz = input("Ingresa el peso en libras (mayor que cero): ")
            try:
                lbaoz = float(lbaoz)
                
                if lbaoz > 0:
                    break
                
                else:
                    print("Peso no válida. Intenta de nuevo.")
            except ValueError:
                print("Peso no válida. Intenta de nuevo.")

        rcm = lbaoz * 16.0
        print(f"{lbaoz} libras equivale a {rcm}  onzas.")

    elif medpeso==4:
        
        while True:
            lbakm = input("Ingresa el peso en libras (mayor que cero): ")
            try:
                lbakm = float(lbakm)
                
                if lbakm > 0:
                    break
                
                else:
                    print("Peso no válida. Intenta de nuevo.")
            except ValueError:
                print("Peso no válida. Intenta de nuevo.")

        rkm = lbakm / 2.205
        print(f"{lbakm} libras equivale a {rkm} kilogramos.")

    if medpeso==5:
        
        while True:
            kaoz = input("Ingresa peso en kilogramos (mayor que cero): ")
            try:
                kaoz = float(kaoz)
                
                if kaoz > 0:
                    break
                
                else:
                    print("Peso no válida. Intenta de nuevo.")
            except ValueError:
                print("Peso no válida. Intenta de nuevo.")

        roz = kaoz * 35.274
        print(f"{kaoz} kilogramos equivale a {roz}  onzas.")

    elif medpeso==6:
        
        while True:
            kalb = input("Ingresa peso en kilogramos (mayor que cero): ")
            try:
                kalb = float(kalb)
                
                if kalb > 0:
                    break
                
                else:
                    print("Peso no válida. Intenta de nuevo.")
            except ValueError:
                print("Peso no válida. Intenta de nuevo.")

        rlbk = kalb * 2.205
        print(f"{kalb} kilogramos equivale a {rlbk} libras.")
#Bytes    
if opcion==3:
    
    print("Ingresa la operacion a realizar: \n(1)Bytes a Kilobytes. \n(2)Bytes a Megabytes. \n(3)Kilobytes a Bytes.\n(4)Kilobytes a Megabytes. \n(5)Megabytes a Bytes. \n(6)Megabytes a Kilobytes..")
    while True:
        medby = input("Ingresa la operacion a realizar: ")
        if medby.isdigit() and int(medby) in range(1, 7):
            medby = int(medby)
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
        
    if medby==1:
        
        while True:
            byakilo = input("Ingresa los Bytes (mayor que cero): ")
            try:
                byakilo = float(byakilo)
                
                if byakilo > 0:
                    break
                
                else:
                    print("Cantidad no válida. Intenta de nuevo.")
            except ValueError:
                print("Cantidad no válida. Intenta de nuevo.")

        rbKilobytes = byakilo / 1000.0
        print(f"{byakilo} Bytes equivale a {rbKilobytes} Kilobytes.")

    elif medby==2:
        
        while True:
            bamg = input("Ingresa el Cantidad en Bytes (mayor que cero): ")
            try:
                bamg = float(bamg)
                
                if bamg > 0:
                    break
                
                else:
                    print("Cantidad no válida. Intenta de nuevo.")
            except ValueError:
                print("Cantidad no válida. Intenta de nuevo.")

        rbMegabytes = bamg / (1*10)**6
        print(f"{bamg} Bytes equivale a {rbMegabytes} Megabytes.")


    if medby==3:
        
        while True:
            kiaby = input("Ingresa el Cantidad en Kilobytes (mayor que cero): ")
            try:
                kiaby = float(kiaby)
                
                if kiaby > 0:
                    break
                
                else:
                    print("Cantidad no válida. Intenta de nuevo.")
            except ValueError:
                print("Cantidad no válida. Intenta de nuevo.")

        rkby = kiaby * 1000.0
        print(f"{kiaby} Kilobytes equivale a {rkby}  Bytes.")

    elif medby==4:
        
        while True:
            kiame = input("Ingresa el Cantidad en Kilobytes (mayor que cero): ")
            try:
                kiame = float(kiame)
                
                if kiame > 0:
                    break
                
                else:
                    print("Longitud no válida. Intenta de nuevo.")
            except ValueError:
                print("Longitud no válida. Intenta de nuevo.")

        rkme = kiame / 1000.0
        print(f"{kiame} Kilobytes equivale a {rkme} Megabytes.")

    if medby==5:
        
        while True:
            meaby = input("Ingresa los Megabytes (mayor que cero): ")
            try:
                meaby = float(meaby)
                
                if meaby > 0:
                    break
                
                else:
                    print("Cantidad válida. Intenta de nuevo.")
            except ValueError:
                print("Cantidad no válida. Intenta de nuevo.")

        rmby = meaby * (1*10)**6
        print(f"{meaby} Megabytes equivale a {rmby}  Bytes.")

    elif medby==6:
        
        while True:
            Meaki = input("Ingresa cantidad en Megabytes (mayor que cero): ")
            try:
                Meaki = float(Meaki)
                
                if Meaki > 0:
                    break
                
                else:
                    print("Cantidad no válida. Intenta de nuevo.")
            except ValueError:
                print("Cantidad no válida. Intenta de nuevo.")

        rmki = Meaki * 1000.0
        print(f"{Meaki} Megabytes equivale a {rmki} Kilobytes.")
    
if opcion==4:
    print("Ingresa la operacion a realizar: \n(1)Decimales a binarios. \n(2)Decimales a octal. \n(3)Binario a decimales.\n(4)Binarios a octal. \n(5)octal a decimal. \n(6)Octal a binario.")
    while True:
        n = input("Ingresa la operacion a realizar: ")
        if n.isdigit() and int(n) in range(1, 7):
            n = int(n)
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
    if n==1 :
        def Decimal2binary(numero):
            
            Binario = ""
            
            while numero // 2 != 0:
                
                Binario = str (numero%2) + Binario
                numero = numero // 2 
                
            return str(numero) + Binario


        valor_prueba = int(input("Ingrese el número que desea convertir: "))

        valor_binario = Decimal2binary(valor_prueba)

        print ("Su numero {} en binario es {}".format(valor_prueba, valor_binario))   
    #octal digits = [] funciona para crear una lista vacia, luego la llena la variable y sus divisiones dentro del decimal
    # % muestra el residuo y este lo divide nuevamente dentro de 8.   
    if n==2:
        decimal = int(input("Ingresa un número decimal: "))
        octal_digits = []

        while decimal > 0:
            remainder = decimal % 8
            octal_digits.append(str(remainder))
            decimal = decimal // 8

        octal_digits.reverse()
        octal = ''.join(octal_digits)

        print("El número octal correspondiente es:", octal)                        

    if n==3:
        numero_binario = input("Ingrese un número binario: ")

        numero_decimal = 0
        for i in range(len(numero_binario)):
            
            digito = int(numero_binario[i])
            
            valor_decimal = digito * 2**(len(numero_binario)-i-1)
            
            numero_decimal += valor_decimal

        print("El número decimal equivalente es:", numero_decimal)
        
    if n==4:

        numero_binario = input("Ingrese un número binario: ")

        numero_decimal = 0
        for i in range(len(numero_binario)):
        
            digito = int(numero_binario[i])
            
            valor_decimal = digito * 2**(len(numero_binario)-i-1)
            
            numero_decimal += valor_decimal


        numero_octal = oct(numero_decimal)


        print("El número octal equivalente es:", numero_octal)
    
    if n==5:
        oc = ""
        while True:
            oc = input("Ingrese un número octal positivo sin ceros: ")
            if "0" in oc:
                print("Error: el número octal no puede contener ceros.")
            elif int(oc) < 0:
                print("Error: el número octal debe ser positivo.")
            else:
                break

        nd = 0
        for k in range(len(oc)):
            digito = int(oc[k])
            v_d = digito * 8**(len(oc)-k-1)
            nd += v_d


        print("El número decimal equivalente es:", nd)
            
    if n==6:
        def octal_a_binario(numoc):
            
            nudeci = 0
            for i in range(len(numoc)):
                
                digito = int(numoc[i])
                
                Vadeci = digito * 8**(len(numoc)-i-1)
                
                nudeci += Vadeci

            
            Nubi = bin(nudeci)[2:]

            
            return Nubi


        numoc = ""
        while numoc == "" or numoc == "0":
            numoc = input("Ingrese un número octal distinto de cero: ")


        Nubi = octal_a_binario(numoc)
        print("El número binario equivalente es:", Nubi)


        while True:
            numoc = input("Ingrese otro número octal distinto de cero (o escriba 'salir' para terminar): ")
            if numoc.lower() == "salir":
                break
            elif numoc == "0":
                print("Error: el número octal no puede ser cero.")
            else:
                
                Nubi = octal_a_binario(numoc)
                print("El número binario equivalente es:", Nubi)        



print("Gracias por tu prefencia hasta la proxima  ")