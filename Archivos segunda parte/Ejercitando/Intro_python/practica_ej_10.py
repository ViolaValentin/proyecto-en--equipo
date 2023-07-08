from datetime import date
socios_totales=3
numero_de_socio=["1","2","3"]
nombre_y_apellido="Florencia Ocampo,David Estevez,Sofía Cáceres"
fecha_de_ingreso="14/09/2001,14/09/2001,14/09/2001"
cuota_al_dia="Cuota al día,Cuota al día,Cuota al día"
def gestion_socios (numero_socio_a_revisar):
    socios_totales=3
    numero_de_socio=["1","2","3"]
    nombre_y_apellido="Florencia Ocampo,David Estevez,Sofía Cáceres"
    fecha_de_ingreso="14/09/2001,14/09/2001,14/09/2001"
    cuota_al_dia="Cuota al día,Cuota al día,Cuota al día"
    suma_socios_totales=socios_totales+1
    nuevo_nombre=nombre_y_apellido.split (",")
    nueva_fecha=fecha_de_ingreso.split (",")
    nueva_cuota=cuota_al_dia.split (",")

    #Inicia el programa
    print (f"Bienvenido! Comenzaremos con tu proceso de inscripción. Tu nuevo número de socio es {suma_socios_totales}" )
    agregar_nombre_y_apellido= (input ("Cual es su nombre?: "))
    nuevo_nombre.append (agregar_nombre_y_apellido)
    nueva_fecha.append (date.today())
    print (fecha_de_ingreso)
    agregar_cuota_al_dia=input ("Tiene la cuota al día?: ")
    if agregar_cuota_al_dia =="SI" or "Si" or "si":
        nueva_cuota.append ("Cuota al día")
    else:
        nueva_cuota.append ("Su cuota vano está al día")
    if numero_socio_a_revisar == "Cuota al día" in nueva_fecha[numero_socio_a_revisar][:]:
            print ("La cuota de FLor está al día")
    return (f"El club cuenta con {suma_socios_totales} socios",nuevo_nombre[numero_socio_a_revisar][:],nueva_fecha[:][numero_socio_a_revisar],nueva_cuota[numero_socio_a_revisar][:])
    

print (gestion_socios(2))

"""
    
"""