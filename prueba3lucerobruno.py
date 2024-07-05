def rut_valid(rut):
    return rut.isdigit()
def nom_valid(nom):
    return nom.isalpha() and nom.isascii()
def apell_valid(apell):
    return apell.isalpha() and apell.isascii()
def val_edad(edad):
    return edad.isdigit() and 21<int(edad)<=120
def niv_est_val(nivel):
    return nivel.lower() in ['b','m','s']
def afp_ant_val(afpant):
    return afpant.isascii() and len(afpant)>0
def val_saldo(saldo):
    try:
        saldotot=float(saldo)
        return saldotot>1000000
    except ValueError:
        return False
    
def ingresodat():
    datos={}
    
    rut=input('ingrese rut solo con numeros(si termina en k, remplace por un 0):')
    if not rut_valid(rut):
        print('rut invalido, reingrese nuevamente')
        return None
    nom=input('ingrese nombre:')
    if not nom_valid(nom):
        print('nombre que es ingresado no es valido')
        return None
    apell=input('ingrese apellido:')
    if not apell_valid(apell):
        print('apellido ingresados no son validos')
        return None
    edad=input('ingrese edad (mayor de 21 años):')
    if not val_edad(edad):
        print('ud. no cumple con la edad necesarea para postular')
        return None
    nivel=input('ingrese su nivel de estudios. Basica(b), Media(m), Superior(s):')
    if not niv_est_val(nivel):
        print('letra invalida')
        return None
    aftant=input('ingrese su anterior afp:')
    if not afp_ant_val(aftant):
        print('afp inexistente u invalida')
        return None
    saldodisp=input('ingrese su saldo disponible (mayor a $1000000):')
    if not val_saldo(saldodisp):
        print('saldo no cumple con lo requerido')
        return None
    
    datos=[]
    datos['Rut']=rut
    datos['Nombre Afiliado']=nom
    datos['Apellido']=apell
    datos['Edad']=edad
    datos['Nivel de estudios']=nivel.upper()
    datos['AFP anterior']=aftant
    datos['Saldo disponible']=saldodisp
    return datos
    
def generar_certificado(datos):
    certificado= f"==== Certificado de Afiliación ====\n\n"
    for clave, valor in datos.items():
        certificado= certificado+f"{clave}: {valor}\n" 
    
    certificado= certificado + "\n===== Fin del Certificado ======\n"        
    
    nombre_archivo= "certificado_afiliacion.txt"
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(certificado)
    print(f"Certificado generado y guardado en {nombre_archivo}")

while True:
    datos=ingresodat()
    if datos:
        generar_certificado(datos)
        break
    else:
        print("Por favor, vuelva a ingresar los datos correctamente.")

