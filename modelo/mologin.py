from interfaz.inmenu import menu
import hashlib


def incriptar(contra):

    incrip = hashlib.sha256()
    incrip.update(contra.encode('utf-8'))
    contraIncrip = incrip.hexdigest()
    return contraIncrip

contra = "SISGESA"
incriptada = incriptar(contra)
print(incriptada)



def inicioSesion(usu, contra):

    usuario ="admin"
    contra = input("ingrese su contraseña")
    contraincrip =  incriptar(contra)

    if usu == usuario and  contraincrip == "2fc2c9f066f015d7b9b43ed16cb07ff19724ec3d3876ccb1f3e5276a0dd65568":
        menu()



nom= input("usuario")
con= input("contra")
print(inicioSesion(nom, con))
    
