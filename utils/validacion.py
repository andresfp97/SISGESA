def leerUsuario():
    while True:
        try:
            nombre = input("Ingrese el nombre?: ").strip()
            
            if len(nombre) == 0:
                print(">>> ERROR. nombre invalido")
                continue
            return nombre

        except Exception as e:
            print("Error al ingresar el nombre.\n" + e)
            
def leerCodigo():
    while True:
        try:
            nombre = input("Ingrese el codigo?: ").strip()
            
            if len(nombre) == 0:
                print(">>> ERROR. codigo invalido")
                continue
            return nombre

        except Exception as e:
            print("Error al ingresar el codigo.\n" + e)
            

def leerEdad():
    while True:
        try:
            cant = int(input("Leer edad: "))
            if cant < 10:
                print(">>> Error. en edad")
                continue
            return cant

        except ValueError:
            print("Error. cantidad invalido.\n")
            
            
def leerSexo():
    while True:
        try:
            sexo = input("Ingrese el sexo?: ").strip().lower()
            
            if len(sexo) == 0:
                print(">>> ERROR. sexo invalido")
                continue
            
            if sexo =="m" or  sexo == "f":
               return sexo

        except Exception as e:
            print("Error al ingresar la marca.\n" + e)