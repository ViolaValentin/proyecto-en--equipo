def verificacion_elementos (lista):
        if "control" in lista:
                lista.remove ("control")
                lista.insert ("revisado")
        return lista
print (verificacion_elementos (["control","proceso","monitoreo"]))